# HMK홀딩스그룹 공식 홈페이지 — 정식 오픈 가이드

**도메인** www.hmkholdings.com · **저장소** github.com/naadaa87/hmkholdingsgroup · **기준일** 2026-09-07

빌드 도구가 필요 없는 정적 사이트입니다. 이 폴더 안의 내용이 저장소 **루트**에 그대로 올라가야 합니다.

---

## 1. 오픈 순서

### ① GitHub 업로드
1. 저장소 `naadaa87/hmkholdingsgroup` → 기존 파일이 있으면 모두 삭제
2. **Add file → Upload files** — `choose your files` 버튼은 누르지 말고, 압축을 푼 `hmk-website` 폴더 **안의 항목을 전부 드래그**
3. 목록에 `model/space/index.html` 처럼 **슬래시 경로**가 보이는지 확인 → **Commit changes**

### ② Cloudflare Pages
- Framework preset **None** / Build command **비움** / Build output directory **`/`**(칸 왼쪽에 `/`가 보이면 비워둠)
- **Custom domains** → `www.hmkholdings.com` 추가 → DNS 안내대로 설정
- `hmkholdings.com`(루트)도 추가하고 **www로 리다이렉트**: 도메인 → **Rules → Redirect Rules** → `hmkholdings.com/*` → `https://www.hmkholdings.com/$1` (301)
- 배포 후 `https://www.hmkholdings.com/`, `/affiliates/`, `/model/space/` 가 열리면 정상

### ③ 네이버 서치어드바이저
1. https://searchadvisor.naver.com → 웹마스터 도구 → 사이트 등록 `https://www.hmkholdings.com`
2. 소유확인 — **HTML 파일 업로드** 권장: 내려받은 `naver○○○○.html`을 저장소 **루트**에 올리고 커밋 → 확인
3. 요청 → **사이트맵 제출**: `https://www.hmkholdings.com/sitemap.xml`
4. 검증 → robots.txt 수집 허용 확인 (Yeti 허용 설정됨)
5. 요청 → **웹 페이지 수집**: 메인, `/model/`, `/model/space/`, `/affiliates/` 수동 요청

### ④ 구글 서치콘솔
1. https://search.google.com/search-console → 속성 추가 → URL 접두어 `https://www.hmkholdings.com`
2. 소유확인 — HTML 파일 방식: `google○○○○.html`을 저장소 루트에 올리고 커밋 → 확인
3. Sitemaps → `sitemap.xml` 제출 → URL 검사 → 색인 생성 요청

### ⑤ 오픈 후 확인
- 네이버에서 `site:hmkholdings.com` 검색 → 며칠 내 색인 시작
- 카카오톡에 메인 주소를 붙여넣어 미리보기(og.jpg) 확인. 예전 내용이 보이면 https://developers.kakao.com/tool/debugger/sharing 에서 캐시 초기화

---

## 2. 이번 변경 (2026-09-07 · 이미지 반영판)

**브랜드 이미지 20장 배치** — 오렌지 창고마켓·라이브커머스·공유창고·멤버십·플랫폼 건물 이미지를 `assets/` 아래 5개 폴더로 정리해 배치했습니다.

| 폴더 | 사용 위치 |
|---|---|
| `assets/platform/` | 메인 히어로(단면 야경) · 공간수익화 상단(외관) · 시너지·공간수익화(공간배분 조감도) |
| `assets/market/` | 오렌지 마켓 페이지 상단·갤러리 · 공간수익화 1F · 메인 오렌지월드 카드 |
| `assets/live/` | 라이브커머스 페이지 상단·갤러리 · 공간수익화 2F · 시너지(물류 프로세스) · 메인 |
| `assets/storage/` | 스토리지 페이지 상단·갤러리 · 공간수익화 B1 · 메인 오렌지월드 카드 |
| `assets/membership/` | 멤버십 페이지 · 시너지 페이지 · 메인 시너지 섹션 |

