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

## 3. SEO 구성 내역

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
