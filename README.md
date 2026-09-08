# HMK홀딩스그룹 공식 홈페이지 — 최종본

**도메인** www.hmkholdings.com · **저장소** github.com/naadaa87/hmkholdingsgroup
**빌드** 2026-09-08 · **총 24페이지**

이 폴더 **안의 내용**이 저장소 **루트**에 그대로 올라가야 합니다.

---

## 1. 업로드 방법

1. 저장소에서 **기존 파일을 모두 삭제**합니다 (남아 있으면 옛 파일과 섞입니다)
2. **Add file → Upload files**
3. **`choose your files` 버튼은 절대 누르지 마세요.** 폴더 경로가 지워져 파일이 뒤엉킵니다
4. 압축을 푼 `hmk-website` 폴더 **안으로 들어가서** 항목 전부 선택(Ctrl+A) → 브라우저 화면으로 **드래그**
5. 목록이 `model/space/index.html`, `assets/market/store-front.jpg` 처럼 **슬래시 경로**로 보이는지 확인 → **Commit changes**

**업로드 후 확인** — `https://www.hmkholdings.com/` 에서 **Ctrl+U**(소스 보기)를 눌러 첫 줄에
`<!-- HMK build 202609080041 -->` 이 보이면 최신본이 배포된 것입니다.

**Cloudflare Pages 설정** — Framework preset **None** / Build command **비움** / Build output directory **`/`**

---

## 2. 네이버 소유확인 — 준비 완료

전 페이지 `<head>`에 **두 주소의 소유확인 코드가 모두** 들어 있습니다. 업로드만 하면 바로 확인됩니다.

```html
<meta name="naver-site-verification" content="fcb0b86a1678a6f2ca6c42120a2cd4d77d9db236" />  <!-- www.hmkholdings.com -->
<meta name="naver-site-verification" content="134949796298c20ab73107f90d1660284aea3216" />  <!-- hmkholdings.com -->
```

**순서**
1. 업로드 → 2분 대기
2. 소스 보기(Ctrl+U) → Ctrl+F로 `fcb0b86a` 검색해서 보이는지 확인
3. 서치어드바이저 소유확인 화면 → **HTML 태그** 선택 → **소유확인** 클릭
4. www 없는 주소(`hmkholdings.com`)도 같은 방법으로 확인

**소유확인 직후**
- 요청 → 사이트맵 제출: `https://www.hmkholdings.com/sitemap.xml`
- 요청 → 웹 페이지 수집: 메인 · `/model/` · `/affiliates/` 수동 요청

**구글 서치콘솔 코드 추가** — `_generator/gen.py` 상단 `SITE_VERIFY` 목록에 한 줄 넣고 `cd _generator && python3 gen.py` 실행. 또는 `index.html` `<head>`에 직접 붙여넣어도 됩니다.

**HTML 파일 방식을 쓸 경우** — 네이버에서 받은 `naver○○○.html`을 저장소 루트에 올리면 됩니다. 생성기를 다시 돌려도 `naver`·`google`로 시작하는 html 파일은 지워지지 않습니다.

---

## 3. 화면 깨짐 재발 방지

이전에 `/affiliates/` 아이콘이 거대하게 나온 원인은 **배포된 CSS가 옛 버전**이었기 때문입니다. 세 가지로 막아 두었습니다.

1. **CSS·JS 주소에 버전 번호** — `style.css?v=202609080041`. 파일이 바뀌면 주소도 바뀌어 옛 캐시가 쓰이지 않습니다
2. **모든 아이콘에 크기 속성 직접 지정** — CSS가 없어도 아이콘이 커지지 않습니다
3. **HTML 첫 줄 빌드 번호 주석** — 배포 버전을 소스 보기로 즉시 확인

**업로드 시 `css/`와 `js/` 폴더를 반드시 함께 올려 주세요.**

---

## 4. 사이트 구성 — 5개 메뉴 · 24페이지

| 메뉴 | 하위 페이지 |
|---|---|
| **그룹소개** | 회장 인사말 · 그룹 개요·비전 · 조직·거버넌스 · 오시는길 |
| **사업모델** | 밸류업 순환플랫폼 · AI 초저가 매입 · 공간수익화 모델 · 통합물류·멤버십 시너지 · 자산 유동화 · 보유 자산 |
| **그룹사소개** | HMK그룹사 전체보기 · HMK 대부 · HMK 스토리지 · 오렌지 창고마켓 · 오렌지 라이브커머스 · 오렌지 멤버십 · 관련 사이트 안내 |
| **뉴스** | 분류 필터(전체/그룹 뉴스/프로젝트/시장 인사이트) |
| **채용** | 인재상 · 일하는 환경 · 전형 · HMK 파트너모집 |
| *(상시)* | 문의하기 · 개인정보처리방침 · 이용약관 · 404 |

