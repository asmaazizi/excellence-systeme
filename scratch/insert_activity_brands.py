import os

activity_brands = {
    "detection-incendie.html": (
        "Détection Incendie & S.S.I.",
        [
            ("TELETEK", "../assets/marques_activites/image1.jpeg"),
            ("ELKRON", "../assets/marques_activites/image2.jpeg"),
            ("NUGELEC", "../assets/marques_activites/image3.jpeg"),
            ("DETNOV", "../assets/marques_activites/image14.jpeg"),
            ("FINSECUR", "../assets/marques_activites/image33.jpeg"),
            ("COMELIT", "../assets/marques_activites/image34.jpeg")
        ]
    ),
    "anti-intrusion.html": (
        "Alarme Anti-intrusion & Périmétrique",
        [
            ("TELETEK", "../assets/marques_activites/image1.jpeg"),
            ("SOMFY", "../assets/marques_activites/image5.jpeg"),
            ("SECOLINK", "../assets/marques_activites/image4.jpeg"),
            ("ELKRON", "../assets/marques_activites/image2.jpeg"),
            ("DAHUA", "../assets/marques_activites/image12.jpeg"),
            ("AJAX", "../assets/marques_activites/image35.jpeg")
        ]
    ),
    "reseau-informatique.html": (
        "Réseaux Informatiques & Datacenter",
        [
            ("UBIQUITI", "../assets/marques_activites/image6.jpeg"),
            ("RUIJIE | REYEE", "../assets/marques_activites/image7.jpeg"),
            ("CISCO", "../assets/marques_activites/image8.jpeg"),
            ("ARUBA", "../assets/marques_activites/image9.jpeg"),
            ("GRANDSTREAM", "../assets/marques_activites/image10.jpeg"),
            ("NEXANS", "../assets/marques_activites/image36.jpeg"),
            ("IPCOM", "../assets/marques_activites/image40.jpeg"),
            ("AGINODE", "../assets/marques_activites/image37.jpeg")
        ]
    ),
    "videosurveillance.html": (
        "Vidéosurveillance IP & Vidéoprotection",
        [
            ("UNV (UNIVIEW)", "../assets/marques_activites/image11.jpeg"),
            ("HIKVISION", "../assets/marques_activites/image12.jpeg"),
            ("UNIARCH", "../assets/marques_activites/image15.jpeg"),
            ("EZVIZ", "../assets/marques_activites/image39.jpeg"),
            ("BOSCH", "../assets/marques_activites/image30.jpeg"),
            ("AXIS", "../assets/marques_activites/image31.jpeg"),
            ("IMOU", "../assets/marques_activites/image32.jpeg")
        ]
    ),
    "telephonie-ip.html": (
        "Téléphonie IP & Standard VoIP",
        [
            ("GRANDSTREAM", "../assets/marques_activites/image10.jpeg"),
            ("FANVIL", "../assets/marques_activites/image13.jpeg"),
            ("ALCATEL-LUCENT", "../assets/marques_activites/image17.jpeg"),
            ("NEC", "../assets/marques_activites/image42.jpeg"),
            ("CISCO", "../assets/marques_activites/image8.jpeg")
        ]
    ),
    "controle-acces.html": (
        "Contrôle d'Accès & Biométrie",
        [
            ("ZKTECO", "../assets/marques_activites/image20.jpeg"),
            ("HIKVISION", "../assets/marques_activites/image16.jpeg"),
            ("CDVI", "../assets/marques_activites/image21.jpeg"),
            ("SUPREMA", "../assets/marques_activites/image22.jpeg"),
            ("SLINEX", "../assets/marques_activites/image19.jpeg"),
            ("DAHUA", "../assets/marques_activites/image12.jpeg"),
            ("WDLINK", "../assets/marques_activites/image48.jpeg"),
            ("UNV", "../assets/marques_activites/image11.jpeg"),
            ("ALCAD", "../assets/marques_activites/image44.jpeg")
        ]
    ),
    "audiovisuel.html": (
        "Audiovisuel & Sonorisation",
        [
            ("BIAMP", "../assets/marques_activites/image24.jpeg"),
            ("HIKVISION", "../assets/marques_activites/image16.jpeg"),
            ("BOSE", "../assets/marques_activites/image23.jpeg"),
            ("SONANCE", "../assets/marques_activites/image51.jpeg"),
            ("PHONIC", "../assets/marques_activites/image52.jpeg")
        ]
    ),
    "domotique.html": (
        "Domotique & Smart Building",
        [
            ("iNELS", "../assets/marques_activites/image26.jpeg"),
            ("SHELLY", "../assets/marques_activites/image28.jpeg"),
            ("EAE", "../assets/marques_activites/image53.jpeg"),
            ("i.LUXUS", "../assets/marques_activites/image29.jpeg"),
            ("LOXONE", "../assets/marques_activites/image54.jpeg")
        ]
    ),
    "motorisation.html": (
        "Motorisation Portail & Garage",
        [
            ("BENINCA", "../assets/marques_activites/image37.jpeg"),
            ("PROTECO", "../assets/marques_activites/image38.jpeg"),
            ("V2", "../assets/marques_activites/image3.jpeg"),
            ("NICE", "../assets/marques_activites/image55.jpeg"),
            ("SOMFY", "../assets/marques_activites/image5.jpeg"),
            ("BFT", "../assets/marques_activites/image56.jpeg")
        ]
    ),
    "reseau-optique.html": (
        "Réseau Optique & Fibre Optique",
        [
            ("AGINODE", "../assets/marques_activites/image37.jpeg"),
            ("NEXANS", "../assets/marques_activites/image36.jpeg"),
            ("MMC", "../assets/marques_activites/image49.jpeg"),
            ("CORNING", "../assets/marques_activites/image50.jpeg")
        ]
    ),
    "teledistribution.html": (
        "Télédistribution Collective & IP TV",
        [
            ("TELEVES", "../assets/marques_activites/image46.jpeg"),
            ("TELETEK", "../assets/marques_activites/image1.jpeg"),
            ("SAB", "../assets/marques_activites/image47.jpeg")
        ]
    )
}

