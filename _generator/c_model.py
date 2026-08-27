# -*- coding: utf-8 -*-
"""사업모델 — 순환모델 / AI 초저가 매입 / 공간수익화 / 자산 유동화 / 보유 자산"""

ARROW = '<svg viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CR = [("사업모델", "/model/")]

STEPS = ["AI 초저가 매입", "공간 수익화", "자산 유동화", "재투자 순환"]


def minirail(active):
    li = []
    for i, s in enumerate(STEPS, 1):
        on = ' style="border-color:var(--orange);background:var(--orange-soft);color:var(--orange-deep)"' if i in active else ""
        li.append(f'<li class="chip"{on}>{i:02d} {s}</li>')
    return '<ul style="display:flex;gap:8px;flex-wrap:wrap;margin-top:22px">' + "".join(li) + "</ul>"


def spec(rows):
    out = ['<div class="spec rv">']
    for i, (t, body) in enumerate(rows, 1):
        out.append(f'<div class="spec-row"><div class="spec-key"><span class="no">{i:02d}</span>'
                   f'<span class="t">{t}</span></div><div class="spec-val">{body}</div></div>')
    return "".join(out) + "</div>"


CTA = r'''
<section class="cta-band"><div class="wrap"><div class="inner">
  <div class="rv"><h2>검토할 자산이 있으신가요</h2><p>물건 개요만 보내주셔도 됩니다. 검토 가능 여부와 다음 절차를 회신드립니다.</p></div>
  <div class="acts rv"><a class="btn btn-white" href="/contact/">물건 제안하기</a><a class="btn btn-outline-w" href="/model/">사업모델 전체 보기</a></div>
</div></div></section>
'''

# ───────────────── 허브 ─────────────────
HUB = r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="prose rv" style="max-width:46em">
      <h2 style="margin-top:0">왜 "순환"이라고 부르는가</h2>
      <p>부동산으로 수익을 내는 방법은 많습니다. 싸게 사서 파는 회사도, 임대만 하는 회사도, 분석만 파는 회사도 있습니다. HMK가 다른 점은 <strong>매입부터 유동화까지 네 단계를 한 회사 체계 안에서 직접 수행</strong>하고, 그 결과를 다시 처음으로 되돌린다는 것입니다.</p>
      <p>단계가 이어져 있으면 각 단계의 판단이 좋아집니다. 운영을 아는 팀이 매입을 검토하니 "살 수 있는 물건"이 아니라 "살려낼 수 있는 물건"을 고르고, 매입을 아는 팀이 운영 데이터를 보니 다음 소싱의 기준이 정교해집니다.</p>
    </div>
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">4 STEPS</span><h2>네 단계, 각각의 일</h2></div>
    <p class="lead">아래 순서는 실제 자산 하나가 지나가는 순서 그대로입니다.</p></div>
    <div class="cyc">
      <a class="cyc-c rv" href="/model/ai-sourcing/"><div class="no">01</div><h3>AI 프롭테크<br>초저가 매입</h3><p>월 23만 건 이상 분석 → 저평가 물건 선별 → 권리 해결 → 감정가 대비 20% 이하 확보</p><div class="arw">→</div></a>
      <a class="cyc-c rv" href="/model/space/"><div class="no">02</div><h3>HMK<br>공간수익화 모델</h3><p>공유창고 · 창고형 할인매장 · 라이브커머스를 한 건물에 결합해 임대수익 극대화</p><div class="arw">→</div></a>
      <a class="cyc-c rv" href="/model/liquidity/"><div class="no">03</div><h3>토큰증권<br>자산 유동화</h3><p>운영 수익 기반 자산가치 재평가 → 2027년 2월 4일 시행 제도에 맞춘 발행·상장 준비</p><div class="arw">→</div></a>
      <div class="cyc-c last rv"><div class="no">04</div><h3>재투자<br>선순환 확장</h3><p>회수 자금을 다음 자산 매입에 재투입. 반복할수록 속도와 정확도가 올라갑니다.</p></div>
    </div>
    <div class="loop rv">↻ &nbsp;01 → 02 → 03 → 04 → 다시 01. 이 순환이 HMK 밸류업 모델입니다.</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">ROADMAP</span><h2>사업 프로세스 &<br>Value-Up 로드맵</h2></div>
    <p class="lead">한 자산에서 여러 현금흐름을 만들고, 자산가치를 극대화하여 회수까지 이어갑니다.</p></div>
    <figure class="figure rv">
      <img src="/assets/model/roadmap.jpg" alt="저가 부동산 매입, 리모델링·콘텐츠 결합, 운영 정상화, NOI·자산가치 상승, 금융·포트폴리오 회수의 5단계 프로세스" width="1448" height="1086">
      <figcaption>① 저가 부동산 매입 → ② 리모델링·콘텐츠 결합 → ③ 운영 정상화 → ④ NOI·자산가치 상승 → ⑤ 금융·포트폴리오 회수</figcaption>
    </figure>
  </div>
