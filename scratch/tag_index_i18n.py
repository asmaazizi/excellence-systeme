with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Navbar links
html = html.replace('href="activites.html" class="nav-link">', 'href="activites.html" class="nav-link" data-i18n="navActivities">')
html = html.replace('href="services.html" class="nav-link">', 'href="services.html" class="nav-link" data-i18n="navServices">')
html = html.replace('href="marques.html" class="nav-link">', 'href="marques.html" class="nav-link" data-i18n="navBrands">')

# Dropdown Items
html = html.replace('href="activites/detection-incendie.html" class="dropdown-item">', 'href="activites/detection-incendie.html" class="dropdown-item" data-i18n="actDetection">')
html = html.replace('href="activites/anti-intrusion.html" class="dropdown-item">', 'href="activites/anti-intrusion.html" class="dropdown-item" data-i18n="actIntrusion">')
html = html.replace('href="activites/reseau-informatique.html" class="dropdown-item">', 'href="activites/reseau-informatique.html" class="dropdown-item" data-i18n="actReseau">')
html = html.replace('href="activites/videosurveillance.html" class="dropdown-item">', 'href="activites/videosurveillance.html" class="dropdown-item" data-i18n="actVideo">')
html = html.replace('href="activites/telephonie-ip.html" class="dropdown-item">', 'href="activites/telephonie-ip.html" class="dropdown-item" data-i18n="actTelephonie">')
html = html.replace('href="activites/controle-acces.html" class="dropdown-item">', 'href="activites/controle-acces.html" class="dropdown-item" data-i18n="actAcces">')
html = html.replace('href="activites/audiovisuel.html" class="dropdown-item">', 'href="activites/audiovisuel.html" class="dropdown-item" data-i18n="actAudio">')
html = html.replace('href="activites/domotique.html" class="dropdown-item">', 'href="activites/domotique.html" class="dropdown-item" data-i18n="actDomotique">')
html = html.replace('href="activites/motorisation.html" class="dropdown-item">', 'href="activites/motorisation.html" class="dropdown-item" data-i18n="actMotorisation">')
html = html.replace('href="activites/reseau-optique.html" class="dropdown-item">', 'href="activites/reseau-optique.html" class="dropdown-item" data-i18n="actOptique">')
html = html.replace('href="activites/teledistribution.html" class="dropdown-item">', 'href="activites/teledistribution.html" class="dropdown-item" data-i18n="actTeledist">')

html = html.replace('href="services.html#hotellerie" class="dropdown-item">', 'href="services.html#hotellerie" class="dropdown-item" data-i18n="srvHotel">')
html = html.replace('href="services.html#villas" class="dropdown-item">', 'href="services.html#villas" class="dropdown-item" data-i18n="srvVilla">')
html = html.replace('href="services.html#entreprises" class="dropdown-item">', 'href="services.html#entreprises" class="dropdown-item" data-i18n="srvEntreprise">')
html = html.replace('href="services.html#administrations" class="dropdown-item">', 'href="services.html#administrations" class="dropdown-item" data-i18n="srvAdmin">')

# Activities section headers
html = html.replace('<span>NOS DOMAINES D\'EXPERTISE ÉPROUVÉS</span>', '<span data-i18n="homeExpertiseTag">NOS DOMAINES D\'EXPERTISE ÉPROUVÉS</span>')
html = html.replace('<h2 class="section-title">Nos Activités Principales</h2>', '<h2 class="section-title" data-i18n="homeExpertiseTitle">Nos Activités Principales</h2>')
html = html.replace('<p class="section-subtitle">', '<p class="section-subtitle" data-i18n="homeExpertiseSub">')

# Cards
html = html.replace('<div class="card-badge"><i class="fa-solid fa-fire-flame-curved"></i> Certifié S.S.I.</div>', '<div class="card-badge" data-i18n="card1Badge"><i class="fa-solid fa-fire-flame-curved"></i> Certifié S.S.I.</div>')
html = html.replace('<h3 class="card-title">Détection Incendie</h3>', '<h3 class="card-title" data-i18n="card1Title">Détection Incendie</h3>')
html = html.replace('<p class="card-description">Centrales ECS/CMSI conventionnelles et adressables conformes aux normes ERP.</p>', '<p class="card-description" data-i18n="card1Desc">Centrales ECS/CMSI conventionnelles et adressables conformes aux normes ERP.</p>')

