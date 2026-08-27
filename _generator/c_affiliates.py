# -*- coding: utf-8 -*-
"""그룹사소개 — 허브 + 5개 계열사"""

ARROW = '<svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CR = [("그룹사소개", "/affiliates/")]

CTA = r'''
<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>함께할 파트너를 찾습니다</h2><p>공간·상품·기술·금융 각 분야의 제휴 제안을 기다립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/?type=partner">제휴 제안하기</a><a class="btn btn-outline-w" href="/affiliates/">계열사 전체 보기</a></div>
</div></div></section>
'''

HUB = r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="prose rv" style="max-width:46em;margin-bottom:44px">
      <h2 style="margin-top:0">법인이 나뉜 이유는<br>책임이 다르기 때문입니다</h2>
      <p>소싱·금융, 공간운영, 유통, 방송, 온라인 판매는 각각 요구되는 전문성과 규제가 다릅니다. HMK는 기능별로 법인을 분리해 각자의 책임을 분명히 하고, 그룹이 전체 전략을 조율합니다. 아래에서 각 계열사가 밸류업 순환의 어느 구간을 맡는지 확인하실 수 있습니다.</p>
    </div>
    <div class="grid g3">
      <a class="card rv" href="/affiliates/loan/"><div class="card-ic">🏢</div>
        <span class="chip" style="margin-bottom:10px">STEP 01</span>
        <h3>HMK 대부</h3><p>AI 프롭테크 소싱, 부동산 매입, 채권 매입, 경·공매. 그룹의 자산 확보와 금융 구조를 담당합니다.</p><span class="chip" style="margin-top:12px;font-size:11px">공식 사이트 운영</span>
        <span class="link-more" style="margin-top:16px">자세히 보기 __ARR__</span></a>
      <a class="card rv" href="/affiliates/storage/"><div class="card-ic">📦</div>
        <span class="chip" style="margin-bottom:10px">STEP 02 · B1</span>
        <h3>HMK 스토리지</h3><p>무인 공유창고 <b>오렌지</b>의 조성·운영. 유닛 설계, 전환 시공 관리, IoT 관제를 책임집니다.</p><span class="chip" style="margin-top:12px;font-size:11px">공식 사이트 운영</span>
        <span class="link-more" style="margin-top:16px">자세히 보기 __ARR__</span></a>
      <a class="card rv" href="/affiliates/market/"><div class="card-ic">🛒</div>
        <span class="chip" style="margin-bottom:10px">STEP 02 · 1F</span>
        <h3>HMK 오렌지마켓</h3><p>창고형 할인매장과 공동구매 운영. 오프라인 고객 접점을 만들고 상권을 회복시킵니다.</p><span class="chip" style="margin-top:12px;font-size:11px">공식 사이트 운영</span>
        <span class="link-more" style="margin-top:16px">자세히 보기 __ARR__</span></a>
      <a class="card rv" href="/affiliates/live/"><div class="card-ic">🎥</div>
        <span class="chip" style="margin-bottom:10px">STEP 02 · 2F</span>
        <h3>HMK 라이브커머스</h3><p>라이브 방송 제작·송출과 셀러 통합관리·정산. 오프라인 상품을 전국 판매로 확장합니다.</p><span class="chip" style="margin-top:12px;font-size:11px">공식 사이트 운영</span>
        <span class="link-more" style="margin-top:16px">자세히 보기 __ARR__</span></a>
      <a class="card rv" href="/affiliates/ecommerce/"><div class="card-ic">💻</div>
        <span class="chip" style="margin-bottom:10px">STEP 02 · ONLINE</span>
        <h3>HMK E커머스</h3><p>오렌지 1,000원마켓 등 온라인 쇼핑몰 운영. 그룹의 상품을 온라인 채널로 확장합니다.</p><span class="chip" style="margin-top:12px;font-size:11px">공식 사이트 운영</span>
        <span class="link-more" style="margin-top:16px">자세히 보기 __ARR__</span></a>
      <div class="card navy rv"><div class="card-ic">⚙️</div>
        <span class="chip" style="margin-bottom:10px;border-color:rgba(255,255,255,.3);color:rgba(255,255,255,.8)">GROUP</span>
        <h3>통합매입관리</h3><p>계열사 전체의 상품·제품을 통합 관리합니다. 매입·재고·유통·정산을 하나의 시스템으로 연결하는 그룹 운영 코어입니다.</p></div>
    </div>
    <div class="note-box rv" style="margin-top:26px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px">
      <div><b>계열사와 사업부는 개별 홈페이지를 함께 운영합니다.</b><br>서비스 이용, 입점·셀러 신청, 지점 안내는 각 사이트에서 확인하실 수 있습니다.</div>
      <a class="btn btn-primary btn-sm" href="/sites/">관련 사이트 전체 보기 ''' + ARROW + r'''</a>
    </div>
    <p class="note-plain rv" style="margin-top:16px">· 각 법인의 등기 정보(법인명·대표·등록번호)는 페이지 하단 공통 표기를 따릅니다.</p>
  </div>