**신설 페이지 2개**
- `/model/synergy/` **통합물류·멤버십 시너지** — 세 사업을 잇는 두 장치(상품=통합물류, 고객=멤버십)와 매출 활성화→자산가치 밸류업 흐름
- `/affiliates/membership/` **HMK 오렌지 멤버십** — 통합 포인트·교차 혜택·앱/카드

**사업모델 서사 보강** — 매입 → 3 in 1(사고·보고·맡기고) → **통합물류·멤버십 시너지** → 유동화. 메인에 시너지 섹션 추가, 순환모델 02단계에 시너지 명시, 그룹사 허브 9번 카드를 '통합물류·유통시스템'으로 정리.

**개발 저장소 (내부 참고, 사이트에는 미노출)**
- 오렌지 창고마켓 github.com/naadaa87/orangemarket
- 오렌지 라이브커머스 github.com/naadaa87/orangelivehub
- 오렌지 멤버십 github.com/naadaa87/orangemembership


**투자권유·청약권유 관련 경고·안내문구 전면 삭제** — 사업모델 허브, 공간수익화, 자산 유동화, 보유 자산, 관련 사이트, FAQ, 이용약관에서 "투자 권유가 아닙니다", "수익을 보장하지 않습니다", "결과는 달라질 수 있습니다", "청약·모집을 진행하지 않습니다" 등 모든 단서 문구를 제거했습니다.
※ 대부 부문 페이지의 **대부업 이용 시 유의사항 4줄**은 대부업법상 게재 의무가 있는 문구라 유지했습니다.


- 메뉴 **계열사 한눈에 → HMK그룹사 전체보기**, 제목·본문 문구 지시대로 교체
- 그룹사 허브를 지정 순서 9개 카드로 재구성 (아래 표)
- 홈페이지 주소를 정식 도메인으로 교체
- **HMK E커머스 삭제** — 페이지·메뉴·조직도·메인 카드 제거, 오렌지 1,000원마켓 온라인몰은 오렌지 마켓 페이지로 흡수, 구 주소는 그룹사 페이지로 자동 이동
- 메뉴·상세 페이지 명칭을 **오렌지 마켓 / 오렌지 라이브커머스**로 통일

| 순서 | 그룹사 | 홈페이지 | 사이트 내 소개 페이지 |
|---|---|---|---|
| 1 | HMK 대부 | hmknplauction.pages.dev | `/affiliates/loan/` |
| 2 | HMK 스토리지 | hmkstorage.com | `/affiliates/storage/` |
| 3 | 김재동 회장 | kimjaedong.com | `/group/message/` |
| 4 | 오렌지 마켓 | orange1000.com | `/affiliates/market/` |
| 5 | 오렌지 라이브커머스 | orangeliveon.com | `/affiliates/live/` |
| 6 | 오렌지 공유창고 | storage-orange.co.kr | — |
| 7 | 오렌지 멤버십 | orangemembership.com | — |
| 8 | HMK 파트너모집 | hmkpartner.com | `/careers/` |
| 9 | 통합매입관리 | (내부 시스템) | — |

이 링크들은 그룹사 허브 외에 **전 페이지 푸터 FAMILY SITES 바**, `/sites/` 관련 사이트 안내, 각 상세 페이지 버튼·정보표, 메인 서비스 섹션에도 동일하게 반영되어 있습니다.

## 2-0. 화면 깨짐 원인과 조치 (중요)

**증상** — `/affiliates/` 등에서 아이콘 화살표가 거대하게 표시되고 카드 레이아웃이 무너짐.

**원인** — 배포된 `css/style.css`가 **옛 버전**이었습니다. HTML은 새 버전이라 새 클래스(`.gcard`, `.g-link`)를 쓰는데, CSS에 해당 규칙이 없어 아이콘이 기본 크기(300×150)로 커진 것입니다. CSS 파일이 갱신되지 않았거나 캐시된 옛 파일이 사용된 경우입니다.