</section>

<section class="sec sec-cool">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">CYCLE</span><h2>끝이 다시 시작이 됩니다</h2></div></div>
    <div class="grid g3">
      <div class="card rv"><h3>유동화 → 재원</h3><p>안정된 운영 수익으로 자산가치가 재평가되면, 상승분은 회수 또는 재투자의 재원이 됩니다.</p></div>
      <div class="card rv"><h3>운영 데이터 → 소싱 기준</h3><p>어떤 입지·평형·유닛 구성이 잘 되는지 운영에서 확인된 데이터가 다음 매입의 기준이 됩니다.</p></div>
      <div class="card rv"><h3>반복 → 확장</h3><p>같은 체계를 반복할수록 속도와 정확도가 올라갑니다. 다점포 확장은 이 반복 위에 서 있습니다.</p></div>
    </div>
    <div class="note-box rv" style="margin-top:24px"><b>안내</b> — 이 페이지의 단계 설명은 사업 구조에 대한 안내이며, 특정 자산의 수익이나 성과를 보장하는 내용이 아닙니다. 개별 자산의 결과는 물건과 시장 상황에 따라 달라집니다.</div>
  </div>
</section>
''' + CTA

# ───────────────── AI 소싱 ─────────────────
AI_SPEC = spec([
    ("이런 문제를 다룹니다",
     "<p>사람이 전국의 경·공매 공고와 매물을 모두 볼 수는 없습니다. 그래서 좋은 물건은 대개 <strong>못 봐서</strong> 놓치고, 나쁜 물건은 <strong>제대로 못 봐서</strong> 잡습니다. AI 소싱 시스템은 이 두 문제를 동시에 줄이기 위해 만들어졌습니다.</p>"),
    ("무엇을 분석하는가",
     "<ul><li>전국 경매·공매 공고와 진행 이력</li><li>부실채권(NPL) 및 급매 물건 정보</li><li>등기·건축물대장 등 권리 관련 공적 정보</li><li>상권·배후 세대·임대 시세 등 수요 데이터</li></ul>"
     "<p>이 데이터를 상시 수집·정제해 <strong>월 23만 건 이상</strong>을 분석 대상으로 다룹니다.</p>"),
    ("어떻게 걸러내는가",
     "<p>유찰 횟수, 권리 하자 유형, 공실 기간처럼 남들이 피하는 신호를 오히려 필터로 씁니다. 시스템이 후보군을 스코어링하면 담당 조직이 1차 검토 리스트를 만들고, 현장 검증으로 결론을 냅니다. <strong>시스템의 목적은 사기 위해서가 아니라 거르기 위해서</strong>입니다.</p>"),
    ("권리 문제를 푸는 힘",
     "<p>유치권, 법정지상권, 선순위 임차권, 점유 분쟁 — 가격이 눌려 있는 이유는 대개 문제를 풀어줄 사람이 없기 때문입니다. 20여 년간 축적한 권리분석·협상 경험과 법무 파트너 네트워크로 이 구간을 해결합니다.</p>"),
    ("확보 기준",
     "<p>복잡한 권리관계를 해결하여 최적의 입지를 <strong>감정가 대비 20% 이하</strong>로 확보하는 것이 매입 기준입니다. 매입가는 전환 후 만들 수 있는 수익에서 역산하므로, 단지 싸다는 이유만으로 사지 않습니다.</p>"),
    ("사람의 역할",
     "<p>시스템은 판단의 재료를 만들고, 결정은 사람이 합니다. 현장 검증, 리스크 등급 확정, 매입 심의는 모두 담당 조직과 전문가가 수행합니다. 어떤 시스템도 매입이나 계약을 스스로 결정하지 않습니다.</p>"),
])

AI_BODY = r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="facts rv">
      <div class="fact"><div class="num">23<small>만 건 이상</small></div><div class="lb">월간 분석 물건 수</div><div class="sb">경·공매 · 부실채권 · 급매</div></div>
      <div class="fact"><div class="num">20<small>% 이하</small></div><div class="lb">감정가 대비 확보 수준</div><div class="sb">권리 해결을 전제로 한 매입</div></div>
      <div class="fact"><div class="num">200<small>여 명</small></div><div class="lb">전문 인력 네트워크</div><div class="sb">직원 · 프리랜서 · 파트너법인</div></div>
      <div class="fact"><div class="num">최초</div><div class="lb">AI부동산 초저가 매입시스템</div><div class="sb">국내 최초 구축</div></div>
    </div>
  </div>
</section>

<section class="sec sec-warm" style="padding-top:clamp(56px,6vw,80px)">
  <div class="wrap">__SPEC__</div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">FIELD CHECK</span><h2>현장에서 반드시 보는 것</h2></div>
    <p class="lead">데이터가 후보를 고르면, 사람이 현장에서 결론을 냅니다.</p></div>
    <div class="grid g4">
      <div class="card rv"><h3 style="font-size:17px">입지·수요</h3><p>배후 세대, 접근 동선, 주차. 보관 수요라면 반경 내 주거 밀도와 차량 접근성을 봅니다.</p></div>
      <div class="card rv"><h3 style="font-size:17px">권리·서류</h3><p>등기·건축물대장과 현장의 불일치, 무단 증축, 점유 현황을 눈으로 확인합니다.</p></div>
      <div class="card rv"><h3 style="font-size:17px">시설·구조</h3><p>층고, 전기 용량, 누수 흔적, 공조. 전환 공사비를 좌우하는 항목들입니다.</p></div>
      <div class="card rv"><h3 style="font-size:17px">시장·경쟁</h3><p>주변 임대료 실거래, 경쟁 시설 현황, 향후 공급 계획까지 반영합니다.</p></div>
    </div>
    <div class="note-box rv" style="margin-top:24px"><b>정직한 안내</b> — 권리 하자가 있는 물건은 기대수익만큼 리스크도 큽니다. HMK는 해결 가능성이 검증된 물건만 다루며, 검토 결과 풀 수 없다고 판단되면 그렇게 말씀드립니다.</div>
  </div>
</section>
'''.replace("__SPEC__", AI_SPEC) + CTA

