(() => {
  'use strict';
  const path = window.location.pathname || '';
  const isInWebsiteFolder = /\/website(?:\/|$)/.test(path);

  // Reuse repository-root artwork when the site is viewed in the repo. The
  // self-contained SVG illustrations are used when the repository assets are
  // unavailable (for example, when this folder is previewed on its own).
  document.querySelectorAll('[data-root-src]').forEach((element) => {
    if (!isInWebsiteFolder) element.setAttribute('src', element.dataset.rootSrc);
  });
  document.querySelectorAll('link[data-root-href]').forEach((element) => {
    if (!isInWebsiteFolder) element.setAttribute('href', element.dataset.rootHref);
  });
  document.querySelectorAll('img[data-fallback], link[data-fallback]').forEach((element) => {
    const fallback = element.dataset.fallback;
    if (!fallback) return;
    const swapToFallback = () => {
      if (element.dataset.fallbackUsed === 'true') return;
      element.dataset.fallbackUsed = 'true';
      if (element.tagName === 'LINK') element.setAttribute('href', fallback);
      else element.setAttribute('src', fallback);
    };
    element.addEventListener('error', swapToFallback);
    // Handle resources that failed before the deferred script attached its listener.
    if (element.tagName === 'IMG' && element.complete && element.naturalWidth === 0) swapToFallback();
  });

  // Mark the active page explicitly, including when a page is opened directly.
  const activePage = document.body.dataset.page;
  document.querySelectorAll('.nav-link[data-nav]').forEach((link) => {
    if (link.dataset.nav === activePage) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });

  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav');
  const closeMenu = () => {
    if (!toggle || !nav) return;
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
  };
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      nav.classList.toggle('is-open', open);
    });
    nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', (event) => { if (event.key === 'Escape') closeMenu(); });
    window.addEventListener('resize', () => { if (window.innerWidth > 820) closeMenu(); });
  }

  const year = document.querySelector('[data-year]');
  if (year) year.textContent = String(new Date().getFullYear());
})();