activites_dir = "activites"
updated_count = 0

for filename, (title, brands) in activity_brands.items():
    filepath = os.path.join(activites_dir, filename)
    if not os.path.exists(filepath):
        print("Missing file:", filepath)
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    cards_html = ""
    for name, img_path in brands:
        cards_html += f'''
                <div class="activity-brand-card">
                    <div class="brand-logo-holder">
                        <img src="{img_path}" alt="Logo {name}">
                    </div>
                    <span class="brand-name-tag">{name}</span>
                </div>'''

    section_html = f'''
    <!-- SECTION MARQUES SPÉCIFIQUES À L'ACTIVITÉ (3D GLASS HOVER GRID) -->
    <section class="activity-brands-section" style="padding: 70px 0; background: #131518; border-top: 1px solid var(--charcoal-border);">
        <div class="container">
            <div class="text-center" style="margin-bottom: 40px;">
                <div class="section-tag">
                    <i class="fa-solid fa-certificate"></i> <span>CONSTRUCTEURS & MARQUES ÉPROUVÉES</span>
                </div>
                <h2 class="section-title">Marques & Partenaires Officiels</h2>
                <p class="section-subtitle">
                    Nous intégrons et maintenons les équipements des leaders mondiaux certifiés pour {title}.
                </p>
            </div>

            <div class="activity-brand-grid">
                {cards_html}
            </div>
        </div>
    </section>
'''

    # Remove previous section if present
    if 'class="activity-brands-section"' in html:
        import re
        html = re.sub(r'<!-- SECTION MARQUES SPÉCIFIQUES.*?<footer', '<footer', html, flags=re.DOTALL)

    # Insert section before footer
    if '<!-- Footer -->' in html:
        html = html.replace('<!-- Footer -->', section_html + '\n    <!-- Footer -->')
    elif '<footer' in html:
        html = html.replace('<footer', section_html + '\n    <footer')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    updated_count += 1
    print(f"Successfully inserted brands section into {filename}")

print(f"Total updated files: {updated_count}")
