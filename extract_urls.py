import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def get_session():
    session = requests.Session()
    retry = Retry(
        total=5,
        read=5,
        connect=5,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504)
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    })
    return session

def crawl(start_url, max_pages=300):
    visited = set()
    to_visit = {start_url}
    all_site_urls = set()
    base_domain = urlparse(start_url).netloc
    session = get_session()

    print(f"Starting crawl at {start_url}...")
    
    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue
            
        visited.add(url)
        all_site_urls.add(url)
        print(f"Crawling ({len(visited)}/{max_pages}): {url}")
        
        try:
            # We skip downloading heavy files
            if any(url.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.zip']):
                continue
                
            response = session.get(url, timeout=10, verify=False) # Ignoring SSL verification just in case
            time.sleep(0.5) # Sleep half a second to be nice to the server
            
            if 'text/html' in response.headers.get('Content-Type', ''):
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for a_tag in soup.find_all('a', href=True):
                    href = a_tag['href']
                    next_url = urljoin(url, href)
                    parsed_next = urlparse(next_url)
                    
                    if parsed_next.scheme in ('http', 'https'):
                         clean_url = parsed_next._replace(fragment='').geturl()
                         if urlparse(clean_url).netloc == base_domain and clean_url not in visited:
                             to_visit.add(clean_url)
                             all_site_urls.add(clean_url)
                            
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    # Save URLs to file, filtering out heavy files
    filtered_urls = [u for u in sorted(all_site_urls) if not any(u.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.zip'])]
    with open('old_urls.txt', 'w') as f:
        for u in filtered_urls:
            f.write(u + '\n')
            
    print(f"\nFinished crawling. Found {len(filtered_urls)} unique page URLs.")
    print("Saved to old_urls.txt")

if __name__ == "__main__":
    # Suppress insecure request warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    crawl("https://gonzalezpulidoabogados.com/", max_pages=400)