</section>
'''.replace("__ARR__", ARROW) + CTA


def aff(intro, table, points, extra=""):
    pts = "".join(f'<div class="card rv"><h3 style="font-size:17px">{t}</h3><p>{d}</p></div>' for t, d in points)
    return f'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="split">
      <div class="prose rv">{intro}</div>
      <div class="rv"><div class="tbl-wrap"><table class="tbl">{table}</table></div></div>
    </div>
  </div>
</section>
<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">WHAT WE DO</span><h2>핵심 업무</h2></div></div>
    <div class="grid g4">{pts}</div>
  </div>
</section>{extra}''' + CTA


LOAN = aff(
    """<h2 style="margin-top:0">그룹의 자산 확보를<br>책임지는 법인</h2>
    <p>HMK 대부는 AI 프롭테크 소싱 시스템을 운용하며 그룹이 매입할 자산을 찾아내고 확보하는 법인입니다. 경·공매, 부실채권 매입, 급매 협상 등 물건에 맞는 경로를 설계하고, 권리관계가 복잡한 자산의 문제를 해결합니다.</p>
    <p>담보 기반 금융 업무는 관계 법령에 따라 등록된 범위 안에서 수행하며, 자산 확보·정상화 과정에 필요한 금융 구조를 지원합니다. 모든 거래는 법정 최고금리(연 20%) 이내로 이루어집니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://hmknplauction.pages.dev" target="_blank" rel="noopener">HMK 대부 공식 사이트 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>법인</th><td>에이치엠케이홀딩스대부 주식회사<br>대표이사 이영복 · 사업자등록 501-87-03194</td></tr>
    <tr><th>담당 단계</th><td>STEP 01 — AI 소싱 · 매입 · 권리 정상화</td></tr>
    <tr><th>주요 업무</th><td>AI 프롭테크 소싱 · 부동산 매입 · 채권 매입 · 경·공매</td></tr>
    <tr><th>대부업 등록</th><td>등록기관·등록번호: ○○○○○○ (게재 전 최종 확인 중)</td></tr>
    <tr><th>이자율</th><td>법정 최고금리 연 20% 이내 (연체이자율 포함 관계 법령 준수)</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://hmknplauction.pages.dev" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">hmknplauction.pages.dev</a></td></tr>
    <tr><th>상담</th><td><a href="tel:1555-5335" style="font-weight:700;color:var(--orange-deep)">1555-5335</a></td></tr>""",
    [("AI 프롭테크 소싱", "월 23만 건 이상의 물건 데이터를 분석해 저평가 자산 후보군을 선별합니다."),
     ("권리분석·협상", "유치권·법정지상권·선순위 임차권 등 하자를 분석하고 해결 경로를 설계합니다."),
     ("경·공매 실행", "입찰가 산정부터 잔금·명도까지 확보 절차를 체크리스트로 관리합니다."),
     ("금융 구조 지원", "담보 기반 금융으로 자산 확보·정상화 과정의 자금 구조를 뒷받침합니다.")],
    r'''
<section class="sec">
  <div class="wrap">
    <div class="note-box rv">
      <b>대부(중개)업 이용 시 유의사항</b><br>
      · 과도한 빚, 고통의 시작입니다.<br>
      · 대출 시 귀하의 신용점수 또는 등급이 하락할 수 있습니다.<br>
      · 중개수수료를 요구하거나 받는 행위는 불법입니다.<br>
      · 상환 능력에 맞는 계획적인 이용이 필요합니다.
    </div>
  </div>
</section>''')

