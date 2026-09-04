import os, re

# Comprehensive translations dictionary to update js/main.js
new_translations_js = '''const translations = {
    fr: {
        navHome: "Accueil",
        navAbout: "À propos",
        navActivities: "Nos activités <i class='fa-solid fa-chevron-down' style='font-size:0.75rem; margin-left:4px;'></i>",
        navServices: "Nos services <i class='fa-solid fa-chevron-down' style='font-size:0.75rem; margin-left:4px;'></i>",
        navRealizations: "Nos réalisations",
        navBrands: "Nos marques",
        navContact: "Contact",
        btnQuote: "Demander un devis",

        actDetection: "<i class='fa-solid fa-fire-flame-curved'></i> Détection incendie",
        actIntrusion: "<i class='fa-solid fa-shield-cat'></i> Anti-intrusion",
        actReseau: "<i class='fa-solid fa-network-wired'></i> Réseau informatique",
        actVideo: "<i class='fa-solid fa-video'></i> Vidéosurveillance IP",
        actTelephonie: "<i class='fa-solid fa-phone-volume'></i> Téléphonie IP",
        actAcces: "<i class='fa-solid fa-fingerprint'></i> Contrôle d'accès",
        actAudio: "<i class='fa-solid fa-tv'></i> Audiovisuel",
        actDomotique: "<i class='fa-solid fa-house-signal'></i> Domotique & GTB",
        actMotorisation: "<i class='fa-solid fa-torii-gate'></i> Motorisation portail",
        actOptique: "<i class='fa-solid fa-bolt-lightning'></i> Réseau optique",
        actTeledist: "<i class='fa-solid fa-satellite-dish'></i> Télédistribution",

        srvHotel: "<i class='fa-solid fa-hotel'></i> Hôtellerie & Resorts",
        srvVilla: "<i class='fa-solid fa-house-chimney'></i> Villas & Résidences",
        srvEntreprise: "<i class='fa-solid fa-building'></i> Entreprises & Bureaux",
        srvAdmin: "<i class='fa-solid fa-landmark'></i> Administrations & Industrie",

        heroTag: "EXPERT EN COURANT FAIBLE & SÉCURITÉ ÉLECTRONIQUE",
        heroTitle: "Votre partenaire de confiance en <span class='highlight'>courant faible et sécurité électronique</span>",
        heroDesc: "Plus de 10 ans d'expérience dans le conseil, la fourniture, l'intégration et la maintenance de solutions de sécurité électronique, réseaux informatiques et domotique au Maroc.",
        btnDiscover: "Découvrir nos activités <i class='fa-solid fa-arrow-right'></i>",
        stat1Label: "Projets & Solutions déployés",
        stat2Label: "Clients accompagnés au Maroc",
        stat3Label: "Années d'expertise éprouvée",
        stat4Label: "Support technique & maintenance",

        homeExpertiseTag: "NOS DOMAINES D'EXPERTISE ÉPROUVÉS",
        homeExpertiseTitle: "Nos Activités Principales",
        homeExpertiseSub: "Découvrez nos domaines d'intervention clés. Cliquez sur une carte pour consulter nos équipements et réalisations réelles.",
        btnSeeAllActivities: "Explorer nos 11 activités intégrales <i class='fa-solid fa-arrow-right'></i>",

        card1Badge: "<i class='fa-solid fa-fire-flame-curved'></i> Certifié S.S.I.",
        card1Title: "Détection Incendie",
        card1Desc: "Centrales ECS/CMSI conventionnelles et adressables conformes aux normes ERP.",

        card2Badge: "<i class='fa-solid fa-video'></i> Ultra HD 4K",
        card2Title: "Vidéosurveillance IP",
        card2Desc: "Caméras motorisées PTZ, reconnaissance de plaques LPR et serveurs NVR réseau.",

        card3Badge: "<i class='fa-solid fa-network-wired'></i> Cat6 / Cat7 / Fibre",
        card3Title: "Réseau Informatique",
        card3Desc: "Câblage structuré, baies de brassage serveur et switching PoE administrable.",

        card4Badge: "<i class='fa-solid fa-fingerprint'></i> Biométrie & RFID",
        card4Title: "Contrôle d'Accès",
        card4Desc: "Reconnaissance faciale, tourniquets piétons, badges RFID et pointeuses horaires.",

        card5Badge: "<i class='fa-solid fa-house-signal'></i> iNELS & KNX",
        card5Title: "Domotique & GTB",
        card5Desc: "Gestion technique des bâtiments, automatisation d'éclairage et régulation HVAC.",

        card6Badge: "<i class='fa-solid fa-shield-cat'></i> Alarme Connectée",
        card6Title: "Système Anti-intrusion",
        card6Desc: "Protection périmétrique extérieure, détecteurs double technologie et sirènes.",

        btnLearnMore: "En savoir plus <i class='fa-solid fa-arrow-right'></i>",

        aboutTag: "À PROPOS D'EXCELLENCE SYSTÈME",
        aboutTitle: "Plus de 10 ans d'expertise technique au Maroc",
        aboutDesc1: "Excellence Système est votre partenaire de confiance spécialisé dans l'ingénierie, l'intégration et la maintenance des systèmes de courant faible, de sécurité électronique, de réseaux informatiques et de domotique.",
        aboutDesc2: "Nous accompagnons les entreprises grands comptes, les institutions publiques, le secteur hôtelier et les résidences privées en offrant des prestations complètes du conseil à la maintenance 24/7.",
        aboutBenefit1Title: "Conseil & Étude d'Ingénierie Préalable",
        aboutBenefit1Desc: "Analyse schématique de vos plans architecturaux et réglementaires.",
        aboutBenefit2Title: "Fourniture de Matériel Certifié & Intégration",
        aboutBenefit2Desc: "Déploiement rigoureux et paramétrage par des techniciens qualifiés.",
        btnAboutMore: "En savoir plus sur notre entreprise <i class='fa-solid fa-arrow-right'></i>",

        homeSectorsTag: "CHAMPS D'INTERVENTION",
        homeSectorsTitle: "Solutions Adaptées à Votre Secteur",
        homeSectorsSub: "Nos ingénieurs déploient des architectures de sécurité électronique et courant faible taillées pour vos besoins métiers.",
        sec1Title: "Hôtellerie & Resorts",
        sec1Desc: "Télédistribution IP TV, Wi-Fi très haute densité, serrures à cartes magnétiques & sonorisation d'ambiance.",
        sec2Title: "Villas & Résidences",
        sec2Desc: "Domotique iNELS, alarme anti-intrusion connectée, visiophonie et contrôle d'accès sur smartphone.",
        sec3Title: "Entreprises & Tertiaire",
        sec3Desc: "Baies informatiques Datacenter, vidéoprotection 4K, pointage horaire biométrique & téléphonie IP.",
        sec4Title: "Industrie & Administrations",
        sec4Desc: "Détection incendie SSI globale, supervision GTB/GTC, tourniquets de sécurité et motorisation de barrières.",
        btnDiscoverSector: "Découvrir l'offre <i class='fa-solid fa-chevron-right'></i>",

        ctaBannerTag: "PROJET COURANT FAIBLE OU SÉCURITÉ ?",
        ctaBannerTitle: "Prêt à sécuriser & automatiser vos infrastructures ?",
        ctaBannerSub: "Nos experts réalisent une étude de vos plans et un devis sur-mesure sous 24h.",
        btnFreeQuote: "<i class='fa-solid fa-paper-plane'></i> Demander un Devis Gratuit"
    },
    en: {
        navHome: "Home",
        navAbout: "About Us",
        navActivities: "Our Activities <i class='fa-solid fa-chevron-down' style='font-size:0.75rem; margin-left:4px;'></i>",
        navServices: "Our Services <i class='fa-solid fa-chevron-down' style='font-size:0.75rem; margin-left:4px;'></i>",
        navRealizations: "Projects",
        navBrands: "Our Brands",
        navContact: "Contact",
        btnQuote: "Get a Quote",

        actDetection: "<i class='fa-solid fa-fire-flame-curved'></i> Fire Detection",
        actIntrusion: "<i class='fa-solid fa-shield-cat'></i> Intrusion Alarm",
        actReseau: "<i class='fa-solid fa-network-wired'></i> IT Networking",
        actVideo: "<i class='fa-solid fa-video'></i> IP CCTV",
        actTelephonie: "<i class='fa-solid fa-phone-volume'></i> IP Telephony",
        actAcces: "<i class='fa-solid fa-fingerprint'></i> Access Control",
        actAudio: "<i class='fa-solid fa-tv'></i> Audio & Visual",
        actDomotique: "<i class='fa-solid fa-house-signal'></i> Smart Home & BMS",
        actMotorisation: "<i class='fa-solid fa-torii-gate'></i> Gate Automation",
        actOptique: "<i class='fa-solid fa-bolt-lightning'></i> Fiber Optics",
        actTeledist: "<i class='fa-solid fa-satellite-dish'></i> Satellite & TV",

        srvHotel: "<i class='fa-solid fa-hotel'></i> Hotels & Resorts",
        srvVilla: "<i class='fa-solid fa-house-chimney'></i> Villas & Residences",
        srvEntreprise: "<i class='fa-solid fa-building'></i> Corporate & Offices",
        srvAdmin: "<i class='fa-solid fa-landmark'></i> Public & Industry",

        heroTag: "LOW CURRENT & ELECTRONIC SECURITY EXPERT",
        heroTitle: "Your trusted partner in <span class='highlight'>low current & electronic security</span>",
        heroDesc: "Over 10 years of expertise in consulting, supply, integration, and maintenance of electronic security, IT networking, and smart home solutions in Morocco.",
        btnDiscover: "Explore Our Activities <i class='fa-solid fa-arrow-right'></i>",
        stat1Label: "Deployed Projects",
        stat2Label: "Satisfied Clients in Morocco",
        stat3Label: "Years of Proven Expertise",
        stat4Label: "Technical Support & Maintenance",

        homeExpertiseTag: "OUR PROVEN EXPERTISE",
        homeExpertiseTitle: "Our Main Activities",
        homeExpertiseSub: "Discover our key intervention domains. Click a card to view specs and real projects.",
        btnSeeAllActivities: "Explore all 11 activities <i class='fa-solid fa-arrow-right'></i>",

        card1Badge: "<i class='fa-solid fa-fire-flame-curved'></i> S.S.I. Certified",
        card1Title: "Fire Detection",
        card1Desc: "Conventional & addressable fire panels compliant with safety standards.",

        card2Badge: "<i class='fa-solid fa-video'></i> Ultra HD 4K",
        card2Title: "IP Surveillance",
        card2Desc: "PTZ motorized cameras, LPR plate recognition, and network NVR servers.",

        card3Badge: "<i class='fa-solid fa-network-wired'></i> Cat6 / Cat7 / Fiber",
        card3Title: "IT Networking",
        card3Desc: "Structured cabling, datacenter server racks, and managed PoE switches.",

        card4Badge: "<i class='fa-solid fa-fingerprint'></i> Biometrics & RFID",
        card4Title: "Access Control",
        card4Desc: "Facial recognition, turnstiles, RFID badges, and time attendance devices.",

        card5Badge: "<i class='fa-solid fa-house-signal'></i> iNELS & KNX",
        card5Title: "Smart Home & BMS",
        card5Desc: "Building management systems, lighting automation, and HVAC control.",

        card6Badge: "<i class='fa-solid fa-shield-cat'></i> Connected Alarm",
        card6Title: "Intrusion Alarm",
        card6Desc: "Perimeter outdoor protection, dual tech sensors, and loud alarm sirens.",

        btnLearnMore: "Learn more <i class='fa-solid fa-arrow-right'></i>",

        aboutTag: "ABOUT EXCELLENCE SYSTÈME",
        aboutTitle: "Over 10 Years of Technical Expertise in Morocco",
        aboutDesc1: "Excellence Système is your trusted engineering and maintenance partner for low current, electronic security, IT networks, and home automation.",
        aboutDesc2: "We support large corporations, public institutions, hotels, and luxury private residences with 24/7 support.",
        aboutBenefit1Title: "Consulting & Prior Engineering Study",
        aboutBenefit1Desc: "Schematic analysis of architectural plans and regulatory compliance.",
        aboutBenefit2Title: "Certified Hardware Supply & Integration",
        aboutBenefit2Desc: "Rigorous deployment and configuration by certified technicians.",
        btnAboutMore: "Learn more about our company <i class='fa-solid fa-arrow-right'></i>",

        homeSectorsTag: "FIELDS OF INTERVENTION",
        homeSectorsTitle: "Solutions Tailored to Your Sector",
        homeSectorsSub: "Our engineers deploy custom electronic security and low current architectures suited to your industry.",
        sec1Title: "Hotels & Resorts",
        sec1Desc: "IP TV, High-Density Wi-Fi, Magnetic Card Locks & Background Sound Systems.",
        sec2Title: "Villas & Residences",
        sec2Desc: "iNELS Smart Home, connected alarm, video intercom & mobile access control.",
        sec3Title: "Corporate & Offices",
        sec3Desc: "Datacenter IT racks, 4K video surveillance, biometric attendance & IP telephony.",
        sec4Title: "Industry & Public Sector",
        sec4Desc: "Global SSI Fire Detection, BMS supervision, security turnstiles & gate automation.",
        btnDiscoverSector: "Explore offering <i class='fa-solid fa-chevron-right'></i>",

        ctaBannerTag: "LOW CURRENT OR SECURITY PROJECT?",
        ctaBannerTitle: "Ready to secure & automate your premises?",
        ctaBannerSub: "Our experts audit your blueprints and deliver a custom quote within 24h.",
        btnFreeQuote: "<i class='fa-solid fa-paper-plane'></i> Request a Free Quote"
    },
    ar: {
        navHome: "الرئيسية",
        navAbout: "عن الشركة",
        navActivities: "أنشطتنا <i class='fa-solid fa-chevron-down' style='font-size:0.75rem; margin-right:4px;'></i>",
        navServices: "خدماتنا <i class='fa-solid fa-chevron-down' style='font-size:0.75rem; margin-right:4px;'></i>",
        navRealizations: "مشاريعنا",
        navBrands: "علاماتنا التجارية",
        navContact: "اتصل بنا",
        btnQuote: "طلب استشارة / سعر",

        actDetection: "<i class='fa-solid fa-fire-flame-curved'></i> كشف الحرائق",
        actIntrusion: "<i class='fa-solid fa-shield-cat'></i> إنذار السرقة",
        actReseau: "<i class='fa-solid fa-network-wired'></i> الشبكات المعلوماتية",
        actVideo: "<i class='fa-solid fa-video'></i> المراقبة بالفيديو IP",
        actTelephonie: "<i class='fa-solid fa-phone-volume'></i> الهاتفية الرقمية IP",
        actAcces: "<i class='fa-solid fa-fingerprint'></i> التحكم في الدخول",
        actAudio: "<i class='fa-solid fa-tv'></i> الأنظمة الصوتية والمرئية",
        actDomotique: "<i class='fa-solid fa-house-signal'></i> المنازل الذكية وGTB",
        actMotorisation: "<i class='fa-solid fa-torii-gate'></i> أتمتة البوابات",
        actOptique: "<i class='fa-solid fa-bolt-lightning'></i> الألياف البصرية",
        actTeledist: "<i class='fa-solid fa-satellite-dish'></i> البث الفضائي والمركزي",

        srvHotel: "<i class='fa-solid fa-hotel'></i> الفنادق والمنتجعات",
        srvVilla: "<i class='fa-solid fa-house-chimney'></i> الفيلات والإقامات",
        srvEntreprise: "<i class='fa-solid fa-building'></i> الشركات والمكاتب",
        srvAdmin: "<i class='fa-solid fa-landmark'></i> الإدارات والمصانع",

        heroTag: "خبير التيار المنخفض والأمان الإلكتروني",
        heroTitle: "شريكك الموثوق في <span class='highlight'>التيار المنخفض والأمان الإلكتروني</span>",
        heroDesc: "أكثر من 10 سنوات من الخبرة في الاستشارة والتوريد والتكامل والصيانة لحلول الأمان الإلكتروني والشبكات والمنزل الذكي بالمغرب.",
        btnDiscover: "اكتشف أنشطتنا <i class='fa-solid fa-arrow-left'></i>",
        stat1Label: "مشروع ونظام تم تشغيله",
        stat2Label: "عميل مرافَق بالمغرب",
        stat3Label: "سنوات من الخبرة المثبتة",
        stat4Label: "دعم فني وصيانة متواصلة 24/7",

        homeExpertiseTag: "مجالات خبرتنا المعتمدة",
        homeExpertiseTitle: "أنشطتنا الرئيسية",
        homeExpertiseSub: "اكتشف مجالات تدخلنا الرئيسية. انقر على إحدى البطاقات للاطلاع على معداتنا وإنجازاتنا الفعلية.",
        btnSeeAllActivities: "استكشف كافة أنشطتنا الـ 11 <i class='fa-solid fa-arrow-left'></i>",

        card1Badge: "<i class='fa-solid fa-fire-flame-curved'></i> معتمد S.S.I.",
        card1Title: "كشف الحرائق",
        card1Desc: "لوحات إنذار الحريق العادية والمعنونة المعتمدة وفق المعايير.",

        card2Badge: "<i class='fa-solid fa-video'></i> دقة فائقة 4K",
        card2Title: "المراقبة بالفيديو IP",
        card2Desc: "كاميرات PTZ المتحركة، التعرف على لوحات السيارات وسيرفرات NVR.",

        card3Badge: "<i class='fa-solid fa-network-wired'></i> Cat6 / Cat7 / ألياف",
        card3Title: "الشبكات المعلوماتية",
        card3Desc: "الكابلات المهيكلة، كبائن السيرفر والمفاتيح الذكية PoE.",

        card4Badge: "<i class='fa-solid fa-fingerprint'></i> البصمة والبطاقات الذكية",
        card4Title: "التحكم في الدخول",
        card4Desc: "التعرف على الوجه، البوابات الدوارة، بطاقات RFID وأجهزة الحضور.",

        card5Badge: "<i class='fa-solid fa-house-signal'></i> iNELS و KNX",
        card5Title: "المنازل الذكية و GTB",
        card5Desc: "إدارة المباني الذكية، أتمتة الإضاءة والتحكم في التكييف.",

        card6Badge: "<i class='fa-solid fa-shield-cat'></i> إنذار ذكي متصل",
        card6Title: "نظام إنذار السرقة",
        card6Desc: "حماية المحيط الخارجي، كاشفات حركة مزدوجة وسيرينات إنذار.",

        btnLearnMore: "معرفة المزيد <i class='fa-solid fa-arrow-left'></i>",

        aboutTag: "عن شركة التميز للنظم",
        aboutTitle: "أكثر من 10 سنوات من الخبرة التقنية بالمغرب",
        aboutDesc1: "التميز للنظم هي شريككم الموثوق المتخصص في الهندسة، التكامل وصيانة أنظمة التيار المنخفض، الأمان الإلكتروني، الشبكات والمنزل الذكي.",
        aboutDesc2: "نرافق الشركات الكبرى، المؤسسات العمومية، القطاع الفندقي والإقامات الخاصة بتقديم خدمات شاملة من الاستشارة إلى الصيانة على مدار الساعة.",
        aboutBenefit1Title: "استشارة ودراسة هندسية مسبقة",
        aboutBenefit1Desc: "تحليل مخططاتكم المعمارية والتنظيمية بدقة.",
        aboutBenefit2Title: "توريد معدات معتمدة وتكامل تقني",
        aboutBenefit2Desc: "تركيب دقيق وبرمجة من طرف تقنيين مؤهلين.",
        btnAboutMore: "معرفة المزيد عن شركتنا <i class='fa-solid fa-arrow-left'></i>",

        homeSectorsTag: "مجالات التدخل",
        homeSectorsTitle: "حلول مخصصة لقطاعكم",
        homeSectorsSub: "مهندسونا يصممون وينشرون بنى تحتية للأمان الإلكتروني والأنظمة المنخفضة التيار المصممة خصيصاً لاحتياجاتكم.",
        sec1Title: "الفنادق والمنتجعات",
        sec1Desc: "البث التلفزيوني الفضائي، واي فاي عالي الكثافة، أقفال البطاقات والنظام الصوتي.",
        sec2Title: "الفيلات والإقامات",
        sec2Desc: "منازل ذكية iNELS، إنذار متصل، إنتركوم فيديو والتحكم عبر الهاتف.",
        sec3Title: "الشركات والمكاتب",
        sec3Desc: "كبائن شبكات مراكز البيانات، مراقبة 4K، أجهزة الحضور بالبصمة وهاتفية IP.",
        sec4Title: "الإدارات والمصانع",
        sec4Desc: "كشف حريق شامل SSI، إدارة المباني GTB، بوابات أمان وأتمتة الحاجز.",
        btnDiscoverSector: "اكتشف العرض <i class='fa-solid fa-chevron-left'></i>",

        ctaBannerTag: "مشروع أنظمة أمان أو شبكات؟",
        ctaBannerTitle: "مستعد لتأمين وأتمتة منشآتك؟",
        ctaBannerSub: "خبراؤنا يقدمون دراسة لمخططاتكم وتقدير سعر في أقل من 24 ساعة.",
        btnFreeQuote: "<i class='fa-solid fa-paper-plane'></i> طلب تقدير سعر مجاني"
    }
};'''

# Update js/main.js
with open("js/main.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Replace translations object in js/main.js
js_content = re.sub(r'const translations = \{.*?\};', new_translations_js, js_content, flags=re.DOTALL)

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Updated js/main.js translations object!")
