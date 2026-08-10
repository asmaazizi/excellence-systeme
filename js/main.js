/* ==========================================
   EXCELLENCE SYSTEME - MAIN INTERACTIVE JS
   ========================================== */

document.addEventListener('DOMContentLoaded', () => {
    initHeaderScroll();
    initMobileNav();
    initHeroCanvas();
    initStatsCounter();
    initProductFilters();
    initPortfolioFilters();
    initTestimonialCarousel();
    initModals();
    initContactForm();
    initLanguageSwitcher();
});

/* 1. Header Scroll Effect */
function initHeaderScroll() {
    const header = document.querySelector('.site-header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

/* 2. Mobile Navigation Drawer */
function initMobileNav() {
    const toggleBtn = document.querySelector('.mobile-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (!toggleBtn || !navMenu) return;

    toggleBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        const icon = toggleBtn.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-xmark');
        }
    });

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            const icon = toggleBtn.querySelector('i');
            if (icon) {
                icon.classList.add('fa-bars');
                icon.classList.remove('fa-xmark');
            }
        });
    });
}

/* 3. Hero Canvas Network Background */
function initHeroCanvas() {
    const canvas = document.getElementById('hero-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = Math.min(Math.floor(width / 25), 45);

    for (let i = 0; i < particleCount; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.6,
            vy: (Math.random() - 0.5) * 0.6,
            radius: Math.random() * 2 + 1,
            alpha: Math.random() * 0.5 + 0.2
        });
    }

    function draw() {
        ctx.clearRect(0, 0, width, height);

        // Draw connections
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 140) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(99, 196, 196, ${0.15 * (1 - dist / 140)})`;
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }

        // Draw particles
        particles.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(99, 196, 196, ${p.alpha})`;
            ctx.shadowBlur = 8;
            ctx.shadowColor = '#63C4C4';
            ctx.fill();

            p.x += p.vx;
            p.y += p.vy;

            if (p.x < 0 || p.x > width) p.vx *= -1;
            if (p.y < 0 || p.y > height) p.vy *= -1;
        });

        requestAnimationFrame(draw);
    }

    draw();
}

/* 4. Stats Counter Animation */
function initStatsCounter() {
    const statNumbers = document.querySelectorAll('.stat-number');
    let animated = false;

    function startCounter() {
        statNumbers.forEach(stat => {
            const target = parseInt(stat.getAttribute('data-target') || '0', 10);
            const prefix = stat.getAttribute('data-prefix') || '';
            const suffix = stat.getAttribute('data-suffix') || '';
            let current = 0;
            const increment = Math.ceil(target / 40);

            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                stat.textContent = `${prefix}${current}${suffix}`;
            }, 35);
        });
    }

    window.addEventListener('scroll', () => {
        const statsSection = document.querySelector('.trust-bar');
        if (!statsSection || animated) return;

        const rect = statsSection.getBoundingClientRect();
        if (rect.top <= window.innerHeight * 0.85) {
            animated = true;
            startCounter();
        }
    });
}

/* 5. Product Category Filtering */
function initProductFilters() {
    const tabs = document.querySelectorAll('.products .tab-btn');
    const cards = document.querySelectorAll('.product-card');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            const category = tab.getAttribute('data-category');

            cards.forEach(card => {
                const cardCat = card.getAttribute('data-category');
                if (category === 'all' || category === cardCat) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

/* 6. Portfolio Category Filtering */
function initPortfolioFilters() {
    const tabs = document.querySelectorAll('.realizations .tab-btn');
    const cards = document.querySelectorAll('.portfolio-card');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            const category = tab.getAttribute('data-category');

            cards.forEach(card => {
                const cardCat = card.getAttribute('data-category');
                if (category === 'all' || category === cardCat) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

/* 7. Testimonial Carousel Slider */
function initTestimonialCarousel() {
    const track = document.querySelector('.testimonial-track');
    const slides = document.querySelectorAll('.testimonial-slide');
    const dots = document.querySelectorAll('.carousel-dots .dot');

    if (!track || slides.length === 0) return;

    let currentIndex = 0;

    function goToSlide(index) {
        currentIndex = index;
        const isRTL = document.documentElement.getAttribute('dir') === 'rtl';
        const offset = isRTL ? index * 100 : -index * 100;
        track.style.transform = `translateX(${offset}%)`;

        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
    }

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => goToSlide(index));
    });

    setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        goToSlide(currentIndex);
    }, 5000);
}

/* 8. Modal Management */
function initModals() {
    const quoteModal = document.getElementById('quoteModal');
    const modalCloseBtns = document.querySelectorAll('.modal-close');
    const openQuoteBtns = document.querySelectorAll('[data-open-quote]');
    const solutionSelect = document.getElementById('modalSolutionSelect');

    openQuoteBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const subject = btn.getAttribute('data-subject');
            if (subject && solutionSelect) {
                solutionSelect.value = subject;
            }
            if (quoteModal) {
                quoteModal.classList.add('active');
            }
        });
    });

    modalCloseBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            if (quoteModal) quoteModal.classList.remove('active');
        });
    });

    if (quoteModal) {
        quoteModal.addEventListener('click', (e) => {
            if (e.target === quoteModal) {
                quoteModal.classList.remove('active');
            }
        });
    }
}

