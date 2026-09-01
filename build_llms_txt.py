# -*- coding: utf-8 -*-
"""生成 llms.txt（llmstxt.org 标准）—— 财情可倍增的价值守恒定律
数据源：README.md 系列总览表 + zh 目录 + en/es/fr 目录
"""
import re
import glob
import os
from urllib.parse import quote

BASE = "https://wecando.vip/value-conservation-law"
README = "README.md"

def enc(fn: str) -> str:
    """中文文件名 -> 百分号编码 URL 段"""
    return quote(fn, safe="")

def url(*parts) -> str:
    return BASE + "/" + "/".join(enc(p) for p in parts)

# ---------- 1. 解析 README 系列总览表 ----------
rows = []  # (编号, 中文标题, zh文件名, 英文标题, 描述)
pat = re.compile(r"^\|\s*(S\d{2}|E\d{2}|F\d{2}|P\d{2})\s*\|\s*\[([^\]]+)\]\(zh/([^)]+)\)\s*\|\s*([^|]*?)\s*\|\s*(.+?)\s*\|$")
with open(README, encoding="utf-8") as f:
    for line in f:
        m = pat.match(line.strip())
        if m:
            rows.append((m.group(1), m.group(2), m.group(3), m.group(4).strip(), m.group(5).strip()))

print("README 表解析:", len(rows), "篇")
by_code = {r[0]: r for r in rows}

# ---------- 2. zh 目录全量（含无编号专题） ----------
zh_files = sorted(glob.glob("zh/*.html"))
zh_extra = []  # 无编号
for fn in zh_files:
    code = os.path.basename(fn)[:3]
    if not re.match(r"^(S|E|F|P)\d{2}$", code):
        zh_extra.append(os.path.basename(fn))
        print("  无编号:", os.path.basename(fn))

# ---------- 3. en/es/fr 15 篇 主题映射 ----------
en_theme = {  # en 文件名前缀 -> (中文主题, English 标题)
    "01 five-economic-crises": ("经济危机解码", "The Five Economic Crises Decoded"),
    "02 break-free-murphys-law": ("突破墨菲定律", "Breaking Free of Murphy's Law"),
    "03 parkinsons-law": ("帕金森定律", "Parkinson's Law"),
    "04 peter-principle": ("彼得原理", "The Peter Principle"),
    "05 debt-crises-new-currency-value": ("债务危机与新货币价值内涵", "Debt Crises and the New Connotation of Money"),
    "06 fiscal-code-central-empires": ("中央帝国的财政密码", "The Fiscal Code of Central Empires"),
    "07 central-empire-trilogy": ("中央帝国三部曲", "The Central Empire Trilogy"),
    "08 economic-reforms-dynasties": ("历代经济变革得失", "Economic Reforms Through the Dynasties"),
    "09 political-gains-losses-dynasties": ("中国历代政治得失", "The Gains and Losses of Chinese Dynastic Politics"),
    "10 inside-the-game": ("置身事内", "Inside the Game: Government and Economic Development"),
    "11 great-nation-great-city": ("大国大城", "Great Nation, Great City"),
    "12 entropy-law": ("熵增定律", "The Law of Entropy Increase"),
    "13 yi-jing-three-changes": ("易经三易", "The Three Changes of the I Ching"),
    "14 tao-te-ching-heavenly-way": ("道德经天道人道", "The Heavenly Way and the Human Way"),
    "15 sapiens": ("人类简史", "Sapiens: A Brief History of Humankind"),
}

def theme_of(fn: str) -> tuple:
    for prefix, (zh_t, en_t) in en_theme.items():
        if fn.startswith(prefix):
            return zh_t, en_t
    return fn, fn

# ---------- 4. 组装 llms.txt ----------
L = []
L.append("# 财情可倍增的价值守恒定律 | The Law of Value Conservation for Wealth–Wellbeing Multiplication")
L.append("")
L.append("> 统一大市场价值计量及价值倍增引导系统：以价值守恒定律 `Y = E × S × T`（经济价值 × 社会价值 × 时间价值）论证经济、社会、企业与个人的兴衰规律。价值既不会凭空产生，也不会凭空消失，只会转化与转移，总量守恒；乘则兴，除则衰。")
L.append(">")
L.append("> 语言：中文（zh，89 篇）/ English（15）/ Español（15）/ Français（15）· 许可：CC BY-NC 4.0（署名-非商业性使用）· 作者：财情双生智库 Econ-Sentiment Twin Think Tank · 仓库：https://github.com/wecando-vip/value-conservation-law")
L.append("")