STORAGE = aff(
    """<h2 style="margin-top:0">공간을 수익으로<br>바꾸는 법인</h2>
    <p>HMK 스토리지는 그룹이 확보한 자산의 지하층을 무인 공유창고 <strong>오렌지</strong>로 전환하고 운영하는 법인입니다. 전환 설계와 시공 관리, 오픈 이후의 무인 운영과 고객 서비스, IoT 유닛 관리까지 책임집니다.</p>
    <p>비대면 계약·결제, 스마트 출입 통제, 24시간 CCTV 관제가 하나의 시스템으로 연동되어 상주 인력 없이 운영됩니다. 개인의 계절용품부터 소상공인의 재고까지, 집 가까운 곳에 안전하게 보관하는 생활 인프라를 지향합니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://hmkstorage.pages.dev" target="_blank" rel="noopener">HMK 스토리지 공식 사이트 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a><a class="btn btn-ghost" href="https://storage-orange.co.kr" target="_blank" rel="noopener">오렌지 공유창고 서비스 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>법인</th><td>에이치엠케이스토리지 주식회사<br>대표이사 이영복 · 사업자등록 229-87-03308</td></tr>
    <tr><th>담당 단계</th><td>STEP 02 — 공간수익화 (B1 공유창고)</td></tr>
    <tr><th>주요 업무</th><td>공유창고 오렌지 조성·운영 · 유닛 설계 · IoT 관제</td></tr>
    <tr><th>브랜드</th><td>공유창고 오렌지</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://hmkstorage.pages.dev" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">hmkstorage.pages.dev</a><br><a href="https://storage-orange.co.kr" target="_blank" rel="noopener" style="text-decoration:underline">storage-orange.co.kr</a> (서비스 사이트)</td></tr>
    <tr><th>소재지</th><td>서울특별시 강남구 봉은사로 129-1, 751빌딩 3층</td></tr>""",
    [("전환 설계·시공 관리", "실측과 동선 설계를 거쳐 유닛을 배치하고, 보안·환경 설비를 표준 사양으로 시공합니다."),
     ("무인 운영", "비대면 계약·결제와 스마트 출입으로 상주 인력 없이 24시간 운영합니다."),
     ("IoT 관제", "온·습도, 화재 감지, CCTV가 통합 대시보드로 연결되어 이상상황에 즉시 대응합니다."),
     ("입·출고 지원", "공용 장비와 출고·배송 연계로 개인과 소상공인의 이용 편의를 높입니다.")])

