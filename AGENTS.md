# AGENTS.md — 接手说明

这是 Tuosen Apparel 官网 www.tuosenapparel.com 的仓库。

## 0. 先读这个

**本仓库是公开的，而且 GitHub Pages 会把仓库里的每个文件原样发布到官网上**（比如这份文件就能在 www.tuosenapparel.com/AGENTS.md 打开）。所以：

- 内部信息（价格、成本、客户名单、账号、路线图、预算）**一律不准 commit**。
- 完整交接在 **`private/HANDOFF.md`**。`private/` 已写进 `.gitignore`，只存在 ky 的电脑上。**开始任何工作前先读它。**
- 如果 `private/` 不存在：请 ky 在 Claude App 项目文件里下载 `handoff/拓森_本地交接包.zip`，解压到仓库根目录（得到 `private/HANDOFF.md` 等文件）。

## 1. 身份与分工

- ky（GitHub `Hahasky-afk`）是监督员，Claude 是执行者。只把必须 ky 本人做的事交给 ky（付钱、拍摄、提供数字、注册账号、批准上线），其余由 Claude 主动完成。
- ky 要的是**明确方案和结论**（花多少钱、怎么做、预期效果），不是模糊的选择题。交付物要简单、可视化。
- 用中文回复 ky，简短整句。
- 对外身份：**Yang, Export Manager, Tuosen Apparel**
  - yang@tuosenapparel.com · WhatsApp +86 155 4931 5379 · https://www.tuosenapparel.com
  - No. 14, Lane 4, Dalujiao, Dongwei, Jiedong District, Jieyang, Guangdong, China
- ky 不出镜：图片和视频只拍车间、手、面料、成衣，不露脸，不用 AI 人脸。

## 2. 网站怎么改、怎么上线

- 纯静态站，GitHub Pages 从 `main` 分支根目录发布，`CNAME` = www.tuosenapparel.com，HTTPS 已强制。推到 main 约 1 分钟生效；HTML/CSS 缓存约 10 分钟，看不到更新就强制刷新。
- **不要直接手改根目录的 `index.html` 和各语言目录**，它们是生成的：
  - 页面模板：`src/template.html`
  - 文案：`src/lang_en.py`、`lang_es.py`、`lang_pt.py`、`lang_fr.py`、`lang_ar.py`（阿语 RTL）、`lang_zh.py`（繁中）
  - 审核后的覆盖文案：`src/lang_audit.py`（在 lang_*.py 之后应用，**以它为准**）
  - 产品标签/品类：`src/lang_extra.py`；档口款式数据：`src/stall_items.json`
  - 生成：在仓库根目录运行 `python3 src/build.py`（可加语言代码只生成部分），输出 `/index.html`、`/es/`、`/pt/`、`/fr/`、`/ar/`、`/zh-tw/` 和 `/products.json`
- 共享资源：`site.css`、`site.js`（构建时自动加 `?v=<hash>` 防缓存）。
- 图片：`img/`（`b-ts-*.jpg` 光板白底平铺、`p/`、`s/`、`s2/` 档口实拍）。
- **Logo**：`img/logo-on-dark.png`（深色底用）、`img/logo-on-light.png`（浅色底用）。图形 = 荧光绿方块 + 黑色 T（竖笔斜切）+ "TUOSEN / APPAREL FACTORY"。
- 品牌色：黑 `#0B0B0C`、荧光绿 `#D7FF3B`；字体 Anton（标题）+ Space Grotesk（正文）。ky 定了只要这一套黑绿配色。
- 视频：`film.mp4`（工厂宣传片 v6，页面引用 `film.mp4?v=6`）、`video/hero.mp4`（首屏）、`video/hero-m.mp4`（手机首屏 2MB）、`video/clip-*.mp4`（流程短片）。
- 询价表单：FormSubmit，直接发到 yang@tuosenapparel.com（已激活）。
- SEO：`sitemap.xml`、`robots.txt`、`404.html`。**不要删 `googlee1d985e380f11401.html`**（Google Search Console 验证文件，删了就掉验证）。
- 上线流程：在分支上改 → 截图给 ky 看 → ky 说"上线"/"推"后再合并到 main。
- 开放中的 PR：**#1** 买家专属页 `/for/duke|kam|barocco|bolf/`（noindex，主站不链接），等 ky 合并。

## 3. 网站文案规则（ky 定的）

- 用"我们"口吻；措辞稳妥不绝对；各语言的数字必须一致。
- 定位是"专业服装工厂"，男女装都做（不要写 men's basics）。
- 首屏标题："专注服装批量生产，为全球批发商与品牌提供稳定供应"。
- 少讲报价、流程、门槛：首屏和简介不写起订量/FOB/打样；按钮用 "Contact us / 联系我们"；起订量等细节只出现在 FAQ。
- 不写价格、付款/定金/尾款条款、认证/资质相关、公司成立年份。
- 交期写"常规返单约 7–14 个工作日，新开发订单依规格确认交期"；售后写"品质问题经核实后依订单约定处理"。
- 尺码写"部分款式最大 8XL"，不暗示所有款都到 8XL。
- 规模数字用 "+" 写法：10,000,000+、500,000+、300,000+、200,000+、2,000+ 款。
- 暂不写面料成分（Milk-silk 保持原写法）。
- 产品图必须风格统一：不要档口水印、中文促销字、拼图、AI 感重的图、大牌字样款。不用老人画面。
- 网站上暂不挂社媒图标。

## 4. 邮箱（技术部分）

- 域名在 Namecheap。收信：Catch-All 转发到 ky 的 Gmail；发信：Gmail 以 yang@tuosenapparel.com 代发。
- DNS：4 条 A 记录 185.199.108–111.153，CNAME www → hahasky-afk.github.io.，SPF `v=spf1 include:spf.efwd.registrar-servers.com include:_spf.google.com ~all`。**改 DNS 绝不能破坏 SPF 和转发。**
- 还缺 DKIM 和 DMARC，计划和待办见 `private/HANDOFF.md` 第 6 节。

## 5. 路线图、已做和待做

全部在 `private/HANDOFF.md`：公司背景、目标客户、ky 的偏好、已完成工作、按周的路线图、ky 待办、已否决方案。
