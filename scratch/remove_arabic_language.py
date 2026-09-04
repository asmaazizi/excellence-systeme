import os, glob, re

# 1. Update all HTML files (root and activites/)
html_files = glob.glob("*.html") + glob.glob("activites/*.html")
updated_html_count = 0

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove the AR language button
    new_content = re.sub(r'<button type="button" class="lang-btn" data-lang="ar">AR</button>\s*', '', content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated_html_count += 1

print(f"Removed AR button from {updated_html_count} HTML files!")

# 2. Update js/main.js to remove 'ar' key from translations and fallback from 'ar' to 'fr'
with open("js/main.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Remove 'ar: { ... }' from translations
js_content = re.sub(r',\s*ar:\s*\{.*?\n\s*\}', '', js_content, flags=re.DOTALL)

# In initLanguageSwitcher, fallback 'ar' to 'fr'
js_content = js_content.replace("document.documentElement.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');", "document.documentElement.setAttribute('dir', 'ltr');")
js_content = js_content.replace("const savedLang = localStorage.getItem('preferredLang');", "let savedLang = localStorage.getItem('preferredLang'); if (savedLang === 'ar') savedLang = 'fr';")

with open("js/main.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Updated js/main.js to remove Arabic language dictionary and fallback to FR!")
