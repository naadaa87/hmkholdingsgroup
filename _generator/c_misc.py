# -*- coding: utf-8 -*-
"""뉴스 / 채용 / 문의 / 정책 / 404"""

ARROW = '<svg viewBox="0 0 16 16" width="16" height="16" fill="none" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

NEWS = r'''
<section class="sec" style="padding-top:clamp(46px,5vw,70px)">
  <div class="wrap">
    <div class="news-filter rv" role="group" aria-label="소식 분류 필터">
      <button type="button" class="chip on" data-cat="all" aria-pressed="true">전체</button>
      <button type="button" class="chip" data-cat="그룹 뉴스" aria-pressed="false">그룹 뉴스</button>
      <button type="button" class="chip" data-cat="프로젝트" aria-pressed="false">프로젝트</button>
      <button type="button" class="chip" data-cat="시장 인사이트" aria-pressed="false">시장 인사이트</button>
    </div>
    <div class="grid g3" id="news-list">
      <article class="post-card rv" data-cat="그룹 뉴스"><div class="post-meta"><span class="post-cat">그룹 뉴스</span><span class="post-date">2026.08.20</span></div>
        <h3>HMK홀딩스그룹, 그룹 공식 홈페이지 개편</h3>
        <p>사업 확장에 맞춰 그룹 소개 체계를 새로 정리했습니다. 밸류업 순환플랫폼과 공간수익화 구조, 보유 자산 정보를 공식 채널에서 확인하실 수 있습니다.</p></article>
      <article class="post-card rv" data-cat="프로젝트"><div class="post-meta"><span class="post-cat">프로젝트</span><span class="post-date">2026.08.12</span></div>
        <h3>일산 엠시티타워, 공유창고 전환 조성 착수</h3>
        <p>복합 상가 내 장기 공실 구간을 무인 보관 시설로 전환하는 공사에 들어갔습니다. 조성 완료와 오픈 소식은 이 채널로 공개할 예정입니다.</p></article>
      <article class="post-card rv" data-cat="시장 인사이트"><div class="post-meta"><span class="post-cat">시장 인사이트</span><span class="post-date">2026.08.05</span></div>
        <h3>비어 있는 상가는 왜 계속 늘어나는가</h3>
        <p>수요의 이동, 공급의 관성, 가격의 경직성. 공실의 세 가지 원인을 짚고, 공실 상가를 검토할 때 확인해야 할 다섯 가지를 정리했습니다.</p></article>
      <article class="post-card rv" data-cat="프로젝트"><div class="post-meta"><span class="post-cat">프로젝트</span><span class="post-date">2026.07.28</span></div>
        <h3>강동 로데오팰리스 B103 확보</h3>
        <p>천호역 더블 역세권 생활상권의 지하 1층 단일 공간을 확보했습니다. 도심형 공간수익화 모델을 검증하는 자산이 될 예정입니다.</p></article>
      <article class="post-card rv" data-cat="프로젝트"><div class="post-meta"><span class="post-cat">프로젝트</span><span class="post-date">2026.07.15</span></div>
        <h3>화성 송산시티 L-Tower 301·302호 확보</h3>
        <p>송산그린시티 중심상권 3층 두 개 호실을 확보했습니다. 8,700세대 배후 수요를 겨냥한 신도시형 표준 모델을 적용합니다.</p></article>
      <article class="post-card rv" data-cat="시장 인사이트"><div class="post-meta"><span class="post-cat">시장 인사이트</span><span class="post-date">2026.07.02</span></div>
        <h3>상가 한 층이 공유창고가 되기까지</h3>
        <p>실측, 유닛 배치, 전기·보안 설비, 무인 운영 세팅. 전환 공사 현장에서 실제로 진행되는 일들을 순서대로 기록했습니다.</p></article>
    </div>
    <p class="note-plain rv" style="margin-top:26px">· 새 소식을 계속 추가합니다. 지점 오픈, 자산 확보, 프로젝트 진행 등 그룹의 공식 소식은 이 공간에서 가장 먼저 공개됩니다. 개별 기사 상세 페이지는 순차 게재할 예정입니다.</p>
  </div>
</section>
'''

