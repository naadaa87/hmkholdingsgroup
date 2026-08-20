# -*- coding: utf-8 -*-
"""메인 — 8블록 원페이지 서사"""

ARROW = '<svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

BODY = r'''
<!-- 01 히어로 -->
<section class="hero">
  <div class="hero-in">
    <div>
      <span class="eyebrow">HMK HOLDINGS GROUP</span>
      <h1>싸게 사고,<br>자산가치 극대화,<br><span class="accent">자산을 유동화</span>합니다.</h1>
      <p class="lead">AI 프롭테크로 저평가 부동산을 감정가 대비 20% 이하로 확보하고, 한 건물에 세 개의 수익을 겹쳐 넣는 공간수익화 모델로 임대수익을 끌어올립니다. 그리고 그 자산을 유동화해 다시 다음 자산으로 순환시킵니다.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="/model/">사업모델 보기 __ARR__</a>
        <a class="btn btn-ghost" href="/model/assets/">보유 자산 보기</a>
      </div>
      <p class="hero-note">보유 자산의 매각·활용을 검토 중이신가요? 권리관계가 복잡한 물건도 검토 대상입니다.</p>
    </div>
    <div class="hero-visual">
      <img src="/assets/model/building.jpg" alt="HMK Value-Up Asset — B1 공유창고, 1F 창고형 할인매장, 2F 라이브커머스가 결합된 복합 자산" width="1600" height="1032">
      <div class="cap"><b>HMK Value-Up Asset</b><span>한 건물에서 세 가지 수익이 동시에 발생합니다</span></div>
    </div>
  </div>
  <div class="hero-steps"><ol>
    <li><span class="n">STEP 01</span><b>AI 초저가 매입</b><span>감정가 대비 20% 이하</span></li>
    <li><span class="n">STEP 02</span><b>공간 수익화</b><span>평당 임대수익 극대화</span></li>
    <li><span class="n">STEP 03</span><b>자산 유동화</b><span>토큰증권 준비 중</span></li>
    <li><span class="n">STEP 04</span><b>재투자 순환</b><span>다음 자산 확보</span></li>
  </ol></div>
</section>

<!-- 02 핵심 지표 -->
<section class="sec" style="padding-top:clamp(56px,6vw,84px);padding-bottom:0">
  <div class="wrap">
    <div class="facts rv">
      <div class="fact"><div class="num">23<small>만 건 이상</small></div><div class="lb">월간 물건 분석량</div><div class="sb">경·공매·부실채권·급매 데이터</div><span class="chip">AI 소싱 시스템</span></div>
      <div class="fact"><div class="num">20<small>% 이하</small></div><div class="lb">감정가 대비 확보 수준</div><div class="sb">권리 문제 해결을 전제로 한 매입</div><span class="chip">확보 기준</span></div>
      <div class="fact"><div class="num">450<small>% 이상</small></div><div class="lb">일반 상가 대비 수익 창출</div><div class="sb">공간수익화 모델 적용 시</div><span class="chip">모델 기준</span></div>
      <div class="fact"><div class="num">3<small>건</small></div><div class="lb">확보·전환 진행 자산</div><div class="sb">일산 · 화성 · 강동</div><span class="chip">2026.08 기준</span></div>
    </div>
  </div>
</section>

<!-- 03 보유 자산 -->
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">PORTFOLIO</span><h2>좋은 입지 위에 서 있는<br>보유 부동산</h2></div>
      <p class="lead">배후 수요가 검증된 상권에서만 확보합니다. 가격이 아니라 입지가 말해주는 가치를 보여드립니다.</p>
    </div>
    <div class="grid g3">
      <a class="card pf-card rv" href="/model/assets/#ilsan">
        <div class="ph"><img src="/assets/portfolio/ilsan.jpg" alt="일산 엠시티타워 전경" loading="lazy"><span class="badge tag">보유 물건 01</span></div>
        <div class="bd"><h3>일산 엠시티타워</h3><div class="addr">고양 일산동구 · 일산호수공원 인접 · 179평</div>
          <ul class="pts"><li>단지 950세대 + 오피스텔 646세대 자체 배후</li><li>반경 2km 인구 10만 명 생활권</li><li>일산테크노밸리 · GTX-A 수혜권</li></ul>
          <span class="link-more">입지 자세히 보기 __ARR__</span></div>
      </a>
      <a class="card pf-card rv" href="/model/assets/#hwaseong">
        <div class="ph"><img src="/assets/portfolio/hwaseong.jpg" alt="화성 송산시티 L-Tower 전경" loading="lazy"><span class="badge tag">보유 물건 02</span></div>
        <div class="bd"><h3>화성 송산시티 L-Tower</h3><div class="addr">화성 새솔동 · 송산그린시티 중심상권 · 91.4평</div>
          <ul class="pts"><li>아파트 5개 단지 8,700세대 배후</li><li>1인·신혼 가구 밀집 — 보관 수요 발생 구조</li><li>신세계 국제테마파크(예정) 배후권</li></ul>
          <span class="link-more">입지 자세히 보기 __ARR__</span></div>
      </a>
      <a class="card pf-card rv" href="/model/assets/#gangdong">
        <div class="ph"><img src="/assets/portfolio/gangdong.jpg" alt="강동 로데오팰리스 전경" loading="lazy"><span class="badge tag">보유 물건 03</span></div>
        <div class="bd"><h3>강동 로데오팰리스</h3><div class="addr">서울 강동구 천호동 · 지하 1층 · 90평</div>
          <ul class="pts"><li>천호역 5·8호선 더블 역세 생활권</li><li>로데오거리 · 현대백화점 천호점 인접</li><li>천호 재정비촉진지구 수혜권</li></ul>
          <span class="link-more">입지 자세히 보기 __ARR__</span></div>
      </a>
    </div>
  </div>
</section>

<!-- 04 순환모델 -->
<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">BUSINESS MODEL</span><h2>네 단계가<br>하나의 고리로 돌아갑니다</h2></div>
      <p class="lead">각 단계를 다른 회사에 맡기지 않습니다. 발굴부터 유동화까지 그룹이 직접 수행하기 때문에 판단이 빠르고 정확합니다.</p>
    </div>
    <div class="cyc">
      <div class="cyc-c rv"><div class="no">01</div><h3>AI 프롭테크<br>초저가 매입</h3><p>월 23만 건 이상의 물건 데이터를 분석해 저평가 자산을 선별하고, 권리 문제를 해결해 감정가 대비 20% 이하로 확보합니다.</p><div class="arw">→</div></div>
      <div class="cyc-c rv"><div class="no">02</div><h3>HMK<br>공간수익화 모델</h3><p>공유창고·창고형 할인매장·라이브커머스를 한 건물에 결합해, 단일 임차 구조로는 나올 수 없는 임대수익을 만듭니다.</p><div class="arw">→</div></div>
      <div class="cyc-c rv"><div class="no">03</div><h3>토큰증권<br>자산 유동화</h3><p>안정된 운영 수익(NOI)을 근거로 자산가치를 재평가받고, 2027년 2월 4일 시행되는 제도에 맞춰 발행·상장을 준비하고 있습니다.</p><div class="arw">→</div></div>
      <div class="cyc-c last rv"><div class="no">04</div><h3>재투자<br>선순환 확장</h3><p>유동화로 회수한 자금을 다음 자산 매입에 다시 투입합니다. 반복할수록 속도와 정확도가 올라갑니다.</p></div>
    </div>
  </div>
</section>

<!-- 05 공간수익화 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">SPACE MONETIZING</span><h2>HMK의 3 in 1<br>공간수익화 전략</h2></div>
      <p class="lead">층마다 다른 콘텐츠를 넣고 물류 동선을 공유합니다. 같은 면적에서 더 많은 수익이 나오는 이유입니다.</p>
    </div>
    <div class="split">
      <figure class="figure rv">
        <img src="/assets/model/ecosystem.jpg" alt="한 자산에서 세 가지 수익이 연결되는 HMK Value-Up 생태계 구조도" width="1448" height="1086">
        <figcaption>공유창고 · 창고형 할인매장 · 라이브커머스가 통합 물류 코어로 연결됩니다</figcaption>
      </figure>
      <div class="rv">
        <div class="floors">
          <div class="floor"><div class="lv">2F</div><div><b>라이브커머스 스튜디오</b><span>입점 셀러의 방송 제작과 송출. 유튜브·네이버 등 외부 채널로 판매를 확장합니다.</span></div></div>
          <div class="floor"><div class="lv">1F</div><div><b>창고형 할인매장 · 공동구매</b><span>오프라인 고객 접점. 매입한 상품을 직접 판매하고 온라인 쇼핑몰과 연동합니다.</span></div></div>
          <div class="floor"><div class="lv">B1</div><div><b>무인 공유창고 오렌지</b><span>비대면 계약·스마트 출입·24시간 CCTV로 상주 인력 없이 운영합니다.</span></div></div>
          <div class="floor core"><div class="lv">CORE</div><div><b>통합 물류·운영 코어</b><span>재고 관리 → 포장·검수 → 배송·출고를 하나의 시스템으로 연결해 운영비를 낮춥니다.</span></div></div>
        </div>
        <a class="btn btn-ghost" style="margin-top:24px" href="/model/space/">공간수익화 모델 자세히 __ARR__</a>
      </div>
    </div>
  </div>
</section>

<!-- 06 밸류업 효과 -->
<section class="sec sec-cool">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">VALUE-UP EFFECT</span><h2>같은 건물, 달라지는 수익 구조</h2></div>
      <p class="lead">단일 임차 구조에서는 임대료 하나가 전부입니다. 세 개의 수익원을 겹치면 현금흐름과 자산가치가 함께 움직입니다.</p>
    </div>
    <figure class="figure rv">
      <img src="/assets/model/before-after.jpg" alt="저활용 자산과 HMK Value-Up 자산의 수익 구조 비교" width="1448" height="1086">
      <figcaption>수익 구조 개선에 따른 밸류업 예시 — 자산 조건에 따라 결과는 달라질 수 있습니다</figcaption>
    </figure>
  </div>
</section>

<!-- 07 계열사 -->
<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">AFFILIATES</span><h2>다섯 개 계열사가<br>한 흐름으로 움직입니다</h2></div>
    </div>
    <div class="grid g5">
      <a class="card rv" href="/affiliates/loan/"><div class="card-ic">🏢</div><h3 style="font-size:17px">HMK 대부</h3><p>AI 프롭테크 소싱 · 채권매입 · 경공매</p></a>
      <a class="card rv" href="/affiliates/storage/"><div class="card-ic">📦</div><h3 style="font-size:17px">HMK 스토리지</h3><p>공유창고 오렌지 조성·운영 · IoT 관리</p></a>
      <a class="card rv" href="/affiliates/market/"><div class="card-ic">🛒</div><h3 style="font-size:17px">HMK 오렌지마켓</h3><p>창고형 할인매장 · 공동구매</p></a>
      <a class="card rv" href="/affiliates/live/"><div class="card-ic">🎥</div><h3 style="font-size:17px">HMK 라이브커머스</h3><p>방송 제작·송출 · 셀러 통합관리</p></a>
      <a class="card rv" href="/affiliates/ecommerce/"><div class="card-ic">💻</div><h3 style="font-size:17px">HMK E커머스</h3><p>오렌지 1,000원마켓 · 온라인 쇼핑몰</p></a>
    </div>
  </div>
</section>

<!-- 08 뉴스 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">NEWS</span><h2>그룹 소식</h2></div>
      <a class="link-more rv" href="/news/">전체 보기 __ARR__</a>
    </div>
    <div class="grid g3">
      <a class="post-card rv" href="/news/"><div class="post-meta"><span class="post-cat">그룹 뉴스</span><span class="post-date">2026.08.20</span></div>
        <h3>HMK 홀딩스그룹, 그룹 공식 홈페이지 개편</h3><p>사업 확장에 맞춰 그룹 소개 체계를 새로 정리했습니다.</p></a>
      <a class="post-card rv" href="/news/"><div class="post-meta"><span class="post-cat">프로젝트</span><span class="post-date">2026.08.12</span></div>
        <h3>일산 엠시티타워, 공유창고 오렌지 전환 조성 착수</h3><p>복합 상가 공실 구간을 무인 보관 시설로 전환합니다.</p></a>
      <a class="post-card rv" href="/news/"><div class="post-meta"><span class="post-cat">시장 인사이트</span><span class="post-date">2026.08.05</span></div>
        <h3>비어 있는 상가는 왜 계속 늘어나는가</h3><p>공실을 자산 기회로 읽기 위해 확인해야 할 다섯 가지.</p></a>
    </div>
  </div>
</section>

<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>검토할 자산이 있으신가요</h2><p>물건 개요만 보내주셔도 됩니다. 검토 가능 여부와 다음 절차를 회신드립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/">물건 제안하기</a><a class="btn btn-outline-w" href="/model/">사업모델 보기</a></div>
</div></div></section>
'''.replace("__ARR__", ARROW)

PAGES = {
    "/": {
        "title": "HMK 홀딩스그룹 — 부동산 밸류업 그룹",
        "desc": "AI 프롭테크로 저평가 부동산을 초저가 매입하고, 공간수익화 모델로 임대수익을 극대화하며, 자산 유동화로 순환시키는 부동산 밸류업 그룹.",
        "active": "", "no_hero": True, "body_class": "page home", "body": BODY,
        "extra_head": """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"HMK 홀딩스그룹","alternateName":"HMK Holdings Group","url":"https://www.hmkholdings.com","logo":"https://www.hmkholdings.com/assets/logo.png","address":{"@type":"PostalAddress","streetAddress":"봉은사로 129-1, 751빌딩 3층","addressLocality":"강남구","addressRegion":"서울특별시","addressCountry":"KR"},"contactPoint":{"@type":"ContactPoint","telephone":"+82-1555-5335","contactType":"customer service"}}
</script>""",
    },
}
