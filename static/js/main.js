(function () {
  "use strict";

  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ============================================================ */
  /* Page load-in                                                   */
  /* ============================================================ */
  document.body.classList.remove("pre-load");
  requestAnimationFrame(() => document.body.classList.add("is-loaded"));

  /* ============================================================ */
  /* Mobile nav toggle                                              */
  /* ============================================================ */
  const navToggle = document.getElementById("navToggle");
  const navLinks = document.getElementById("navLinks");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      const isOpen = navLinks.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });
    navLinks.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        navLinks.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  /* ============================================================ */
  /* Scroll progress bar                                            */
  /* ============================================================ */
  const progressBar = document.getElementById("scrollProgress");
  function updateProgress() {
    const doc = document.documentElement;
    const scrollTop = doc.scrollTop || document.body.scrollTop;
    const height = doc.scrollHeight - doc.clientHeight;
    const pct = height > 0 ? (scrollTop / height) * 100 : 0;
    if (progressBar) progressBar.style.width = pct + "%";
  }
  document.addEventListener("scroll", updateProgress, { passive: true });
  updateProgress();

  /* ============================================================ */
  /* Scroll reveal (IntersectionObserver)                           */
  /* ============================================================ */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reducedMotion) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  /* ============================================================ */
  /* Animated stat counters                                         */
  /* ============================================================ */
  const statEls = document.querySelectorAll(".stat-value");
  function animateCount(el) {
    const target = parseFloat(el.getAttribute("data-count")) || 0;
    const decimals = parseInt(el.getAttribute("data-decimals"), 10) || 0;
    const suffix = el.getAttribute("data-suffix") || "";
    const duration = 1200;
    const start = performance.now();
    function tick(now) {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3); // ease-out-cubic
      const value = target * eased;
      el.textContent = value.toFixed(decimals) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    if (reducedMotion) {
      el.textContent = target.toFixed(decimals) + suffix;
    } else {
      requestAnimationFrame(tick);
    }
  }
  if (statEls.length && "IntersectionObserver" in window) {
    const statIo = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            statIo.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    statEls.forEach((el) => statIo.observe(el));
  } else {
    statEls.forEach(animateCount);
  }

  /* ============================================================ */
  /* Tilt cards (pointer-follow 3D tilt)                            */
  /* ============================================================ */
  if (!reducedMotion) {
    document.querySelectorAll(".tilt-card").forEach((card) => {
      const maxTilt = 5; // degrees
      card.addEventListener("mousemove", (e) => {
        const rect = card.getBoundingClientRect();
        const px = (e.clientX - rect.left) / rect.width - 0.5;
        const py = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.setProperty("--rx", (px * maxTilt * 2).toFixed(2) + "deg");
        card.style.setProperty("--ry", (-py * maxTilt * 2).toFixed(2) + "deg");
      });
      card.addEventListener("mouseleave", () => {
        card.style.setProperty("--rx", "0deg");
        card.style.setProperty("--ry", "0deg");
      });
    });
  }

  /* ============================================================ */
  /* Ticker (home page only)                                        */
  /* ============================================================ */
  const tickerTrack = document.getElementById("tickerTrack");
  if (tickerTrack) {
    try {
      const items = JSON.parse(tickerTrack.getAttribute("data-ticker") || "[]");
      const build = () =>
        items
          .map(
            (t) => `
        <span class="ticker-item">
          <span class="${t.tag}">●</span> ${t.html}
          <span style="color:var(--text-faint)">— ${t.src}</span>
        </span>`
          )
          .join("");
      tickerTrack.innerHTML = build() + build(); // duplicate for seamless loop
    } catch (e) {
      /* no ticker data on this page */
    }
  }

  /* ============================================================ */
  /* Page transitions between internal routes                       */
  /* ============================================================ */
  const internalLinks = document.querySelectorAll("a[data-internal]");
  internalLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      const url = link.getAttribute("href");
      if (!url || link.target === "_blank") return;
      // allow modified clicks (new tab, etc.) to behave normally
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

      e.preventDefault();
      if (reducedMotion) {
        window.location.href = url;
        return;
      }
      document.body.classList.remove("is-loaded");
      document.body.classList.add("is-leaving");
      setTimeout(() => {
        window.location.href = url;
      }, 260);
    });
  });
})();
