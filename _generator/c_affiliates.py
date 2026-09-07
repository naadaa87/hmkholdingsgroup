# -*- coding: utf-8 -*-
"""그룹사소개 — 허브 + 5개 계열사"""

ARROW = '<svg viewBox="0 0 16 16" width="16" height="16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CR = [("HMK그룹사", "/affiliates/")]

CTA = r'''
<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>함께할 파트너를 찾습니다</h2><p>공간·상품·기술·금융 각 분야의 제휴 제안을 기다립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/?type=partner">제휴 제안하기</a><a class="btn btn-outline-w" href="/affiliates/">HMK그룹사 전체보기</a></div>
</div></div></section>
'''

CTA_HUB = r'''
<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>함께할 파트너를 찾습니다</h2><p>공간·상품·기술·금융 각 분야의 제휴 제안을 기다립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/?type=partner">제휴 제안하기</a><a class="btn btn-outline-w" href="https://hmkpartner.com" target="_blank" rel="noopener">사업파트너 모집 ↗</a></div>
</div></div></section>
'''

EXT = '<svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def gcard(no, icon, name, tag, desc, url=None, page=None, internal_only=False):
    """그룹사 카드 — 외부 홈페이지 + 내부 소개 링크"""
    links = []
    if url:
        links.append(f'<a class="g-link" href="https://{url}" target="_blank" rel="noopener">홈페이지 방문 {EXT}</a>')
    if page:
        links.append(f'<a class="g-link sub" href="{page}">소개 보기 {ARROW}</a>')
    urltxt = f'<span class="g-url">{url}</span>' if url else '<span class="g-url mute">그룹 내부 운영 시스템</span>'
    cls = "gcard rv" + (" gcard-int" if internal_only else "")
    return f'''
      <div class="{cls}">
        <div class="g-top"><span class="g-no">{no:02d}</span><span class="g-ic">{icon}</span><span class="chip">{tag}</span></div>
        <h3>{name}</h3>
        <p>{desc}</p>
        {urltxt}
        <div class="g-links">{"".join(links)}</div>
      </div>'''


