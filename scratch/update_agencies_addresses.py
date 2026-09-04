import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html') and not 'node_modules' in root:
            html_files.append(os.path.join(root, f))

print(f"Found {len(html_files)} HTML files to update address info.")

addr_marrakech = "1057, Lot Al Housna 2, ASKJOUR - Marrakech"
addr_agadir = "IMM 42, APP 166 ADRAR - Agadir"

footer_addr_replacement = '<i class="fa-solid fa-location-dot" style="color:#63C4C4; margin-right:8px;"></i> Marrakech: 1057 Lot Al Housna 2 | Agadir: Imm 42 App 166'
footer_addr_subpage_replacement = '<i class="fa-solid fa-location-dot" style="color:#63C4C4; margin-right:6px;"></i> Marrakech &amp; Agadir'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig_content = content

    # Replace footer address line
    content = re.sub(
        r'<i class="fa-solid fa-location-dot"[^>]*></i>\s*Blvd Zerktouni,\s*Casablanca',
        footer_addr_replacement if not file_path.startswith('./activites/') else footer_addr_subpage_replacement,
        content
    )
    content = re.sub(
        r'<i class="fa-solid fa-location-dot"[^>]*></i>\s*Casablanca,\s*Maroc',
        r'<i class="fa-solid fa-location-dot" style="color:#63C4C4;"></i> Marrakech & Agadir, Maroc',
        content
    )

    if content != orig_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer/location in {file_path}")

print("Footer addresses updated.")
