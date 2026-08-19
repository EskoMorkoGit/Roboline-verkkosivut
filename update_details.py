import os

html_files = [
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/index.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/innovaatiot.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/ymmarryksentie.html'
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update footer address (multiline)
    content = content.replace('<p>Kievarintie 23</p>\n              <p>08700 LOHJA</p>', '<p>Markkinakuja 10 A 11</p>\n              <p>08700 Lohja</p>')
    # Fallback in case spacing is different
    content = content.replace('Kievarintie 23', 'Markkinakuja 10 A 11')
    content = content.replace('08700 LOHJA', '08700 Lohja')
    
    # 2. Update privacy policy address (single line, which is caught by fallback above, but let's be sure)
    # The fallbacks above will change "Kievarintie 23, 08700 LOHJA" to "Markkinakuja 10 A 11, 08700 Lohja"
    
    # 3. Update Mikael's title
    content = content.replace('>Perustajaosakas<', '>Perustajaosakas, HPJ<')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Details updated.")
