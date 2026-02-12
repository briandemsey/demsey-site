from docx import Document
import os

output_dir = "C:/Users/Brian-CO/demsey-site/pages"

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Brian Demsey</title>
    <meta name="description" content="{description}">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Georgia', 'Times New Roman', serif; line-height: 1.7; color: #2c2c2c; background: #faf9f7; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
        header {{ background: rgba(45, 52, 54, 0.95); padding: 16px 0; position: fixed; width: 100%; top: 0; z-index: 1000; }}
        header .container {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ color: #fff; font-size: 1.4rem; font-weight: 600; text-decoration: none; }}
        nav {{ display: flex; gap: 32px; }}
        nav a {{ color: rgba(255,255,255,0.85); text-decoration: none; font-size: 0.95rem; }}
        nav a:hover {{ color: #fff; }}
        .hero {{ background: linear-gradient(135deg, rgba(45, 52, 54, 0.85), rgba(99, 110, 114, 0.8)), url('../assets/gallery-2.jpg') center/cover no-repeat; color: white; padding: 120px 24px 60px; text-align: center; }}
        .hero h1 {{ font-size: 2.4rem; font-weight: 400; margin-bottom: 16px; max-width: 900px; margin-left: auto; margin-right: auto; }}
        .hero .subtitle {{ font-size: 1.1rem; opacity: 0.9; max-width: 700px; margin: 0 auto; font-style: italic; }}
        .hero .meta {{ margin-top: 20px; font-size: 0.9rem; opacity: 0.7; }}
        .article-content {{ max-width: 800px; margin: 0 auto; padding: 40px 24px; }}
        .article-content h2 {{ font-size: 1.6rem; margin-top: 40px; margin-bottom: 16px; color: #2d3436; }}
        .article-content p {{ font-size: 1.05rem; color: #444; margin-bottom: 18px; line-height: 1.8; }}
        .article-content ul {{ margin: 16px 0 16px 24px; }}
        .article-content li {{ font-size: 1.05rem; color: #444; margin-bottom: 10px; line-height: 1.7; }}
        .article-content hr {{ border: none; border-top: 1px solid #ddd; margin: 32px 0; }}
        .article-content a {{ color: #bd9280; text-decoration: none; }}
        .article-content a:hover {{ text-decoration: underline; }}
        .back-link {{ display: inline-block; margin-bottom: 20px; color: #bd9280; text-decoration: none; font-size: 0.95rem; }}
        .back-link:hover {{ text-decoration: underline; }}
        .author-box {{ background: #f5f3f0; padding: 24px; border-radius: 8px; margin: 32px 0; border-left: 4px solid #bd9280; }}
        .author-box p {{ margin-bottom: 0; font-size: 0.95rem; color: #555; }}
        footer {{ background: #2d3436; color: white; padding: 40px 0 20px; margin-top: 40px; }}
        .footer-bottom {{ text-align: center; color: rgba(255,255,255,0.5); font-size: 0.85rem; }}
        @media (max-width: 768px) {{ .hero h1 {{ font-size: 1.8rem; }} nav {{ display: none; }} }}
    </style>
</head>
<body>
<header>
    <div class="container">
        <a href="../index.html" class="logo">Brian Demsey</a>
        <nav>
            <a href="../index.html">Home</a>
            <a href="../index.html#articles">Articles</a>
            <a href="../index.html#gallery">Gallery</a>
            <a href="../index.html#contact">Contact</a>
        </nav>
    </div>
</header>
<section class="hero">
    <div class="container">
        <h1>{title}</h1>
        <p class="subtitle">{subtitle}</p>
        <p class="meta">Brian Demsey | {date}</p>
    </div>
</section>
<article class="article-content">
    <a href="../index.html#articles" class="back-link">&larr; Back to Articles</a>
    {content}
    <div class="author-box">
        <p><strong>Brian Demsey</strong> is the founder and CEO of Hallucinations.cloud LLC, an AI safety company focused on multi-model truth verification. He has over fifty years of experience in enterprise technology.</p>
    </div>
</article>
<footer>
    <div class="container">
        <div class="footer-bottom">
            <p>&copy; 2026 Brian Demsey. All rights reserved.</p>
        </div>
    </div>
</footer>
</body>
</html>'''

files = [
    ('The_Watermen_of_Bondi_Complete.docx', 'article-watermen-of-bondi.html', 'The Watermen of Bondi', 'Heroes, history, and the lessons of light from Sydney', '2026'),
    ('Its_No_Secret_Anymore_Final_2.docx', 'article-no-secret-anymore.html', "It's No Secret Anymore", 'Breaking eighty years of silence about Jewish identity', 'December 2025'),
    ('Parkinsons.docx', 'article-parkinsons.html', 'The Parkinsons Misdiagnosis', 'When machines are smarter than a five-minute exam', 'December 2025'),
    ('Silicon Valley Cassandra.docx', 'article-silicon-valley-cassandra.html', 'Silicon Valley Cassandras Reality Check', 'What the groundhog sees in AIs future', 'December 2025'),
    ('The_Mirror_Broke_v2.docx', 'article-mirror-broke.html', 'The Mirror Broke', 'How eight AI models answered the most divisive question', 'December 2025'),
    ('Archiology of Beliefs.docx', 'article-archaeology-of-beliefs.html', 'The Archaeology of Belief', 'How your politics were decided by age twelve', '2025'),
    ('WHERE IS THE HERO.docx', 'article-where-is-the-hero.html', 'Where Is The Hero?', 'And what happens when we stop waiting', 'December 2025'),
    ('Peter anf The Wolf.docx', 'article-peter-and-wolf.html', 'Peter and The Wolf: A Silicon Valley Fairy Tale', 'A symphonic satire for orchestra and narrator', '2025'),
    ('The 500 Billion Dollar Bug.docx', 'article-500-billion-bug.html', 'The $500 Billion Bug', 'How AIs hallucination economy turns failure into profit', '2025'),
    ('This Generation.docx', 'article-this-generation.html', "This Generations Cold War", 'Measured in bots, not nuclear stockpiles', '2025'),
    ('The AI Paradox.docx', 'article-ai-paradox.html', 'The AI Paradox', 'Why techs biggest spenders may be building fragility', '2025'),
    ('When the Algorithm Meets the Ocean.docx', 'article-algorithm-ocean.html', 'When the Algorithm Meets the Ocean', 'What outrigger racing teaches us about software', '2025'),
    ('AI Society and Its Future.docx', 'article-ai-society.html', 'AI Society and Its Future', 'A response to critiques of technology', '2025'),
    ('Disruption Or Empowerment.docx', 'article-disruption-empowerment.html', 'Disruption or Empowerment', 'A view from the prairie at age 83', '2025'),
    ('The Global Wellbeing Paradox.docx', 'article-global-wellbeing.html', 'The Global Wellbeing Paradox', 'When traditional metrics fail to capture human flourishing', '2025'),
    ('Chicken Little Goes to Washington.docx', 'article-chicken-little.html', 'Chicken Little Goes to Washington', 'A shutdown fable for our times', '2025'),
    ('Eight Women Speak Out.docx', 'article-eight-women.html', 'Eight Women Speak Out', 'From Eleanor Roosevelt to Taylor Swift', '2025'),
    ('Eight Men Speak Out.docx', 'article-eight-men.html', 'Eight Men Speak Out', 'A panel of legends discusses American democracy', '2025'),
    ('The Supreme Court.docx', 'article-supreme-court.html', 'The Supreme Court', 'How a Rabbinical model inspired autonomous AI law', '2025'),
    ('The Unicorn.docx', 'article-unicorn.html', "The Unicorns Paradox", 'Silicon Valley billionaires and work-life balance', '2025'),
    ('The Clarity of Age.docx', 'article-clarity-of-age.html', 'The Clarity of Age', 'Why 83 is my most creative year yet', '2025'),
]

def clean_text(text):
    replacements = {
        '\u2014': '-', '\u2013': '-',
        '\u2018': "'", '\u2019': "'",
        '\u201c': '"', '\u201d': '"',
        '\u2026': '...', '\u00a0': ' ',
        '\u2022': '*', '\u00b7': '*',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return ''.join(c if ord(c) < 128 else ' ' for c in text)

def format_content(paragraphs):
    html_parts = []
    skip_count = 0
    for p in paragraphs:
        text = clean_text(p.strip())
        if not text:
            continue
        if skip_count < 3 and len(text) < 100:
            skip_count += 1
            continue

        if text.startswith('* * *') or text == '---' or text.startswith('___'):
            html_parts.append('<hr>')
        elif len(text) < 80 and not text.endswith('.') and not text.endswith(':') and not text.endswith('?'):
            html_parts.append(f'<h2>{text}</h2>')
        else:
            html_parts.append(f'<p>{text}</p>')
    return '\n    '.join(html_parts)

os.chdir("C:/Users/Brian-CO/Desktop/The Information")

for docx_file, html_file, title, subtitle, date in files:
    if not os.path.exists(docx_file):
        print(f"SKIP: {docx_file} not found")
        continue

    try:
        doc = Document(docx_file)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]

        content_html = format_content(paragraphs)
        description = clean_text(subtitle)

        html = template.format(
            title=title,
            subtitle=subtitle,
            description=description,
            date=date,
            content=content_html
        )

        output_path = os.path.join(output_dir, html_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"CREATED: {html_file}")
    except Exception as e:
        print(f"ERROR: {docx_file} - {e}")

print("\nDone!")