CAREERS = r'''
<section class="sec" style="padding-top:clamp(56px,6vw,84px)">
  <div class="wrap">
    <div class="prose rv" style="max-width:46em;margin-bottom:44px">
      <h2 style="margin-top:0">문제를 즐기는 사람과<br>일하고 싶습니다</h2>
      <p>HMK의 일은 정답이 정해진 일이 아닙니다. 권리가 얽힌 자산 앞에서 해법을 설계하고, 비어 있던 공간의 쓰임을 다시 상상하고, 무인 매장의 기술 스택을 만들어 가는 일입니다. 어렵지만, 그만큼 성장의 밀도가 높은 현장입니다.</p>
      <p>우리는 직급보다 근거를 존중합니다. 데이터와 현장 확인으로 뒷받침된 의견이면 연차와 무관하게 채택됩니다.</p>
    </div>
    <div class="sec-head rv"><div><span class="eyebrow">JOB FAMILIES</span><h2>이런 동료를 찾습니다</h2></div></div>
    <div class="grid g4">
      <div class="card rv"><h3 style="font-size:17px">투자·자산</h3><p>물건 검토, 권리분석, 매입 실행. 부동산·금융·법무 배경이면 좋습니다.</p></div>
      <div class="card rv"><h3 style="font-size:17px">공간·운영</h3><p>지점 조성 관리, 운영 기획, 고객 경험. 공간 서비스 경험을 환영합니다.</p></div>
      <div class="card rv"><h3 style="font-size:17px">유통·커머스</h3><p>상품 매입, 매장 운영, 라이브 방송 기획, 셀러 관리.</p></div>
      <div class="card rv"><h3 style="font-size:17px">기술·데이터</h3><p>AI 소싱, IoT·관제, 데이터 분석. 만든 것이 현장에서 바로 쓰입니다.</p></div>
    </div>
  </div>
</section>

<section class="sec sec-warm">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">WORK ENVIRONMENT</span><h2>일하는 환경</h2></div></div>
    <div class="grid g3">
      <div class="card rv"><h3>본사 인프라</h3><p>강남 신논현역 563평 본사에 독립 사무공간, 사무기기, 대형 세미나룸, 카페테리아를 갖추고 있습니다.</p></div>
      <div class="card rv"><h3>파트너 개방</h3><p>직원뿐 아니라 함께 일하는 파트너에게도 본사 인프라를 제공합니다. 파트너 모집은 <a href="https://hmkpartner.com" target="_blank" rel="noopener" style="text-decoration:underline;font-weight:700">hmkpartner.com</a>에서 진행합니다.</p></div>
      <div class="card rv"><h3>현장 중심</h3><p>책상에서만 판단하지 않습니다. 현장 확인과 데이터가 의사결정의 기준입니다.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><div><span class="eyebrow">PROCESS</span><h2>전형 안내</h2></div></div>
    <div class="grid g4 rv">
      <div class="card"><span class="eyebrow" style="margin-bottom:8px">STEP 1</span><h3 style="font-size:17px">서류 지원</h3><p>이력서(자유 양식)를 이메일로 보내주세요.</p></div>
      <div class="card"><span class="eyebrow" style="margin-bottom:8px">STEP 2</span><h3 style="font-size:17px">실무 인터뷰</h3><p>담당 부서와 직무 중심으로 대화합니다.</p></div>
      <div class="card"><span class="eyebrow" style="margin-bottom:8px">STEP 3</span><h3 style="font-size:17px">경영진 인터뷰</h3><p>일하는 방식과 방향을 함께 확인합니다.</p></div>
      <div class="card"><span class="eyebrow" style="margin-bottom:8px">STEP 4</span><h3 style="font-size:17px">처우 협의·입사</h3><p>조건을 협의하고 합류 일정을 정합니다.</p></div>
    </div>
    <div class="prose rv" style="margin-top:34px">
      <p>수시 채용으로 운영합니다. 이력서를 <a href="mailto:hmkholdings@hmkholdings.com" style="text-decoration:underline;font-weight:700">hmkholdings@hmkholdings.com</a>으로 보내주시면 검토 후 개별 연락드립니다. 지원 서류는 채용 목적 외에 사용하지 않으며, 전형 종료 후 관계 법령에 따라 파기합니다.</p>
      <div class="note-box" style="margin-top:20px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px">
        <div><b>사업 파트너 모집</b><br>사업총괄·분야별 파트너·투자 파트너 모집은 전용 사이트에서 진행합니다. 계열사별 채용 소식도 각 그룹사 홈페이지에서 안내됩니다.</div>
        <a class="btn btn-primary btn-sm" href="https://hmkpartner.com" target="_blank" rel="noopener">HMK 파트너모집 사이트 <svg viewBox="0 0 12 12" width="12" height="12" fill="none" aria-hidden="true"><path d="M3 9L9 3M9 3H4.2M9 3v4.8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      </div>
    </div>
  </div>
</section>
'''

