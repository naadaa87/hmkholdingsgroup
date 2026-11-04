# -*- coding: utf-8 -*-
"""메인 — 8블록 원페이지 서사"""

ARROW = '<svg viewBox="0 0 16 16" width="16" height="16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

BODY = r'''
<!-- 01 히어로 -->
<section class="hero hero-reference">
  <picture class="hero-art" aria-hidden="true">
    <source media="(min-width: 1900px)" srcset="/assets/platform/hero-panorama-v2.webp">
    <img class="hero-backdrop" src="/assets/platform/hero-desktop-v2.webp" alt="" width="1774" height="887" fetchpriority="high" decoding="async">
  </picture>
  <div class="hero-in">
    <div class="hero-copy">
      <span class="eyebrow">상업용 부동산 자산가치 밸류업 플랫폼</span>
      <h1>싸게 사고, 자산가치 극대화,<br><span class="accent">자산을 유동화</span>합니다.</h1>
      <p class="lead">500억 이상 대형 상업용 부동산을 AI 프롭테크와 20년 노하우로<br class="desktop-break"> 초저가에 매입하고, 창고형마켓·라이브커머스·공유창고 세 가지<br class="desktop-break"> 사업의 시너지로 임대 수익과 자산가치를 극대화합니다.</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="/model/">HMK밸류업모델 <svg viewBox="0 0 16 16" width="16" height="16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a class="btn btn-ghost" href="/affiliates/">그룹사 전체보기</a>
        <a class="btn btn-ghost" href="https://hmkpartner.com" target="_blank" rel="noopener">사업파트너 모집 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>
<div class="hero-pagination" aria-hidden="true"><i></i><i></i><i></i></div>
    </div>
    <a class="hero-asset" href="/model/assets/">
      <span class="hero-asset-thumb"><img src="/assets/storage/entrance.jpg" alt="공유창고 내부"><span aria-hidden="true">▶</span></span>
      <span><b>HMK 밸류업 자산</b><small>라이브쇼핑 · 창고마켓 · 공유창고의<br>복합 수익 모델</small></span><span class="asset-arrow" aria-hidden="true">→</span>
    </a>
  </div>
<div class="hero-stats-wrap">    <div class="facts hero-facts">
      <div class="fact"><svg class="fact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 2 8l10 5 10-5-10-5ZM2 12l10 5 10-5M2 16l10 5 10-5"/></svg><div class="fact-copy"><div class="num">23<small>만 건 이상</small></div><div class="lb">월간 물건 분석량</div></div></div>
      <div class="fact"><svg class="fact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 7c0 3-16 3-16 0s16-3 16 0ZM4 7v10c0 4 16 4 16 0V7M4 12c0 4 16 4 16 0"/></svg><div class="fact-copy"><div class="num">20<small>% 이하</small></div><div class="lb">감정가 대비 확보 수준</div></div></div>
      <div class="fact"><svg class="fact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21V13h4v8M10 21V8h4v13M17 21V3h4v18"/></svg><div class="fact-copy"><div class="num">450<small>% 이상</small></div><div class="lb">일반 상가 대비 수익 창출</div></div></div>
      <div class="fact"><svg class="fact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V3h13v18M2 21h20M17 10h4v11M8 7h1m3 0h1M8 11h1m3 0h1M8 15h1m3 0h1M10 21v-3"/></svg><div class="fact-copy"><div class="num">3<small>건</small></div><div class="lb">확보·전환 진행 자산</div></div></div>
    </div></div>
</section>
  <div class="hero-steps reference-process"><div class="process-heading"><span>OUR PROCESS</span><h2>HMK의<br>자산 밸류업 프로세스</h2><p>매입부터 운영, 유동화까지<br>부동산의 가치를 단계적으로 극대화합니다.</p></div><ol>
    <li class="process-step"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21v-7h4v7M10 21V9h4v12M16 21V3h4v18"/></svg><span class="n">STEP 01</span><b>AI 초저가 매입</b><span>감정가 대비 20% 이하</span></li>
    <li class="process-step"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10h18l-2-6H5l-2 6ZM4 10v11h16V10M8 21v-7h8v7M3 10c0 4 4 4 4 0 0 4 5 4 5 0 0 4 5 4 5 0 0 4 4 4 4 0"/></svg><span class="n">STEP 02</span><b>공간 수익화</b><span>평당 임대수익 극대화</span></li>
    <li class="process-step"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 2 8l10 5 10-5-10-5ZM2 12l10 5 10-5M2 16l10 5 10-5"/></svg><span class="n">STEP 03</span><b>자산 유동화</b><span>토큰증권 준비 중</span></li>
    <li class="process-step"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 7a9 9 0 0 0-15-2L2 8m0-5v5h5M4 17a9 9 0 0 0 15 2l3-3m0 5v-5h-5"/></svg><span class="n">STEP 04</span><b>재투자 순환</b><span>다음 자산 확보</span></li>
  </ol></div>

<!-- 03 보유 자산 -->
<section class="portfolio-showcase" id="portfolio" aria-labelledby="portfolio-title">
  <svg class="portfolio-skyline" viewBox="0 0 460 300" fill="none" stroke="currentColor" aria-hidden="true"><path d="M80 290V83L190 15l92 57v218M190 15v275M80 83l110 65 92-76M105 68v222m28-238v238m28-255v255m56-259v259m28-242v242M80 126l110 63 92-74M80 170l110 61 92-74M80 215l110 59 92-74M295 290V118l68-44 67 43v173M363 74v216m-45-188v188m22-202v202m46-201v201m22-187v187M295 162l68 43 67-43M295 207l68 43 67-43"/></svg>
  <div class="portfolio-wrap">
    <div class="portfolio-heading">
      <div class="portfolio-intro"><span class="eyebrow">PORTFOLIO</span>
        <h2 id="portfolio-title">좋은 입지 위에 서 있는<br>검증된 <span>보유 부동산</span></h2>
        <p>배후 수요가 검증된 상권에서만 확보합니다.<br>가격이 아니라 입지가 말해주는 가치를 보여드립니다.</p>
      </div>
      <dl class="portfolio-metrics"><div class="portfolio-metric"><span class="metric-icon"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V7l8-4v18M12 9h7v12M2 21h20M7 9v1m0 3v1m0 3v1m9-5v1m0 3v1"/></svg></span><div><dt>확보·전환 자산</dt><dd>3<small>개</small></dd></div></div><div class="portfolio-metric"><span class="metric-icon"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="7" r="3"/><path d="M2 21v-3a7 7 0 0 1 14 0v3M16 4a3 3 0 0 1 0 6M18 14a5 5 0 0 1 4 5v2"/></svg></span><div><dt>송산 배후 수요</dt><dd>8,700<small>세대+</small></dd></div></div><div class="portfolio-metric"><span class="metric-icon"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21v-7h4v7M10 21V8h4v13M17 21V3h4v18"/></svg></span><div><dt>공간수익화 모델</dt><dd>3<small> in 1</small></dd></div></div><div class="portfolio-metric"><span class="metric-icon"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 3 10 5-10 5L2 8l10-5ZM2 12l10 5 10-5M2 16l10 5 10-5"/></svg></span><div><dt>운영 노하우</dt><dd>20<small>년+</small></dd></div></div></dl></div><div class="portfolio-cards" aria-label="보유 부동산 목록"><article class="portfolio-card" data-asset="ilsan" aria-labelledby="asset-title-ilsan">
      <div class="portfolio-photo"><a href="/model/assets/#ilsan" tabindex="-1" aria-hidden="true"><img src="/assets/portfolio/ilsan.jpg" alt="" loading="lazy" width="900" height="500"></a>
        <span class="portfolio-tag"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg> 보유 물건 01</span>
        <button class="portfolio-save" type="button" data-save="ilsan" aria-label="일산 엠시티타워 관심 자산 저장" aria-pressed="false"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z"/></svg></button>
      </div>
      <div class="portfolio-body"><h3 id="asset-title-ilsan"><a href="/model/assets/#ilsan">일산 엠시티타워</a></h3>
        <div class="portfolio-meta"><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg>고양 일산동구</span><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V7l8-4v18M12 9h7v12M2 21h20M7 9v1m0 3v1m0 3v1m9-5v1m0 3v1"/></svg>일산호수공원 인접</span><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5M8 8h8v8H8Z"/></svg>179평</span></div><ul class="portfolio-points"><li>단지 950세대 + 오피스텔 646세대 자체 배후</li><li>반경 2km 인구 10만 명 생활권</li><li>일산테크노밸리 · GTX-A 수혜권</li></ul><a class="portfolio-detail" href="/model/assets/#ilsan">입지 자세히 보기 <svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16m-6-6 6 6-6 6"/></svg></a></div></article><article class="portfolio-card is-featured" data-asset="hwaseong" aria-labelledby="asset-title-hwaseong">
      <div class="portfolio-photo"><a href="/model/assets/#hwaseong" tabindex="-1" aria-hidden="true"><img src="/assets/portfolio/hwaseong.jpg" alt="" loading="lazy" width="900" height="500"></a>
        <span class="portfolio-tag"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg> 보유 물건 02</span>
        <button class="portfolio-save" type="button" data-save="hwaseong" aria-label="화성 송산시티 L-Tower 관심 자산 저장" aria-pressed="false"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z"/></svg></button>
      </div>
      <div class="portfolio-body"><h3 id="asset-title-hwaseong"><a href="/model/assets/#hwaseong">화성 송산시티 L-Tower</a></h3>
        <div class="portfolio-meta"><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg>화성 새솔동</span><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V7l8-4v18M12 9h7v12M2 21h20M7 9v1m0 3v1m0 3v1m9-5v1m0 3v1"/></svg>송산그린시티 중심상권</span><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5M8 8h8v8H8Z"/></svg>91.4평</span></div><ul class="portfolio-points"><li>아파트 5개 단지 8,700세대 배후</li><li>1인·신혼 가구 밀집 — 보관 수요 발생 구조</li><li>신세계 국제테마파크(예정) 배후권</li></ul><a class="portfolio-detail" href="/model/assets/#hwaseong">입지 자세히 보기 <svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16m-6-6 6 6-6 6"/></svg></a></div></article><article class="portfolio-card" data-asset="gangdong" aria-labelledby="asset-title-gangdong">
      <div class="portfolio-photo"><a href="/model/assets/#gangdong" tabindex="-1" aria-hidden="true"><img src="/assets/portfolio/gangdong.jpg" alt="" loading="lazy" width="900" height="500"></a>
        <span class="portfolio-tag"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg> 보유 물건 03</span>
        <button class="portfolio-save" type="button" data-save="gangdong" aria-label="강동 로데오팰리스 관심 자산 저장" aria-pressed="false"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8Z"/></svg></button>
      </div>
      <div class="portfolio-body"><h3 id="asset-title-gangdong"><a href="/model/assets/#gangdong">강동 로데오팰리스</a></h3>
        <div class="portfolio-meta"><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg>서울 강동구 천호동</span><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 21V7l8-4v18M12 9h7v12M2 21h20M7 9v1m0 3v1m0 3v1m9-5v1m0 3v1"/></svg>지하 1층</span><span><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5M8 8h8v8H8Z"/></svg>90평</span></div><ul class="portfolio-points"><li>천호역 5·8호선 더블 역세 생활권</li><li>로데오거리 · 현대백화점 천호점 인접</li><li>천호 재정비촉진지구 수혜권</li></ul><a class="portfolio-detail" href="/model/assets/#gangdong">입지 자세히 보기 <svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16m-6-6 6 6-6 6"/></svg></a></div></article></div>
    <div class="portfolio-controls" role="group" aria-label="강조 자산 선택">
      <button type="button" class="portfolio-prev" aria-label="이전 자산 강조"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m14 5-7 7 7 7"/></svg></button>
      <div class="portfolio-dots"><button type="button" data-portfolio-index="0" aria-label="일산 엠시티타워 강조" aria-pressed="false"></button><button type="button" data-portfolio-index="1" aria-label="화성 송산시티 L-Tower 강조" aria-pressed="true"></button><button type="button" data-portfolio-index="2" aria-label="강동 로데오팰리스 강조" aria-pressed="false"></button></div><button type="button" class="portfolio-next" aria-label="다음 자산 강조"><svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m10 5 7 7-7 7"/></svg></button></div></div></section>

<!-- 04 순환플랫폼 -->
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
      <p class="lead">사고 · 보고 · 맡기고. 초저가로 매입한 부동산에 세 가지 사업을 넣어 매출과 임대수익을 극대화합니다.</p>
    </div>
    <div class="trio rv">
      <a href="https://orange1000.com" target="_blank" rel="noopener"><span class="verb">사고</span><div><b>창고형마켓</b><span class="brand">오렌지 창고마켓</span></div></a>
      <a href="https://orangeliveon.com" target="_blank" rel="noopener"><span class="verb">보고</span><div><b>라이브커머스</b><span class="brand">오렌지 라이브커머스</span></div></a>
      <a href="https://storage-orange.co.kr" target="_blank" rel="noopener"><span class="verb">맡기고</span><div><b>공유창고</b><span class="brand">오렌지 공유창고</span></div></a>
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
      <figcaption>단일 임차 구조에서 3 in 1 복합 수익 구조로 — 연간 수익·임대수익률·자산가치가 함께 상승합니다</figcaption>
    </figure>
  </div>
</section>

<!-- 06+ 시너지: 통합물류 + 멤버십 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">SYNERGY</span><h2>세 사업을 하나로 묶는<br>통합물류와 오렌지 멤버십</h2></div>
      <p class="lead">상품은 자체 통합물류·유통시스템으로, 고객은 HMK 오렌지 멤버십으로 연결됩니다. 시너지가 매출을 활성화하고 자산가치를 밀어올립니다.</p>
    </div>
    <div class="split">
      <div class="rv">
        <div class="floors">
          <div class="floor"><div class="lv" style="width:64px">물류</div><div><b>자체 통합물류·유통시스템</b><span>창고마켓이 매입한 재고 하나가 매장·라이브·온라인 세 채널에서 팔리고, 같은 건물에서 당일 출고됩니다. 별도 물류센터 없이 재고 회전은 빠르게, 운영비는 나눠서.</span></div></div>
          <div class="floor"><div class="lv" style="width:64px">멤버십</div><div><b>HMK 오렌지 멤버십</b><span>세 사업장의 고객을 하나의 회원으로 묶습니다. 창고 이용자에게 마켓 쿠폰, 마켓 고객에게 방송 특가, 시청자에게 창고 혜택 — 한 명이 세 번 방문합니다.</span></div></div>
          <div class="floor core"><div class="lv" style="width:64px">결과</div><div><b>매출 활성화 → 임대수익 상승 → 자산가치 밸류업</b><span>교차 방문과 재방문이 늘면 건물의 순영업이익이 커지고, 그 수익이 자산의 평가가치를 끌어올립니다.</span></div></div>
        </div>
        <div class="extlinks" style="margin-top:22px"><a class="btn btn-ghost" href="/model/synergy/">시너지 구조 자세히 <svg viewBox="0 0 16 16" width="16" height="16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></a><a class="btn btn-ghost" href="https://orangemembership.com" target="_blank" rel="noopener">오렌지 멤버십 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div>
      </div>
      <div class="gallery g2 tall rv">
        <figure><img src="/assets/live/logistics.jpg" alt="주문부터 배송까지 오렌지 통합 물류 프로세스" loading="lazy"><figcaption>통합물류 — 주문·피킹·포장·출고·배송</figcaption></figure>
        <figure><img src="/assets/membership/card-hero.jpg" alt="HMK 오렌지 멤버십 카드" loading="lazy"><figcaption>오렌지 멤버십 — 하나의 회원, 세 개의 혜택</figcaption></figure>
        <figure><img src="/assets/membership/use-market.jpg" alt="창고마켓에서 멤버십 카드 결제" loading="lazy"><figcaption>창고마켓에서 적립</figcaption></figure>
        <figure><img src="/assets/membership/use-storage.jpg" alt="공유창고에서 멤버십 카드 사용" loading="lazy"><figcaption>공유창고에서 할인</figcaption></figure>
      </div>
    </div>
  </div>
</section>

<!-- 07 계열사 -->
<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv">
      <div><span class="eyebrow">AFFILIATES</span><h2>상업용 부동산 매입부터<br>자산가치 밸류업까지</h2></div>
      <a class="link-more" href="/affiliates/">HMK그룹사 전체보기 __ARR__</a>
    </div>
    <div class="grid g4">
      <a class="card rv" href="/affiliates/loan/"><div class="card-ic affiliate-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M3 21h18M10 21v-4h4v4M9 7h1m4 0h1M9 11h1m4 0h1"/></svg></div><h3 style="font-size:17px">HMK 대부</h3><p>AI 프롭테크 소싱 · 채권매입 · 경공매</p></a>
      <a class="card rv" href="/affiliates/storage/"><div class="card-ic affiliate-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m3 7 9-4 9 4v10l-9 4-9-4Zm0 0 9 4 9-4M12 11v10M7.5 5l9 4v4"/></svg></div><h3 style="font-size:17px">HMK 스토리지</h3><p>공유창고 오렌지 조성·운영 · IoT 관리</p></a>
      <a class="card rv" href="/affiliates/market/"><div class="card-ic affiliate-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h2l2.5 12h11L21 7H6M8 11h11"/><circle cx="9" cy="20" r="1"/><circle cx="18" cy="20" r="1"/></svg></div><h3 style="font-size:17px">오렌지 창고마켓</h3><p>창고형 할인매장 · 온라인몰 · 공동구매</p></a>
      <a class="card rv" href="/affiliates/live/"><div class="card-ic affiliate-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="6" width="12" height="12" rx="3"/><path d="m15 10 6-3v10l-6-3"/><path d="m8 10 3 2-3 2Z" fill="currentColor" stroke="none"/></svg></div><h3 style="font-size:17px">오렌지 라이브커머스</h3><p>방송 제작·송출 · 셀러 통합관리</p></a>
    </div>

    <div class="sec-head rv" style="margin-top:clamp(56px,6vw,80px)">
      <div><span class="eyebrow">ORANGE WORLD</span><h2>가치를 올리는<br>오렌지월드</h2></div>
      <div style="text-align:right"><p class="lead" style="max-width:24em">HMK와 한번에 "가치"하세요.<br>사고·보고·맡기고, 그리고 잇고. 각 서비스는 아래 사이트에서 바로 이용하실 수 있습니다.</p>
      <a class="link-more" style="margin-top:10px" href="/sites/">관련 사이트 전체 보기 __ARR__</a></div>
    </div>
    <div class="grid g4">
      <a class="card pf-card rv" href="https://orange1000.com" target="_blank" rel="noopener"><div class="ph"><img src="/assets/market/exterior.jpg" alt="오렌지 창고마켓 매장 외관" loading="lazy"></div><div class="bd"><h3 style="font-size:17px">오렌지 창고마켓</h3><p style="font-size:13.5px;color:var(--ink-soft);margin-top:6px">사고 — 창고형 할인매장 · 온라인몰</p><span class="link-more">사이트 방문 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span></div></a>
      <a class="card pf-card rv" href="https://orangeliveon.com" target="_blank" rel="noopener"><div class="ph"><img src="/assets/live/seller.jpg" alt="오렌지 라이브쇼핑 셀러 방송" loading="lazy"></div><div class="bd"><h3 style="font-size:17px">오렌지 라이브커머스</h3><p style="font-size:13.5px;color:var(--ink-soft);margin-top:6px">보고 — 라이브 방송 · 셀러 입점</p><span class="link-more">사이트 방문 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span></div></a>
      <a class="card pf-card rv" href="https://storage-orange.co.kr" target="_blank" rel="noopener"><div class="ph"><img src="/assets/storage/entrance.jpg" alt="오렌지 공유창고 매장 입구" loading="lazy"></div><div class="bd"><h3 style="font-size:17px">오렌지 공유창고</h3><p style="font-size:13.5px;color:var(--ink-soft);margin-top:6px">맡기고 — 무인 보관 · 24시간</p><span class="link-more">사이트 방문 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span></div></a>
      <a class="card pf-card rv" href="https://orangemembership.com" target="_blank" rel="noopener"><div class="ph"><img src="/assets/membership/app.jpg" alt="HMK 오렌지 멤버십 앱과 카드" loading="lazy"></div><div class="bd"><h3 style="font-size:17px">오렌지 멤버십</h3><p style="font-size:13.5px;color:var(--ink-soft);margin-top:6px">잇고 — 통합 포인트 · 교차 혜택</p><span class="link-more">사이트 방문 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span></div></a>
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
        <h3>HMK홀딩스그룹, 그룹 공식 홈페이지 개편</h3><p>사업 확장에 맞춰 그룹 소개 체계를 새로 정리했습니다.</p></a>
      <a class="post-card rv" href="/news/"><div class="post-meta"><span class="post-cat">프로젝트</span><span class="post-date">2026.08.12</span></div>
        <h3>일산 엠시티타워, 공유창고 오렌지 전환 조성 착수</h3><p>복합 상가 공실 구간을 무인 보관 시설로 전환합니다.</p></a>
      <a class="post-card rv" href="/news/"><div class="post-meta"><span class="post-cat">시장 인사이트</span><span class="post-date">2026.08.05</span></div>
        <h3>비어 있는 상가는 왜 계속 늘어나는가</h3><p>공실을 자산 기회로 읽기 위해 확인해야 할 다섯 가지.</p></a>
    </div>
  </div>
</section>

<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>검토할 자산이 있으신가요</h2><p>물건 개요만 보내주셔도 됩니다. 검토 가능 여부와 다음 절차를 회신드립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/">물건 제안하기</a><a class="btn btn-outline-w" href="/model/">HMK밸류업모델</a></div>
</div></div></section>
'''.replace("__ARR__", ARROW)