MARKET = aff(
    """<h2 style="margin-top:0">오프라인 고객 접점을<br>만드는 법인</h2>
    <p>HMK 오렌지마켓은 확보한 자산의 1층에 창고형 할인매장을 조성하고 운영하는 법인입니다. 그룹이 직접 매입한 상품을 창고형으로 진열해 판매하며, 공동구매로 매입 단가를 낮춰 가격 경쟁력을 확보합니다.</p>
    <p>오프라인 매장은 단순한 판매 공간이 아닙니다. 집객이 만드는 유동 인구가 건물 전체의 상권 가치를 끌어올리고, 이곳에서 확인된 인기 상품이 2층 라이브커머스와 온라인 쇼핑몰의 판매 품목이 됩니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://hmkorangemarket.pages.dev" target="_blank" rel="noopener">오렌지 창고마켓 사이트 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>부문</th><td>HMK 오렌지마켓</td></tr>
    <tr><th>담당 단계</th><td>STEP 02 — 공간수익화 (1F 창고형 할인매장)</td></tr>
    <tr><th>주요 업무</th><td>창고형 할인매장 운영 · 공동구매 · 상품 매입</td></tr>
    <tr><th>취급 카테고리</th><td>식품 · 생활용품 · 가전리빙 · 대량벌크</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://hmkorangemarket.pages.dev" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">hmkorangemarket.pages.dev</a></td></tr>
    <tr><th>문의</th><td><a href="/contact/?type=partner" style="text-decoration:underline">입점·제휴 문의</a></td></tr>""",
    [("창고형 할인매장 운영", "카테고리별 진열과 벌크 판매로 창고형 매장의 가격 경쟁력을 구현합니다."),
     ("공동구매", "그룹 채널의 수요를 모아 매입 단가를 낮추고 그 이익을 가격에 반영합니다."),
     ("상품 소싱", "직접 매입한 상품을 오프라인·온라인 채널에 동시에 공급합니다."),
     ("상권 회복", "집객으로 유동 인구를 만들어 건물과 주변 상권의 가치를 함께 끌어올립니다.")])

LIVE = aff(
    """<h2 style="margin-top:0">상품을 전국으로<br>확장하는 법인</h2>
    <p>HMK 라이브커머스는 자산 2층에 스튜디오를 조성하고 라이브 방송 제작·송출을 담당하는 법인입니다. 아래층 매장의 상품을 그대로 방송하고, 주문은 같은 건물의 물류 코어에서 바로 출고됩니다.</p>
    <p>입점 셀러에게는 스튜디오와 물류, 정산 시스템을 함께 제공합니다. 방송 장비와 창고를 따로 마련하기 어려운 소상공인이 판매에만 집중할 수 있는 환경을 만드는 것이 이 법인의 역할입니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://orangelivehub.pages.dev" target="_blank" rel="noopener">오렌지 라이브쇼핑 사이트 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>부문</th><td>HMK 라이브커머스</td></tr>
    <tr><th>담당 단계</th><td>STEP 02 — 공간수익화 (2F 라이브커머스 스튜디오)</td></tr>
    <tr><th>주요 업무</th><td>라이브 방송 제작·송출 · 셀러 통합관리 · 정산</td></tr>
    <tr><th>송출 채널</th><td>유튜브 · 네이버 등 외부 플랫폼</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://orangelivehub.pages.dev" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">orangelivehub.pages.dev</a></td></tr>
    <tr><th>문의</th><td><a href="/contact/?type=partner" style="text-decoration:underline">셀러 입점 문의</a></td></tr>""",
    [("방송 제작·송출", "스튜디오 시설과 제작 인력을 갖춰 촬영부터 송출까지 한 곳에서 진행합니다."),
     ("셀러 통합관리", "입점 셀러의 상품 등록, 방송 일정, 주문 처리를 하나의 체계로 관리합니다."),
     ("물류 연계", "같은 건물의 통합 물류 코어와 연결되어 주문 즉시 포장·출고가 이루어집니다."),
     ("정산 지원", "판매 정산 내역을 투명하게 관리합니다. 정산 대금은 그룹 운영자금과 분리해 취급합니다.")],
    r'''
<section class="sec">
  <div class="wrap">
    <div class="note-box rv"><b>정산에 관한 안내</b> — 셀러 판매대금의 정산은 관련 법령이 정한 절차와 요건에 따라 수행합니다. 정산 대금은 그룹의 운영자금과 분리해 관리하며, 세부 정산 조건은 입점 계약 시 개별 안내드립니다.</div>
  </div>
</section>''')