# ───────────────── 공간수익화 ─────────────────
SPACE_BODY = r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="split">
      <div class="prose rv">
        <h2 style="margin-top:0">임대만 놓으면<br>수익은 하나뿐입니다</h2>
        <p>상가 한 층에 임차인 한 명, 임대료 하나. 이것이 일반적인 상가의 수익 구조입니다. 공실이 나면 그 층의 수익은 0이 됩니다.</p>
        <p>HMK 공간수익화 모델은 같은 건물에 <strong>보관 · 판매 · 방송</strong>이라는 세 개의 수익 콘텐츠를 겹쳐 넣습니다. 세 콘텐츠는 하나의 물류 코어를 공유하므로 운영비는 나누고 매출은 서로를 끌어올립니다.</p>
        <p>공간수익화는 밸류업 모델의 엔진입니다. 여기서 만들어지는 안정적인 운영 수익이 있어야 다음 단계인 자산가치 재평가와 유동화가 가능해집니다.</p>
      </div>
      <figure class="figure rv">
        <img src="/assets/model/building.jpg" alt="B1 공유창고, 1F 창고형 할인매장, 2F 라이브커머스로 구성된 HMK Value-Up Asset" width="1600" height="1032">
        <figcaption>HMK Value-Up Asset — 한 자산에서 세 가지 수익이 발생하는 복합 구조</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">THREE CONTENTS</span><h2>층마다 다른 수익,<br>하나로 이어지는 동선</h2></div>
    <p class="lead">각 층은 독립적으로 수익을 내면서, 상품과 물류를 통해 서로 연결됩니다.</p></div>

    <div class="split rv" style="margin-bottom:34px">
      <figure class="figure"><img src="/assets/model/floor-b1.jpg" alt="B1 공유창고 내부 — 오렌지 도어 유닛과 입출고 동선" loading="lazy" width="1448" height="1086"></figure>
      <div>
        <span class="badge">B1</span>
        <h3 style="margin:14px 0 10px;font-size:24px">무인 공유창고 오렌지</h3>
        <p class="lead">개인과 소상공인의 짐을 보관하는 무인 시설입니다. 비대면 계약·결제, 스마트 출입, 24시간 CCTV 관제로 상주 인력 없이 운영합니다.</p>
        <ul class="pts" style="margin-top:16px;display:flex;flex-direction:column;gap:8px">
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>개인 · 소상공인 보관 수요를 안정적 임대수익으로</li>
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>지하층 저비용 공간을 수익 공간으로 전환</li>
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>입·출고 지원과 공용 장비로 이용 편의 제공</li>
        </ul>
      </div>
    </div>

    <div class="split rev rv" style="margin-bottom:34px">
      <div>
        <span class="badge">1F</span>
        <h3 style="margin:14px 0 10px;font-size:24px">창고형 할인매장 · 공동구매</h3>
        <p class="lead">그룹이 직접 매입한 상품을 창고형으로 진열해 판매합니다. 오프라인 집객이 상권을 회복시키고, 온라인 판매의 기반이 됩니다.</p>
        <ul style="margin-top:16px;display:flex;flex-direction:column;gap:8px">
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>식품 · 생활용품 · 가전리빙 · 대량벌크 카테고리 운영</li>
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>공동구매로 매입 단가를 낮춰 가격 경쟁력 확보</li>
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>집객이 만드는 유동 인구가 상권 가치를 끌어올림</li>
        </ul>
      </div>
      <figure class="figure"><img src="/assets/model/floor-1f.jpg" alt="1F 창고형 할인매장 내부 — 카테고리 진열과 계산대" loading="lazy" width="1448" height="1086"></figure>
    </div>

    <div class="split rv">
      <figure class="figure"><img src="/assets/model/floor-2f.jpg" alt="2F 라이브커머스 스튜디오 — 방송 촬영과 상품 포장 구역" loading="lazy" width="1448" height="1086"></figure>
      <div>
        <span class="badge">2F</span>
        <h3 style="margin:14px 0 10px;font-size:24px">라이브커머스 스튜디오</h3>
        <p class="lead">촬영·방송·판매가 한 공간에서 이루어집니다. 아래층 상품을 그대로 방송하고, 주문은 아래층 물류에서 바로 출고됩니다.</p>
        <ul style="margin-top:16px;display:flex;flex-direction:column;gap:8px">
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>유튜브 · 네이버 등 외부 채널로 전국 판매 확장</li>
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>입점 셀러에게 스튜디오와 물류를 함께 제공</li>
          <li style="position:relative;padding-left:15px;font-size:14.5px"><span style="position:absolute;left:0;top:10px;width:7px;height:2px;background:var(--orange);display:block"></span>오프라인 인기 상품을 온라인 판매로 즉시 연결</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">LOGISTICS CORE</span><h2>세 개를 하나로 묶는<br>통합 물류·운영 코어</h2></div>
    <p class="lead">재고 관리 · 포장 · 검수 · 배송 · 출고가 하나의 시스템으로 연결됩니다. 이 코어가 있어야 세 콘텐츠가 겹쳐질 수 있습니다.</p></div>
    <figure class="figure rv">
      <img src="/assets/model/logistics-core.jpg" alt="재고 관리, 포장·검수, 배송·출고로 이어지는 통합 물류 운영 시스템" width="1448" height="1086">
      <figcaption>① 재고 관리 → ② 포장·검수 → ③ 배송·출고 — 세 가지 비즈니스가 하나의 운영 코어로 연결됩니다</figcaption>
    </figure>
  </div>