# --- 核心入口 ---
L.append("## 核心入口 Core Pages")
L.append(f"- [首页 · 中文]({BASE}/index.html): 理论总纲 · 宏观公式 Y=E×S×T 与微观公式 y=f(m)×f(h)×f(t) · 三色三卡开篇")
L.append(f"- [Home · English]({BASE}/index.en.html): The Law of Value Conservation — theory overview (EN)")
L.append(f"- [文库总索引 library.html]({BASE}/library.html): 语言 × 领域分类矩阵总入口（S 国家/E 企业/F 家庭/P 个人）")
L.append(f"- [分类导航 · 国家经济社会]({BASE}/library-society.html) · [企业]({BASE}/library-enterprise.html) · [家庭]({BASE}/library-family.html) · [个人]({BASE}/library-personal.html)")
L.append(f"- [量化统计系统分析]({BASE}/%E4%BB%B7%E5%80%BC%E5%AE%88%E6%81%92%E5%AE%9A%E5%BE%8B_%E9%87%8F%E5%8C%96%E7%BB%9F%E8%AE%A1%E7%B3%BB%E7%BB%9F%E5%88%86%E6%9E%90.html): 公式的统计学与计量分析研报")
L.append("")

# --- 中文文库 S ---
L.append("## 中文文库 · 国家 · 经济社会（S01–S50）")
for code, zh_t, fn, en_t, desc in rows:
    if code.startswith("S"):
        L.append(f"- [{code} {zh_t}]({url('zh', fn)}): {desc}")

# --- E ---
L.append("")
L.append("## 中文文库 · 企业（E01–E12）")
for code, zh_t, fn, en_t, desc in rows:
    if code.startswith("E"):
        L.append(f"- [{code} {zh_t}]({url('zh', fn)}): {desc}")

# --- F ---
L.append("")
L.append("## 中文文库 · 家庭（F01–F08）")
for code, zh_t, fn, en_t, desc in rows:
    if code.startswith("F"):
        L.append(f"- [{code} {zh_t}]({url('zh', fn)}): {desc}")

# --- P ---
L.append("")
L.append("## 中文文库 · 个人（P01–P17）")
for code, zh_t, fn, en_t, desc in rows:
    if code.startswith("P"):
        L.append(f"- [{code} {zh_t}]({url('zh', fn)}): {desc}")

# --- 专题 ---
if zh_extra:
    L.append("")
    L.append("## 中文文库 · 专题（无编号）")
    for fn in zh_extra:
        title = os.path.basename(fn).replace("_价值守恒论证.html", "").replace("_", "·")
        L.append(f"- [{title}]({url('zh', fn)}): 专题论证（以《中央帝国的财政密码》为线索）")

# --- en ---
L.append("")
L.append("## English Library（15 docs）")
for _f in sorted(glob.glob("en/*.html")):
    fn = os.path.basename(_f)
    zh_t, en_t = theme_of(fn)
    L.append(f"- [{en_t}]({url('en', fn)}): English version of {zh_t} — value conservation argument (EN)")

# --- es ---
L.append("")
L.append("## Biblioteca en Español（15 documentos）")
for _f in sorted(glob.glob("es/*.html")):
    fn = os.path.basename(_f)
    zh_t, en_t = theme_of(fn)
    L.append(f"- [{en_t}]({url('es', fn)}): Versión en español de {zh_t} — argumento de conservación del valor (ES)")

# --- fr ---
L.append("")
L.append("## Bibliothèque en français（15 documents）")
for _f in sorted(glob.glob("fr/*.html")):
    fn = os.path.basename(_f)
    zh_t, en_t = theme_of(fn)
    L.append(f"- [{en_t}]({url('fr', fn)}): Version française de {zh_t} — argument de conservation de la valeur (FR)")

# --- 资源 ---
L.append("")
L.append("## 数据与资源 Resources")
L.append(f"- [structure.json]({BASE}/structure.json): 文档结构化数据（blocks + images 索引）")
L.append(f"- [zh_meta.json]({BASE}/zh_meta.json): 中文文库元数据（89 篇编号/标题/描述/多语言链接）")
L.append(f"- [sitemap.xml]({BASE}/sitemap.xml): 全站站点地图（144 URL）· [valuesitemap.xml]({BASE}/valuesitemap.xml): 文库站点地图（131 URL + hreflang）")
L.append(f"- [robots.txt]({BASE}/robots.txt): 爬虫协议（开放国内外搜索引擎与 AI 大模型爬虫）")
L.append(f"- [LICENSE]({BASE}/LICENSE): CC BY-NC 4.0 · [GitHub 仓库](https://github.com/wecando-vip/value-conservation-law)")

out = "\n".join(L) + "\n"
with open("llms.txt", "w", encoding="utf-8", newline="\n") as f:
    f.write(out)

print("llms.txt 生成:", len(out.splitlines()), "行 /", len(out.encode("utf-8")), "bytes")