/* 9. Contact Form & Modal Form Submission Feedback */
function initContactForm() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            showToast('Votre demande a bien été envoyée. Notre équipe vous contactera dans les plus brefs délais.');

            form.reset();

            const modal = form.closest('.modal-overlay');
            if (modal) {
                modal.classList.remove('active');
            }
        });
    });
}

function showToast(message) {
    let toast = document.getElementById('toast-notification');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast-notification';
        toast.className = 'toast-notification';
        document.body.appendChild(toast);
    }

    toast.innerHTML = `<i class="fa-solid fa-circle-check" style="color:#63C4C4; font-size:1.2rem;"></i> <span>${message}</span>`;
    toast.classList.add('show');

    setTimeout(() => {
        toast.classList.remove('show');
    }, 4500);
}

/* 10. French / English Language Switcher */
const translations = {
    fr: {
        navHome: "Accueil",
        navAbout: "À propos",
        navSolutions: "Solutions",
        navProducts: "Produits",
        navServices: "Services",
        navRealizations: "Réalisations",
        navContact: "Contact",
        btnQuote: "Demander un devis",
        heroTag: "EXPERT SÉCURITÉ ÉLECTRONIQUE",
        heroTitle: "Des solutions intelligentes pour une sécurité <span class='highlight'>sans compromis</span>",
        heroDesc: "Nous concevons, intégrons et installons des solutions de sécurité électronique et de technologie intelligente adaptées aux entreprises, institutions et particuliers.",
        btnDiscover: "Découvrir nos solutions",
        stat1Label: "Solutions déployées",
        stat2Label: "Clients accompagnés",
        stat3Label: "Années d’expertise",
        stat4Label: "Support technique",
        solutionsTitle: "Nos solutions",
        solutionsSub: "Une technologie pensée pour protéger, connecter et simplifier.",
        aboutTitle: "Votre partenaire technologique de confiance",
        whyTitle: "Pourquoi nous choisir ?",
        processTitle: "Notre processus d'intervention",
        realizationsTitle: "Nos réalisations",
        testimonialsTitle: "Ils nous font confiance",
        ctaTitle: "Un projet de sécurité ? Parlons-en.",
        ctaSub: "Notre équipe vous accompagne pour concevoir une solution adaptée à vos besoins.",
        contactTitle: "Contactez notre équipe"
    },
    en: {
        navHome: "Home",
        navAbout: "About Us",
        navSolutions: "Solutions",
        navProducts: "Products",
        navServices: "Services",
        navRealizations: "Projects",
        navContact: "Contact",
        btnQuote: "Get a Quote",
        heroTag: "ELECTRONIC SECURITY EXPERT",
        heroTitle: "Smart solutions for security <span class='highlight'>without compromise</span>",
        heroDesc: "We design, integrate, and install electronic security and smart technology solutions tailored for enterprises, institutions, and private clients.",
        btnDiscover: "Discover Our Solutions",
        stat1Label: "Deployed Solutions",
        stat2Label: "Satisfied Clients",
        stat3Label: "Years of Expertise",
        stat4Label: "Technical Support",
        solutionsTitle: "Our Solutions",
        solutionsSub: "Technology engineered to protect, connect, and simplify.",
        aboutTitle: "Your Trusted Technology Partner",
        whyTitle: "Why Choose Us?",
        processTitle: "Our Implementation Process",
        realizationsTitle: "Our Projects",
        testimonialsTitle: "Trusted by Industry Leaders",
        ctaTitle: "Have a security project? Let's talk.",
        ctaSub: "Our team guides you to design a solution tailored to your exact needs.",
        contactTitle: "Contact Our Team"
    }
};

function initLanguageSwitcher() {
    const frBtns = document.querySelectorAll('[data-lang="fr"]');
    const enBtns = document.querySelectorAll('[data-lang="en"]');

    function setLanguage(lang) {
        document.documentElement.setAttribute('lang', lang);
        document.documentElement.setAttribute('dir', 'ltr');

        if (lang === 'en') {
            frBtns.forEach(b => b.classList.remove('active'));
            enBtns.forEach(b => b.classList.add('active'));
        } else {
            enBtns.forEach(b => b.classList.remove('active'));
            frBtns.forEach(b => b.classList.add('active'));
        }

        // Translate text contents
        const t = translations[lang];
        if (!t) return;

        document.querySelectorAll('[data-i18n]').forEach(elem => {
            const key = elem.getAttribute('data-i18n');
            if (t[key]) {
                elem.innerHTML = t[key];
            }
        });
    }

    frBtns.forEach(btn => btn.addEventListener('click', () => setLanguage('fr')));
    enBtns.forEach(btn => btn.addEventListener('click', () => setLanguage('en')));
}