</section>

<section class="sec sec-cool">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">VALUE-UP EFFECT</span><h2>같은 건물,<br>달라지는 수익 구조</h2></div>
    <p class="lead">단일 임차 구조에서 복합 수익 구조로 바꾸면 현금흐름과 자산가치가 함께 움직입니다.</p></div>
    <figure class="figure rv">
      <img src="/assets/model/before-after.jpg" alt="저활용 자산과 HMK Value-Up 자산의 연간 수익·임대수익률·자산가치 비교" width="1448" height="1086">
      <figcaption>수익 구조 개선에 따른 밸류업 예시입니다. 자산 조건과 시장 상황에 따라 결과는 달라질 수 있습니다.</figcaption>
    </figure>
    <div class="grid g3 rv" style="margin-top:26px">
      <a class="card" href="https://storage-orange.co.kr" target="_blank" rel="noopener"><div class="card-ic">🧡</div><h3 style="font-size:17px">오렌지 공유창고</h3><p>B1 무인 보관 서비스 — 지점·요금·비대면 계약 안내</p><span class="link-more" style="margin-top:12px">사이트 방문 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
      <a class="card" href="https://hmkorangemarket.pages.dev" target="_blank" rel="noopener"><div class="card-ic">🛒</div><h3 style="font-size:17px">오렌지 창고마켓</h3><p>1F 창고형 할인매장 — 취급 상품·매장·입점 안내</p><span class="link-more" style="margin-top:12px">사이트 방문 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
      <a class="card" href="https://orangelivehub.pages.dev" target="_blank" rel="noopener"><div class="card-ic">🎥</div><h3 style="font-size:17px">오렌지 라이브쇼핑</h3><p>2F 라이브커머스 — 방송 일정·상품·셀러 입점</p><span class="link-more" style="margin-top:12px">사이트 방문 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>
    </div>
    <div class="note-box rv" style="margin-top:22px"><b>안내</b> — 공간수익화 모델을 적용한 자산은 <strong>일반 상가 대비 450% 이상의 수익 창출</strong>을 목표로 설계됩니다. 위 도표의 수치는 모델 적용 예시이며, 실제 결과는 자산의 입지·면적·운영 상황에 따라 달라집니다. 수익을 보장하지 않습니다.</div>
  </div>
