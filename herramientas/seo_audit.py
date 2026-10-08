"""Auditoría SEO automática de itacacrecimiento.com.

Lee el sitemap, descarga cada página y comprueba los elementos SEO clave.
Genera informes/auditoria-AAAA-MM-DD.md y .json. Solo usa la librería estándar.

Uso:  python seo_audit.py [https://dominio.com]
"""
import json
import re
import sys
import time
import urllib.request
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

SITE = (sys.argv[1] if len(sys.argv) > 1 else "https://itacacrecimiento.com").rstrip("/")
UA = "Mozilla/5.0 (compatible; ItacaSEOAudit/1.0)"
OUT = Path(__file__).parent / "informes"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode("utf-8", "replace")
            return r.status, body, time.time() - t0, r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, "", time.time() - t0, url
    except Exception as e:  # noqa: BLE001
        return 0, str(e), time.time() - t0, url


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta = {}
        self.canonical = None
        self.h1, self.h2 = [], []
        self.links, self.imgs_no_alt, self.imgs = [], 0, 0
        self.jsonld = []
        self.forms = 0
        self.lang = None
        self._stack = None
        self._buf = ""
        self.text = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._stack, self._buf = "title", ""
        elif tag in ("h1", "h2"):
            self._stack, self._buf = tag, ""
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._stack, self._buf = "jsonld", ""
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag == "link" and "canonical" in (a.get("rel") or ""):
            self.canonical = a.get("href")
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "img":
            self.imgs += 1
            if not a.get("alt"):
                self.imgs_no_alt += 1
        elif tag == "form":
            self.forms += 1

    def handle_endtag(self, tag):
        if self._stack and tag in ("title", "h1", "h2", "script"):
            txt = self._buf.strip()
            if self._stack == "title":
                self.title = txt
            elif self._stack == "h1":
                self.h1.append(re.sub(r"\s+", " ", txt))
            elif self._stack == "h2":
                self.h2.append(re.sub(r"\s+", " ", txt))
            elif self._stack == "jsonld":
                try:
                    data = json.loads(txt)
                    items = data if isinstance(data, list) else data.get("@graph", [data])
                    self.jsonld += [i.get("@type") for i in items if isinstance(i, dict)]
                except Exception:  # noqa: BLE001
                    self.jsonld.append("JSON-LD INVÁLIDO")
            self._stack = None

    def handle_data(self, data):
        if self._stack:
            self._buf += data
        self.text.append(data)


def audit_page(url):
    status, html, secs, final = fetch(url)
    res = {"url": url, "status": status, "segundos": round(secs, 2), "problemas": []}
    P = res["problemas"]
    if status != 200:
        P.append(f"CRÍTICO: estado HTTP {status}")
        return res, []
    if final.rstrip("/") != url.rstrip("/"):
        P.append(f"Redirige a {final}")
    p = PageParser()
    p.feed(html)
    words = len(re.findall(r"\w+", " ".join(p.text)))
    desc = p.meta.get("description", "")
    internal = sorted({urljoin(url, h).split("#")[0] for h in p.links
                       if urlparse(urljoin(url, h)).netloc == urlparse(SITE).netloc})
    res.update(title=p.title, title_len=len(p.title), description=desc, desc_len=len(desc),
               h1=p.h1, n_h2=len(p.h2), palabras=words, canonical=p.canonical,
               schema=p.jsonld, enlaces_internos=len(internal), formularios=p.forms,
               imgs=p.imgs, imgs_sin_alt=p.imgs_no_alt, og_image=bool(p.meta.get("og:image")))
    if not p.title:
        P.append("CRÍTICO: sin <title>")
    elif not 30 <= len(p.title) <= 65:
        P.append(f"Title de {len(p.title)} caracteres (ideal 30-65)")
    if not desc:
        P.append("ALTO: sin meta description")
    elif not 70 <= len(desc) <= 160:
        P.append(f"Meta description de {len(desc)} caracteres (ideal 70-160)")
    if len(p.h1) != 1:
        P.append(f"ALTO: {len(p.h1)} etiquetas H1 (debe haber 1)")
    if not p.canonical:
        P.append("MEDIO: sin canonical")
    elif p.canonical.rstrip("/") != url.rstrip("/"):
        P.append(f"MEDIO: canonical apunta a otra URL ({p.canonical})")
    if not p.jsonld:
        P.append("MEDIO: sin datos estructurados (schema.org)")
    if "noindex" in p.meta.get("robots", ""):
        P.append("CRÍTICO: página marcada noindex")
    if words < 600 and ("/blog/" in url or "/guias/" in url):
        P.append(f"MEDIO: contenido corto ({words} palabras)")
    if p.imgs_no_alt:
        P.append(f"BAJO: {p.imgs_no_alt} imágenes sin alt")
    if not p.meta.get("og:image"):
        P.append("BAJO: sin og:image (vista previa al compartir)")
    if not p.lang:
        P.append("BAJO: <html> sin atributo lang")
    if p.forms == 0 and not any("contact" in l or "#form" in l for l in p.links):
        P.append("CONVERSIÓN: sin formulario ni enlace claro a contacto")
    return res, internal