CONTACT = r'''
<section class="sec" style="padding-top:clamp(46px,5vw,70px)">
  <div class="wrap">
    <div class="contact-grid">
      <form id="contact-form" novalidate>
        <h2 style="font-size:22px;margin-bottom:18px">1. 어떤 문의이신가요?</h2>
        <div class="form-types" role="radiogroup" aria-label="문의 유형 선택">
          <div class="ftype"><input type="radio" name="ctype" id="t-proposal" value="proposal" data-label="물건 제안" checked><label for="t-proposal">물건 제안<small>매각·활용 검토</small></label></div>
          <div class="ftype"><input type="radio" name="ctype" id="t-partner" value="partner" data-label="사업 제휴"><label for="t-partner">사업 제휴<small>입점·셀러·공간</small></label></div>
          <div class="ftype"><input type="radio" name="ctype" id="t-expert" value="expert" data-label="전문가 협업"><label for="t-expert">전문가 협업<small>법무·평가·시공</small></label></div>
          <div class="ftype"><input type="radio" name="ctype" id="t-media" value="media" data-label="언론·기관"><label for="t-media">언론·기관<small>취재·자료</small></label></div>
          <div class="ftype"><input type="radio" name="ctype" id="t-general" value="general" data-label="일반 문의"><label for="t-general">일반 문의<small>기타·소개서</small></label></div>
        </div>

        <h2 style="font-size:22px;margin:36px 0 16px">2. 내용을 알려주세요</h2>
        <div class="form-grid">
          <div class="field"><label for="f-name">이름 <span class="req">*</span></label><input id="f-name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="f-phone">연락처 <span class="req">*</span></label><input id="f-phone" type="tel" autocomplete="tel" placeholder="010-0000-0000" required></div>
          <div class="field full"><label for="f-email">이메일</label><input id="f-email" type="email" autocomplete="email" placeholder="회신받으실 주소 (선택)"></div>

          <div class="fgroup" data-for="proposal">
            <div class="field"><label for="p-loc">물건 소재지</label><input id="p-loc" data-label="물건 소재지" type="text" placeholder="예: 경기 고양시 일산동구 ○○"></div>
            <div class="field"><label for="p-kind">자산 유형</label><select id="p-kind" data-label="자산 유형"><option value="">선택</option><option>상가·근린생활시설</option><option>지식산업센터·오피스</option><option>특수물건·권리하자 물건</option><option>기타</option></select></div>
          </div>
          <div class="fgroup" data-for="partner">
            <div class="field"><label for="pt-org">회사·소속</label><input id="pt-org" data-label="회사·소속" type="text"></div>
            <div class="field"><label for="pt-area">제휴 분야</label><select id="pt-area" data-label="제휴 분야"><option value="">선택</option><option>공간·부동산</option><option>매장 입점·상품 공급</option><option>라이브커머스 셀러</option><option>기술·IoT</option><option>기타</option></select></div>
          </div>
          <div class="fgroup" data-for="expert">
            <div class="field"><label for="ex-org">소속·자격</label><input id="ex-org" data-label="소속·자격" type="text" placeholder="예: ○○법무법인 / 감정평가사"></div>
            <div class="field"><label for="ex-area">전문 분야</label><select id="ex-area" data-label="전문 분야"><option value="">선택</option><option>법무</option><option>세무·회계</option><option>감정평가</option><option>건설·시설</option><option>기타</option></select></div>
          </div>
          <div class="fgroup" data-for="media">
            <div class="field"><label for="m-org">매체·기관명</label><input id="m-org" data-label="매체·기관명" type="text"></div>
            <div class="field"><label for="m-due">희망 회신 기한</label><input id="m-due" data-label="희망 회신 기한" type="text" placeholder="예: 8/25까지"></div>
          </div>
          <div class="fgroup" data-for="general"></div>

          <div class="field full"><label for="f-body">문의 내용 <span class="req">*</span></label>
            <textarea id="f-body" required placeholder="내용을 자유롭게 적어주세요. 물건 제안은 개요만 주셔도 검토를 시작할 수 있습니다."></textarea>
            <span class="hint">회사소개서가 필요하시면 "회사소개서 요청"이라고 적어주세요. 이메일로 보내드립니다.</span></div>
        </div>

        <div class="consent">
          <b>개인정보 수집·이용 안내</b> — 수집 항목: 이름, 연락처, 이메일, 문의 내용 / 목적: 문의 접수와 회신 / 보유 기간: 처리 완료 후 1년 보관 뒤 파기. 동의를 거부하실 수 있으나, 이 경우 문의 접수가 제한됩니다. <a href="/policy/privacy/" style="text-decoration:underline">자세히 보기</a>
          <label><input type="checkbox" id="f-agree"> 위 내용을 확인했으며, 개인정보 수집·이용에 동의합니다. <span class="req">*</span></label>
        </div>

        <div class="form-actions">
          <button class="btn btn-primary" type="submit">문의 접수하기</button>
          <span class="form-msg" id="form-msg" role="status" aria-live="polite"></span>
        </div>
        <p style="margin-top:14px;font-size:13px;color:var(--ink-soft)">· 접수 버튼을 누르면 작성 내용이 담긴 메일이 열립니다. 전송까지 완료해 주세요. 영업일 기준 2일 안에 담당 부서가 회신드립니다.</p>
      </form>

      <aside>
        <div class="card rv" style="position:sticky;top:calc(var(--top-h) + 20px)">
          <h3>바로 연락하기</h3>
          <p style="margin-top:8px">전화가 편하시면 바로 주셔도 됩니다.</p>
          <p style="margin-top:14px;font-size:24px;font-weight:800;color:var(--navy)"><a href="tel:1555-5335">1555-5335</a></p>
          <p style="font-size:13.5px;color:var(--ink-soft)">평일 09:00 – 18:00</p>
          <p style="margin-top:12px"><a href="mailto:hmkholdings@hmkholdings.com" style="color:var(--orange-deep);font-weight:700;font-size:14.5px">hmkholdings@hmkholdings.com</a></p>
          <hr style="border:0;border-top:1px solid var(--line);margin:20px 0">
          <p style="font-size:14px"><b>방문 상담 (예약제)</b><br>서울 강남구 봉은사로 129-1<br>751빌딩 3층<br><a href="/group/location/" style="text-decoration:underline">오시는길 보기</a></p>
          <hr style="border:0;border-top:1px solid var(--line);margin:20px 0">
          <p style="font-size:14px"><b>서비스별 문의</b><br>공유창고 이용, 매장 입점, 셀러 신청 등은 해당 서비스 사이트에서 더 빠르게 안내받으실 수 있습니다.<br><a href="/sites/" style="text-decoration:underline;font-weight:700;color:var(--orange-deep)">관련 사이트 안내</a></p>
        </div>
      </aside>
    </div>
  </div>
</section>
'''

