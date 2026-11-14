# Catalogue strings (categories, fabric tags, UI) merged into each page's JS strings.
CATS = ["all","basics","tees","polos","sets","pants","shorts","sweats","knit","shirts","jackets"]
X = {
"en": dict(
 cats=dict(all="All",basics="Plain basics",tees="T-shirts",polos="Polos",sets="Sets",pants="Pants",shorts="Shorts",sweats="Sweatshirts & hoodies",knit="Knitwear",shirts="Shirts",jackets="Jackets"),
 tags=dict(milk="Milk silk",ice="Ice silk, cool touch",sorona="Sorona",cotton="100% cotton",waffle="Waffle knit",heavy="Heavyweight",knit="Cotton-feel knit",fleece="Fleece-lined",air="Air-layer knit",linen="Linen blend",cord="Corduroy",washed="Washed",thermal="Thermal",pique="Piqué",cargo="Cargo",wide="Wide leg",barrel="Barrel leg",zip="Zip",embroid="Embroidered",jacquard="Jacquard",gradient="Gradient",layered="Layered look",plain="Plain",print="Printed"),
 shipped="pcs made", search="Search style no.", more="Show more", count="{n} styles", proven="Bulk proven",
 ts={"TS-01":"Oversized milk-silk T-shirt","TS-02":"Wide-leg knit sweatpants","TS-03":"Pleated wide-leg sweatpants","TS-04":"Wide-leg lounge sweatpants","TS-05":"Men's long-sleeve shirt","TS-06":"Fleece half-zip pullover","TS-07":"Barrel-leg cargo knit pants","TS-08":"Chino work shorts","TS-09":"Sorona flatlock long-sleeve tee","TS-10":"Fitted tank top","TS-11":"Pullover hoodie","TS-12":"Sleeveless muscle tank","TS-13":"Women's plush zip jacket","TS-14":"Long fleece-lined hooded coat","TS-15":"Sherpa zip jacket"}),
"es": dict(
 cats=dict(all="Todo",basics="Básicos lisos",tees="Camisetas",polos="Polos",sets="Conjuntos",pants="Pantalones",shorts="Shorts",sweats="Sudaderas y hoodies",knit="Punto",shirts="Camisas",jackets="Chaquetas"),
 tags=dict(milk="Seda de leche",ice="Seda fría",sorona="Sorona",cotton="100% algodón",waffle="Punto waffle",heavy="Gramaje alto",knit="Punto tipo algodón",fleece="Forro polar",air="Punto air-layer",linen="Mezcla de lino",cord="Pana",washed="Lavado",thermal="Térmico",pique="Piqué",cargo="Cargo",wide="Pierna ancha",barrel="Pierna barril",zip="Cremallera",embroid="Bordado",jacquard="Jacquard",gradient="Degradado",layered="Efecto dos piezas",plain="Liso",print="Estampado"),
 shipped="piezas fabricadas", search="Buscar nº de modelo", more="Ver más", count="{n} modelos", proven="Probado en volumen",
 ts={"TS-01":"Camiseta oversize seda de leche","TS-02":"Pantalón de punto pierna ancha","TS-03":"Pantalón ancho con pinzas","TS-04":"Pantalón lounge pierna ancha","TS-05":"Camisa manga larga hombre","TS-06":"Polar media cremallera","TS-07":"Pantalón cargo pierna barril","TS-08":"Short chino de trabajo","TS-09":"Camiseta manga larga Sorona flatlock","TS-10":"Camiseta sin mangas ajustada","TS-11":"Hoodie","TS-12":"Camiseta sin mangas","TS-13":"Chaqueta peluche mujer","TS-14":"Abrigo largo con capucha forrado","TS-15":"Chaqueta sherpa con cremallera"}),
"pt": dict(
 cats=dict(all="Todos",basics="Básicos lisos",tees="Camisetas",polos="Polos",sets="Conjuntos",pants="Calças",shorts="Bermudas",sweats="Moletons",knit="Tricô",shirts="Camisas",jackets="Jaquetas"),
 tags=dict(milk="Seda de leite",ice="Seda gelada",sorona="Sorona",cotton="100% algodão",waffle="Waffle",heavy="Gramatura alta",knit="Malha tipo algodão",fleece="Forrado",air="Malha air-layer",linen="Linho misto",cord="Veludo cotelê",washed="Lavado",thermal="Térmico",pique="Piquet",cargo="Cargo",wide="Pantalona",barrel="Perna barril",zip="Zíper",embroid="Bordado",jacquard="Jacquard",gradient="Degradê",layered="Efeito sobreposto",plain="Liso",print="Estampado"),
 shipped="peças feitas", search="Buscar nº do modelo", more="Ver mais", count="{n} modelos", proven="Testado em volume",
 ts={"TS-01":"Camiseta oversized seda de leite","TS-02":"Calça de moletom pantalona","TS-03":"Calça pantalona com pregas","TS-04":"Calça lounge pantalona","TS-05":"Camisa manga longa masculina","TS-06":"Fleece meio zíper","TS-07":"Calça cargo perna barril","TS-08":"Bermuda chino","TS-09":"Camiseta manga longa Sorona flatlock","TS-10":"Regata justa","TS-11":"Moletom com capuz","TS-12":"Regata cavada","TS-13":"Jaqueta pelúcia feminina","TS-14":"Casaco longo forrado com capuz","TS-15":"Jaqueta sherpa com zíper"}),
"fr": dict(
 cats=dict(all="Tout",basics="Basiques unis",tees="T-shirts",polos="Polos",sets="Ensembles",pants="Pantalons",shorts="Shorts",sweats="Sweats et hoodies",knit="Maille",shirts="Chemises",jackets="Vestes"),
 tags=dict(milk="Soie de lait",ice="Effet frais",sorona="Sorona",cotton="100 % coton",waffle="Gaufré",heavy="Grammage lourd",knit="Maille effet coton",fleece="Doublé polaire",air="Maille air-layer",linen="Lin mélangé",cord="Velours côtelé",washed="Délavé",thermal="Thermique",pique="Piqué",cargo="Cargo",wide="Jambe large",barrel="Coupe tonneau",zip="Zip",embroid="Brodé",jacquard="Jacquard",gradient="Dégradé",layered="Effet superposé",plain="Uni",print="Imprimé"),
 shipped="pièces fabriquées", search="Chercher une réf.", more="Voir plus", count="{n} modèles", proven="Éprouvé en volume",
 ts={"TS-01":"T-shirt oversize soie de lait","TS-02":"Pantalon maille jambe large","TS-03":"Pantalon large à pinces","TS-04":"Pantalon lounge jambe large","TS-05":"Chemise manches longues homme","TS-06":"Polaire demi-zip","TS-07":"Pantalon cargo coupe tonneau","TS-08":"Short chino","TS-09":"T-shirt manches longues Sorona flatlock","TS-10":"Débardeur ajusté","TS-11":"Sweat à capuche","TS-12":"Débardeur sans manches","TS-13":"Veste peluche femme","TS-14":"Manteau long à capuche doublé","TS-15":"Veste sherpa zippée"}),
"ar": dict(
 cats=dict(all="الكل",basics="أساسيات سادة",tees="تيشيرتات",polos="بولو",sets="أطقم",pants="بناطيل",shorts="شورتات",sweats="سويت شيرت وهوديز",knit="تريكو",shirts="قمصان",jackets="جاكيتات"),
 tags=dict(milk="حرير الحليب",ice="قماش بارد",sorona="سورونا",cotton="قطن 100%",waffle="وافل",heavy="قماش ثقيل",knit="تريكو قطني الملمس",fleece="مبطن",air="تريكو إير",linen="مزيج كتان",cord="قطيفة مضلعة",washed="مغسول",thermal="حراري",pique="بيكيه",cargo="كارغو",wide="ساق واسعة",barrel="قصة برميل",zip="سحاب",embroid="مطرز",jacquard="جاكار",gradient="متدرج",layered="طبقتين",plain="سادة",print="مطبوع"),
 shipped="قطعة مصنوعة", search="ابحث برقم الموديل", more="عرض المزيد", count="{n} موديل", proven="مجرَّب بكميات كبيرة",
 ts={"TS-01":"تيشيرت أوفر سايز حرير الحليب","TS-02":"بنطال تريكو واسع","TS-03":"بنطال واسع بكسرات","TS-04":"بنطال منزلي واسع","TS-05":"قميص رجالي بأكمام طويلة","TS-06":"فليس بنصف سحاب","TS-07":"بنطال كارغو قصة برميل","TS-08":"شورت تشينو","TS-09":"تيشيرت سورونا بأكمام طويلة","TS-10":"فانلة ضيقة","TS-11":"هودي","TS-12":"فانلة بدون أكمام","TS-13":"جاكيت فرو نسائي","TS-14":"معطف طويل مبطن بقبعة","TS-15":"جاكيت شيربا بسحاب"}),
"zh": dict(
 cats=dict(all="全部",basics="光板通用款",tees="T恤",polos="Polo衫",sets="套裝",pants="長褲",shorts="短褲",sweats="衛衣",knit="針織衫",shirts="襯衫",jackets="外套"),
 tags=dict(milk="牛奶絲",ice="冰絲涼感",sorona="索羅娜",cotton="100% 純棉",waffle="華夫格",heavy="重磅",knit="華棉",fleece="加絨",air="空氣層",linen="亞麻混紡",cord="燈芯絨",washed="水洗",thermal="德絨保暖",pique="珠地",cargo="工裝",wide="闊腿",barrel="彎刀",zip="拉鍊",embroid="刺繡",jacquard="提花",gradient="漸層",layered="假兩件",plain="素色",print="印花"),
 shipped="件已生產", search="搜尋款號", more="顯示更多", count="共 {n} 款", proven="大貨驗證",
 ts={"TS-01":"寬鬆牛奶絲T恤","TS-02":"華棉闊腿衛褲","TS-03":"打褶闊腿衛褲","TS-04":"闊腿休閒衛褲","TS-05":"男裝長袖襯衫","TS-06":"搖粒絨半拉鍊上衣","TS-07":"華棉彎刀工裝褲","TS-08":"工裝短褲","TS-09":"索羅娜四針六線長袖","TS-10":"牛奶絲修身背心","TS-11":"連帽衛衣","TS-12":"無袖坎肩背心","TS-13":"女裝毛絨外套","TS-14":"加絨連帽長大衣","TS-15":"羊羔毛拉鍊外套"}),
}
# Factory-made basics (from ky's 做过的货): code, image, categories, tags, pieces made
TS = [("TS-01","w-ts-01a",["basics","tees"],["milk","plain"],"3,000,000+"),("TS-12","w-ts-12a",["basics","tees"],["plain"],"100,000+"),
("TS-08","w-ts-08",["basics","shorts"],["cargo"],"100,000+"),("TS-02","ts-02",["basics","pants"],["knit","wide"],"80,000+"),
("TS-09","ts-09",["basics","tees"],["sorona"],"50,000+"),("TS-05","ts-05",["basics","shirts"],["plain"],"40,000+"),
("TS-03","ts-03",["basics","pants"],["knit","wide"],"40,000+"),("TS-06","w-ts-06",["basics","jackets"],["fleece","zip"],"30,000+"),
("TS-04","ts-04",["basics","pants"],["knit","wide"],"20,000+"),("TS-11","w-ts-11a",["basics","sweats"],["plain"],"20,000+"),
("TS-14","w-ts-14",["basics","jackets"],["fleece"],"18,000+"),("TS-13","ts-13",["basics","jackets"],["zip"],"15,000+"),
("TS-15","ts-15",["basics","jackets"],["zip"],"14,000+"),("TS-10","w-ts-10",["basics","tees"],["milk"],"10,000+"),
("TS-07","ts-07",["basics","pants"],["knit","barrel","cargo"],"10,000+")]
# Page-level strings for the catalogue sections
P = {
"en": dict(prod_h2b="Our styles, all categories", search_ph="Search style no., e.g. T38", more_btn="Show more styles", n_styles="{n} styles",
  prod_note2="Real photos of styles we make and sell every week under our own wholesale label, nearly all in M–8XL, plus plain basics we have made in bulk. Send a photo of any style you sell and we quote it, or put your logo on ours.",
  cat_note2="Plain basics are styles we have already made in tens of thousands to millions of pieces. Everything else is from our own label's current range."),
"es": dict(prod_h2b="Nuestros modelos, todas las categorías", search_ph="Buscar nº de modelo, ej. T38", more_btn="Ver más modelos", n_styles="{n} modelos",
  prod_note2="Fotos reales de modelos que fabricamos y vendemos cada semana con nuestra marca mayorista, casi todos en M–8XL, más básicos lisos que ya hemos producido en volumen. Envía la foto de cualquier modelo que vendas y lo cotizamos, o pon tu logo en los nuestros.",
  cat_note2="Los básicos lisos son modelos que ya hemos fabricado por decenas de miles o millones de piezas. El resto es la colección actual de nuestra marca."),
"pt": dict(prod_h2b="Nossos modelos, todas as categorias", search_ph="Buscar nº do modelo, ex. T38", more_btn="Ver mais modelos", n_styles="{n} modelos",
  prod_note2="Fotos reais de modelos que fabricamos e vendemos toda semana com nossa marca de atacado, quase todos em M–8XL, além de básicos lisos que já produzimos em volume. Envie a foto de qualquer modelo que você vende e cotamos, ou coloque sua marca nos nossos.",
  cat_note2="Os básicos lisos são modelos que já produzimos em dezenas de milhares a milhões de peças. O resto é a coleção atual da nossa marca."),
"fr": dict(prod_h2b="Nos modèles, toutes catégories", search_ph="Chercher une réf., ex. T38", more_btn="Voir plus de modèles", n_styles="{n} modèles",
  prod_note2="Vraies photos de modèles que nous fabriquons et vendons chaque semaine sous notre marque de gros, presque tous en M–8XL, plus des basiques unis déjà produits en volume. Envoyez la photo de n'importe quel modèle et nous le chiffrons, ou ajoutez votre logo sur les nôtres.",
  cat_note2="Les basiques unis sont des modèles déjà fabriqués à des dizaines de milliers, voire des millions de pièces. Le reste vient de la gamme actuelle de notre marque."),
"ar": dict(prod_h2b="موديلاتنا، كل الفئات", search_ph="ابحث برقم الموديل، مثل T38", more_btn="عرض المزيد من الموديلات", n_styles="{n} موديل",
  prod_note2="صور حقيقية لموديلات نصنعها ونبيعها كل أسبوع تحت علامتنا للجملة، ومعظمها بمقاسات M–8XL، بالإضافة إلى أساسيات سادة أنتجناها بكميات كبيرة. أرسل صورة أي موديل تبيعه ونسعّره لك، أو ضع شعارك على موديلاتنا.",
  cat_note2="الأساسيات السادة موديلات أنتجناها بعشرات الآلاف إلى ملايين القطع. والباقي من التشكيلة الحالية لعلامتنا."),
"zh": dict(prod_h2b="全部款式，按品類瀏覽", search_ph="搜尋款號，例如 T38", more_btn="顯示更多款式", n_styles="{n} 款",
  prod_note2="以下是自有批發品牌每週生產和銷售的款式實拍，幾乎都做到 M–8XL，另外加上我們已經大貨生產過的光板通用款。把你在賣的任何款式傳圖給我們就能報價，也可以在我們的款式上加你的 Logo。",
  cat_note2="光板通用款是我們已經生產過數萬到數百萬件的款式，其他是自有品牌目前在賣的款式。"),
}
