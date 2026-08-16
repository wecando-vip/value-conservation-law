#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_fr.py — 从 zh/ 提取样式与脚本, 组合 fr_parts/NN.txt 法语正文, 生成 fr/NN.fr.html"""
import re, os

ROOT = r"D:/00 财情双生智库/AI财情双生智库/财情倍增的价值守恒定律"
os.chdir(ROOT)

# 每篇: 中文源文件, 法语标题, 输出文件名
PAGES = [
    ("zh/01 经济危机解码-价值守恒定律.html", "Décrypter les Cinq Grandes Crises Économiques — Loi de Conservation de la Valeur Y=E×S×T", "01 décrypter-crises-économiques.fr.html"),
    ("zh/02 突破墨菲定律，对你的压制-价值守恒论证.html", "Briser la Loi de Murphy — Loi de Conservation de la Valeur Y=E×S×T", "02 briser-loi-murphy.fr.html"),
    ("zh/03 帕金森定律-价值守恒论证.html", "La Loi de Parkinson — Loi de Conservation de la Valeur Y=E×S×T", "03 loi-parkinson.fr.html"),
    ("zh/04 彼得原理-价值守恒论证.html", "Le Principe de Peter — Loi de Conservation de la Valeur Y=E×S×T", "04 principe-peter.fr.html"),
    ("zh/05 债务危机-新货币价值内涵论证.html", "Crise de la Dette et Nouvelle Connotation de la Monnaie — Loi de Conservation de la Valeur Y=E×S×T", "05 crise-dette-nouvelle-monnaie.fr.html"),
    ("zh/06 中央帝国的财政密码-价值守恒论证.html", "Le Code Fiscal des Empires Centraux — Loi de Conservation de la Valeur Y=E×S×T", "06 code-fiscal-empires-centraux.fr.html"),
    ("zh/07 中央帝国三部曲-价值守恒论证.html", "La Trilogie de l'Empire Central — Loi de Conservation de la Valeur Y=E×S×T", "07 trilogie-empire-central.fr.html"),
    ("zh/08 历代经济变革得失-价值守恒论证.html", "Gains et Pertes des Réformes Économiques — Loi de Conservation de la Valeur Y=E×S×T", "08 réformes-économiques-dynasties.fr.html"),
    ("zh/09 中国历代政治得失-价值守恒论证.html", "Gains et Pertes de la Politique des Dynasties Chinoises — Loi de Conservation de la Valeur Y=E×S×T", "09 politique-dynasties-chinoises.fr.html"),
    ("zh/10 置身事内-价值守恒论证.html", "Au Cœur du Jeu : le Gouvernement Chinois et le Développement Économique — Loi de Conservation de la Valeur Y=E×S×T", "10 au-coeur-du-jeu.fr.html"),
    ("zh/11 大国大城-价值守恒论证.html", "Grande Nation, Grande Ville — Loi de Conservation de la Valeur Y=E×S×T", "11 grande-nation-grande-ville.fr.html"),
    ("zh/12 熵增定律-价值守恒论证.html", "La Loi de l'Augmentation de l'Entropie — Loi de Conservation de la Valeur Y=E×S×T", "12 loi-entropie.fr.html"),
    ("zh/13 易经三易-价值守恒论证.html", "Les Trois Changements du Yi Jing — Loi de Conservation de la Valeur Y=E×S×T", "13 trois-changements-iching.fr.html"),
    ("zh/14 道德经天道人道-价值守恒论证.html", "La Voie Céleste et la Voie Humaine — Loi de Conservation de la Valeur Y=E×S×T", "14 voie-céleste-voie-humaine.fr.html"),
    ("zh/15 人类简史-价值守恒论证.html", "Sapiens : une brève histoire de l'humanité, expliquée par une formule — Loi de Conservation de la Valeur Y=E×S×T", "15 sapiens.fr.html"),
]

def extract(html, tag):
    m = re.search(rf"<{tag}[\s\S]*?</{tag}>", html)
    return m.group(0) if m else ""

for zh_path, fr_title, out_name in PAGES:
    zh = open(zh_path, encoding="utf-8").read()
    style = extract(zh, "style")
    script = extract(zh, "script")
    n = out_name.split()[0]
    part_path = f"fr_parts/{n}.txt"
    if not os.path.exists(part_path):
        print(f"  ✗ 缺少正文 {part_path} — 跳过")
        continue
    body = open(part_path, encoding="utf-8").read().strip()
    if "<body" not in body:
        body = "<body>\n<div id=\"progress\"></div>\n" + body + "\n</body>"
    out = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{fr_title}</title>
{style}
</head>
{body}
{script}
</html>"""
    open(f"fr/{out_name}", "w", encoding="utf-8").write(out)
    print(f"  ✓ 生成 fr/{out_name}")

print("完成")
