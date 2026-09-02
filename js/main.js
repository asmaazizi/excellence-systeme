/* ==========================================
   EXCELLENCE SYSTÈME - MULTI-PAGE INTERACTIVE JS
   ========================================== */

document.addEventListener('DOMContentLoaded', () => {
    initActiveNavLink();
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

/* 0. Highlight Active Navigation Link based on current page URL */
function initActiveNavLink() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (currentPath === '' && href === 'index.html')) {
            link.classList.add('active');
        } else if (href && !href.startsWith('#') && !currentPath.includes(href)) {
            link.classList.remove('active');
        }
    });
}

/* 1. Header Scroll Effect */
function initHeaderScroll() {
    const header = document.querySelector('.site-header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
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

    if (!toggleBtn || !navMenu) return;

    toggleBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        const icon = toggleBtn.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-xmark');
        }
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

    const statsSection = document.querySelector('.trust-bar');
    if (statsSection) {
        const rect = statsSection.getBoundingClientRect();
        if (rect.top <= window.innerHeight) {
            animated = true;
            startCounter();
        }
    }
}

/* 5. Product Category Filtering */
function initProductFilters() {
    const tabs = document.querySelectorAll('.products .tab-btn');
    const cards = document.querySelectorAll('.product-card');

    if (tabs.length === 0 || cards.length === 0) return;

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
    const tabs = document.querySelectorAll('.realisations .tab-btn');
    const cards = document.querySelectorAll('.portfolio-card');

    if (tabs.length === 0 || cards.length === 0) return;

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

/* 9. Contact Form & Submission Toast */
function initContactForm() {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            showToast('Votre demande a bien été transmise à Excellence Système. Notre équipe vous recontactera sous 24h.');

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

/* 10. Multi-Page Language Switcher (FR / EN / AR) */
const translations = {
    fr: {
        navHome: "Accueil",
        navAbout: "À propos",
        navActivities: "Nos activités",
        navProducts: "Produits",
        navServices: "Services",
        navRealizations: "Réalisations",
        navContact: "Contact",
        btnQuote: "Demander un devis",
        heroTag: "EXPERT EN COURANT FAIBLE & SÉCURITÉ ÉLECTRONIQUE",
        heroTitle: "Votre partenaire de confiance en <span class='highlight'>courant faible et sécurité électronique</span>",
        heroDesc: "Plus de 10 ans d'expérience dans le conseil, la fourniture, l'intégration et la maintenance de solutions de sécurité électronique, réseaux informatiques et domotique au Maroc.",
        btnDiscover: "Découvrir nos activités",
        stat1Label: "Projets & Solutions déployés",
        stat2Label: "Clients accompagnés au Maroc",
        stat3Label: "Années d’expertise éprouvée",
        stat4Label: "Support technique & maintenance",
        solutionsTitle: "Nos domaines d'activités",
        solutionsSub: "Une expertise globale pour sécuriser, connecter et automatiser vos espaces.",
        aboutTitle: "Votre partenaire technologique de confiance",
        whyTitle: "Pourquoi choisir Excellence Système ?",
        processTitle: "Notre méthodologie d'intervention",
        realizationsTitle: "Nos réalisations",
        testimonialsTitle: "Ils nous font confiance",
        ctaTitle: "Un projet de sécurité ou réseau ? Parlons-en.",
        ctaSub: "Notre équipe vous accompagne de l'étude du besoin jusqu'à l'installation et le support 24/7.",
        contactTitle: "Contactez Excellence Système"
    },
    en: {
        navHome: "Home",
        navAbout: "About Us",
        navActivities: "Our Activities",
        navProducts: "Products",
        navServices: "Services",
        navRealizations: "Projects",
        navContact: "Contact",
        btnQuote: "Get a Quote",
        heroTag: "LOW CURRENT & ELECTRONIC SECURITY EXPERT",
        heroTitle: "Your trusted partner in <span class='highlight'>low current & electronic security</span>",
        heroDesc: "Over 10 years of expertise in consulting, supply, integration, and maintenance of electronic security, IT networking, and smart home solutions in Morocco.",
        btnDiscover: "Explore Our Activities",
        stat1Label: "Deployed Projects",
        stat2Label: "Satisfied Clients",
        stat3Label: "Years of Proven Expertise",
        stat4Label: "Technical Support & Maintenance",
        solutionsTitle: "Our Core Activities",
        solutionsSub: "Comprehensive expertise to secure, connect, and automate your premises.",
        aboutTitle: "Your Trusted Technology Partner",
        whyTitle: "Why Choose Excellence Système?",
        processTitle: "Our Implementation Methodology",
        realizationsTitle: "Our Projects",
        testimonialsTitle: "Trusted by Industry Leaders",
        ctaTitle: "Have a security or IT project? Let's talk.",
        ctaSub: "Our team supports you from initial audit to installation and 24/7 technical support.",
        contactTitle: "Contact Excellence Système"
    },
    ar: {
        navHome: "الرئيسية",
        navAbout: "عن الشركة",
        navActivities: "أنشطتنا",
        navProducts: "المنتجات",
        navServices: "الخدمات",
        navRealizations: "مشاريعنا",
        navContact: "اتصل بنا",
        btnQuote: "طلب استشارة / سعر",
        heroTag: "خبير التيار المنخفض والأمان الإلكتروني",
        heroTitle: "شريكك الموثوق في <span class='highlight'>التيار المنخفض والأمان الإلكتروني</span>",
        heroDesc: "أكثر من 10 سنوات من الخبرة في الاستشارة والتوريد والتكامل والصيانة لحلول الأمان الإلكتروني والشبكات والمنزل الذكي بالمغرب.",
        btnDiscover: "اكتشف أنشطتنا",
        stat1Label: "مشروع ونظام تم تشغيله",
        stat2Label: "عميل مرافَق بالمغرب",
        stat3Label: "سنوات من الخبرة المثبتة",
        stat4Label: "دعم فني وصيانة متواصلة",
        solutionsTitle: "مجالات أنشطتنا",
        solutionsSub: "خبرة شاملة لتأمين وربط وأتمتة مساحاتكم.",
        aboutTitle: "شريكك التكنولوجي الموثوق",
        whyTitle: "لماذا تختار التميز للنظم؟",
        processTitle: "مراحل تنفيذ مشروعك",
        realizationsTitle: "أبرز إنجازاتنا",
        testimonialsTitle: "ثقة علمائنا وشركائنا",
        ctaTitle: "هل لديك مشروع أمان أو شبكات؟ لنناقشه معاً.",
        ctaSub: "فريقنا المتخصص في خدمتك لتصميم وتطبيق أفضل الحلول المناسبة لاحتياجاتك.",
        contactTitle: "تواصل مع فريقنا"
    }
};

function initLanguageSwitcher() {
    const langBtns = document.querySelectorAll('.lang-btn');

    function setLanguage(lang) {
        document.documentElement.setAttribute('lang', lang);
        document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');

        langBtns.forEach(b => {
            b.classList.toggle('active', b.getAttribute('data-lang') === lang);
        });

        const t = translations[lang];
        if (!t) return;

        document.querySelectorAll('[data-i18n]').forEach(elem => {
            const key = elem.getAttribute('data-i18n');
            if (t[key]) {
                elem.innerHTML = t[key];
            }
        });
    }

    langBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.getAttribute('data-lang');
            setLanguage(lang);
        });
    });
}