ECOM = aff(
    """<h2 style="margin-top:0">온라인으로<br>판매를 넓히는 법인</h2>
    <p>HMK E커머스는 <strong>오렌지 1,000원마켓</strong>을 비롯한 온라인 쇼핑몰을 운영하는 법인입니다. 오프라인 매장과 라이브커머스에서 검증된 상품을 온라인 채널로 확장해, 지역에 묶여 있던 매출을 전국으로 넓힙니다.</p>
    <p>온라인 주문은 자산 내부의 통합 물류 코어에서 처리됩니다. 별도의 물류센터를 두지 않고 보관·판매·출고가 한 건물에서 이루어지는 것이 이 구조의 강점입니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://orangemembership.pages.dev" target="_blank" rel="noopener">오렌지 멤버십 사이트 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a><a class="btn btn-ghost" href="https://hmkorangemarket.pages.dev" target="_blank" rel="noopener">오렌지 창고마켓 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>부문</th><td>HMK E커머스</td></tr>
    <tr><th>담당 단계</th><td>STEP 02 — 공간수익화 (온라인 판매)</td></tr>
    <tr><th>주요 업무</th><td>온라인 쇼핑몰 운영 · 상품 등록·판매 · 고객 대응</td></tr>
    <tr><th>운영 채널</th><td>오렌지 1,000원마켓 등</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://orangemembership.pages.dev" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">orangemembership.pages.dev</a> (오렌지 멤버십)</td></tr>
    <tr><th>문의</th><td><a href="/contact/?type=partner" style="text-decoration:underline">입점·제휴 문의</a></td></tr>""",
    [("온라인 쇼핑몰 운영", "상품 등록부터 주문·배송·고객 응대까지 온라인 판매 전 과정을 담당합니다."),
     ("채널 연동", "오프라인 매장·라이브커머스의 상품을 온라인에 동일하게 노출합니다."),
     ("물류 연계", "건물 내 통합 물류 코어에서 포장·출고가 이루어져 처리 속도가 빠릅니다."),
     ("데이터 활용", "온라인 판매 데이터를 매입과 방송 편성 판단에 반영합니다.")])

# ───────────────── 관련 사이트 안내 ─────────────────
EXT = '<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def site(icon, name, url, desc, label=None, soon=False):
    if soon:
        return (f'<div class="site-card soon"><div class="st"><span class="ic">{icon}</span>'
                f'<h3>{name}</h3></div><p>{desc}</p>'
                f'<span class="url">홈페이지 준비 중</span></div>')
    return (f'<a class="site-card" href="https://{url}" target="_blank" rel="noopener">'
            f'<div class="st"><span class="ic">{icon}</span><h3>{name}</h3></div>'
            f'<p>{desc}</p><span class="url">{label or url}{EXT}</span></a>')