**메인 스크롤** — 히어로 → 핵심 지표 → 보유 부동산 → 4단계 순환 → 3 in 1 공간수익화 → 밸류업 효과 → 통합물류·멤버십 시너지 → 그룹사 → 오렌지월드 → 뉴스 → 문의

---

## 5. 그룹사 홈페이지 연결

| 순서 | 그룹사 | 홈페이지 | 사이트 내 소개 |
|---|---|---|---|
| 1 | HMK 대부 | hmknplauction.pages.dev | `/affiliates/loan/` |
| 2 | HMK 스토리지 | hmkstorage.com | `/affiliates/storage/` |
| 3 | 김재동 회장 | kimjaedong.com | `/group/message/` |
| 4 | 오렌지 창고마켓 | orange1000.com | `/affiliates/market/` |
| 5 | 오렌지 라이브커머스 | orangeliveon.com | `/affiliates/live/` |
| 6 | 오렌지 공유창고 | storage-orange.co.kr | `/affiliates/storage/` |
| 7 | HMK 오렌지 멤버십 | orangemembership.com | `/affiliates/membership/` |
| 8 | HMK 파트너모집 | hmkpartner.com | `/careers/` |
| 9 | 통합물류·유통시스템 | (내부 시스템) | `/model/synergy/` |

전 페이지 푸터 FAMILY SITES 바, `/affiliates/`, `/sites/`, 메인 오렌지월드 섹션에 동일하게 반영되어 있습니다.

---

## 6. SEO 구성

| 항목 | 내용 |
|---|---|
| 제목·설명·키워드 | 24페이지 고유 작성 (`_generator/seo.py`에서 관리) |
| canonical | 전 페이지 `https://www.hmkholdings.com/…` |
| 공유 이미지 | 페이지별 대표 사진 (카카오톡·SNS 미리보기) |
| 구조화 데이터 | Organization + WebSite / Person(회장) / FAQPage 3곳 / ItemList(그룹사 9) / BreadcrumbList |
| sitemap.xml | 23개 URL, lastmod·priority |
| robots.txt | 네이버 Yeti·Googlebot 명시, sitemap 위치 |
| 구 URL 301 | `_redirects` |

**핵심 키워드** — 부동산 밸류업 플랫폼 · 상업용 부동산 초저가 매입 · AI 프롭테크 · 3 in 1 공간수익화 · 창고형마켓 · 라이브커머스 · 공유창고 · 오렌지 멤버십 · 통합물류 · 자산 유동화·토큰증권 · 김재동 회장 · 오렌지월드

---

## 7. 품질 검사 결과

**24페이지 × 5해상도 = 120건 자동 감사 통과** (PC 1440 · 노트북 1280 · 태블릿 768 · 모바일 390/360)

가로 스크롤, 화면 밖 요소, 아이콘 크기, 스크롤 등장 효과, 이미지 깨짐, alt 누락, h1 개수, 텍스트 잘림, 터치 탭 영역, 소유확인 태그 — 전 항목 이상 없음. 내부 링크 깨짐 0건, 구조화 데이터 오류 0건, 중복 제목 0건.

---

## 8. 오픈 전 확정 필요

| # | 항목 | 현재 상태 | 위치 |
|---|---|---|---|
| 1 | **대부업 등록기관·등록번호** | `○○○○○○` 자리표시 — 기입 전 게시 불가 | `/affiliates/loan/` |
| 2 | 개인정보 보호책임자 | 성명·직책 미기재 | `/policy/privacy/` |
| 3 | 대표 이메일 | `hmkholdings@hmkholdings.com` 수신 가능 여부 | 전 페이지 |
| 4 | Before/After 이미지 수치 | 이미지 3.3배 vs 본문 450% — 기준 통일 권장 | 메인, 공간수익화 |
| 5 | `/sites/` 와 `/affiliates/` | 내용이 상당 부분 겹침 — 통합 검토 권장 | 그룹사소개 메뉴 |

---

## 9. 내용 수정

- **문구 몇 군데** → 해당 폴더의 `index.html` 직접 수정 후 커밋
- **검색 제목·설명** → `_generator/seo.py` 수정 후 `cd _generator && python3 gen.py`
- **구조 변경·페이지 추가** → `_generator/c_*.py` 수정 후 동일하게 실행
  (`c_home.py` 메인 / `c_group.py` 그룹소개 / `c_model.py` 사업모델 / `c_affiliates.py` 그룹사 / `c_misc.py` 뉴스·채용·문의·정책)

© 2026 HMK HOLDINGS GROUP