PRIVACY = r'''
<section class="sec" style="padding-top:clamp(46px,5vw,70px)">
  <div class="wrap"><div class="prose rv" style="max-width:52em">
    <p class="lead">HMK홀딩스그룹(이하 "그룹")은 개인정보 보호법 등 관계 법령을 준수하며, 이용자의 개인정보를 아래와 같이 처리합니다. 본 방침은 그룹 홈페이지의 문의·상담 과정에 적용됩니다.</p>
    <h2>1. 수집하는 개인정보 항목과 방법</h2>
    <p>홈페이지 문의(문의하기, 이메일, 전화) 과정에서 이름, 연락처, 이메일 주소, 문의 내용을 수집합니다. 채용 지원 시에는 이력서에 기재된 정보를 수집합니다.</p>
    <h2>2. 수집·이용 목적</h2>
    <p>문의 접수와 회신, 상담 진행, 채용 전형 진행. 수집한 정보는 명시된 목적 외의 용도로 이용하지 않습니다.</p>
    <h2>3. 보유·이용 기간</h2>
    <p>문의 정보는 처리 완료 후 1년간 보관한 뒤 지체 없이 파기합니다. 채용 서류는 전형 종료 후 관계 법령이 정한 기간 내 파기합니다. 법령에 따라 보존이 필요한 경우 해당 기간 동안 보관합니다.</p>
    <h2>4. 제3자 제공과 처리 위탁</h2>
    <p>그룹은 이용자의 동의 없이 개인정보를 제3자에게 제공하지 않습니다. 처리 위탁이 발생하는 경우 수탁자와 위탁 업무 내용을 본 방침에 공개합니다.</p>
    <h2>5. 정보주체의 권리</h2>
    <p>이용자는 언제든지 자신의 개인정보에 대한 열람·정정·삭제·처리정지를 요구할 수 있습니다. 요청은 아래 연락처로 주시면 지체 없이 조치합니다.</p>
    <h2>6. 파기 절차와 방법</h2>
    <p>보유 기간이 지난 개인정보는 재생 불가능한 방법으로 파기합니다. 전자 파일은 복구할 수 없는 기술적 방법으로 삭제하고, 출력물은 분쇄 또는 소각합니다.</p>
    <h2>7. 개인정보 보호책임 연락처</h2>
    <p>개인정보 관련 문의: 대표전화 1555-5335 / hmkholdings@hmkholdings.com<br>개인정보 보호책임자 성명·직책은 내부 지정 절차 확정 후 본 방침에 게재합니다.</p>
    <h2>8. 방침의 변경</h2>
    <p>본 방침이 변경되는 경우 시행 7일 전부터 홈페이지에 공지합니다.</p>
    <p style="font-size:14px;color:var(--ink-soft)">시행일: 2026년 8월</p>
  </div></div>
</section>
'''