html = html.replace('<div class="card-badge"><i class="fa-solid fa-video"></i> Ultra HD 4K</div>', '<div class="card-badge" data-i18n="card2Badge"><i class="fa-solid fa-video"></i> Ultra HD 4K</div>')
html = html.replace('<h3 class="card-title">Vidéosurveillance IP</h3>', '<h3 class="card-title" data-i18n="card2Title">Vidéosurveillance IP</h3>')
html = html.replace('<p class="card-description">Caméras motorisées PTZ, reconnaissance de plaques LPR et serveurs NVR réseau.</p>', '<p class="card-description" data-i18n="card2Desc">Caméras motorisées PTZ, reconnaissance de plaques LPR et serveurs NVR réseau.</p>')

html = html.replace('<div class="card-badge"><i class="fa-solid fa-network-wired"></i> Cat6 / Cat7 / Fibre</div>', '<div class="card-badge" data-i18n="card3Badge"><i class="fa-solid fa-network-wired"></i> Cat6 / Cat7 / Fibre</div>')
html = html.replace('<h3 class="card-title">Réseau Informatique</h3>', '<h3 class="card-title" data-i18n="card3Title">Réseau Informatique</h3>')
html = html.replace('<p class="card-description">Câblage structuré, baies de brassage serveur et switching PoE administrable.</p>', '<p class="card-description" data-i18n="card3Desc">Câblage structuré, baies de brassage serveur et switching PoE administrable.</p>')

html = html.replace('<div class="card-badge"><i class="fa-solid fa-fingerprint"></i> Biométrie & RFID</div>', '<div class="card-badge" data-i18n="card4Badge"><i class="fa-solid fa-fingerprint"></i> Biométrie & RFID</div>')
html = html.replace('<h3 class="card-title">Contrôle d\'Accès</h3>', '<h3 class="card-title" data-i18n="card4Title">Contrôle d\'Accès</h3>')
html = html.replace('<p class="card-description">Reconnaissance faciale, tourniquets piétons, badges RFID et pointeuses horaires.</p>', '<p class="card-description" data-i18n="card4Desc">Reconnaissance faciale, tourniquets piétons, badges RFID et pointeuses horaires.</p>')

html = html.replace('<div class="card-badge"><i class="fa-solid fa-house-signal"></i> iNELS & KNX</div>', '<div class="card-badge" data-i18n="card5Badge"><i class="fa-solid fa-house-signal"></i> iNELS & KNX</div>')
html = html.replace('<h3 class="card-title">Domotique & GTB</h3>', '<h3 class="card-title" data-i18n="card5Title">Domotique & GTB</h3>')
html = html.replace('<p class="card-description">Gestion technique des bâtiments, automatisation d\'éclairage et régulation HVAC.</p>', '<p class="card-description" data-i18n="card5Desc">Gestion technique des bâtiments, automatisation d\'éclairage et régulation HVAC.</p>')

html = html.replace('<div class="card-badge"><i class="fa-solid fa-shield-cat"></i> Alarme Connectée</div>', '<div class="card-badge" data-i18n="card6Badge"><i class="fa-solid fa-shield-cat"></i> Alarme Connectée</div>')
html = html.replace('<h3 class="card-title">Système Anti-intrusion</h3>', '<h3 class="card-title" data-i18n="card6Title">Système Anti-intrusion</h3>')
html = html.replace('<p class="card-description">Protection périmétrique extérieure, détecteurs double technologie et sirènes.</p>', '<p class="card-description" data-i18n="card6Desc">Protection périmétrique extérieure, détecteurs double technologie et sirènes.</p>')

