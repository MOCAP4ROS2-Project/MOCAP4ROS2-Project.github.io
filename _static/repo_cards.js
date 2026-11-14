// Stars and forks of the repository cards in the right sidebar (cached per session).
(function () {
  'use strict';
  const fill = (card, s) => {
    card.querySelector('[data-stars]').textContent = s.stars;
    card.querySelector('[data-forks]').textContent = s.forks;
  };
  document.querySelectorAll('.mocap4r2-repo[data-repo]').forEach((card) => {
    const repo = card.dataset.repo;
    const key = `mocap4r2/repo/${repo}`;
    try {
      const cached = sessionStorage.getItem(key);
      if (cached) {
        fill(card, JSON.parse(cached));
        return;
      }
    } catch (e) { /* storage unavailable */ }
    fetch(`https://api.github.com/repos/MOCAP4ROS2-Project/${repo}`)
      .then((r) => (r.ok ? r.json() : null))
      .then((d) => {
        if (!d) {
          return;
        }
        const s = {stars: d.stargazers_count, forks: d.forks_count};
        fill(card, s);
        try {
          sessionStorage.setItem(key, JSON.stringify(s));
        } catch (e) { /* storage unavailable */ }
      })
      .catch(() => {});
  });
})();
