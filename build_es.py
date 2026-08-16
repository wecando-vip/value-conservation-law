#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_es.py — 从 zh/ 提取样式与脚本, 组合 es_parts/NN.txt 西语正文, 生成 es/NN.es.html"""
import re, os

ROOT = r"D:/00 财情双生智库/AI财情双生智库/财情倍增的价值守恒定律"
os.chdir(ROOT)

# 每篇: 中文源文件, 西语标题, 输出文件名
PAGES = [
    ("zh/01 经济危机解码-价值守恒定律.html", "Descifrando las Cinco Grandes Crisis Económicas — Ley de Conservación del Valor Y=E×S×T", "01 descifrando-crisis-economicas.es.html"),
    ("zh/02 突破墨菲定律，对你的压制-价值守恒论证.html", "Rompiendo la Ley de Murphy — Ley de Conservación del Valor Y=E×S×T", "02 rompiendo-ley-murphy.es.html"),
    ("zh/03 帕金森定律-价值守恒论证.html", "La Ley de Parkinson — Ley de Conservación del Valor Y=E×S×T", "03 ley-parkinson.es.html"),
    ("zh/04 彼得原理-价值守恒论证.html", "El Principio de Peter — Ley de Conservación del Valor Y=E×S×T", "04 principio-peter.es.html"),
    ("zh/05 债务危机-新货币价值内涵论证.html", "Crisis de Deuda y la Nueva Connotación del Dinero — Ley de Conservación del Valor Y=E×S×T", "05 crisis-deuda-nueva-moneda.es.html"),
    ("zh/06 中央帝国的财政密码-价值守恒论证.html", "El Código Fiscal de los Imperios Centrales — Ley de Conservación del Valor Y=E×S×T", "06 codigo-fiscal-imperios-centrales.es.html"),
    ("zh/07 中央帝国三部曲-价值守恒论证.html", "La Trilogía del Imperio Central — Ley de Conservación del Valor Y=E×S×T", "07 trilogia-imperio-central.es.html"),
    ("zh/08 历代经济变革得失-价值守恒论证.html", "Ganancias y Pérdidas de las Reformas Económicas — Ley de Conservación del Valor Y=E×S×T", "08 reformas-economicas-dinastias.es.html"),
    ("zh/09 中国历代政治得失-价值守恒论证.html", "Ganancias y Pérdidas de la Política de las Dinastías Chinas — Ley de Conservación del Valor Y=E×S×T", "09 politica-dinastias-chinas.es.html"),
    ("zh/10 置身事内-价值守恒论证.html", "Dentro del Juego: El Gobierno Chino y el Desarrollo Económico — Ley de Conservación del Valor Y=E×S×T", "10 dentro-del-juego.es.html"),
    ("zh/11 大国大城-价值守恒论证.html", "Gran Nación, Gran Ciudad — Ley de Conservación del Valor Y=E×S×T", "11 gran-nacion-gran-ciudad.es.html"),
    ("zh/12 熵增定律-价值守恒论证.html", "La Ley del Aumento de la Entropía — Ley de Conservación del Valor Y=E×S×T", "12 ley-entropia.es.html"),
    ("zh/13 易经三易-价值守恒论证.html", "Los Tres Cambios del I Ching — Ley de Conservación del Valor Y=E×S×T", "13 tres-cambios-iching.es.html"),
    ("zh/14 道德经天道人道-价值守恒论证.html", "El Camino del Cielo y el Camino Humano — Ley de Conservación del Valor Y=E×S×T", "14 camino-cielo-camino-humano.es.html"),
]

def extract(html, tag):
    m = re.search(rf"<{tag}[\s\S]*?</{tag}>", html)
    return m.group(0) if m else ""

for zh_path, es_title, out_name in PAGES:
    zh = open(zh_path, encoding="utf-8").read()
    style = extract(zh, "style")
    script = extract(zh, "script")
    n = out_name.split()[0]
    part_path = f"es_parts/{n}.txt"
    if not os.path.exists(part_path):
        print(f"  ✗ 缺少正文 {part_path} — 跳过")
        continue
    body = open(part_path, encoding="utf-8").read().strip()
    # 若正文不含 <body> 则包装
    if "<body" not in body:
        body = "<body>\n<div id=\"progress\"></div>\n" + body + "\n</body>"
    out = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{es_title}</title>
{style}
</head>
{body}
{script}
</html>"""
    open(f"es/{out_name}", "w", encoding="utf-8").write(out)
    print(f"  ✓ 生成 es/{out_name}")

print("完成")
