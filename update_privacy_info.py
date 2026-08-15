import os

html_files = [
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/index.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/innovaatiot.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/ymmarryksentie.html'
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replacements
    content = content.replace('[Y-tunnus]', '3223626-1')
    content = content.replace('[Osoite]', 'Kievarintie 23, 08700 LOHJA')
    content = content.replace('www.roboline.fi', 'www.robolinegroup.fi')
    content = content.replace('[sähköposti]', 'contact@robolinegroup.fi')
    content = content.replace('[numero]', '+358 50 3000 111')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Privacy info updated.")