**조치**
1. **CSS·JS에 캐시 버전 붙임** — `style.css?v=202609071004` 형태. 파일이 바뀌면 주소도 바뀌므로 옛 캐시가 절대 쓰이지 않습니다.
2. **모든 인라인 아이콘에 width/height 속성 부여** — CSS가 없어도 아이콘이 커지지 않습니다.
3. HTML 첫 줄에 `<!-- HMK build 202609071004 -->` 주석 삽입 — 브라우저에서 소스 보기로 배포 버전을 즉시 확인할 수 있습니다.

**업로드 시 주의** — `css/` 와 `js/` 폴더를 반드시 함께 올려 주세요. 올린 뒤 `https://www.hmkholdings.com/` 소스 보기로 build 주석의 숫자가 최신인지 확인하시면 됩니다.

## 2-1. 전체 UI/UX 감사 결과 (2026-09-07)

**24페이지 × 6해상도 = 144건 자동 감사 통과** (PC 1440·노트북 1280·태블릿 1024/768·모바일 390/360)
검사 항목: 가로 스크롤, 화면 밖 요소, 아이콘 크기 이상, 스크롤 등장 애니메이션, 이미지 깨짐, alt 누락, h1 개수, 빈 링크, 텍스트 잘림, 카드 내용 넘침, 터치 탭 영역

**수정한 것**
- 터치 기기 탭 영역 확보 — `자세히 보기`·`홈페이지 방문` 링크와 뉴스 필터 칩을 38~44px로 확대 (기존 23~26px)
- **뉴스 분류 필터가 실제로 동작하도록 구현** — 기존에는 눌러도 반응이 없었습니다. 전체/그룹 뉴스/프로젝트/시장 인사이트 전환이 됩니다
- 뉴스 카드는 상세 페이지가 없으므로 클릭 가능한 것처럼 떠오르던 hover 효과 제거
- **조직도에 계층 라벨 추가** — `계열사` / `그룹 부문` 배지를 넣어 "그룹 — 계열사 — 사업 부문" 3단 구조가 눈에 보이도록 수정

## 2-2. 최신 변경

**메인 히어로 버튼 3개로 교체**
- HMK밸류업모델 → `/model/`
- 그룹사 전체보기 → `/affiliates/`
- 사업파트너 모집 → hmkpartner.com (새 창)
- "보유 자산 보기" 삭제. 하단 CTA 버튼도 "HMK밸류업모델"로 통일

**"밸류업 순환모델" → "밸류업 순환플랫폼"** 으로 전 사이트 명칭 변경 (메뉴·제목·본문·검색 메타 84곳)

**순환플랫폼 페이지 대폭 보강**
- 상단 대표 이미지(주간 전경) 추가 + LCP 프리로드
- **한 자산 안에서 사업이 층으로 나뉩니다** 섹션 신설 — 층별 단면도 + 면적 배분 조감도(창고 마켓 65% · 공유창고 20% · 라이브 쇼핑 15%)
- **플랫폼을 채우는 네 개의 사업** 섹션 신설 — 사진 카드 4장, 각 카드마다 `사업 소개`(사이트 내부) + `홈페이지`(외부) 두 개 링크

| 사업 | 사진 | 사업 소개 | 홈페이지 |
|---|---|---|---|
| 오렌지 창고 마켓 | market/store-front.jpg | `/affiliates/market/` | orange1000.com |
| 오렌지 라이브커머스 | live/studio-fashion.jpg | `/affiliates/live/` | orangeliveon.com |
| 오렌지 공유창고 | storage/branch-front.jpg | `/affiliates/storage/` | storage-orange.co.kr |
| HMK 오렌지 멤버십 | membership/app-card.jpg | `/affiliates/membership/` | orangemembership.com |

## 3. SEO 구성 내역 (2026-09-07 재정비)