HUB = (r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="prose rv" style="max-width:48em;margin-bottom:44px">
      <h2 style="margin-top:0">상업용 부동산 매입부터<br>자산가치 밸류업까지! HMK홀딩스그룹</h2>
      <p>500억이상 대형 상업용 부동산을 중심으로, HMK홀딩스그룹은 매입·소싱·부동산·금융·공간운영·유통·방송·온라인판매까지, 밸류업 플랫폼을 직접 운영합니다. <strong class="accent">HMK와 가치!</strong></p>
    </div>
    <div class="grid g3">
'''
+ gcard(1, "🏢", "HMK 대부", "STEP 01 · 매입", "AI 프롭테크 소싱, 경·공매, 채권 매입. 상업용 부동산 확보와 금융 구조를 담당하는 계열사입니다.", "hmknplauction.pages.dev", "/affiliates/loan/")
+ gcard(2, "📦", "HMK 스토리지", "STEP 02 · B1", "무인 공유창고 오렌지를 조성·운영합니다. 유닛 설계, 전환 시공, IoT 관제를 책임집니다.", "hmkstorage.com", "/affiliates/storage/")
+ gcard(3, "👤", "김재동 회장", "CHAIRMAN", "국내 AI부동산 초저가 매입시스템을 최초 구축한 HMK홀딩스그룹 회장. 사업 철학과 걸어온 길을 담은 개인 홈페이지입니다.", "kimjaedong.com", "/group/message/")
+ gcard(4, "🛒", "오렌지 창고마켓", "STEP 02 · 1F", "창고형 할인매장과 오렌지 1,000원마켓 온라인몰. 공동구매로 가격을 낮추고 집객으로 상권을 살립니다.", "orange1000.com", "/affiliates/market/")
+ gcard(5, "🎥", "오렌지 라이브커머스", "STEP 02 · 2F", "라이브 방송 제작·송출과 셀러 통합관리. 스튜디오와 물류를 함께 제공해 전국 판매로 확장합니다.", "orangeliveon.com", "/affiliates/live/")
+ gcard(6, "🧡", "오렌지 공유창고", "SERVICE", "개인·소상공인을 위한 무인 보관 서비스. 지점 안내, 유닛 요금, 비대면 계약을 이용하실 수 있습니다.", "storage-orange.co.kr", "/affiliates/storage/")
+ gcard(7, "💳", "HMK 오렌지 멤버십", "SYNERGY", "창고마켓·라이브커머스·공유창고를 하나의 회원으로 잇는 통합 멤버십. 포인트 통합과 교차 혜택으로 매출을 활성화합니다.", "orangemembership.com", "/affiliates/membership/")
+ gcard(8, "🤝", "HMK 파트너모집", "PARTNER", "사업총괄·분야별 파트너·투자 파트너를 모집하는 전용 채널입니다. 함께 성장할 파트너를 기다립니다.", "hmkpartner.com", "/careers/")
+ gcard(9, "⚙️", "통합물류·유통시스템", "GROUP CORE", "그룹사 전체의 상품을 통합 관리합니다. 매입·재고·포장·출고·정산을 하나로 연결해 재고 하나로 세 채널에 판매하는 운영 코어입니다.", None, "/model/synergy/", internal_only=True)
+ r'''
    </div>
    <p class="note-plain rv" style="margin-top:22px">· 각 홈페이지는 별도 도메인에서 운영되며 사이트별 이용약관이 적용될 수 있습니다. 법인 등기 정보(법인명·대표·등록번호)는 페이지 하단 공통 표기를 따릅니다.</p>
  </div>
</section>
''' + CTA_HUB)


def aff(intro, table, points, extra="", visual="", gallery=""):
    pts = "".join(f'<div class="card rv"><h3 style="font-size:17px">{t}</h3><p>{d}</p></div>' for t, d in points)
    vis = f'<div class="page-visual rv" style="margin-bottom:clamp(40px,5vw,60px)">{visual}</div>' if visual else ""
    return f'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    {vis}
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
    {gallery}
  </div>
</section>{extra}''' + CTA


LOAN = aff(
    """<h2 style="margin-top:0">그룹의 자산 확보를<br>책임지는 법인</h2>
    <p>HMK 대부는 AI 프롭테크 소싱 시스템을 운용하며 그룹이 매입할 자산을 찾아내고 확보하는 법인입니다. 경·공매, 부실채권 매입, 급매 협상 등 물건에 맞는 경로를 설계하고, 권리관계가 복잡한 자산의 문제를 해결합니다.</p>
    <p>담보 기반 금융 업무는 관계 법령에 따라 등록된 범위 안에서 수행하며, 자산 확보·정상화 과정에 필요한 금융 구조를 지원합니다. 모든 거래는 법정 최고금리(연 20%) 이내로 이루어집니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://hmknplauction.pages.dev" target="_blank" rel="noopener">HMK 대부 공식 사이트 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
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
    <div class="extlinks"><a class="btn btn-primary" href="https://hmkstorage.com" target="_blank" rel="noopener">HMK 스토리지 공식 사이트 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a><a class="btn btn-ghost" href="https://storage-orange.co.kr" target="_blank" rel="noopener">오렌지 공유창고 서비스 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>법인</th><td>에이치엠케이스토리지 주식회사<br>대표이사 이영복 · 사업자등록 229-87-03308</td></tr>
    <tr><th>담당 단계</th><td>STEP 02 — 공간수익화 (B1 공유창고)</td></tr>
    <tr><th>주요 업무</th><td>공유창고 오렌지 조성·운영 · 유닛 설계 · IoT 관제</td></tr>
    <tr><th>브랜드</th><td>공유창고 오렌지</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://hmkstorage.com" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">hmkstorage.com</a><br><a href="https://storage-orange.co.kr" target="_blank" rel="noopener" style="text-decoration:underline">storage-orange.co.kr</a> (서비스 사이트)</td></tr>
    <tr><th>소재지</th><td>서울특별시 강남구 봉은사로 129-1, 751빌딩 3층</td></tr>""",
    [("전환 설계·시공 관리", "실측과 동선 설계를 거쳐 유닛을 배치하고, 보안·환경 설비를 표준 사양으로 시공합니다."),
     ("무인 운영", "비대면 계약·결제와 스마트 출입으로 상주 인력 없이 24시간 운영합니다."),
     ("IoT 관제", "온·습도, 화재 감지, CCTV가 통합 대시보드로 연결되어 이상상황에 즉시 대응합니다."),
     ("입·출고 지원", "공용 장비와 출고·배송 연계로 개인과 소상공인의 이용 편의를 높입니다.")],
    visual='<img src="/assets/storage/entrance.jpg" alt="오렌지 공유창고 매장 입구 — 24시간 무인 출입" width="1600" height="1131">',
    gallery='<div class="gallery g3 rv" style="margin-top:34px"><figure><img src="/assets/storage/using.jpg" alt="오렌지 공유창고 유닛을 이용하는 고객" loading="lazy"><figcaption>스마트 도어락으로 열리는 개인 유닛</figcaption></figure><figure><img src="/assets/storage/sizes.jpg" alt="소형·중형·대형·비즈니스 유닛 크기 안내" loading="lazy"><figcaption>소형부터 비즈니스형까지 다양한 유닛</figcaption></figure><figure><img src="/assets/storage/zoning.jpg" alt="A·B·C 존과 접수·포장·로딩 구역 조감도" loading="lazy"><figcaption>존 구성과 입·출고 동선</figcaption></figure></div>')

MARKET = aff(
    """<h2 style="margin-top:0">오프라인 고객 접점을<br>만드는 법인</h2>
    <p>HMK 오렌지마켓은 확보한 자산의 1층에 창고형 할인매장을 조성하고 운영하는 법인입니다. 그룹이 직접 매입한 상품을 창고형으로 진열해 판매하며, 공동구매로 매입 단가를 낮춰 가격 경쟁력을 확보합니다.</p>
    <p>오프라인 매장은 단순한 판매 공간이 아닙니다. 집객이 만드는 유동 인구가 건물 전체의 상권 가치를 끌어올리고, 이곳에서 확인된 인기 상품이 2층 라이브커머스와 <strong>오렌지 1,000원마켓</strong> 온라인몰의 판매 품목이 됩니다. 온라인 주문은 같은 건물의 통합 물류 코어에서 바로 출고됩니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://orange1000.com" target="_blank" rel="noopener">오렌지 창고마켓 사이트 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>부문</th><td>오렌지 창고마켓 (HMK 오렌지마켓)</td></tr>
    <tr><th>담당 단계</th><td>STEP 02 — 공간수익화 (1F 창고형 할인매장)</td></tr>
    <tr><th>주요 업무</th><td>창고형 할인매장 운영 · 오렌지 1,000원마켓 온라인몰 · 공동구매 · 상품 매입</td></tr>
    <tr><th>취급 카테고리</th><td>식품 · 생활용품 · 가전리빙 · 대량벌크</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://orange1000.com" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">orange1000.com</a></td></tr>
    <tr><th>문의</th><td><a href="/contact/?type=partner" style="text-decoration:underline">입점·제휴 문의</a></td></tr>""",
    [("창고형 할인매장 운영", "카테고리별 진열과 벌크 판매로 창고형 매장의 가격 경쟁력을 구현합니다."),
     ("오렌지 1,000원마켓 온라인몰", "오프라인에서 검증된 상품을 온라인으로 확장합니다. 주문은 건물 내 물류 코어에서 출고됩니다."),
     ("공동구매", "그룹 채널의 수요를 모아 매입 단가를 낮추고 그 이익을 가격에 반영합니다."),
     ("상권 회복", "집객으로 유동 인구를 만들어 건물과 주변 상권의 가치를 함께 끌어올립니다.")],
    visual='<img src="/assets/market/exterior.jpg" alt="오렌지 창고마켓 매장 외관 — 초저가! 창고형!" width="1491" height="1055">',
    gallery='<div class="gallery g3 rv" style="margin-top:34px"><figure><img src="/assets/market/interior.jpg" alt="오렌지 창고마켓 내부 — 카테고리별 진열" loading="lazy"><figcaption>식품 · 생활용품 · 가전리빙 · 대량벌크</figcaption></figure><figure><img src="/assets/market/delivery.jpg" alt="오렌지 창고마켓 배송 트럭과 픽업 구역" loading="lazy"><figcaption>빠른 배송 · 매장 픽업</figcaption></figure><figure><img src="/assets/live/live-screen.jpg" alt="오렌지 라이브쇼핑 방송 화면 — 매장 상품을 온라인으로" loading="lazy"><figcaption>같은 상품이 라이브 방송에서 판매됩니다</figcaption></figure></div>')

LIVE = aff(
    """<h2 style="margin-top:0">상품을 전국으로<br>확장하는 법인</h2>
    <p>HMK 라이브커머스는 자산 2층에 스튜디오를 조성하고 라이브 방송 제작·송출을 담당하는 법인입니다. 아래층 매장의 상품을 그대로 방송하고, 주문은 같은 건물의 물류 코어에서 바로 출고됩니다.</p>
    <p>입점 셀러에게는 스튜디오와 물류, 정산 시스템을 함께 제공합니다. 방송 장비와 창고를 따로 마련하기 어려운 소상공인이 판매에만 집중할 수 있는 환경을 만드는 것이 이 법인의 역할입니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://orangeliveon.com" target="_blank" rel="noopener">오렌지 라이브커머스 사이트 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>부문</th><td>오렌지 라이브커머스 (HMK 라이브커머스)</td></tr>
    <tr><th>담당 단계</th><td>STEP 02 — 공간수익화 (2F 라이브커머스 스튜디오)</td></tr>
    <tr><th>주요 업무</th><td>라이브 방송 제작·송출 · 셀러 통합관리 · 정산</td></tr>
    <tr><th>송출 채널</th><td>유튜브 · 네이버 등 외부 플랫폼</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://orangeliveon.com" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">orangeliveon.com</a></td></tr>
    <tr><th>문의</th><td><a href="/contact/?type=partner" style="text-decoration:underline">셀러 입점 문의</a></td></tr>""",
    [("방송 제작·송출", "스튜디오 시설과 제작 인력을 갖춰 촬영부터 송출까지 한 곳에서 진행합니다."),
     ("셀러 통합관리", "입점 셀러의 상품 등록, 방송 일정, 주문 처리를 하나의 체계로 관리합니다."),
     ("물류 연계", "같은 건물의 통합 물류 코어와 연결되어 주문 즉시 포장·출고가 이루어집니다."),
     ("정산 지원", "판매 정산 내역을 투명하게 관리합니다. 정산 대금은 그룹 운영자금과 분리해 취급합니다.")],
    visual='<img src="/assets/live/studio.jpg" alt="오렌지 라이브쇼핑 스튜디오 — 조명·카메라 세팅과 상품 진열대" width="1491" height="1055">',
    gallery='<div class="gallery g3 rv" style="margin-top:34px"><figure><img src="/assets/live/seller.jpg" alt="셀러 ON AIR — 입점 셀러의 라이브 방송" loading="lazy"><figcaption>입점 셀러가 직접 방송합니다</figcaption></figure><figure><img src="/assets/live/seller-fresh.jpg" alt="신선식품 셀러의 라이브 방송" loading="lazy"><figcaption>농산물 · 수제식품 등 다양한 셀러</figcaption></figure><figure><img src="/assets/live/logistics.jpg" alt="주문부터 배송까지 통합 물류 프로세스" loading="lazy"><figcaption>주문 즉시 같은 건물에서 출고</figcaption></figure></div>',
    extra=r'''
<section class="sec">
  <div class="wrap">
    <div class="note-box rv"><b>정산에 관한 안내</b> — 셀러 판매대금의 정산은 관련 법령이 정한 절차와 요건에 따라 수행합니다. 정산 대금은 그룹의 운영자금과 분리해 관리하며, 세부 정산 조건은 입점 계약 시 개별 안내드립니다.</div>
  </div>
</section>''')

MEMBERSHIP = aff(
    """<h2 style="margin-top:0">하나의 회원으로<br>세 사업의 혜택을</h2>
    <p>HMK 오렌지 멤버십은 창고마켓·라이브커머스·공유창고의 고객을 <strong>하나의 회원 계정</strong>으로 묶는 통합 멤버십입니다. 어디서 가입하든 세 곳에서 포인트가 쌓이고 혜택이 교차됩니다.</p>
    <p>창고 이용자에게는 마켓 할인 쿠폰이, 마켓 고객에게는 라이브 방송 특가가, 방송 시청자에게는 창고 첫 달 혜택이 이어집니다. 한 명의 고객이 세 사업을 모두 경험하게 만드는 것 — 이것이 멤버십이 그룹 매출을 활성화하는 방식입니다.</p>
    <div class="extlinks"><a class="btn btn-primary" href="https://orangemembership.com" target="_blank" rel="noopener">오렌지 멤버십 사이트 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a><a class="btn btn-ghost" href="/model/synergy/">시너지 구조 보기 <svg viewBox="0 0 16 16" width="16" height="16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>""",
    """<tr><th>부문</th><td>HMK 오렌지 멤버십</td></tr>
    <tr><th>담당 단계</th><td>STEP 02+ — 세 사업 시너지 · 매출 활성화</td></tr>
    <tr><th>주요 업무</th><td>통합 회원 관리 · 포인트 · 교차 혜택 · 앱 운영</td></tr>
    <tr><th>적용 사업장</th><td>오렌지 창고마켓 · 오렌지 라이브커머스 · 오렌지 공유창고</td></tr>
    <tr><th>공식 사이트</th><td><a href="https://orangemembership.com" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">orangemembership.com</a></td></tr>
    <tr><th>가입</th><td>앱 또는 각 사업장 현장에서 가입</td></tr>""",
    [("통합 포인트", "세 사업장의 결제가 하나의 포인트로 쌓이고, 어디서든 사용할 수 있습니다."),
     ("교차 혜택", "창고 이용자에게 마켓 쿠폰, 마켓 고객에게 방송 특가, 시청자에게 창고 혜택이 이어집니다."),
     ("멤버 등급", "이용 실적에 따라 등급이 올라가고, 등급별 할인율과 전용 서비스가 달라집니다."),
     ("앱 · 카드", "모바일 앱과 실물 카드로 포인트 조회, 쿠폰 사용, 예약을 한 번에 처리합니다.")],
    visual='<img src="/assets/membership/card-hero.jpg" alt="HMK 오렌지 멤버십 카드와 오렌지 캐릭터 — 멤버십 전용 혜택, 포인트 적립, VIP 서비스, 이벤트 초대" width="1448" height="1086">',
    gallery='<div class="gallery g3 rv" style="margin-top:34px"><figure><img src="/assets/membership/app.jpg" alt="HMK 오렌지 멤버십 앱 화면 — 포인트·등급·쿠폰" loading="lazy"><figcaption>앱에서 포인트와 쿠폰을 한눈에</figcaption></figure><figure><img src="/assets/membership/use-market.jpg" alt="오렌지 창고마켓에서 멤버십 카드로 결제" loading="lazy"><figcaption>창고마켓 — 결제와 동시에 적립</figcaption></figure><figure><img src="/assets/membership/use-storage.jpg" alt="HMK 스토리지에서 멤버십 카드 확인" loading="lazy"><figcaption>공유창고 — 보관료 할인 적용</figcaption></figure></div>',
    extra=r'''
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">FAQ</span><h2>멤버십 자주 묻는 질문</h2></div></div>
    <div class="faq-list"><details class="faq rv"><summary>오렌지 멤버십은 어디에서 쓸 수 있나요?</summary><div class="faq-a">오렌지 창고마켓, 오렌지 라이브커머스, 오렌지 공유창고 세 곳에서 하나의 회원으로 씁니다. 어디서 가입하든 세 사업장의 포인트가 통합되고 혜택이 교차 적용됩니다.</div></details><details class="faq rv"><summary>포인트는 어떻게 쌓이고 어디에 쓰나요?</summary><div class="faq-a">창고마켓 결제, 라이브 방송 구매, 공유창고 이용료 결제 시 포인트가 쌓입니다. 쌓인 포인트는 세 곳 어디에서든 결제에 사용할 수 있습니다.</div></details><details class="faq rv"><summary>가입은 어떻게 하나요?</summary><div class="faq-a">오렌지 멤버십 앱 또는 각 사업장 현장에서 가입할 수 있습니다. 실물 카드와 모바일 앱 모두 제공되며, 앱에서 포인트 조회·쿠폰 사용·예약을 한 번에 처리합니다.</div></details></div>
  </div>
</section>
''')

# ───────────────── 관련 사이트 안내 ─────────────────
EXT = '<svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'


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
    <p class="lead">각 계열사의 사업 소개와 회장 홈페이지를 개별 사이트에서 확인하실 수 있습니다.</p></div>
    <div class="grid g3">
""" + site("🏢", "HMK 대부", "hmknplauction.pages.dev",
           "AI 프롭테크 소싱과 경·공매, 채권 매입을 담당하는 계열사입니다. 물건 정보와 매입 절차, 상담 안내를 확인하실 수 있습니다.")
   + site("📦", "HMK 스토리지", "hmkstorage.com",
           "무인 공유창고 오렌지를 조성·운영하는 계열사입니다. 공간 전환 사업과 지점 유치 제안을 안내합니다.")
   + site("👤", "김재동 회장", "kimjaedong.com",
           "HMK홀딩스그룹 회장 김재동의 개인 홈페이지입니다. 사업 철학과 걸어온 길을 담았습니다.")
   + r"""
    </div>
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">SERVICE SITES</span><h2>사업부 서비스 사이트</h2></div>
    <p class="lead">3 in 1 공간수익화 모델을 구성하는 각 서비스의 이용 안내와 신청은 아래에서 진행하실 수 있습니다.</p></div>
    <div class="grid g2">
""" + site("🛒", "오렌지 창고마켓", "orange1000.com",
           "창고형 할인매장과 오렌지 1,000원마켓 온라인몰입니다. 취급 상품과 매장 안내, 입점·공급 문의를 확인하실 수 있습니다.")
   + site("🎥", "오렌지 라이브커머스", "orangeliveon.com",
           "라이브커머스 방송과 판매 채널입니다. 방송 일정, 판매 상품, 셀러 입점 절차를 안내합니다.")
   + site("🧡", "오렌지 공유창고", "storage-orange.co.kr",
           "개인과 소상공인을 위한 무인 보관 서비스입니다. 지점 안내, 유닛 크기와 요금, 비대면 계약을 이용하실 수 있습니다.")
   + site("💳", "오렌지 멤버십", "orangemembership.com",
           "그룹 서비스를 함께 이용하는 회원 프로그램입니다. 혜택 구성과 가입 안내를 확인하실 수 있습니다.")
   + r"""
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">GROUP CHANNELS</span><h2>그룹 채널</h2></div>
    <p class="lead">사업 안내와 파트너 모집 채널을 별도로 운영합니다.</p></div>
    <div class="grid g2">
""" + site("📈", "HMK 투자안내", "hmkinvestment.pages.dev",
           "그룹의 사업 개요와 강점, 밸류업 모델을 정리해 안내하는 채널입니다.")
   + site("🤝", "HMK 파트너모집", "hmkpartner.com", "사업총괄·분야별 파트너·투자 파트너를 모집하는 전용 채널입니다. 함께 성장할 파트너를 기다립니다.")
   + r"""
    </div>
    <p class="note-plain rv" style="margin-top:26px">· 각 사이트는 별도 도메인에서 운영되며, 서비스 이용과 계약은 해당 사이트를 운영하는 법인·사업부와 이루어집니다.</p>
  </div>
</section>

<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>어디로 문의해야 할지 모르시겠다면</h2><p>그룹 대표 채널로 남겨주시면 담당 부서로 정확히 전달해 드립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/">그룹 문의하기</a><a class="btn btn-outline-w" href="tel:1555-5335">1555-5335</a></div>
</div></div></section>
""")

PAGES = {
    "/affiliates/": {
        "title": "HMK그룹사 전체보기 | HMK홀딩스그룹", "active": "그룹사소개",
        "desc": "HMK 대부, 스토리지, 오렌지마켓, 라이브커머스, E커머스 — 다섯 계열사가 밸류업 순환의 어느 구간을 맡는지 안내합니다.",
        "crumbs": [("그룹사소개", "/affiliates/")],
        "eyebrow": "HMK GROUP", "h1": "HMK그룹사 전체보기",
        "extra_head": '''<script type="application/ld+json">{"@context": "https://schema.org", "@type": "ItemList", "name": "HMK홀딩스그룹 그룹사·사업부", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "HMK 대부", "url": "https://hmknplauction.pages.dev"}, {"@type": "ListItem", "position": 2, "name": "HMK 스토리지", "url": "https://hmkstorage.com"}, {"@type": "ListItem", "position": 3, "name": "김재동 회장", "url": "https://kimjaedong.com"}, {"@type": "ListItem", "position": 4, "name": "오렌지 창고마켓", "url": "https://orange1000.com"}, {"@type": "ListItem", "position": 5, "name": "오렌지 라이브커머스", "url": "https://orangeliveon.com"}, {"@type": "ListItem", "position": 6, "name": "오렌지 공유창고", "url": "https://storage-orange.co.kr"}, {"@type": "ListItem", "position": 7, "name": "HMK 오렌지 멤버십", "url": "https://orangemembership.com"}, {"@type": "ListItem", "position": 8, "name": "HMK 파트너모집", "url": "https://hmkpartner.com"}]}</script>''',
        "lead": "매입부터 밸류업까지, 그룹사와 사업부가 하나의 흐름으로 움직입니다. 각 홈페이지로 바로 이동하실 수 있습니다.",
        "body": HUB,
    },
    "/affiliates/loan/": {
        "title": "HMK 대부 | HMK홀딩스그룹", "active": "그룹사소개",
        "desc": "AI 프롭테크 소싱, 부동산·채권 매입, 경·공매를 담당하는 HMK 대부. 그룹의 자산 확보를 책임집니다.",
        "crumbs": CR + [("HMK 대부", "/affiliates/loan/")],
        "eyebrow": "AFFILIATES / HMK LOAN", "h1": "HMK 대부",
        "lead": "AI 소싱으로 물건을 찾고, 권리 문제를 풀어 자산을 확보합니다. 밸류업 순환의 첫 단계를 담당합니다.",
        "body": LOAN,
    },
    "/affiliates/storage/": {
        "title": "HMK 스토리지 | HMK홀딩스그룹", "active": "그룹사소개",
        "desc": "무인 공유창고 오렌지의 조성·운영 법인 HMK 스토리지 — 유닛 설계, 전환 시공, IoT 관제를 책임집니다.",
        "crumbs": CR + [("HMK 스토리지", "/affiliates/storage/")],
        "eyebrow": "AFFILIATES / HMK STORAGE", "h1": "HMK 스토리지",
        "lead_pre": "오렌지 공유창고 조성·운영",
        "lead": "비어 있던 지하층을 24시간 무인 보관 시설로 바꿉니다. 공간수익화의 기반 층을 맡습니다.",
        "body": STORAGE,
    },
    "/affiliates/market/": {
        "title": "HMK 오렌지마켓 | HMK홀딩스그룹", "active": "그룹사소개",
        "desc": "창고형 할인매장과 공동구매를 운영하는 HMK 오렌지마켓 — 오프라인 고객 접점을 만들고 상권을 회복시킵니다.",
        "crumbs": CR + [("오렌지 창고마켓", "/affiliates/market/")],
        "eyebrow": "AFFILIATES / ORANGE MARKET", "h1": "오렌지 창고마켓",
        "lead": "1층에 사람이 모이면 건물 전체가 살아납니다. 창고형 할인매장으로 집객과 매출을 동시에 만듭니다.",
        "body": MARKET,
    },
    "/affiliates/live/": {
        "title": "HMK 라이브커머스 | HMK홀딩스그룹", "active": "그룹사소개",
        "desc": "라이브 방송 제작·송출과 셀러 통합관리를 담당하는 HMK 라이브커머스 — 오프라인 상품을 전국 판매로 확장합니다.",
        "crumbs": CR + [("오렌지 라이브커머스", "/affiliates/live/")],
        "eyebrow": "AFFILIATES / LIVE COMMERCE", "h1": "오렌지 라이브커머스",
        "lead": "같은 건물에서 촬영하고, 방송하고, 출고합니다. 셀러에게는 스튜디오와 물류를 함께 제공합니다.",
        "body": LIVE,
    },
    "/affiliates/membership/": {
        "title": "오렌지 멤버십 | HMK홀딩스그룹", "active": "그룹사소개",
        "extra_head": '''<script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "오렌지 멤버십은 어디에서 쓸 수 있나요?", "acceptedAnswer": {"@type": "Answer", "text": "오렌지 창고마켓, 오렌지 라이브커머스, 오렌지 공유창고 세 곳에서 하나의 회원으로 씁니다. 어디서 가입하든 세 사업장의 포인트가 통합되고 혜택이 교차 적용됩니다."}}, {"@type": "Question", "name": "포인트는 어떻게 쌓이고 어디에 쓰나요?", "acceptedAnswer": {"@type": "Answer", "text": "창고마켓 결제, 라이브 방송 구매, 공유창고 이용료 결제 시 포인트가 쌓입니다. 쌓인 포인트는 세 곳 어디에서든 결제에 사용할 수 있습니다."}}, {"@type": "Question", "name": "가입은 어떻게 하나요?", "acceptedAnswer": {"@type": "Answer", "text": "오렌지 멤버십 앱 또는 각 사업장 현장에서 가입할 수 있습니다. 실물 카드와 모바일 앱 모두 제공되며, 앱에서 포인트 조회·쿠폰 사용·예약을 한 번에 처리합니다."}}]}</script>''',
        "desc": "창고마켓·라이브커머스·공유창고를 하나의 회원으로 잇는 HMK 오렌지 멤버십.",
        "crumbs": CR + [("오렌지 멤버십", "/affiliates/membership/")],
        "eyebrow": "AFFILIATES / ORANGE MEMBERSHIP", "h1": "HMK 오렌지 멤버십",
        "lead": "세 사업의 고객을 하나로 묶습니다. 포인트가 통합되고 혜택이 교차되면 고객은 세 번 방문합니다.",
        "body": MEMBERSHIP,
    },
    "/sites/": {
        "title": "관련 사이트 안내 | HMK홀딩스그룹", "active": "그룹사소개",
        "desc": "HMK 대부·HMK 스토리지·김재동 회장 홈페이지와 오렌지 마켓·라이브커머스·공유창고·멤버십, HMK 파트너모집·투자안내 채널을 한곳에 안내합니다.",
        "crumbs": CR + [("관련 사이트 안내", "/sites/")],
        "eyebrow": "RELATED SITES", "h1": "관련 사이트 안내",
        "lead": "계열사와 사업부는 각각의 홈페이지를 함께 운영합니다. 찾으시는 정보의 위치를 한곳에 정리했습니다.",
        "body": SITES,
    },
}
