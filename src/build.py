"""Build static per-language pages + /products.json:  python3 src/build.py [lang ...]  (run from repo root).
Text lives in src/lang_*.py (page copy) and src/lang_extra.py (catalogue labels); products in src/stall_items.json + lang_extra.TS."""
import html, json, os, re, sys, importlib
sys.path.insert(0, os.path.dirname(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = [  # code, html lang, hreflang, path, native name, short, dir
    ("en", "en", "en", "/", "English", "EN", "ltr"),
    ("es", "es", "es", "/es/", "Español", "ES", "ltr"),
    ("pt", "pt", "pt", "/pt/", "Português", "PT", "ltr"),
    ("fr", "fr", "fr", "/fr/", "Français", "FR", "ltr"),
    ("ar", "ar", "ar", "/ar/", "العربية", "AR", "rtl"),
    ("zh", "zh-Hant", "zh-TW", "/zh-tw/", "繁體中文", "繁", "ltr"),
]
from lang_extra import X, P, TS, CATS
tpl = open(os.path.join(ROOT, "src/template.html"), encoding="utf-8").read()
EN = importlib.import_module("lang_en").L

# ---- product data (language-neutral) ----
stall = json.load(open(os.path.join(ROOT, "src/stall_items.json"), encoding="utf-8"))
CLEAN = {"TS-01","TS-02","TS-03","TS-04","TS-05","TS-07","TS-08","TS-09","TS-11","TS-13","TS-15"}  # uniform flat-lays; TS-06/10/12/14 wait for redo
prods = [dict(c=c, img=img, k=k, t=t, z="", n=n, p=3) for c, img, k, t, n in TS if c in CLEAN]
prods += [dict(c=s["c"], img=s["img"], k=s["k"], t=s["t"], z=s["z"], p=s["p"]) for s in stall]
# "All" order: basics first, then round-robin across categories by priority so page one shows variety
first = [p for p in prods if p["p"] == 3]
rest = sorted([p for p in prods if p["p"] < 3], key=lambda p: -p["p"])
buckets = {}
for p in rest: buckets.setdefault(p["k"][0], []).append(p)
order = ["tees", "sets", "polos", "pants", "sweats", "shirts", "jackets", "knit", "shorts"]
rr = []
while any(buckets.values()):
    for c in order:
        if buckets.get(c): rr.append(buckets[c].pop(0))
prods = first + sorted(rr, key=lambda p: -min(p["p"], 1))
json.dump([[p["c"], p["img"], p["k"], p["t"], p["z"], p.get("n", "")] for p in prods],
          open(os.path.join(ROOT, "products.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
counts = {c: sum(c in p["k"] for p in prods) for c in CATS}; counts["all"] = len(prods)
CARD = [("basics", "b-ts-01", True), ("sets", "p/r046", True), ("tees", "p/r078", False), ("polos", "p/r155", False),
        ("pants", "s/" + next(s["i"] for s in stall if s["c"] == "CK41"), False), ("sweats", "p/r104", False),
        ("knit", "s/" + next(s["i"] for s in stall if s["c"] == "ZY02"), False), ("shirts", "p/r134", False),
        ("jackets", next(s["img"] for s in stall if "jackets" in s["k"]), False)]

def page(code, hl, hrl, path, name, short, d):
    L = dict(EN)
    if code != "en":
        L.update(importlib.import_module("lang_" + code).L)
    js = dict(EN["js"]); js.update(L.get("js", {})); js.update(X[code]); js.pop("names", None)
    v = {k: x for k, x in L.items() if isinstance(x, str)}
    v.update(P[code])
    v.update(lang=hl, dir=d, path=path, lang_short=short)
    v["ticker"] = "".join(f"<span>{html.escape(t)}</span>" for t in L["ticker"])
    v["hreflang"] = "\n".join(f'<link rel="alternate" hreflang="{h}" href="https://www.tuosenapparel.com{p}">' for _, _, h, p, *_ in LANGS) + \
        '\n<link rel="alternate" hreflang="x-default" href="https://www.tuosenapparel.com/">'
    v["lang_menu"] = "".join(f'<li><a href="{p}" hreflang="{h}" lang="{l}"{" aria-current=\"page\"" if c == code else ""}>{n}<small>{s}</small></a></li>' for c, l, h, p, n, s, _ in LANGS)
    v["faq_html"] = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in L["faq"])
    v["faq_ld"] = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": hl,
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L["faq"]]}, ensure_ascii=False) + "</script>"
    v["font_extra"] = {"ar": "&family=Cairo:wght@400;600;700", "zh": "&family=Noto+Sans+TC:wght@400;500;700"}.get(code, "")
    cl = X[code]["cats"]; ns = P[code]["n_styles"]
    v["filter_btns"] = "".join(f'<button type="button" aria-pressed="{str(c == "all").lower()}" data-c="{c}">{cl[c]} <small>{counts[c]}</small></button>' for c in CATS if counts[c])
    cards = []
    for c, img, big in CARD:
        if not counts.get(c): continue
        cards.append(f'<a class="cat{" big" if big else ""}{" basics" if c == "basics" else ""}" href="#products" data-c="{c}"><img src="/img/{img}.jpg" alt="" loading="lazy">'
                     f'<div><h3>{cl[c]} <i>→</i></h3><p>{ns.format(n=counts[c])} · {X[code]["proven"] if c == "basics" else "M–8XL"}</p></div>'
                     + (f'<em>{v["cat_size"]}</em>' if big and c != "basics" else "") + '</a>')
    cards.append(f'<a class="cat own" href="#contact"><div><h3>{v["c_own"]} <i>→</i></h3><p>{v["c_own_p"]}</p></div></a>')
    v["cat_cards"] = "".join(cards)
    v["js_strings"] = json.dumps(js, ensure_ascii=False)
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
print("products", len(prods), counts)
