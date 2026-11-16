"""Rebuild colour variants /1-/4 from the built English index.html. Run after src/build.py."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = {"1": ("#E9B44C", None, False), "2": ("#FF7A1A", None, False),
     "3": ("#B8693A", "https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=Inter:wght@400;500;600&family=Anton&display=swap", True),
     "4": ("#0058A0", "https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Inter:wght@400;500;600&family=Anton&display=swap", True)}
OWN = ('<div class="w"><div class="ownrow"><figure><img src="/v/own-stock.jpg" alt="Our own stock room" loading="lazy"><figcaption>Our stock room: styles we sell every week</figcaption></figure>'
       '<figure><img src="/v/own-ship.jpg" alt="Printing e-commerce shipping labels" loading="lazy"><figcaption>Online orders: shipping labels printed daily</figcaption></figure>'
       '<figure><img src="/v/own-pack.jpg" alt="Packing wholesale and online orders" loading="lazy"><figcaption>Packed for our wholesale stalls and online store</figcaption></figure></div></div>')
src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
for n, (acc, font, light) in V.items():
    s = src.replace("<title>", '<meta name="robots" content="noindex">\n<title>', 1)
    s = s.replace("fill='%23D7FF3B'", "fill='%23" + acc[1:] + "'")
    s = s.replace('<rect width="64" height="64" fill="#D7FF3B"/>', f'<rect width="64" height="64" fill="{acc}"/>')
    s = re.sub(r'href="/site\.css\?', f'href="/{n}/site.css?', s)
    s = s.replace('<source src="/film.mp4"', '<source src="/v/film.mp4"').replace('<img src="/img/trim.jpg"', '<img src="/v/trim.jpg"')
    if light:
        s = s.replace('https://fonts.googleapis.com/css2?family=Anton&amp;family=Space+Grotesk:wght@400;500;700&amp;display=swap', font)
        s = s.replace('https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@400;500;700&display=swap', font)
        s = s.replace('<path d="M12 12h40v11H37.5v20L26.5 54V23H12z" fill="#0B0B0C"/>', '<path d="M12 12h40v11H37.5v20L26.5 54V23H12z" fill="#FFFFFF"/>')
        a = s.index('<section id="products" class="pt0">'); b = s.index("</section>", a) + len("</section>")
        prod = s[a:b].replace('<section id="products" class="pt0">', '<section id="products">', 1)
        s = s[:a] + s[b:]
        c = s.index('<section id="categories">')
        s = s[:c] + prod + "\n\n" + s[c:]
        a = s.index('<section id="about"'); b = s.index("</section>", a)
        s = s[:b] + OWN + s[b:]
    open(os.path.join(ROOT, n, "index.html"), "w", encoding="utf-8").write(s)
    print("variant", n, len(s))