PAGES = {
    "/": {
        "title": "HMK홀딩스그룹 — 부동산 밸류업 그룹",
        "desc": "AI 프롭테크로 저평가 부동산을 초저가 매입하고, 공간수익화 모델로 임대수익을 극대화하며, 자산 유동화로 순환시키는 부동산 밸류업 그룹.",
        "active": "", "no_hero": True, "body_class": "page home", "body": BODY,
        "preload": "/assets/platform/cutaway-night.jpg",
        "extra_head": """<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":"Organization","@id":"https://www.hmkholdings.com/#org","name":"HMK홀딩스그룹","alternateName":["HMK Holdings Group","HMK홀딩스","에이치엠케이홀딩스"],"url":"https://www.hmkholdings.com","logo":"https://www.hmkholdings.com/assets/logo.png","image":"https://www.hmkholdings.com/assets/og.jpg","description":"상업용 부동산을 초저가 매입해 창고형마켓·라이브커머스·공유창고 3가지 사업으로 임대수익과 자산가치를 높이는 부동산 밸류업 플랫폼","slogan":"HMK와 한번에 가치하세요","founder":{"@type":"Person","name":"김재동","jobTitle":"회장","url":"https://kimjaedong.com"},"address":{"@type":"PostalAddress","streetAddress":"봉은사로 129-1, 751빌딩 3층","addressLocality":"강남구","addressRegion":"서울특별시","postalCode":"06120","addressCountry":"KR"},"telephone":"+82-1555-5335","email":"hmkholdings@hmkholdings.com","areaServed":"KR","contactPoint":{"@type":"ContactPoint","telephone":"+82-1555-5335","contactType":"customer service","availableLanguage":"Korean"},"sameAs":["https://hmknplauction.pages.dev","https://hmkstorage.com","https://kimjaedong.com","https://orange1000.com","https://orangeliveon.com","https://storage-orange.co.kr","https://orangemembership.com","https://hmkpartner.com","https://hmkinvestment.pages.dev"],"brand":[{"@type":"Brand","name":"오렌지 공유창고"},{"@type":"Brand","name":"오렌지 창고마켓"},{"@type":"Brand","name":"오렌지 라이브커머스"},{"@type":"Brand","name":"오렌지 멤버십"}],"knowsAbout":["상업용 부동산 매입","부동산 밸류업","무인 공유창고","창고형 할인매장","라이브커머스","AI 프롭테크","부동산 자산 유동화"]},
{"@type":"WebSite","@id":"https://www.hmkholdings.com/#website","url":"https://www.hmkholdings.com","name":"HMK홀딩스그룹","publisher":{"@id":"https://www.hmkholdings.com/#org"},"inLanguage":"ko-KR"}
]}
</script>""",
    },
}
