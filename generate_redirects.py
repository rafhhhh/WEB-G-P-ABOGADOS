import os
from urllib.parse import urlparse
import difflib

# List of all available new HTML files
new_html_files = [
    f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html'
]

# Manual mappings for known sections or hard-to-match slugs
MANUAL_MAPPINGS = {
    '/areas-de-especializacion/accidentes-de-trafico/': '/accidentes-trafico.html',
    '/areas-de-especializacion/accidentes-de-trafico/contacto': '/accidentes-trafico.html',
    '/areas-de-especializacion/derecho-bancario/': '/derecho-bancario.html',
    '/areas-de-especializacion/derecho-penal/': '/derecho-penal.html',
    '/areas-de-especializacion/divorcios/': '/divorcios.html',
    '/areas-de-especializacion/gestion-inmobiliaria/': '/gestion-inmobiliaria.html',
    '/areas-de-especializacion/herencias/': '/herencias.html',
    '/contacto/': '/#contacto',
    '/aviso-legal/': '/aviso-legal.html',
    '/politica-de-privacidad/': '/politica-privacidad.html',
    '/politica-de-cookies/': '/politica-cookies.html',
    '/nacionalidad-espanola-por-residencia-en-2025-todo-lo-que-necesitas-saber/': '/nacionalidad-por-residencia.html',
    '/regularizacion-masiva-de-extranjeros-en-espana-2026/': '/regularizacion-masiva.html',
    '/residencia-familiar-2025-nueva-instruccion-para-familiares-de-espanoles-con-el-reglamento-de-extranjeria/': '/visado-familiar-ciudadano-espanol.html',
}

def clean_slug(url_path):
    parts = [p for p in url_path.strip('/').split('/') if p]
    if not parts:
        return ""
    slug = parts[-1]
    # some cleanup, e.g. "modificacion-de-residencia-a-residencia-y-trabajo-por-cuenta-propia"
    return slug

def find_best_match(slug, choices):
    if not slug or not choices:
        return None
    # match against html filename without extension
    clean_choices = [c.replace('.html', '') for c in choices]
    matches = difflib.get_close_matches(slug, clean_choices, n=1, cutoff=0.5)
    
    if matches:
        return "/" + matches[0] + ".html"
        
    # fallback: keyword matching
    for choice in choices:
        choice_clean = choice.replace('.html', '')
        if all(word in choice_clean for word in slug.split('-') if len(word) > 4):
            return "/" + choice
        
    return None

def generate_htaccess():
    if not os.path.exists('old_urls.txt'):
        print("Error: old_urls.txt not found")
        return

    redirects = []
    redirects.append("# REDIRECCIONES 301 DE LA WEB ANTIGUA")
    redirects.append("<IfModule mod_rewrite.c>")
    redirects.append("RewriteEngine On")
    redirects.append("")
    
    with open('old_urls.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    mapped_count = 0
    unmapped_count = 0

    for url in urls:
        parsed = urlparse(url)
        path = parsed.path
        
        # Skip root path
        if path == '/' or path == '':
            continue
            
        # Avoid generating rules for files that don't need redirecting if they're exactly the same, but wait, WordPress to HTML changes extension.
        
        # 1. Check manual overrides
        if path in MANUAL_MAPPINGS:
            new_path = MANUAL_MAPPINGS[path]
            redirects.append(f"Redirect 301 {path} {new_path}")
            mapped_count += 1
            continue
            
        # 2. Extract slug and attempt matching
        if path.startswith('/areas-de-especializacion/extranjeria/'):
            slug = clean_slug(path)
            new_path = find_best_match(slug, new_html_files)
            
            if new_path:
                redirects.append(f"Redirect 301 {path} {new_path}")
                mapped_count += 1
                continue
                
        # 3. For any other URLs (/category/, /wp-content/, /blog/... ) map to Home / to avoid 404 and pass domain authority
        if path.startswith('/category/') or path.startswith('/wp-content/'):
             redirects.append(f"Redirect 301 {path} /")
             unmapped_count += 1
             continue
             
        # Catch-all for unmapped articles/pages
        redirects.append(f"Redirect 301 {path} /")
        unmapped_count += 1

    redirects.append("</IfModule>")

    with open('.htaccess', 'w') as f:
        f.write("\n".join(redirects) + "\n")
        
    print(f"Generated .htaccess successfully!")
    print(f"- Specifically Mapped URLs: {mapped_count}")
    print(f"- Unmapped/Fallback to Home: {unmapped_count}")

if __name__ == "__main__":
    generate_htaccess()
