# -*- coding: utf-8 -*-
"""HMK 홀딩스그룹 공식 홈페이지 생성기"""
import os, base64, io, shutil, json
from seo import meta_for, SITE_NAME

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("HMK_OUT") or os.path.join(BASE, "..")
DOMAIN = "https://www.hmkholdings.com"

NAV = [
    ("그룹소개", "/group/message/", "GROUP", [
        ("회장 인사말", "/group/message/"),
        ("그룹 개요·비전", "/group/about/"),
        ("조직·거버넌스", "/group/organization/"),
        ("오시는길", "/group/location/"),
    ]),
    ("사업모델", "/model/", "BUSINESS MODEL", [
        ("밸류업 순환모델", "/model/"),
        ("AI 초저가 매입", "/model/ai-sourcing/"),
        ("공간수익화 모델", "/model/space/"),
        ("통합물류·멤버십 시너지", "/model/synergy/"),
        ("자산 유동화", "/model/liquidity/"),
        ("보유 자산", "/model/assets/"),
    ]),
    ("그룹사소개", "/affiliates/", "AFFILIATES", [
        ("HMK그룹사 전체보기", "/affiliates/"),
        ("HMK 대부", "/affiliates/loan/"),
        ("HMK 스토리지", "/affiliates/storage/"),
        ("오렌지 마켓", "/affiliates/market/"),
        ("오렌지 라이브커머스", "/affiliates/live/"),
        ("오렌지 멤버십", "/affiliates/membership/"),
        ("관련 사이트 안내", "/sites/"),
    ]),
    ("뉴스", "/news/", "NEWS", []),
    ("채용", "/careers/", "CAREERS", []),
]

