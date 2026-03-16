import json
import urllib.request
import re
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_script_or_style = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'nav', 'header', 'footer'):
            self.in_script_or_style = True
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.text.append('\n\n### ')
        elif tag == 'p':
            self.text.append('\n\n')
        elif tag == 'li':
            self.text.append('\n- ')
        elif tag == 'br':
            self.text.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'nav', 'header', 'footer'):
            self.in_script_or_style = False

    def handle_data(self, data):
        if not self.in_script_or_style:
            cleaned = data.strip()
            if cleaned:
                self.text.append(cleaned + " ")

    def get_text(self):
        result = ''.join(self.text)
        # Clean up excessive newlines
        result = re.sub(r'\n{3,}', '\n\n', result)
        return result.strip()

with open('links.json', 'r', encoding='utf-8') as f:
    links = json.load(f)

# Filter links that belong to areas-de-especializacion, which covers both Extranjeria and Otras Especialidades
urls_to_scrape = {}
for l in links:
    href = l['href']
    if href and href.startswith('https://gonzalezpulidoabogados.com/areas-de-especializacion/'):
        # Exclude anchor links on the same page
        if '#' not in href:
            urls_to_scrape[href] = l['text']

print(f"Found {len(urls_to_scrape)} links to scrape.")

md_content = "# Información de Especialidades - González Pulido Abogados\n\n"

for url, text in urls_to_scrape.items():
    print(f"Scraping: {text} - {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
        
        # Try to extract the main content area to avoid menus and footers
        main_match = re.search(r'<main.*?>(.*?)</main>', html, re.IGNORECASE | re.DOTALL)
        if main_match:
            content_to_parse = main_match.group(1)
        else:
            # Fallback to mostly body content
            content_to_parse = html
            
        extractor = TextExtractor()
        extractor.feed(content_to_parse)
        page_text = extractor.get_text()
        
        md_content += f"## {text}\n"
        md_content += f"**URL:** {url}\n\n"
        md_content += page_text + "\n\n"
        md_content += "---\n\n"
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

with open('informacion_especialidades.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Done! Check informacion_especialidades.md")