TERMS = r'''
<section class="sec" style="padding-top:clamp(46px,5vw,70px)">
  <div class="wrap"><div class="prose rv" style="max-width:52em">
    <p class="lead">본 약관은 HMK홀딩스그룹 홈페이지 이용에 관한 기본 사항을 정합니다.</p>
    <h2>1. 목적과 적용</h2>
    <p>본 홈페이지는 그룹과 소속 법인의 사업을 소개하기 위한 정보 제공 채널입니다.</p>
    <h2>2. 정보의 정확성</h2>
    <p>그룹은 게재 정보의 정확성을 위해 노력하며, 실적 수치에는 기준 시점을 표기합니다. 사업 환경 변화에 따라 내용은 갱신될 수 있습니다.</p>
    <h2>3. 법적 행위의 주체</h2>
    <p>계약 등 법적 행위는 해당 업무를 수행하는 개별 법인과 이루어집니다. 각 법인의 정보는 홈페이지 하단 표기를 따릅니다.</p>
    <h2>4. 지식재산권</h2>
    <p>홈페이지의 콘텐츠(글·도표·디자인)에 대한 권리는 그룹에 있습니다. 출처를 표기한 인용은 환영하며, 상업적 무단 전재는 금합니다.</p>
    <h2>5. 책임의 한계</h2>
    <p>이용자가 홈페이지 정보를 근거로 한 의사결정의 결과에 대하여, 관계 법령이 허용하는 범위에서 그룹은 책임을 지지 않습니다. 중요한 의사결정 전에는 반드시 개별 상담과 전문가 확인을 거치시기 바랍니다.</p>
    <p style="font-size:14px;color:var(--ink-soft)">시행일: 2026년 8월</p>
  </div></div>
</section>
'''