# Card action buttons
html = html.replace('class="card-action-btn">\n                            En savoir plus', 'class="card-action-btn" data-i18n="btnLearnMore">\n                            En savoir plus')
html = html.replace('class="card-action-btn">\n                            En savoir plus <i class="fa-solid fa-arrow-right"></i>', 'class="card-action-btn" data-i18n="btnLearnMore">\n                            En savoir plus <i class="fa-solid fa-arrow-right"></i>')
html = html.replace('Explorer nos 11 activités intégrales <i class="fa-solid fa-arrow-right"></i>', '<span data-i18n="btnSeeAllActivities">Explorer nos 11 activités intégrales <i class="fa-solid fa-arrow-right"></i></span>')

# About section
html = html.replace('<span>À PROPOS D\'EXCELLENCE SYSTÈME</span>', '<span data-i18n="aboutTag">À PROPOS D\'EXCELLENCE SYSTÈME</span>')
html = html.replace('<h2 class="section-title">Plus de 10 ans d\'expertise technique au Maroc</h2>', '<h2 class="section-title" data-i18n="aboutTitle">Plus de 10 ans d\'expertise technique au Maroc</h2>')
html = html.replace('En savoir plus sur notre entreprise <i class="fa-solid fa-arrow-right"></i>', '<span data-i18n="btnAboutMore">En savoir plus sur notre entreprise <i class="fa-solid fa-arrow-right"></i></span>')

# Sectors section
html = html.replace('<span>CHAMPS D\'INTERVENTION</span>', '<span data-i18n="homeSectorsTag">CHAMPS D\'INTERVENTION</span>')
html = html.replace('<h2 class="section-title">Solutions Adaptées à Votre Secteur</h2>', '<h2 class="section-title" data-i18n="homeSectorsTitle">Solutions Adaptées à Votre Secteur</h2>')
html = html.replace('<h3>Hôtellerie & Resorts</h3>', '<h3 data-i18n="sec1Title">Hôtellerie & Resorts</h3>')
html = html.replace('<p>Télédistribution IP TV, Wi-Fi très haute densité, serrures à cartes magnétiques & sonorisation d\'ambiance.</p>', '<p data-i18n="sec1Desc">Télédistribution IP TV, Wi-Fi très haute densité, serrures à cartes magnétiques & sonorisation d\'ambiance.</p>')

html = html.replace('<h3>Villas & Résidences</h3>', '<h3 data-i18n="sec2Title">Villas & Résidences</h3>')
html = html.replace('<p>Domotique iNELS, alarme anti-intrusion connectée, visiophonie et contrôle d\'accès sur smartphone.</p>', '<p data-i18n="sec2Desc">Domotique iNELS, alarme anti-intrusion connectée, visiophonie et contrôle d\'accès sur smartphone.</p>')

html = html.replace('<h3>Entreprises & Tertiaire</h3>', '<h3 data-i18n="sec3Title">Entreprises & Tertiaire</h3>')
html = html.replace('<p>Baies informatiques Datacenter, vidéoprotection 4K, pointage horaire biométrique & téléphonie IP.</p>', '<p data-i18n="sec3Desc">Baies informatiques Datacenter, vidéoprotection 4K, pointage horaire biométrique & téléphonie IP.</p>')

html = html.replace('<h3>Industrie & Administrations</h3>', '<h3 data-i18n="sec4Title">Industrie & Administrations</h3>')
html = html.replace('<p>Détection incendie SSI globale, supervision GTB/GTC, tourniquets de sécurité et motorisation de barrières.</p>', '<p data-i18n="sec4Desc">Détection incendie SSI globale, supervision GTB/GTC, tourniquets de sécurité et motorisation de barrières.</p>')

# CTA Banner
html = html.replace('<span>PROJET COURANT FAIBLE OU SÉCURITÉ ?</span>', '<span data-i18n="ctaBannerTag">PROJET COURANT FAIBLE OU SÉCURITÉ ?</span>')
html = html.replace('<h2>Prêt à sécuriser & automatiser vos infrastructures ?</h2>', '<h2 data-i18n="ctaBannerTitle">Prêt à sécuriser & automatiser vos infrastructures ?</h2>')
html = html.replace('<p>Nos experts réalisent une étude de vos plans et un devis sur-mesure sous 24h.</p>', '<p data-i18n="ctaBannerSub">Nos experts réalisent une étude de vos plans et un devis sur-mesure sous 24h.</p>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with all data-i18n attributes!")