</section>
''' + CTA

# ───────────────── 자산 유동화 ─────────────────
LIQ_SPEC = spec([
    ("왜 유동화가 필요한가",
     "<p>부동산은 좋은 자산이지만 느립니다. 가치가 올라도 팔기 전까지는 현금이 되지 않고, 자금이 묶이면 다음 자산을 살 수 없습니다. <strong>유동화는 순환의 속도를 결정하는 단계</strong>입니다.</p>"),
    ("가치의 근거는 운영 수익",
     "<p>싸게 샀다는 사실만으로는 자산가치가 오르지 않습니다. 수익형 부동산의 가치는 통상 <strong>순영업이익(NOI)</strong>과 <strong>환원율(Cap Rate)</strong>을 기준으로 평가됩니다. 공간수익화로 만들어진 계약 기반 수익이 재평가의 재료가 됩니다.</p>"),
    ("어떻게 진행하는가",
     "<p>① 운영 안정화 후 NOI를 정리하고 ② 시장 환원율·거래 사례를 조사한 뒤 ③ 외부 감정평가로 검증받습니다. 내부 계산만으로 가치를 주장하지 않습니다.</p>"),
    ("토큰증권(STO) 준비 현황",
     "<p>개정 전자증권법·자본시장법에 따라 <strong>2027년 2월 4일</strong> 관련 제도가 시행됩니다. HMK는 그 시행일에 맞춰 <strong>토큰증권 발행 및 상장을 준비 중</strong>이며, 현재는 구조 설계·법률 검토·요건 정비 단계에 있습니다.</p>"
     "<p>제도 시행 전에는 발행이 불가능하므로, 현재 어떠한 청약·모집도 진행하지 않습니다.</p>"),
    ("보수적으로 봅니다",
     "<p>환원율은 보수적 구간으로 잡고, 일시적 매출 상승분은 평가 근거에서 제외합니다. 평가기관이 실제로 인정할 수 있는 수준을 기준으로 삼습니다.</p>"),
    ("유동화 이후",
     "<ul><li><b>재투자</b> — 회수 자금을 다음 자산 매입에 투입해 순환을 이어갑니다</li><li><b>보유·운영</b> — 안정 수익 자산으로 계속 운영합니다</li><li><b>재무 활용</b> — 늘어난 담보 여력을 확장 재원으로 씁니다</li></ul>"),
])

LIQ_BODY = r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="note-box rv" style="border-width:2px;padding:24px 26px">
      <b style="font-size:16px;display:block;margin-bottom:8px">먼저 분명히 말씀드립니다</b>
      이 페이지는 HMK 홀딩스그룹의 <strong>사업 구조를 소개하기 위한 정보</strong>이며, 금융투자상품에 대한 <strong>투자 권유나 청약의 권유가 아닙니다.</strong> 토큰증권은 개정 전자증권법·자본시장법 시행일인 <strong>2027년 2월 4일</strong> 이후에 발행이 가능하며, 그 이전에는 어떠한 발행·모집·청약도 진행하지 않습니다. 향후 발행이 이루어지는 경우에도 관련 법령이 정한 절차와 공시를 통해서만 진행됩니다.
    </div>
    <div class="grid g3" style="margin-top:34px">
      <div class="card rv"><span class="eyebrow" style="margin-bottom:10px">INPUT</span><h3>안정된 운영 수익</h3><p>공간수익화 모델로 만들어지는 지속적·검증 가능한 현금흐름. 재평가 논리의 출발점입니다.</p></div>
      <div class="card rv"><span class="eyebrow" style="margin-bottom:10px">LOGIC</span><h3>수익환원 평가</h3><p>NOI를 시장 환원율로 환산해 자산가치를 설명합니다. 외부 감정평가가 이 논리를 검증합니다.</p></div>
      <div class="card rv"><span class="eyebrow" style="margin-bottom:10px">OUTPUT</span><h3>유동화 · 재투자</h3><p>회수된 자금은 다음 자산 매입의 재원이 됩니다. 순환의 속도를 결정하는 단계입니다.</p></div>
    </div>
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">__SPEC__</div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">TIMELINE</span><h2>제도 시행에 맞춘 준비 일정</h2></div></div>
    <div class="tbl-wrap rv">
      <table class="tbl">
        <thead><tr><th style="width:190px">구분</th><th>내용</th><th style="width:170px">상태</th></tr></thead>
        <tr><td><b>제도 시행일</b></td><td>개정 전자증권법·자본시장법에 따른 토큰증권 제도 시행</td><td><span class="chip chip-goal">2027.02.04</span></td></tr>
        <tr><td><b>구조 설계</b></td><td>자산 보유·운영 구조 정비 및 발행 구조 설계</td><td><span class="chip">진행 중</span></td></tr>
        <tr><td><b>법률 검토</b></td><td>자본시장법·전자증권법상 요건 검토 및 자문</td><td><span class="chip">진행 중</span></td></tr>
        <tr><td><b>운영 실적 축적</b></td><td>보유 자산의 공간수익화 운영 데이터 확보</td><td><span class="chip">진행 중</span></td></tr>
        <tr><td><b>발행·상장</b></td><td>관련 법령상 절차와 공시에 따른 발행 및 상장</td><td><span class="chip chip-goal">시행일 이후 준비</span></td></tr>
      </table>
    </div>
    <p class="note-plain rv" style="margin-top:18px">· 위 일정은 현재 준비 상황에 대한 안내이며, 규제 환경과 시장 여건에 따라 변경될 수 있습니다. 확정 사항은 공식 채널로 공지합니다.</p>
    <div class="note-box rv" style="margin-top:22px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px">
      <div><b>사업 개요를 더 자세히 보고 싶으시다면</b><br>그룹의 사업 구조와 강점을 정리한 안내 채널을 별도로 운영하고 있습니다. 게재 내용은 사업 소개이며 투자 권유가 아닙니다.</div>
      <a class="btn btn-primary btn-sm" href="https://hmkinvestment.pages.dev" target="_blank" rel="noopener">HMK 투자안내 <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
    </div>
  </div>
</section>
'''.replace("__SPEC__", LIQ_SPEC) + CTA