**이번 재정비**
- 24페이지 제목·설명·키워드를 시너지·멤버십·브랜드 이미지 반영판에 맞춰 전면 재작성 (`_generator/seo.py`)
- 제목은 핵심 키워드 우선·32자 이내로 압축, 설명문은 검색자 언어로 사업 설명 + 브랜드 1회
- **페이지별 공유 이미지(og:image)** — 그룹사·사업모델 페이지는 각자의 대표 사진이 카카오톡·SNS 미리보기에 뜹니다
- **H1 키워드 강화** — 부동산 밸류업 순환모델 / 3 in 1 공간수익화 모델 / 자산 유동화·토큰증권 / 보유 부동산 포트폴리오
- **FAQ 3곳** (순환모델 5문항·공간수익화 4문항·멤버십 3문항) + FAQPage 구조화 데이터 → 롱테일 검색 대응
- **그룹사 ItemList 구조화 데이터** — 9개 그룹사·사업부를 검색엔진이 목록으로 인식
- **메인 LCP 최적화** — 히어로 이미지 preload + fetchpriority
- 브랜드 표기를 **HMK홀딩스그룹**(붙임)으로 전 페이지 통일, 서비스명 **오렌지 창고마켓**으로 통일
- 본문 키워드 커버리지 검사 통과 — 각 페이지 목표 키워드가 본문(태그 제외)에 실제 등장


| 항목 | 적용 내용 |
|---|---|
| 페이지별 title / description / keywords | 24페이지 고유 작성. `_generator/seo.py`에서 관리 |
| canonical | 전 페이지 `https://www.hmkholdings.com/…` |
| Open Graph / Twitter Card | 공유 시 제목·설명·이미지(og.jpg 1200×630) |
| 구조화 데이터 (JSON-LD) | 메인 Organization(창업자·브랜드·sameAs 9곳)+WebSite / 회장 인사말 Person / 사업모델 FAQPage 5문항 / 하위 페이지 BreadcrumbList |
| sitemap.xml | 23개 URL, lastmod·priority |
| robots.txt | 전체 허용, Yeti·Googlebot 명시, sitemap 위치 |
| 404 | noindex |
| 구 URL 301 | `_redirects` (구 구조 및 삭제 페이지 자동 이관) |

**핵심 키워드** — 부동산 밸류업 플랫폼 · 상업용 부동산 매입 · AI 프롭테크 · 공유창고 · 창고형마켓 · 라이브커머스 · 자산 유동화·토큰증권 · 김재동 회장 · 오렌지월드 · 오렌지 마켓·라이브커머스·공유창고·멤버십

## 4. 폴더 구성

```
(저장소 루트)
├─ index.html · group/ · model/ · affiliates/ · sites/ · news/ · careers/ · contact/ · policy/
├─ assets/  (logo, chairman, og.jpg, model/ 4종, portfolio/ 3종, platform/ market/ live/ storage/ membership/ 20종)
├─ css/ · js/
├─ 404.html · sitemap.xml · robots.txt · _redirects · _headers
├─ _generator/   ← 생성기 (seo.py = 검색 제목·설명·키워드)
└─ README.md
```

## 5. 오픈 전 확정 필요

| # | 항목 | 현재 상태 | 위치 |
|---|---|---|---|
| 1 | **대부업 등록기관·등록번호** | `○○○○○○` 자리표시 — 기입 전 게시 불가 | `/affiliates/loan/` |
| 2 | 개인정보 보호책임자 | 성명·직책 미기재 | `/policy/privacy/` |
| 3 | 대표 이메일 | `hmkholdings@hmkholdings.com` 수신 가능 여부 | 전 페이지 |
| 4 | Before/After 이미지 수치 | 이미지 3.3배 vs 본문 450% — 기준 통일 권장 | 메인, 공간수익화 |
| 5 | HMK 투자안내 사이트 | `hmkinvestment.pages.dev` — 이번 그룹사 목록에는 없어 `/sites/` 그룹 채널에만 유지 | `/sites/`, `/model/liquidity/` |

## 6. 내용 수정

- **문구** → 해당 `index.html` 직접 수정 후 커밋
- **검색 제목·설명** → `_generator/seo.py` 수정 후 `cd _generator && python3 gen.py`
- **구조 변경** → `_generator/c_*.py` 수정 후 동일하게 실행

© 2026 HMK HOLDINGS GROUP