SITES = (r"""
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">AFFILIATE SITES</span><h2>계열사 홈페이지</h2></div>
    <p class="lead">각 법인의 사업 소개와 전문 정보를 개별 사이트에서 확인하실 수 있습니다.</p></div>
    <div class="grid g2">
""" + site("🏢", "HMK 대부", "hmknplauction.pages.dev",
           "AI 프롭테크 소싱과 경·공매, 채권 매입을 담당하는 계열사입니다. 물건 정보와 매입 절차, 상담 안내를 확인하실 수 있습니다.")
   + site("📦", "HMK 스토리지", "hmkstorage.pages.dev",
           "무인 공유창고 오렌지를 조성·운영하는 계열사입니다. 공간 전환 사업과 지점 유치 제안을 안내합니다.")
   + r"""
    </div>
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">SERVICE SITES</span><h2>사업부 서비스 사이트</h2></div>
    <p class="lead">3 in 1 공간수익화 모델을 구성하는 각 서비스의 이용 안내와 신청은 아래에서 진행하실 수 있습니다.</p></div>
    <div class="grid g2">
""" + site("🧡", "오렌지 공유창고", "storage-orange.co.kr",
           "개인과 소상공인을 위한 무인 보관 서비스입니다. 지점 안내, 유닛 크기와 요금, 비대면 계약을 이용하실 수 있습니다.")
   + site("🛒", "오렌지 창고마켓", "hmkorangemarket.pages.dev",
           "창고형 할인매장과 공동구매 서비스입니다. 취급 상품과 매장 안내, 입점·공급 문의를 확인하실 수 있습니다.")
   + site("🎥", "오렌지 라이브쇼핑", "orangelivehub.pages.dev",
           "라이브커머스 방송과 판매 채널입니다. 방송 일정, 판매 상품, 셀러 입점 절차를 안내합니다.")
   + site("💳", "오렌지 멤버십", "orangemembership.pages.dev",
           "그룹 서비스를 함께 이용하는 회원 프로그램입니다. 혜택 구성과 가입 안내를 확인하실 수 있습니다.")
   + r"""
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">GROUP CHANNELS</span><h2>그룹 채널</h2></div>
    <p class="lead">회장 소개, 투자 안내, 인재·파트너 모집 채널을 별도로 운영합니다.</p></div>
    <div class="grid g3">
""" + site("👤", "김재동 회장 홈페이지", "kimjaedong.pages.dev",
           "HMK 홀딩스그룹 회장 김재동의 개인 홈페이지입니다. 사업 철학과 걸어온 길을 담았습니다.")
   + site("📈", "HMK 투자안내", "hmkinvestment.pages.dev",
           "사업 개요와 강점을 정리해 안내하는 채널입니다. 게재 내용은 사업 소개이며 투자 권유가 아닙니다.")
   + site("🤝", "인재·파트너 모집", "", "함께할 인재와 파트너를 위한 전용 채널입니다. 오픈 전까지는 그룹 채용 페이지와 문의 채널을 이용해 주세요.", soon=True)
   + r"""
    </div>
    <div class="note-box rv" style="margin-top:26px"><b>안내</b> — 각 사이트는 별도 도메인에서 운영되며, 사이트별로 개인정보처리방침과 이용약관이 따로 적용될 수 있습니다. 서비스 이용과 계약은 해당 사이트를 운영하는 법인·사업부와 이루어집니다. 주소는 운영 상황에 따라 변경될 수 있으며, 변경 시 이 페이지를 갱신합니다.</div>
  </div>
</section>

<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>어디로 문의해야 할지 모르시겠다면</h2><p>그룹 대표 채널로 남겨주시면 담당 부서로 정확히 전달해 드립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/">그룹 문의하기</a><a class="btn btn-outline-w" href="tel:1555-5335">1555-5335</a></div>
</div></div></section>
""")