CV = '<svg class="cv" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 4.5L6 8l3.5-3.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def _b64(path, h, colors=48):
    from PIL import Image
    im = Image.open(path).convert("RGBA")
    im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    q = im.quantize(colors=colors, method=Image.FASTOCTREE)
    buf = io.BytesIO(); q.save(buf, "PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


A = os.path.join(BASE, "..", "assets")
LOGO_B64 = _b64(os.path.join(A, "logo.png"), 120)
LOGOW_B64 = _b64(os.path.join(A, "logo-white.png"), 120)
FAV_B64 = _b64(os.path.join(A, "favicon.png"), 48, 24)


def head(path, m):
    url = DOMAIN + path
    seo = meta_for(path)
    title = seo["title"] or m["title"]
    desc = seo["desc"] or m["desc"]
    robots = "noindex, nofollow" if seo["noindex"] else "index, follow, max-image-preview:large"
    kw = f'<meta name="keywords" content="{seo["keywords"]}">\n' if seo["keywords"] else ""
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add('js')</script>
<title>{title}</title>
<meta name="description" content="{desc}">
{kw}<meta name="robots" content="{robots}">
<meta name="author" content="{SITE_NAME}">
<link rel="canonical" href="{url}">
<!-- 검색엔진 소유확인: 네이버 서치어드바이저·구글 서치콘솔에서 발급받은 태그를 아래 줄에 넣거나, HTML 파일 업로드 방식을 이용하세요 -->
<meta property="og:type" content="website">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="HMK홀딩스그룹 — 상업용 부동산 자산가치 밸류업 플랫폼">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{DOMAIN}/assets/og.jpg">
<link rel="icon" type="image/png" href="data:image/png;base64,{FAV_B64}">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="/css/style.css">
{m.get('extra_head','')}
{breadcrumb_ld(m.get('crumbs'))}
</head>
<body class="{m.get('body_class','page')}">
<a class="skip" href="#main">본문 바로가기</a>
"""


def breadcrumb_ld(crumbs):
    if not crumbs:
        return ""
    items = [{"@type": "ListItem", "position": 1, "name": "홈", "item": DOMAIN + "/"}]
    for i, (t, h) in enumerate(crumbs, 2):
        items.append({"@type": "ListItem", "position": i, "name": t, "item": DOMAIN + h})
    data = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'


def header_html(active):
    items = []
    for label, href, en, subs in NAV:
        cur = ' aria-current="true"' if label == active else ""
        if subs:
            dd = "".join(f'<a href="{h}">{t}</a>' for t, h in subs)
            items.append(
                f'<li><a class="gnb-link" href="{href}"{cur}>{label}{CV}</a>'
                f'<div class="dropdown"><span class="dd-en">{en}</span>{dd}</div></li>')
        else:
            items.append(f'<li><a class="gnb-link" href="{href}"{cur}>{label}</a></li>')

    drawer = []
    for label, href, en, subs in NAV:
        if subs:
            links = "".join(f'<a href="{h}">{t}</a>' for t, h in subs)
            drawer.append(
                f'<div class="dsec"><button type="button" aria-expanded="false">'
                f'<b>{label}</b><span>{en}</span>{CV}</button><div class="dpanel">{links}</div></div>')
        else:
            drawer.append(f'<div class="dsec"><a class="dsolo" href="{href}"><b>{label}</b><span>{en}</span></a></div>')

    return f"""<div class="site-top">
  <div class="utility"><div class="uwrap">
    <span class="u-tag">REAL ESTATE VALUE-UP GROUP</span>
    <a href="/sites/">관련 사이트</a>
    <a href="https://storage-orange.co.kr" target="_blank" rel="noopener">오렌지 공유창고<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
    <a href="/careers/">채용</a>
    <a class="u-tel" href="tel:1555-5335">1555-5335</a>
  </div></div>
  <header class="header"><div class="hwrap">
    <a class="logo" href="/" aria-label="HMK 홀딩스그룹 홈"><span class="logo-mark" role="img" aria-label="HMK 홀딩스그룹"></span></a>
    <nav aria-label="주 메뉴"><ul class="gnb">{''.join(items)}</ul></nav>
    <a class="header-cta" href="/contact/">문의하기</a>
    <button class="nav-toggle" aria-label="메뉴 열기" aria-expanded="false"><span></span></button>
  </div></header>
</div>
<div class="drawer" hidden>
  <div class="dhead"><span class="logo-mark" role="img" aria-label="HMK 홀딩스그룹"></span>
    <button class="dclose" aria-label="메뉴 닫기">&#10005;</button></div>
  <div class="dbody">{''.join(drawer)}</div>
  <div class="dcta"><a class="a" href="/contact/">문의하기</a><a class="b" href="tel:1555-5335">1555-5335</a></div>
</div>
"""


FOOTER = f"""<footer class="footer"><div class="wrap">
  <div class="ftop">
    <div class="fbrand">
      <span class="logo-mark white" role="img" aria-label="HMK 홀딩스그룹"></span>
      <p><b style="color:#fff">상업용 부동산 자산가치 밸류업 플랫폼.</b> AI 프롭테크로 상업용 부동산을 초저가 매입하고, 창고형마켓·라이브커머스·공유창고 3가지 사업으로 임대수익과 자산가치를 높이며, 자산 유동화로 순환시킵니다.</p>
    </div>
    <div><h4>그룹소개</h4><ul>
      <li><a href="/group/message/">회장 인사말</a></li>
      <li><a href="/group/about/">그룹 개요·비전</a></li>
      <li><a href="/group/organization/">조직·거버넌스</a></li>
      <li><a href="/group/location/">오시는길</a></li></ul></div>
    <div><h4>사업모델</h4><ul>
      <li><a href="/model/">밸류업 순환모델</a></li>
      <li><a href="/model/ai-sourcing/">AI 초저가 매입</a></li>
      <li><a href="/model/space/">공간수익화 모델</a></li>
      <li><a href="/model/synergy/">통합물류·멤버십 시너지</a></li>
      <li><a href="/model/assets/">보유 자산</a></li></ul></div>
    <div><h4>문의</h4><ul>
      <li><a href="tel:1555-5335">대표전화 1555-5335</a></li>
      <li><a href="mailto:hmkholdings@hmkholdings.com">hmkholdings@hmkholdings.com</a></li>
      <li><a href="/group/location/">오시는길</a></li>
      <li><a href="/contact/">물건 제안·제휴 문의</a></li>
      <li><a href="/sites/">관련 사이트 안내</a></li></ul></div>
  </div>
  <div class="family">
    <span class="flabel">FAMILY SITES</span>
    <div class="flinks">
      <a href="https://hmknplauction.pages.dev" target="_blank" rel="noopener">HMK 대부</a>
      <a href="https://hmkstorage.com" target="_blank" rel="noopener">HMK 스토리지</a>
      <a href="https://kimjaedong.com" target="_blank" rel="noopener">김재동 회장</a>
      <a href="https://orange1000.com" target="_blank" rel="noopener">오렌지 마켓</a>
      <a href="https://orangeliveon.com" target="_blank" rel="noopener">오렌지 라이브커머스</a>
      <a href="https://storage-orange.co.kr" target="_blank" rel="noopener">오렌지 공유창고</a>
      <a href="https://orangemembership.com" target="_blank" rel="noopener">오렌지 멤버십</a>
      <a href="https://hmkpartner.com" target="_blank" rel="noopener">HMK 파트너모집</a>
      <a href="/affiliates/" class="fall">그룹사 전체보기 →</a>
    </div>
  </div>
  <div class="fbot">
    <div class="legal">
      <span>에이치엠케이스토리지 주식회사 · 대표이사 이영복 · 사업자등록번호 229-87-03308</span>
      <span>에이치엠케이홀딩스대부 주식회사 · 대표이사 이영복 · 사업자등록번호 501-87-03194</span>
      <span>서울특별시 강남구 봉은사로 129-1, 751빌딩 3층 · 대표전화 1555-5335</span>
      <span class="copy">&copy; <span data-year>2026</span> HMK HOLDINGS GROUP. All rights reserved.</span>
    </div>
    <div class="fpolicy"><a href="/policy/privacy/">개인정보처리방침</a><a href="/policy/terms/">이용약관</a></div>
  </div>
</div></footer>
<script src="/js/main.js" defer></script>
</body></html>"""


def crumbs(items):
    li = ['<li><a href="/">홈</a></li>']
    for i, (t, h) in enumerate(items):
        li.append(f'<li>{t}</li>' if i == len(items) - 1 else f'<li><a href="{h}">{t}</a></li>')
    return f'<nav class="crumbs" aria-label="현재 위치"><div class="wrap"><ol>{"".join(li)}</ol></div></nav>'


def page_hero(m):
    extra = m.get("hero_extra", "")
    lead = f'<p class="lead">{m["lead"]}</p>' if m.get("lead") else ""
    return f"""<section class="phero"><div class="wrap">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1>{m['h1']}</h1>{lead}{extra}
</div></section>"""


def build(pages):
    if os.path.isdir(OUT):
        for n in os.listdir(OUT):
            p = os.path.join(OUT, n)
            if n in ("assets", "css", "js", "_generator", "README.md"):
                continue
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    for path, m in pages.items():
        html = head(path, m) + header_html(m.get("active", ""))
        html += '<main id="main">'
        if not m.get("no_hero"):
            if m.get("crumbs"):
                html += crumbs(m["crumbs"])
            html += page_hero(m)
        html += m["body"] + "</main>" + FOOTER
        if path.endswith(".html"):
            fp = os.path.join(OUT, path.lstrip("/"))
        else:
            fp = os.path.join(OUT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w", encoding="utf-8").write(html)
    return sorted(pages)


def aux(pages):
    import datetime
    today = datetime.date.today().isoformat()
    rows = []
    for p in pages:
        if p.endswith(".html"):
            continue
        pri = meta_for(p)["pri"] or "0.5"
        freq = "weekly" if p in ("/", "/news/") else "monthly"
        rows.append(f"  <url><loc>{DOMAIN}{p}</loc><lastmod>{today}</lastmod>"
                    f"<changefreq>{freq}</changefreq><priority>{pri}</priority></url>")
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8").write(
        "# HMK Holdings Group\n"
        "User-agent: *\nAllow: /\nDisallow: /_generator/\n\n"
        "User-agent: Yeti\nAllow: /\n\n"
        "User-agent: Googlebot\nAllow: /\n\n"
        f"Sitemap: {DOMAIN}/sitemap.xml\n")
    open(os.path.join(OUT, "_redirects"), "w", encoding="utf-8").write(
        "\n".join([
            "# 구 URL → 신규 구조",
            "/greetings        /group/message/     301",
            "/about_us         /group/about/       301",
            "/about_us2        /group/about/       301",
            "/npl              /model/ai-sourcing/ 301",
            "/construction     /model/space/       301",
            "/academy          /model/             301",
            "/portfolio        /model/assets/      301",
            "/portfolio/*      /model/assets/      301",
            "/business/*       /model/             301",
            "/expertise/*      /model/             301",
            "/insight/*        /news/              301",
            "/technology       /model/ai-sourcing/ 301",
            "/affiliates/npl-platform  /affiliates/ 301",
            "/affiliates/ecommerce/*   /affiliates/ 301",
        ]) + "\n")
    open(os.path.join(OUT, "_headers"), "w", encoding="utf-8").write(
        "/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n"
        "/css/*\n  Cache-Control: public, max-age=604800\n"
        "/js/*\n  Cache-Control: public, max-age=604800\n"
        "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n"
        "  X-Frame-Options: SAMEORIGIN\n")


if __name__ == "__main__":
    import sys
    sys.path.insert(0, BASE)
    from c_home import PAGES as P1
    from c_group import PAGES as P2
    from c_model import PAGES as P3
    from c_affiliates import PAGES as P4
    from c_misc import PAGES as P5
    pages = {}
    for P in (P1, P2, P3, P4, P5):
        pages.update(P)
    built = build(pages)
    aux(built)
    # 로고 CSS 주입
    css_path = os.path.join(OUT, "css", "style.css")
    css = open(css_path, encoding="utf-8").read()
    marker = "/*LOGO_DATA*/"
    if marker in css:
        css = css.split(marker)[0] + marker
    css += (f'\n.logo-mark{{background-image:url("data:image/png;base64,{LOGO_B64}")}}'
            f'\n.logo-mark.white{{background-image:url("data:image/png;base64,{LOGOW_B64}")}}\n')
    open(css_path, "w", encoding="utf-8").write(css)
    print(f"{len(built)} pages built")
    for p in built:
        print(" ", p)
