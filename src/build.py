"""Build static per-language pages: python3 src/build.py  (run from repo root)."""
import html, json, os, re, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = [  # code, path, native name, short, dir
    ("en", "/", "English", "EN", "ltr"),
    ("es", "/es/", "Español", "ES", "ltr"),
    ("pt", "/pt/", "Português", "PT", "ltr"),
    ("fr", "/fr/", "Français", "FR", "ltr"),
    ("ar", "/ar/", "العربية", "AR", "rtl"),
]
tpl = open(os.path.join(ROOT, "src/template.html"), encoding="utf-8").read()
EN = importlib.import_module("lang_en").L

def page(code, path, name, short, d):
    L = dict(EN)
    if code != "en":
        L.update(importlib.import_module("lang_" + code).L)
        js = dict(EN["js"]); js.update(L.get("js", {})); L["js"] = js
    v = {k: x for k, x in L.items() if isinstance(x, str)}
    v.update(lang=code, dir=d, path=path, lang_short=short)
    v["ticker"] = "".join(f"<span>{html.escape(t)}</span>" for t in L["ticker"])
    v["hreflang"] = "\n".join(f'<link rel="alternate" hreflang="{c}" href="https://www.tuosenapparel.com{p}">' for c, p, *_ in LANGS) + \
        '\n<link rel="alternate" hreflang="x-default" href="https://www.tuosenapparel.com/">'
    v["lang_menu"] = "".join(f'<li><a href="{p}" hreflang="{c}"{" aria-current=\"page\"" if c == code else ""}>{n}<small>{s}</small></a></li>' for c, p, n, s, _ in LANGS)
    v["faq_html"] = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in L["faq"])
    v["faq_ld"] = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": code,
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L["faq"]]}, ensure_ascii=False) + "</script>"
    v["font_extra"] = "&family=Cairo:wght@400;600;700" if code == "ar" else ""
    v["js_strings"] = json.dumps(L["js"], ensure_ascii=False)
    out = re.sub(r"\{\{(\w+)\}\}", lambda m: v[m.group(1)], tpl)
    if d == "rtl":
        out = out.replace(" →</a>", " ←</a>")
    dest = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w", encoding="utf-8").write(out)
    print("built", dest)

only = sys.argv[1:]
for l in LANGS:
    if not only or l[0] in only:
        page(*l)