def main():
    status, xml, _, _ = fetch(SITE + "/sitemap.xml")
    urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    print(f"{len(urls)} URLs en el sitemap")
    results, all_links = [], set()
    for u in urls:
        r, links = audit_page(u)
        results.append(r)
        all_links.update(links)
        print(f"  {r['status']} {u}  ({len(r['problemas'])} avisos)")

    # Enlaces internos rotos y páginas fuera del sitemap
    in_sitemap = {u.rstrip("/") for u in urls}
    extra = sorted(l for l in all_links if l.rstrip("/") not in in_sitemap
                   and not re.search(r"\.(css|js|png|jpe?g|svg|webp|pdf|xml|ico)$", l))
    broken = []
    for l in extra:
        s, *_ = fetch(l)
        if s != 200:
            broken.append((l, s))

    # Títulos / descripciones duplicados
    dup = {}
    for k in ("title", "description"):
        seen = {}
        for r in results:
            if r.get(k):
                seen.setdefault(r[k], []).append(r["url"])
        dup[k] = {v: us for v, us in seen.items() if len(us) > 1}

    OUT.mkdir(exist_ok=True)
    today = date.today().isoformat()
    (OUT / f"auditoria-{today}.json").write_text(
        json.dumps({"fecha": today, "paginas": results, "rotos": broken,
                    "fuera_sitemap": extra, "duplicados": dup}, ensure_ascii=False, indent=2),
        encoding="utf-8")

    n_prob = sum(len(r["problemas"]) for r in results)
    md = [f"# Auditoría SEO — {SITE} — {today}\n",
          f"- Páginas analizadas: **{len(results)}**",
          f"- Avisos totales: **{n_prob}**",
          f"- Enlaces internos rotos: **{len(broken)}**",
          f"- Páginas enlazadas pero fuera del sitemap: **{len([e for e in extra if e not in dict(broken)])}**\n"]
    if broken:
        md.append("## Enlaces rotos\n")
        md += [f"- `{s}` {l}" for l, s in broken]
    for k, d in dup.items():
        if d:
            md.append(f"\n## {k.capitalize()} duplicados\n")
            for v, us in d.items():
                md.append(f"- \"{v}\" → {', '.join(us)}")
    md.append("\n## Detalle por página\n")
    md.append("| URL | Title (car.) | Desc (car.) | H1 | Palabras | Schema | Avisos |")
    md.append("|---|---|---|---|---|---|---|")
    for r in results:
        path = urlparse(r["url"]).path
        md.append(f"| {path} | {r.get('title_len', '-')} | {r.get('desc_len', '-')} | "
                  f"{len(r.get('h1', []))} | {r.get('palabras', '-')} | "
                  f"{', '.join(map(str, r.get('schema', []))) or '—'} | "
                  f"{'<br>'.join(r['problemas']) or 'OK'} |")
    (OUT / f"auditoria-{today}.md").write_text("\n".join(md), encoding="utf-8")
    print(f"\nInforme: informes/auditoria-{today}.md  ({n_prob} avisos, {len(broken)} rotos)")
    # Si hay problemas graves, termina con error para que GitHub avise por correo
    graves = [f"{r['url']}: {p}" for r in results for p in r["problemas"] if p.startswith("CRÍTICO")]
    graves += [f"Enlace roto ({s}): {l}" for l, s in broken]
    if graves:
        print("\nPROBLEMAS GRAVES:\n" + "\n".join(graves))
        sys.exit(1)


if __name__ == "__main__":
    main()
