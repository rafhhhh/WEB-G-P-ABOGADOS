import urllib.request
import re
import json

url = 'https://gonzalezpulidoabogados.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
except Exception as e:
    print(f"Error: {e}")
    html = ""

# Very simple regex to find all a tags and hrefs
links = []
matches = re.findall(r'<a.*?href="(.*?)".*?>(.*?)</a>', html, re.IGNORECASE | re.DOTALL)
for href, text in matches:
    # Clean text
    clean_text = re.sub(r'<[^>]*>', '', text).strip()
    links.append({'text': clean_text, 'href': href})

with open('links.json', 'w', encoding='utf-8') as f:
    json.dump(links, f, indent=2, ensure_ascii=False)
print("Saved links")
