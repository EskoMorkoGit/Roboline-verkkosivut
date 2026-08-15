import os

html_files = [
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/index.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/innovaatiot.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/ymmarryksentie.html'
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update website URL in privacy policy
    content = content.replace('<li><strong>Verkkosivusto:</strong> www.robolinegroup.fi</li>', '<li><strong>Verkkosivusto:</strong> https://www.roboline-innovations.fi/</li>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Website updated.")
