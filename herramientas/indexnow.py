"""Avisa a Bing (y al resto de buscadores con IndexNow: Yandex, Seznam, Naver…) de las URLs del sitemap.

Bing alimenta Copilot y es una de las fuentes de ChatGPT Search, así que avisar en cuanto
se publica algo acelera que aparezca en sus respuestas. Google no usa IndexNow.

Uso:  python herramientas/indexnow.py            (todas las URLs del sitemap)
      python herramientas/indexnow.py URL [URL…] (solo esas)
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

SITE = "https://itacacrecimiento.com"
ROOT = Path(__file__).resolve().parent.parent
KEY = next(p.stem for p in ROOT.glob("*.txt") if re.fullmatch(r"[0-9a-f]{32}", p.stem))

urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (ROOT / "sitemap.xml").read_text(encoding="utf-8"))
body = json.dumps({"host": "itacacrecimiento.com", "key": KEY, "keyLocation": f"{SITE}/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print(f"IndexNow: {r.status} · {len(urls)} URLs enviadas")
except urllib.error.HTTPError as e:
    # 200/202 = aceptado; 403 = clave no encontrada (aún no desplegada); 422 = URL de otro dominio
    print(f"IndexNow: HTTP {e.code} · {e.read()[:200]!r}")
