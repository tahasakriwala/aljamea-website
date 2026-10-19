/* Aljamea-tus-Saifiyah — interaction & motion. No dependencies.
   Every scroll scene reads one rAF-throttled scroll position; everything degrades to static
   content when JavaScript is off or prefers-reduced-motion is set. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const desktop = () => matchMedia('(min-width: 861px)').matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));

  /* ---------- preloader (once per session) ---------- */
  const finishLoad = () => {
    root.classList.add('loaded');
    try { sessionStorage.setItem('ajs-seen', '1'); } catch (e) {}
    setTimeout(() => $('#loader')?.remove(), 1400);
    $$('.hero .split').forEach(el => el.classList.add('in'));
  };
  if (root.classList.contains('seen')) { $('#loader')?.remove(); requestAnimationFrame(() => $$('.hero .split').forEach(el => el.classList.add('in'))); }
  else { window.addEventListener('load', () => setTimeout(finishLoad, 1500)); setTimeout(finishLoad, 4000); }

  /* ---------- theme ---------- */
  $$('[data-theme-toggle]').forEach(b => b.addEventListener('click', () => {
    const dark = root.dataset.theme === 'dark' || (!root.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('ajs-theme', root.dataset.theme); } catch (e) {}
  }));

  /* ---------- split text into words ---------- */
  $$('[data-split]').forEach(el => {
    let i = 0;
    const walk = node => [...node.childNodes].forEach(n => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(part => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.append(part); return; }
          const w = document.createElement('span'); w.className = 'w';
          const inner = document.createElement('span'); inner.textContent = part; inner.style.setProperty('--i', i++);
          w.append(inner); frag.append(w);
        });
        n.replaceWith(frag);
      } else if (n.nodeType === 1 && !n.classList.contains('hon')) walk(n);
    });
    walk(el);
    el.classList.add(el.dataset.split === 'scrub' ? 'scrub' : 'split');
  });

  /* ---------- reveal on view ---------- */
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { rootMargin: '0px 0px -12% 0px', threshold: .01 });
  $$('[data-reveal], .split:not(.hero .split), [data-steps], .tl-item').forEach(el => io.observe(el));

  /* ---------- counters ---------- */
  const fmt = (v, dec) => dec ? v.toFixed(dec) : Math.round(v).toLocaleString('en-US');
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target, to = parseFloat(el.dataset.count), dec = (el.dataset.count.split('.')[1] || '').length;
    cio.unobserve(el);
    if (reduce) { el.textContent = fmt(to, dec); return; }
    const t0 = performance.now(), dur = 2000;
    const tick = t => { const k = clamp((t - t0) / dur); el.textContent = fmt(to * (1 - Math.pow(1 - k, 4)), dec); if (k < 1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  }), { threshold: .4 });
  $$('[data-count]').forEach(el => cio.observe(el));

  /* ---------- header, progress, to-top ---------- */
  const hdr = $('#hdr'), prog = $('.progress'), top = $('.to-top');
  let lastY = 0;

  /* ---------- scroll scenes ---------- */
  const scenes = [];
  const progressOf = el => { const r = el.getBoundingClientRect(); return clamp(-r.top / (r.height - innerHeight)); };

  // 1. The Hive: a honeycomb of cells, each a window onto one photograph. The comb ripples in on load,
  //    swells under the cursor, and on scroll grows outward until the gaps close into a single image.
  const hero = $('.hero');
  if (hero) {
    const pin = $('.hero-pin'), hive = $('.hive'), lines = $('.hive-lines');
    const slides = JSON.parse(hive.dataset.slides).map(sl => Object.assign(sl, { w: 2560, h: 1707 }));
    let cur = 0;
    let cells = [], W = 0, H = 0, ox = 0, oy = 0, diag = 1, intro = reduce ? 1 : 0, mx = -9999, my = -9999;
    const build = () => {
      W = innerWidth; H = innerHeight;
      const r = W < 700 ? 46 : W < 1100 ? 62 : 74, w = Math.sqrt(3) * r;  // pointy-top hexagon
      const bw = w * 1.1, bh = 2 * r * 1.1;
      ox = W < 861 ? W * .5 : W * .7; oy = W < 861 ? H * .42 : H * .52;    // where the comb grows from
      diag = Math.hypot(Math.max(ox, W - ox), Math.max(oy, H - oy));
      hive.innerHTML = ''; cells = [];
      let path = '';
      for (let row = -1, y = -r; y < H + 2 * r; row++, y = row * 1.5 * r) {
        for (let x = (row & 1) ? w / 2 : 0; x < W + w; x += w) {
          const c = document.createElement('i');
          c.style.cssText = `left:${(x - bw / 2).toFixed(1)}px;top:${(y - bh / 2).toFixed(1)}px;width:${bw.toFixed(1)}px;height:${bh.toFixed(1)}px`;
          hive.append(c);
          const cell = { el: c, x, y, bw, bh, d: Math.hypot(x - ox, y - oy), k: -1 };
          dress(cell, slides[cur]); cells.push(cell);
          const pts = [[0, -r], [w / 2, -r / 2], [w / 2, r / 2], [0, r], [-w / 2, r / 2], [-w / 2, -r / 2]];
          path += 'M' + pts.map(([a, b]) => `${(x + a).toFixed(1)} ${(y + b).toFixed(1)}`).join('L') + 'Z';
        }
      }
      lines.setAttribute('viewBox', `0 0 ${W} ${H}`);
      lines.innerHTML = `<path d="${path}"/>`;
      paint();
    };
    // each cell shows its own slice of the photograph, so together the cells form one image
    function dress(c, sl) {
      const sc = Math.max(W / sl.w, H / sl.h), bgW = sl.w * sc, bgH = sl.h * sc;
      const offX = (W - bgW) / 2, offY = (H - bgH) / 2;
      c.el.style.setProperty('--src', `url("${sl.src}")`);
      c.el.style.backgroundSize = `100% 100%,${bgW.toFixed(0)}px ${bgH.toFixed(0)}px`;
      c.el.style.backgroundPosition = `0 0,${(offX - c.x + c.bw / 2).toFixed(1)}px ${(offY - c.y + c.bh / 2).toFixed(1)}px`;
    }
    slides.forEach(sl => { const im = new Image(); im.onload = () => { sl.w = im.naturalWidth; sl.h = im.naturalHeight; if (sl === slides[cur]) cells.forEach(c => dress(c, sl)); }; im.src = sl.src; });
    // slideshow: the comb flips cell by cell in a ripple from the centre, revealing the next scene
    const cap = $('[data-cap]'), dots = $$('.hero-dots button');
    let timer;
    const go = n => {
      const next = (n + slides.length) % slides.length, sl = slides[next];
      if (next === cur) return;
      cur = next;
      cells.forEach(c => {
        const delay = c.d * .6 + Math.random() * 90;
        setTimeout(() => { c.el.classList.add('flip'); setTimeout(() => { dress(c, sl); c.el.classList.remove('flip'); }, 330); }, delay);
      });
      cap.classList.add('swap');
      setTimeout(() => { cap.textContent = sl.label; cap.href = sl.url; cap.classList.remove('swap'); }, 400);
      dots.forEach((d, i) => { d.classList.remove('on'); d.classList.toggle('done', i < cur); });
      void hero.offsetWidth; dots[cur].classList.add('on');
      schedule();
    };
    // the bar and the photo share one clock: when a bar fills, the next scene always arrives
    const DUR = 4000;
    hero.style.setProperty('--slide', DUR + 'ms');
    const schedule = () => { clearTimeout(timer); if (!reduce) timer = setTimeout(() => go(cur + 1), DUR); };
    // pause (bar included) only while the hero is off screen or the tab is hidden
    const pauseIf = () => {
      const off = document.hidden || progressOf(hero) > .55;
      hero.classList.toggle('paused', off);
      if (off) clearTimeout(timer); else if (hero.dataset.wasOff === '1') { dots[cur].classList.remove('on'); void hero.offsetWidth; dots[cur].classList.add('on'); schedule(); }
      hero.dataset.wasOff = off ? '1' : '0';
    };
    document.addEventListener('visibilitychange', pauseIf);
    scenes.push(pauseIf);
    dots.forEach((d, i) => d.addEventListener('click', () => go(i)));
    schedule();
    const paint = () => {
      const p = progressOf(hero), e = 1 - Math.pow(1 - clamp(p / .78), 3);
      const R = (diag * .34) * intro + diag * 1.15 * e, fall = 210, kmax = .9 + .14 * e;
      cells.forEach(c => {
        let k = clamp((R - c.d) / fall) * kmax;
        const hover = Math.hypot(c.x - mx, c.y - my);
        if (hover < 170 && e < .9) k = Math.max(k, (1 - hover / 170) * .95 * (1 - e));
        k = Math.round(k * 100) / 100;
        if (k !== c.k) { c.k = k; c.el.style.setProperty('--k', k); }
      });
      pin.style.setProperty('--p', p.toFixed(4));
      pin.style.setProperty('--e', e.toFixed(4));
    };
    build();
    addEventListener('resize', () => { clearTimeout(build.t); build.t = setTimeout(build, 150); });
    if (!reduce) {
      pin.addEventListener('pointermove', ev => { mx = ev.clientX; my = ev.clientY; requestAnimationFrame(paint); });
      pin.addEventListener('pointerleave', () => { mx = my = -9999; requestAnimationFrame(paint); });
      const t0 = performance.now() + (root.classList.contains('seen') ? 100 : 1500);
      const grow = t => { intro = clamp((t - t0) / 1800); intro = 1 - Math.pow(1 - intro, 3); paint(); if (intro < 1) requestAnimationFrame(grow); };
      requestAnimationFrame(grow);
    }
    scenes.push(paint);
  }

  // 2. Journey map: route draws itself, one stop per slice of scroll
  const jr = $('.journey');
  if (jr) {
    const route = $('.route', jr), len = route.getTotalLength(), cards = $$('.j-card', jr), pts = $$('.pt', jr), dots = $$('.j-dots i', jr);
    const stopsAt = JSON.parse(jr.dataset.stops);
    route.style.strokeDasharray = len; route.style.strokeDashoffset = len;
    let cur = -1;
    scenes.push(() => {
      if (!desktop()) { route.style.strokeDashoffset = 0; pts.forEach(p => p.classList.add('done')); return; }
      const p = progressOf(jr), n = cards.length, idx = Math.min(n - 1, Math.floor(p * n * .999));
      const local = clamp(p * (n - 1) / .9, 0, n - 1);
      const seg = Math.floor(local), f = local - seg;
      const at = stopsAt[Math.min(seg, n - 1)] + ((stopsAt[Math.min(seg + 1, n - 1)] - stopsAt[Math.min(seg, n - 1)]) * clamp(f * 1.6));
      route.style.strokeDashoffset = (len * (1 - at)).toFixed(1);
      if (idx !== cur) {
        cur = idx;
        cards.forEach((c, i) => c.classList.toggle('on', i === idx));
        dots.forEach((d, i) => d.classList.toggle('on', i <= idx));
        pts.forEach(pt => { const k = +pt.dataset.k; pt.classList.toggle('done', k <= idx); pt.classList.toggle('on', k === idx); });
      }
    });
  }

  // 3. Campus rail: vertical scroll drives a horizontal track
  const railWrap = $('.rail-wrap');
  if (railWrap) scenes.push(() => {
    if (!desktop()) return;
    const rail = $('.rail', railWrap), p = progressOf(railWrap);
    const max = rail.scrollWidth - innerWidth;
    rail.style.setProperty('--x', `${(-max * clamp((p - .05) / .9)).toFixed(1)}px`);
  });

  // 4. Word-by-word scrub
  const scrubs = $$('.scrub');
  if (scrubs.length) scenes.push(() => scrubs.forEach(el => {
    const r = el.getBoundingClientRect(), ws = $$('.w', el);
    const p = clamp((innerHeight * .85 - r.top) / (r.height + innerHeight * .35));
    const lit = Math.round(p * ws.length);
    ws.forEach((w, i) => w.classList.toggle('lit', i < lit));
  }));

  // 5. Timeline fill + current era
  const tl = $('.tl');
  if (tl) {
    const items = $$('.tl-item', tl), era = $('.era span');
    scenes.push(() => {
      const r = tl.getBoundingClientRect();
      tl.style.setProperty('--tp', clamp((innerHeight * .6 - r.top) / r.height).toFixed(4));
      let label = items[0]?.dataset.era;
      items.forEach(it => { if (it.getBoundingClientRect().top < innerHeight * .5) label = it.dataset.era; });
      if (era && label && era.textContent !== label) era.textContent = label;
    });
  }

  // 6. Parallax banners and campus hero zoom
  const pars = $$('.banner img');
  if (pars.length) scenes.push(() => pars.forEach(img => {
    const r = img.parentElement.getBoundingClientRect();
    if (r.bottom < 0 || r.top > innerHeight) return;
    img.style.setProperty('--py', `${((r.top + r.height / 2 - innerHeight / 2) * -.12).toFixed(1)}px`);
  }));
  const ch = $('.c-hero');
  if (ch) scenes.push(() => ch.style.setProperty('--p', clamp(scrollY / innerHeight).toFixed(3)));

  // 7. Sticky table of contents
  const toc = $$('.toc a');
  if (toc.length) {
    const targets = toc.map(a => $(a.getAttribute('href'))).filter(Boolean);
    scenes.push(() => {
      let on = 0;
      targets.forEach((t, i) => { if (t.getBoundingClientRect().top < innerHeight * .35) on = i; });
      toc.forEach((a, i) => a.classList.toggle('on', i === on));
    });
  }

  let ticking = false;
  const frame = () => {
    ticking = false;
    const y = scrollY, h = document.body.scrollHeight - innerHeight;
    hdr?.classList.toggle('scrolled', y > 20);
    hdr?.classList.toggle('hide', y > lastY && y > 400 && !$('#menu.open'));
    lastY = y;
    const p = h > 0 ? y / h : 0;
    prog?.style.setProperty('--p', p.toFixed(4));
    if (top) { top.classList.toggle('on', y > innerHeight); top.style.setProperty('--p', p.toFixed(4)); }
    if (!reduce) scenes.forEach(s => s());
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  frame();
  if (reduce) { scenes.forEach(s => { try { s(); } catch (e) {} }); }
  top?.addEventListener('click', () => scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }));

  /* ---------- menu ---------- */
  const menu = $('#menu');
  const setMenu = open => {
    menu.classList.toggle('open', open);
    menu.setAttribute('aria-hidden', !open);
    document.body.style.overflow = open ? 'hidden' : '';
    $$('[data-menu]').forEach(b => b.setAttribute('aria-expanded', open));
    if (open) setTimeout(() => $('a', menu)?.focus(), 400);
  };
  $$('[data-menu]').forEach(b => b.addEventListener('click', () => setMenu(!menu.classList.contains('open'))));

  /* ---------- the eleven steps ---------- */
  $$('[data-ladder]').forEach(l => {
    const tabs = $$('[role="tab"]', l), panels = $$('.stage-panel', l), steps = $$('.step', l);
    const show = n => {
      tabs.forEach(t => t.setAttribute('aria-selected', t.dataset.stage === n));
      panels.forEach(p => p.classList.toggle('on', p.dataset.stage === n));
      steps.forEach(s => s.classList.toggle('on', s.dataset.stage === n));
    };
    tabs.forEach(t => t.addEventListener('click', () => show(t.dataset.stage)));
    steps.forEach(s => s.addEventListener('click', () => show(s.dataset.stage)));
    l.addEventListener('keydown', e => {
      const i = tabs.findIndex(t => t.getAttribute('aria-selected') === 'true');
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
        const n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length]; n.focus(); show(n.dataset.stage);
      }
    });
  });

  /* ---------- faculty flower ---------- */
  $$('[data-flower]').forEach(fl => {
    io.observe(fl);
    const info = fl.parentElement.querySelector('.flower-info');
    const set = h => {
      info.classList.add('swap');
      setTimeout(() => {
        ['ar', 't', 'd', 'l'].forEach(k => { info.querySelector(`[data-fi="${k}"]`).textContent = h.dataset[k]; });
        info.querySelector('[data-fi="u"]').href = h.href;
        info.classList.remove('swap');
      }, 180);
      $$('.hx', fl).forEach(x => x.classList.toggle('on', x === h));
    };
    $$('.hx', fl).forEach(h => { h.addEventListener('mouseenter', () => set(h)); h.addEventListener('focus', () => set(h)); });
  });

  /* ---------- voices ---------- */
  $$('[data-voices]').forEach(v => {
    const items = $$('.voice', v), btns = $$('.voice-nav button', v);
    let i = 0, t;
    const go = n => { i = n; items.forEach((x, k) => x.classList.toggle('on', k === i));
      btns.forEach((b, k) => { b.classList.remove('on'); void b.offsetWidth; b.classList.toggle('on', k === i); });
      clearTimeout(t); t = setTimeout(() => go((i + 1) % items.length), 7000); };
    btns.forEach((b, k) => b.addEventListener('click', () => go(k)));
    go(0);
  });

  /* ---------- luminary hover peek ---------- */
  const peek = $('.lum-peek');
  if (peek && matchMedia('(hover: hover)').matches) {
    const im = $('img', peek);
    let x = 0, y = 0, tx = 0, ty = 0, raf;
    const loop = () => { x += (tx - x) * .14; y += (ty - y) * .14; peek.style.left = x + 'px'; peek.style.top = y + 'px'; raf = requestAnimationFrame(loop); };
    $$('.lum').forEach(l => {
      l.addEventListener('mouseenter', () => { im.src = l.dataset.img; peek.classList.add('on'); if (!raf) loop(); });
      l.addEventListener('mouseleave', () => peek.classList.remove('on'));
      l.addEventListener('mousemove', e => { tx = e.clientX + 150; ty = e.clientY; });
    });
  }

  /* ---------- card spotlight ---------- */
  $$('.card').forEach(c => c.addEventListener('pointermove', e => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--mx', `${e.clientX - r.left}px`); c.style.setProperty('--my', `${e.clientY - r.top}px`);
  }));

  /* ---------- lightbox ---------- */
  const lb = $('#lb');
  if (lb) {
    let set = [], i = 0;
    const img = $('img', lb), count = $('.count', lb);
    const show = n => { i = (n + set.length) % set.length; img.src = set[i].dataset.full; img.alt = set[i].querySelector('img').alt; count.textContent = `${i + 1} / ${set.length}`; };
    $$('[data-gal]').forEach(g => $$('button', g).forEach((b, k) => b.addEventListener('click', () => {
      set = $$('button', g); show(k); lb.classList.add('open'); lb.setAttribute('aria-hidden', 'false'); $('.x', lb).focus();
    })));
    const close = () => { lb.classList.remove('open'); lb.setAttribute('aria-hidden', 'true'); };
    $('.x', lb).addEventListener('click', close);
    $('.prev', lb).addEventListener('click', () => show(i - 1));
    $('.next', lb).addEventListener('click', () => show(i + 1));
    lb.addEventListener('click', e => { if (e.target === lb) close(); });
    addEventListener('keydown', e => {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close(); if (e.key === 'ArrowRight') show(i + 1); if (e.key === 'ArrowLeft') show(i - 1);
    });
  }

  /* ---------- search (⌘K or /) ---------- */
  const ck = $('#cmdk'), q = $('#cmdk-q'), list = $('#cmdk-list');
  let index = null, sel = 0;
  const norm = s => s.normalize('NFD').replace(/[̀-ͯʿʾʻ’']/g, '').toLowerCase();
  const render = () => {
    const t = norm(q.value.trim());
    const hits = (index || []).filter(x => !t || norm(x.t + ' ' + x.g).includes(t) || (x.a || '').includes(q.value.trim())).slice(0, 12);
    sel = Math.min(sel, Math.max(0, hits.length - 1));
    list.innerHTML = hits.length ? hits.map((h, k) => `<li><a href="${h.u}" class="${k === sel ? 'sel' : ''}"><span>${h.t}</span><span class="g">${h.g}</span></a></li>`).join('')
      : '<li class="empty">Nothing found. Try “library”, “Nairobi” or “Fiqh”.</li>';
  };
  const openSearch = async () => {
    ck.classList.add('open'); q.value = ''; sel = 0; q.focus();
    if (!index) { try { index = await (await fetch(window.AJS.search)).json(); } catch (e) { index = []; } }
    render();
  };
  const closeSearch = () => ck.classList.remove('open');
  $$('[data-search]').forEach(b => b.addEventListener('click', openSearch));
  ck?.addEventListener('click', e => { if (e.target === ck) closeSearch(); });
  q?.addEventListener('input', () => { sel = 0; render(); });
  q?.addEventListener('keydown', e => {
    const a = $$('a', list);
    if (e.key === 'ArrowDown') { sel = Math.min(a.length - 1, sel + 1); render(); e.preventDefault(); }
    if (e.key === 'ArrowUp') { sel = Math.max(0, sel - 1); render(); e.preventDefault(); }
    if (e.key === 'Enter' && a[sel]) location.href = a[sel].href;
  });
  addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); ck.classList.contains('open') ? closeSearch() : openSearch(); }
    else if (e.key === '/' && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); openSearch(); }
    else if (e.key === 'Escape') { closeSearch(); if (menu?.classList.contains('open')) setMenu(false); }
  });
})();