# ───────────────── 보유 자산 ─────────────────

def asset(anchor, no, name, loc, img, sp, now_pts, fut_pts, fut_title, closing):
    now_li = "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in now_pts)
    fut_li = "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in fut_pts)
    sp_dv = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in sp)
    return f'''
<article class="pf-item rv" id="{anchor}" style="scroll-margin-top:calc(var(--top-h) + 20px)">
  <div class="pf-hero">
    <img src="/assets/portfolio/{img}.jpg" alt="{name} 전경" loading="lazy">
    <div class="cap"><span class="badge">보유 물건 {no}</span><h3>{name}</h3><span class="loc">{loc}</span></div>
  </div>
  <dl class="pf-spec">{sp_dv}</dl>
  <div class="pf-cols">
    <div class="pf-panel"><h4><span class="ic">01</span>상권·입지</h4><ul>{now_li}</ul></div>
    <div class="pf-panel navy"><h4><span class="ic">02</span>{fut_title}</h4><ul>{fut_li}</ul></div>
  </div>
  <p style="margin-top:14px;font-size:14.5px;color:var(--ink-soft)">{closing}</p>
</article>'''


ASSETS_BODY = (r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px);padding-bottom:0">
  <div class="wrap">
    <div class="prose rv" style="max-width:46em">
      <h2 style="margin-top:0">숫자보다 먼저, 입지를 보여드립니다</h2>
      <p>HMK가 확보하는 자산의 기준은 단순합니다. <strong>배후 수요가 검증된 입지에서, 시장이 가격을 눌러놓은 공간</strong>을 찾는 것. 아래 세 자산은 그 기준을 통과해 현재 공간수익화 전환을 진행 중인 보유 부동산입니다.</p>
      <p style="font-size:14px;color:var(--ink-soft)">· 본 페이지는 자산과 입지에 대한 소개이며, 매매가·감정가 등 가격 정보와 투자 조건은 게재하지 않습니다. 면적은 등기·건축물대장 기준의 분양면적(전용면적) 표기입니다. <span class="chip" style="vertical-align:middle;margin-left:4px">2026.08 기준</span></p>
    </div>
  </div>
</section>

