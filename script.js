// Mobile menu toggle
const mobileToggle = document.getElementById('mobile-menu');
const navLinks = document.querySelector('.nav-links');

if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        mobileToggle.classList.toggle('is-active');
    });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
            
            // Close mobile menu if open
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileToggle.classList.remove('is-active');
            }
        }
    });
});

// Scroll listener for glass-nav shadow/opacity
window.addEventListener('scroll', () => {
    const nav = document.querySelector('.glass-nav');
    if (window.scrollY > 50) {
        nav.style.padding = '15px 0';
        nav.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
    } else {
        nav.style.padding = '20px 0';
        nav.style.boxShadow = 'none';
    }
});

// Legal Modals Logic
function openLegalModal(modalId, event) {
    if (event) event.preventDefault();
    const modal = document.getElementById(modalId);
    if (!modal) return;
    
    // Prevent background scrolling
    document.body.style.overflow = 'hidden';
    
    modal.classList.remove('hidden');
    // Trigger reflow
    void modal.offsetWidth;
    
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
    
    // Restore background scrolling
    document.body.style.overflow = '';
    
    modal.classList.add('opacity-0');
    const content = modal.querySelector('div[id$="-content"]');
    if (content) {
        content.classList.remove('scale-100');
        content.classList.add('scale-95');
    }
    
    setTimeout(() => {
        modal.classList.add('hidden');
    }, 300); // Matches transition duration
}
