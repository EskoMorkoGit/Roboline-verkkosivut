import os

html_files = [
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/index.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/innovaatiot.html',
    '/Users/eskomaki/Antigravity/VerkkoSivut/Roboline/ymmarryksentie.html'
]

script_html = """
<script>
// Legal Modals Logic
function openLegalModal(modalId, event) {
    if (event) event.preventDefault();
    const modal = document.getElementById(modalId);
    if (!modal) return;
    
    document.body.style.overflow = 'hidden';
    modal.classList.remove('hidden');
    void modal.offsetWidth; // Trigger reflow
    modal.classList.remove('opacity-0');
    
    const content = modal.querySelector('div[id$="-content"]');
    if (content) {
        content.classList.remove('scale-95');
        content.classList.add('scale-100');
    }
}

function closeLegalModal(modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    
    document.body.style.overflow = '';
    modal.classList.add('opacity-0');
    
    const content = modal.querySelector('div[id$="-content"]');
    if (content) {
        content.classList.remove('scale-100');
        content.classList.add('scale-95');
    }
    
    setTimeout(() => {
        modal.classList.add('hidden');
    }, 300);
}
</script>
</body>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'function openLegalModal' not in content:
        content = content.replace('</body>', script_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("JS injected.")