<section class="sec"><div class="wrap">
'''
+ asset("ilsan", "01", "일산 엠시티타워", "경기 고양시 일산동구 장항동 · 일산호수공원 인접", "ilsan",
        [("규모", "179평 (전용 71평)"), ("형태", "복합 상업시설 내 구분상가"), ("활용", "공간수익화 전환 조성 중")],
        [("엠시티 단지 950세대의 자체 배후", "약 6,000명이 상주하는 주거·업무 복합 단지 안에 있어, 건물 밖으로 나가지 않는 고정 수요를 품고 있습니다."),
         ("주거용 오피스텔 646세대 인접", "지하 4층~지상 15층, 총 4개 동 규모의 오피스텔이 붙어 있어 소형 가구의 수납·보관 수요가 두텁습니다."),
         ("지상 15층 오피스, 약 70개 사 입주", "업무 인구가 만드는 서류·비품·재고 보관 수요를 함께 흡수할 수 있는 구조입니다."),
         ("단지 내 상업시설 약 200개 점포", "지하 1층~지상 3층에 상권이 형성되어 있어 유동 인구와 접근성이 검증된 입지입니다.")],
        [("MBC 일산 드림센터 인접", "약 7,000명이 상주하는 방송 제작 인프라가 가까이 있어 안정적인 배후 인구를 더합니다."),
         ("반경 2km 내 인구 10만 명 이상", "정발산역·마두역 도보 5분 생활권으로, 일산 주요 주거·오피스 밀집지역의 한가운데입니다."),
         ("일산테크노밸리 · GTX-A 개통", "대규모 일자리 인프라 조성과 광역 교통 확충이 진행 중인, 수요가 더해지는 방향의 입지입니다."),
         ("풍부한 배후와 안정된 인프라", "이미 완성된 상권 위에 미래 변화가 더해지는, 미래가치가 높게 평가되는 자리입니다.")],
        "미래가치",
        "완성형 복합단지의 검증된 수요 위에서 운영을 시작할 수 있다는 점이 이 자산의 핵심입니다.")
+ asset("hwaseong", "02", "화성 송산시티 L-Tower 301·302호", "경기 화성시 새솔동 · 송산그린시티 중심상권 3층", "hwaseong",
        [("규모", "91.4평 (전용 57.7평)"), ("형태", "중심상권 상가 3층 2개 호실"), ("활용", "공간수익화 전환 조성 중")],
        [("아파트 5개 단지 8,700세대 배후", "약 2만 5천 명이 거주하는 송산그린시티의 생활 수요를 정면으로 받는 자리입니다."),
         ("신흥 주거지의 상업 핵심 입지", "상업지구 중심상권이자 송산그린시티의 중심축에 해당하는 위치입니다."),
         ("복합·중대형 오피스텔 인접", "주거용 오피스 등 배후 수요가 두터워 생활 밀착형 서비스에 유리합니다."),
         ("1인·신혼 가구 밀집 지역", "수납 공간이 부족한 세대 구성이라, 보관 수요가 구조적으로 발생하는 상권입니다.")],
        [("신세계그룹 국제테마파크 조성 예정", "약 4.5조 원 투자 규모의 개발이 예정되어 있는 권역입니다."),
         ("글로벌 관광거점으로의 변화", "스타필드·프리미엄아울렛·호텔·워터파크 등 대형 집객 시설이 계획되어 있습니다."),
         ("연간 약 3,200만 명 관광 수요 기대", "새솔동 상권이 직접 흡수하게 될 배후 상권 규모입니다."),
         ("핵심 배후 상권의 확장 여력", "상권 확장에 따라 자산 가치 상승이 기대되는 성장 초입의 입지입니다.")],
        "미래가치",
        "지금은 신도시의 생활 수요를, 앞으로는 대규모 개발의 파급을 받는 이중 구조의 입지입니다. 개발 계획은 해당 사업 주체의 일정에 따라 변동될 수 있습니다.")
+ asset("gangdong", "03", "강동 로데오팰리스 B103", "서울 강동구 천호동 · 지하 1층 B103", "gangdong",
        [("규모", "90평 (전용 60평)"), ("형태", "지하 1층 단일 공간"), ("활용", "공간수익화 전환 조성 중")],
        [("천호역 5·8호선 더블 역세 생활권", "강동의 핵심 생활상권 안쪽에 자리한, 접근성이 검증된 입지입니다."),
         ("로데오거리·현대백화점 천호점 인접", "배후 주거와 상업 수요를 동시에 흡수할 수 있는 상권 중심부입니다."),
         ("주거·상업 복합 수요", "문서·비품·재고·이사 보관까지, 도심형 보관 수요의 스펙트럼이 넓은 곳입니다."),
         ("반경 500m~1km 주거 배후권", "밀집된 생활 수요를 직접 흡수하는 서울 도심 주거지 한복판입니다.")],
        [("천호 재정비촉진지구 수혜권", "신규 인구 유입과 상권 재편이 예정된 정비 권역에 속해 있습니다."),
         ("서울 도심 상업지 자산", "도심 상업지 자산으로서 중장기 재평가 여지를 가진 위치입니다."),
         ("전용 60평 단일 공간 구조", "기둥 간섭이 적어 유닛 배치 효율이 높은, 공유창고에 최적화된 평면입니다."),
         ("지상 대비 유리한 비용 구조", "지하 1층의 비용 구조가 공간 운영 효율을 높여 줍니다.")],
        "미래가치·운영 여건",
        "서울 도심의 검증된 수요와 정비사업의 변화를 함께 안고 가는 자산입니다.")
+ r'''
  <div class="note-box rv" style="margin-top:40px"><b>안내</b> — 이 페이지는 보유 자산의 입지와 활용 계획을 소개하는 자료이며, 특정 상품·계약에 대한 청약의 권유가 아닙니다. 기재된 세대수·인구·개발계획 등은 공개 자료 기준이며, 외부 개발 사업은 해당 주체의 사정에 따라 변경될 수 있습니다.</div>
