import os, glob, re

# Search for all HTML files
html_files = glob.glob("*.html") + glob.glob("activites/*.html")
updated_count = 0

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    # Replace Email
    new_content = new_content.replace("contact@excellencesysteme.ma", "commercial.exsys@gmail.com")

    # Replace Phone numbers (Tel Fixe)
    new_content = new_content.replace("+212 5 22 34 56 78", "+212 5 25 32 42 88")
    new_content = new_content.replace("tel:+212522345678", "tel:+212525324288")
    new_content = new_content.replace("05 22 34 56 78", "05 25 32 42 88")

    # Replace GSM / WhatsApp 1
    new_content = new_content.replace("https://wa.me/212661123456", "https://wa.me/212668764271")
    new_content = new_content.replace("+212 6 61 12 34 56", "+212 6 68 76 42 71")
    new_content = new_content.replace("tel:+212661123456", "tel:+212668764271")
    new_content = new_content.replace("06 61 12 34 56", "06 68 76 42 71")

    # If contact.html, ensure second GSM is present
    if "contact.html" in filepath:
        if "+212 6 60 27 04 46" not in new_content:
            new_content = new_content.replace(
                '<a href="tel:+212668764271" class="contact-link-secondary"><i class="fa-solid fa-mobile-screen"></i> +212 6 68 76 42 71</a>',
                '<a href="tel:+212668764271" class="contact-link-secondary"><i class="fa-solid fa-mobile-screen"></i> GSM 1: +212 6 68 76 42 71</a>\n                                    <a href="tel:+212660270446" class="contact-link-secondary"><i class="fa-solid fa-mobile-screen"></i> GSM 2: +212 6 60 27 04 46</a>'
            )

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_count += 1
        print(f"Updated contact info in {filepath}")

print(f"Total updated HTML files with real contact info: {updated_count}")
