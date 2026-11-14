// Version selector of the MOCAP4ROS2 site, from /versions.json (scripts/build_site.py).
(function () {
  'use strict';
  const parts = window.location.pathname.split('/').filter(Boolean);
  if (!parts.length) {
    return;
  }
  fetch('/versions.json').then((r) => (r.ok ? r.json() : null)).then((data) => {
    if (!data) {
      return;
    }
    const current = parts[0];
    const known = data.versions.map((v) => v.name);
    if (!known.includes(current)) {
      return;
    }
    const select = document.createElement('select');
    select.className = 'mocap4r2-version';
    select.setAttribute('aria-label', 'Documentation version');
    for (const v of data.versions) {
      const o = document.createElement('option');
      o.value = v.name;
      o.textContent = v.title;
      o.selected = v.name === current;
      select.appendChild(o);
    }
    select.addEventListener('change', () => {
      const rest = parts.slice(1).join('/');
      const target = `/${select.value}/${rest}`;
      fetch(target, {method: 'HEAD'}).then((r) => {
        window.location.href = r.ok ? target : `/${select.value}/`;
      });
    });
    const host = document.querySelector('.sy-head-brand, .sy-head-inner, header') || document.body;
    host.appendChild(select);
  });
})();