</div></section>
''' + CTA)

PAGES = {
    "/model/": {
        "title": "밸류업 순환모델 | HMK 홀딩스그룹", "active": "사업모델",
        "desc": "AI 초저가 매입 → 공간수익화 → 자산 유동화 → 재투자. 네 단계를 그룹이 직접 수행하는 HMK 밸류업 순환모델을 소개합니다.",
        "crumbs": [("사업모델", "/model/")],
        "eyebrow": "BUSINESS MODEL", "h1": "밸류업 순환모델",
        "lead": "저평가된 자산 하나가 수익 자산으로 다시 태어나고, 그 성과가 다음 자산으로 이어지는 네 단계.",
        "hero_extra": minirail({1, 2, 3, 4}), "body": HUB,
    },
    "/model/ai-sourcing/": {
        "title": "AI 초저가 매입 | HMK 홀딩스그룹", "active": "사업모델",
        "desc": "월 23만 건 이상의 물건을 분석해 저평가 자산을 선별하고, 권리 문제를 해결해 감정가 대비 20% 이하로 확보합니다.",
        "crumbs": CR + [("AI 초저가 매입", "/model/ai-sourcing/")],
        "eyebrow": "STEP 01 / AI SOURCING", "h1": "AI 프롭테크<br>초저가 매입",
        "lead": "국내 최초로 구축한 AI부동산 초저가 매입시스템으로 물건을 찾고, 20여 년의 권리분석 경험으로 문제를 풉니다.",
        "hero_extra": minirail({1}), "body": AI_BODY,
    },
    "/model/space/": {
        "title": "공간수익화 모델 | HMK 홀딩스그룹", "active": "사업모델",
        "desc": "공유창고 · 창고형 할인매장 · 라이브커머스를 한 건물에 결합하고 통합 물류 코어로 연결하는 HMK 공간수익화 모델.",
        "crumbs": CR + [("공간수익화 모델", "/model/space/")],
        "eyebrow": "STEP 02 / SPACE MONETIZING", "h1": "HMK<br>공간수익화 모델",
        "lead": "한 건물에 보관·판매·방송 세 개의 수익을 겹쳐 넣습니다. 단일 임차 구조로는 나올 수 없는 수익 구조입니다.",
        "hero_extra": minirail({2}), "body": SPACE_BODY,
    },
    "/model/liquidity/": {
        "title": "자산 유동화 | HMK 홀딩스그룹", "active": "사업모델",
        "desc": "운영 수익을 근거로 자산가치를 재평가받고, 2027년 2월 4일 시행되는 제도에 맞춰 토큰증권 발행·상장을 준비하고 있습니다.",
        "crumbs": CR + [("자산 유동화", "/model/liquidity/")],
        "eyebrow": "STEP 03 / LIQUIDITY", "h1": "자산 유동화",
        "lead": "가치 상승은 주장이 아니라 증명의 문제입니다. 운영 실적이 그 증거가 되고, 유동화가 순환의 속도를 만듭니다.",
        "hero_extra": minirail({3, 4}), "body": LIQ_BODY,
    },
    "/model/assets/": {
        "title": "보유 자산 | HMK 홀딩스그룹", "active": "사업모델",
        "desc": "일산 엠시티타워, 화성 송산시티 L-Tower, 강동 로데오팰리스 — HMK가 보유한 부동산의 상권·입지 강점과 미래가치를 소개합니다.",
        "crumbs": CR + [("보유 자산", "/model/assets/")],
        "eyebrow": "PORTFOLIO", "h1": "보유 자산",
        "lead": "좋은 입지의 기준을 통과한 자산들입니다. 어떤 상권 위에 있고, 어떤 미래를 앞두고 있는지 보여드립니다.",
        "body": ASSETS_BODY,
    },
}
