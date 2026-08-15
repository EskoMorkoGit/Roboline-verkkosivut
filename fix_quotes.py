import os

html_files = [
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/index.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/innovaatiot.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/ymmarryksentie.html'
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("openLegalModal(\\'privacy-modal\\', event)", "openLegalModal('privacy-modal', event)")
    content = content.replace("openLegalModal(\\'terms-modal\\', event)", "openLegalModal('terms-modal', event)")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Quotes fixed.")