NOTFOUND = r'''
<section class="err-wrap"><div class="wrap">
  <span class="err-code">404 NOT FOUND</span>
  <h1 style="margin-top:12px">찾으시는 페이지가 없습니다</h1>
  <p class="lead" style="margin:14px auto 0;max-width:32em">주소가 바뀌었거나 잘못 입력되었을 수 있습니다. 아래에서 원하시는 곳으로 이동해 주세요.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:30px">
    <a class="btn btn-primary" href="/">홈으로</a>
    <a class="btn btn-ghost" href="/model/">사업모델</a>
    <a class="btn btn-ghost" href="/contact/">문의하기</a>
  </div>
</div></section>
'''

PAGES = {
    "/news/": {
        "title": "뉴스 | HMK홀딩스그룹", "active": "뉴스",
        "desc": "그룹 뉴스, 프로젝트 소식, 시장 인사이트 — HMK홀딩스그룹의 공식 소식을 전합니다.",
        "crumbs": [("뉴스", "/news/")],
        "eyebrow": "NEWS", "h1": "뉴스",
        "lead": "확인된 사실만, 기준일과 함께 공개합니다. 그룹의 공식 발표는 이 채널을 기준으로 합니다.",
        "body": NEWS,
    },
    "/careers/": {
        "title": "채용 | HMK홀딩스그룹", "active": "채용",
        "desc": "투자·자산, 공간·운영, 유통·커머스, 기술·데이터 — 문제를 즐기는 동료를 수시 채용으로 찾습니다.",
        "crumbs": [("채용", "/careers/")],
        "eyebrow": "CAREERS", "h1": "채용",
        "lead": "정답이 정해지지 않은 일에서 성장하고 싶은 분과 만나고 싶습니다.",
        "body": CAREERS,
    },
    "/contact/": {
        "title": "문의하기 | HMK홀딩스그룹", "active": "",
        "desc": "물건 제안, 사업 제휴, 전문가 협업, 언론·기관, 일반 문의 — 담당 부서가 영업일 기준 2일 안에 회신드립니다.",
        "crumbs": [("문의하기", "/contact/")],
        "eyebrow": "CONTACT", "h1": "문의하기",
        "lead": "어떤 문의든 담당 부서로 정확히 전달됩니다. 물건 제안은 개요만 주셔도 검토를 시작합니다.",
        "body": CONTACT,
    },
    "/policy/privacy/": {
        "title": "개인정보처리방침 | HMK홀딩스그룹", "active": "",
        "desc": "HMK홀딩스그룹 홈페이지의 개인정보 수집 항목, 이용 목적, 보유 기간, 파기 절차와 정보주체의 권리를 안내합니다.",
        "crumbs": [("개인정보처리방침", "/policy/privacy/")],
        "eyebrow": "POLICY", "h1": "개인정보처리방침", "body": PRIVACY,
    },
    "/policy/terms/": {
        "title": "이용약관 | HMK홀딩스그룹", "active": "",
        "desc": "HMK홀딩스그룹 홈페이지 이용에 관한 기본 사항 — 정보의 성격, 법적 행위의 주체, 금융투자상품 관련 고지, 책임의 한계.",
        "crumbs": [("이용약관", "/policy/terms/")],
        "eyebrow": "POLICY", "h1": "이용약관", "body": TERMS,
    },
    "/404.html": {
        "title": "페이지를 찾을 수 없습니다 | HMK홀딩스그룹", "active": "",
        "desc": "요청하신 페이지가 없습니다. 홈 또는 주요 페이지로 이동해 주세요.",
        "no_hero": True, "body": NOTFOUND,
    },
}
