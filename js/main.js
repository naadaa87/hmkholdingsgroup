(function () {
  "use strict";
  var d = document;

  /* 헤더 — 스크롤 시 유틸리티 접힘 */
  var onScroll = function () { d.body.classList.toggle("stuck", window.scrollY > 30); };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* 모바일 드로어 */
  var toggle = d.querySelector(".nav-toggle"),
      drawer = d.querySelector(".drawer"),
      close = d.querySelector(".dclose");
  var setDrawer = function (open) {
    if (!drawer) return;
    drawer.hidden = !open;
    d.body.style.overflow = open ? "hidden" : "";
    if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
  };
  if (toggle) toggle.addEventListener("click", function () { setDrawer(drawer.hidden); });
  if (close) close.addEventListener("click", function () { setDrawer(false); });
  d.addEventListener("keydown", function (e) { if (e.key === "Escape") setDrawer(false); });

  Array.prototype.forEach.call(d.querySelectorAll(".dsec > button"), function (b) {
    b.addEventListener("click", function () {
      var sec = b.parentElement, open = sec.classList.toggle("open");
      b.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  /* GNB 드롭다운 — 터치·키보드 */
  Array.prototype.forEach.call(d.querySelectorAll(".gnb > li"), function (li) {
    var link = li.querySelector(".gnb-link");
    if (!li.querySelector(".dropdown")) return;
    link.addEventListener("click", function (e) {
      if (window.matchMedia("(hover: none)").matches) {
        if (!li.classList.contains("open")) { e.preventDefault(); }
        Array.prototype.forEach.call(d.querySelectorAll(".gnb > li.open"), function (o) {
          if (o !== li) o.classList.remove("open");
        });
        li.classList.toggle("open");
      }
    });
  });
  d.addEventListener("click", function (e) {
    if (!e.target.closest(".gnb")) {
      Array.prototype.forEach.call(d.querySelectorAll(".gnb > li.open"), function (o) { o.classList.remove("open"); });
    }
  });

  /* 스크롤 리빌 — 한 번 나타나면 유지 */
  var rv = d.querySelectorAll(".rv");
  if ("IntersectionObserver" in window && rv.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px 12% 0px", threshold: 0.01 });
    Array.prototype.forEach.call(rv, function (el, i) {
      el.style.transitionDelay = (Math.min(i % 4, 3) * 70) + "ms";
      io.observe(el);
    });
    /* 안전장치 — 빠른 스크롤로 지나친 요소도 반드시 표시 */
    var sweep = function () {
      var vh = window.innerHeight;
      Array.prototype.forEach.call(rv, function (el) {
        if (!el.classList.contains("in") && el.getBoundingClientRect().top < vh) el.classList.add("in");
      });
    };
    window.addEventListener("scroll", sweep, { passive: true });
    window.addEventListener("load", sweep);
  } else {
    Array.prototype.forEach.call(rv, function (el) { el.classList.add("in"); });
  }

  /* 연도 */
  Array.prototype.forEach.call(d.querySelectorAll("[data-year]"), function (el) {
    el.textContent = new Date().getFullYear();
  });


  /* 뉴스 분류 필터 */
  var nf = d.querySelector(".news-filter");
  if (nf) {
    var cards = d.querySelectorAll("#news-list .post-card");
    Array.prototype.forEach.call(nf.querySelectorAll(".chip"), function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.getAttribute("data-cat");
        Array.prototype.forEach.call(nf.querySelectorAll(".chip"), function (b) {
          var on = b === btn;
          b.classList.toggle("on", on);
          b.setAttribute("aria-pressed", on ? "true" : "false");
        });
        Array.prototype.forEach.call(cards, function (c) {
          c.hidden = !(cat === "all" || c.getAttribute("data-cat") === cat);
        });
      });
    });
  }

  /* 문의 폼 */
  var form = d.getElementById("contact-form");
  if (form) {
    var typeInputs = form.querySelectorAll('input[name="ctype"]');
    var groups = form.querySelectorAll(".fgroup");
    var qs = new URLSearchParams(window.location.search).get("type");
    if (qs) {
      var pre = form.querySelector('input[name="ctype"][value="' + qs + '"]');
      if (pre) pre.checked = true;
    }
    var sync = function () {
      var v = form.querySelector('input[name="ctype"]:checked').value;
      Array.prototype.forEach.call(groups, function (g) {
        g.classList.toggle("on", g.getAttribute("data-for") === v);
      });
    };
    Array.prototype.forEach.call(typeInputs, function (i) { i.addEventListener("change", sync); });
    sync();

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = d.getElementById("form-msg");
      var name = d.getElementById("f-name").value.trim();
      var phone = d.getElementById("f-phone").value.trim();
      var body = d.getElementById("f-body").value.trim();
      var agree = d.getElementById("f-agree").checked;
      if (!name || !phone || !body) { msg.textContent = "이름·연락처·문의 내용을 입력해 주세요."; msg.className = "form-msg err"; return; }
      if (!agree) { msg.textContent = "개인정보 수집·이용에 동의해 주세요."; msg.className = "form-msg err"; return; }
      var checked = form.querySelector('input[name="ctype"]:checked');
      var label = checked.getAttribute("data-label");
      var lines = ["[문의 유형] " + label, "[이름] " + name, "[연락처] " + phone];
      var email = d.getElementById("f-email").value.trim();
      if (email) lines.push("[이메일] " + email);
      var g = form.querySelector('.fgroup[data-for="' + checked.value + '"]');
      if (g) {
        Array.prototype.forEach.call(g.querySelectorAll("input,select"), function (el) {
          if (el.value) lines.push("[" + el.getAttribute("data-label") + "] " + el.value);
        });
      }
      lines.push("", "[문의 내용]", body);
      window.location.href = "mailto:hmkholdings@hmkholdings.com?subject=" +
        encodeURIComponent("[홈페이지 문의] " + label + " - " + name) +
        "&body=" + encodeURIComponent(lines.join("\n"));
      msg.textContent = "메일 작성창이 열립니다. 전송까지 완료해 주세요.";
      msg.className = "form-msg ok";
    });
  }
})();