PAGES = {
    "/affiliates/": {
        "title": "계열사 한눈에 | HMK 홀딩스그룹", "active": "그룹사소개",
        "desc": "HMK 대부, 스토리지, 오렌지마켓, 라이브커머스, E커머스 — 다섯 계열사가 밸류업 순환의 어느 구간을 맡는지 안내합니다.",
        "crumbs": [("그룹사소개", "/affiliates/")],
        "eyebrow": "AFFILIATES", "h1": "계열사 한눈에",
        "lead": "기능별로 나뉜 다섯 개 법인이 하나의 밸류업 흐름을 함께 만듭니다.",
        "body": HUB,
    },
    "/affiliates/loan/": {
        "title": "HMK 대부 | HMK 홀딩스그룹", "active": "그룹사소개",
        "desc": "AI 프롭테크 소싱, 부동산·채권 매입, 경·공매를 담당하는 HMK 대부. 그룹의 자산 확보를 책임집니다.",
        "crumbs": CR + [("HMK 대부", "/affiliates/loan/")],
        "eyebrow": "AFFILIATES / HMK LOAN", "h1": "HMK 대부",
        "lead": "AI 소싱으로 물건을 찾고, 권리 문제를 풀어 자산을 확보합니다. 밸류업 순환의 첫 단계를 담당합니다.",
        "body": LOAN,
    },
    "/affiliates/storage/": {
        "title": "HMK 스토리지 | HMK 홀딩스그룹", "active": "그룹사소개",
        "desc": "무인 공유창고 오렌지의 조성·운영 법인 HMK 스토리지 — 유닛 설계, 전환 시공, IoT 관제를 책임집니다.",
        "crumbs": CR + [("HMK 스토리지", "/affiliates/storage/")],
        "eyebrow": "AFFILIATES / HMK STORAGE", "h1": "HMK 스토리지",
        "lead": "비어 있던 지하층을 24시간 무인 보관 시설로 바꿉니다. 공간수익화의 기반 층을 맡습니다.",
        "body": STORAGE,
    },
    "/affiliates/market/": {
        "title": "HMK 오렌지마켓 | HMK 홀딩스그룹", "active": "그룹사소개",
        "desc": "창고형 할인매장과 공동구매를 운영하는 HMK 오렌지마켓 — 오프라인 고객 접점을 만들고 상권을 회복시킵니다.",
        "crumbs": CR + [("HMK 오렌지마켓", "/affiliates/market/")],
        "eyebrow": "AFFILIATES / ORANGE MARKET", "h1": "HMK 오렌지마켓",
        "lead": "1층에 사람이 모이면 건물 전체가 살아납니다. 창고형 할인매장으로 집객과 매출을 동시에 만듭니다.",
        "body": MARKET,
    },
    "/affiliates/live/": {
        "title": "HMK 라이브커머스 | HMK 홀딩스그룹", "active": "그룹사소개",
        "desc": "라이브 방송 제작·송출과 셀러 통합관리를 담당하는 HMK 라이브커머스 — 오프라인 상품을 전국 판매로 확장합니다.",
        "crumbs": CR + [("HMK 라이브커머스", "/affiliates/live/")],
        "eyebrow": "AFFILIATES / LIVE COMMERCE", "h1": "HMK 라이브커머스",
        "lead": "같은 건물에서 촬영하고, 방송하고, 출고합니다. 셀러에게는 스튜디오와 물류를 함께 제공합니다.",
        "body": LIVE,
    },
    "/sites/": {
        "title": "관련 사이트 안내 | HMK 홀딩스그룹", "active": "그룹사소개",
        "desc": "HMK 스토리지·HMK 대부 등 계열사 홈페이지와 오렌지 공유창고·창고마켓·라이브쇼핑·멤버십 서비스 사이트, 그룹 채널을 한곳에 안내합니다.",
        "crumbs": CR + [("관련 사이트 안내", "/sites/")],
        "eyebrow": "RELATED SITES", "h1": "관련 사이트 안내",
        "lead": "계열사와 사업부는 각각의 홈페이지를 함께 운영합니다. 찾으시는 정보의 위치를 한곳에 정리했습니다.",
        "body": SITES,
    },
    "/affiliates/ecommerce/": {
        "title": "HMK E커머스 | HMK 홀딩스그룹", "active": "그룹사소개",
        "desc": "오렌지 1,000원마켓 등 온라인 쇼핑몰을 운영하는 HMK E커머스 — 그룹 상품을 온라인 채널로 확장합니다.",
        "crumbs": CR + [("HMK E커머스", "/affiliates/ecommerce/")],
        "eyebrow": "AFFILIATES / E-COMMERCE", "h1": "HMK E커머스",
        "lead": "지역에 묶여 있던 매출을 전국으로 넓힙니다. 온라인 주문도 같은 건물에서 출고됩니다.",
        "body": ECOM,
    },
}
