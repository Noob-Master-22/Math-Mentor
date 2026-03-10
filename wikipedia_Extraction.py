import wikipediaapi
import re
import os

wiki = wikipediaapi.Wikipedia('MathMentor/1.0', 'en')

# Map Wikipedia topics → your existing files
TOPIC_FILE_MAP = {
    "Derivative":                    "kb/calculus.md",
    "Integral":                      "kb/calculus.md",
    "L'Hôpital's rule":              "kb/calculus.md",
    "Chain rule":                    "kb/calculus.md",
    "Integration by parts":          "kb/calculus.md",
    "Quadratic equation":            "kb/algebra.md",
    "Binomial theorem":              "kb/algebra.md",
    "Logarithm":                     "kb/algebra.md",
    "Bayes' theorem":                "kb/probability.md",
    "Binomial distribution":         "kb/probability.md",
    "Probability theory":            "kb/probability.md",
    "Matrix (mathematics)":          "kb/linear_algebra.md",
    "Determinant":                   "kb/linear_algebra.md",
    "Eigenvalues and eigenvectors":  "kb/linear_algebra.md",
}

def clean_text(text):
    text = re.sub(r'\{\\displaystyle[^}]*(?:\{[^}]*\}[^}]*)?\}', '', text)
    text = re.sub(r'\\\w+\{[^}]*\}', '', text)
    text = re.sub(r'\{[^}]{0,50}\}', '', text)
    lines = text.split('\n')
    clean_lines = [l.strip() for l in lines if len(l.strip()) > 30]
    return '\n\n'.join(clean_lines)

def get_useful_sections(page):
    skip_sections = {
        'history', 'etymology', 'see also', 'references',
        'external links', 'notes', 'bibliography', 'further reading',
        'ancient', 'modern history', 'background', 'notation'
    }

    content = f"\n\n---\n## {page.title} (from Wikipedia)\n\n"
    summary = clean_text(page.summary[:1500])
    content += summary + "\n\n"

    for section in page.sections:
        if section.title.lower() in skip_sections:
            continue
        if any(skip in section.title.lower() for skip in ['histor', 'etymolog', 'ancient']):
            continue
        section_text = clean_text(section.text)
        if len(section_text) > 100:
            content += f"### {section.title}\n\n{section_text[:2000]}\n\n"

    return content

# Process each topic and append to existing file
for topic, filepath in TOPIC_FILE_MAP.items():
    page = wiki.page(topic)
    if not page.exists():
        print(f"❌ Not found: {topic}")
        continue

    content = get_useful_sections(page)

    # Append to existing file (creates file if somehow missing)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Appended '{topic}' → {filepath}")

print("\n✅ Done. All Wikipedia content merged into existing KB files.")
