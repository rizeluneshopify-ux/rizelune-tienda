/* Rizelune — interacciones propias */
(function () {
  if (window.rzLoaded) return;
  window.rzLoaded = true;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function initReveal() {
    var els = document.querySelectorAll('.rz-reveal:not(.rz-visible)');
    if (!els.length) return;
    if (reduce || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('rz-visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('rz-visible'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  function initParallax() {
    var imgs = document.querySelectorAll('[data-rz-parallax]');
    if (!imgs.length || reduce) return;
    var ticking = false;
    function update() {
      imgs.forEach(function (img) {
        var k = parseFloat(img.getAttribute('data-rz-parallax')) || 0;
        var r = img.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > window.innerHeight) return;
        img.style.setProperty('--rz-parallax', (-r.top * k / 100).toFixed(1) + 'px');
      });
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  function initCounters() {
    var nums = document.querySelectorAll('[data-rz-count]');
    if (!nums.length) return;
    function run(el) {
      var target = parseFloat(el.getAttribute('data-rz-count')) || 0;
      if (reduce) { el.textContent = target; return; }
      var start = null, dur = 1600;
      function step(t) {
        if (!start) start = t;
        var p = Math.min((t - start) / dur, 1);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }
    if (!('IntersectionObserver' in window)) { nums.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { run(e.target); io.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    nums.forEach(function (n) { io.observe(n); });
  }

  function initGallery() {
    document.querySelectorAll('[data-rz-gallery]').forEach(function (g) {
      var main = g.querySelector('[data-rz-main]');
      if (!main) return;
      var vid = g.querySelector('[data-rz-main-video]');
      g.querySelectorAll('[data-rz-thumb]').forEach(function (btn) {
        btn.addEventListener('click', function () {
          g.querySelectorAll('[data-rz-thumb]').forEach(function (b) { b.classList.remove('is-active'); });
          btn.classList.add('is-active');
          var vsrc = btn.getAttribute('data-video');
          main.style.opacity = 0;
          if (vid) vid.style.opacity = 0;
          setTimeout(function () {
            if (vsrc && vid) {
              main.hidden = true;
              vid.hidden = false;
              if (vid.getAttribute('src') !== vsrc) { vid.poster = btn.getAttribute('data-poster') || ''; vid.src = vsrc; }
              vid.setAttribute('aria-label', btn.getAttribute('data-alt') || '');
              vid.style.opacity = 1;
              var p = vid.play(); if (p && p.catch) p.catch(function () {});
              return;
            }
            if (vid) { vid.pause(); vid.hidden = true; }
            main.hidden = false;
            main.src = btn.getAttribute('data-src');
            main.srcset = '';
            main.alt = btn.getAttribute('data-alt') || '';
            main.style.opacity = 1;
          }, 180);
        });
      });
    });
  }

  function formatMoney(cents, format) {
    var value = (cents / 100).toFixed(2);
    var parts = value.split('.');
    var comma = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ',' + parts[1];
    var dot = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',') + '.' + parts[1];
    return (format || '{{amount_with_comma_separator}} €')
      .replace(/\{\{\s*amount_with_comma_separator\s*\}\}/, comma)
      .replace(/\{\{\s*amount_no_decimals\s*\}\}/, parts[0])
      .replace(/\{\{\s*amount\s*\}\}/, dot);
  }

  function initVariants() {
    document.querySelectorAll('[data-rz-product]').forEach(function (root) {
      var dataEl = root.querySelector('[data-rz-variants]');
      if (!dataEl) return;
      var variants = JSON.parse(dataEl.textContent);
      var format = root.getAttribute('data-money-format');
      var selects = root.querySelectorAll('[data-rz-option]');
      var idInputs = document.querySelectorAll('[data-rz-variant-id]');
      var price = root.querySelectorAll('[data-rz-price]');
      var old = root.querySelectorAll('[data-rz-compare]');
      var buttons = document.querySelectorAll('[data-rz-add]');
      function update() {
        var chosen = Array.prototype.map.call(selects, function (s) { return s.value; });
        var v = variants.find(function (x) {
          return x.options.every(function (o, i) { return o === chosen[i]; });
        });
        buttons.forEach(function (b) {
          b.disabled = !v || !v.available;
          var label = b.querySelector('[data-rz-label]');
          if (label) label.textContent = !v ? b.getAttribute('data-unavailable') : (v.available ? b.getAttribute('data-add') : b.getAttribute('data-soldout'));
        });
        if (!v) return;
        idInputs.forEach(function (i) { i.value = v.id; });
        price.forEach(function (p) { p.textContent = formatMoney(v.price, format); });
        old.forEach(function (o) {
          o.textContent = v.compare_at_price > v.price ? formatMoney(v.compare_at_price, format) : '';
        });
        if (v.featured_image) {
          var main = root.querySelector('[data-rz-main]');
          if (main) { main.src = v.featured_image.src; main.srcset = ''; main.hidden = false; }
          var mv = root.querySelector('[data-rz-main-video]');
          if (mv) { mv.pause(); mv.hidden = true; }
        }
      }
      selects.forEach(function (s) { s.addEventListener('change', update); });
    });
  }

  function initQty() {
    document.querySelectorAll('[data-rz-qty]').forEach(function (q) {
      var input = q.querySelector('input');
      q.querySelectorAll('button').forEach(function (b) {
        b.addEventListener('click', function () {
          var n = parseInt(input.value, 10) || 1;
          n += b.getAttribute('data-step') === 'up' ? 1 : -1;
          input.value = Math.max(1, n);
        });
      });
    });
  }

  function initPacks() {
    document.querySelectorAll('[data-rz-packs]').forEach(function (box) {
      var form = box.closest('product-form');
      var qty = form && form.querySelector('[data-rz-pack-qty]');
      var total = form && form.querySelector('[data-rz-pack-total]');
      var isMain = form && form.querySelector('[data-rz-main-form]');
      box.querySelectorAll('input[type=radio]').forEach(function (r) {
        r.addEventListener('change', function () {
          box.querySelectorAll('.rz-pack').forEach(function (l) { l.classList.toggle('is-active', l.contains(r)); });
          if (qty) qty.value = r.value;
          if (total) total.textContent = '· ' + r.getAttribute('data-price');
          if (isMain) document.querySelectorAll('[data-rz-sticky] [data-rz-price]').forEach(function (p) { p.textContent = r.getAttribute('data-price'); });
        });
        if (r.checked && isMain) document.querySelectorAll('[data-rz-sticky] [data-rz-price]').forEach(function (p) { p.textContent = r.getAttribute('data-price'); });
      });
    });
  }

  function initUpsell() {
    if (window.rzUpsellReady) return;
    window.rzUpsellReady = true;
    document.addEventListener('click', function (e) {
      var b = e.target.closest('[data-rz-upsell]');
      if (!b) return;
      var line = b.getAttribute('data-line');
      var input = document.getElementById('Drawer-quantity-' + line) || document.getElementById('Quantity-' + line);
      if (!input) return;
      b.disabled = true;
      input.value = b.getAttribute('data-qty');
      input.dispatchEvent(new Event('change', { bubbles: true }));
    });
  }

  function initRitual() {
    if (window.rzRitualReady) return;
    window.rzRitualReady = true;
    document.addEventListener('click', function (e) {
      var b = e.target.closest('[data-rz-ritual]');
      if (!b) return;
      e.preventDefault();
      var items;
      try { items = JSON.parse(b.getAttribute('data-items')); } catch (err) { return; }
      var box = b.closest('.rz-ritual__item, .rz-ritual, .rz-packcard, .rz-estrella__body, .rz-quiz__result, .rz-comp__card, .rz-pr__card, .rz-pq__ctas');
      var errBox = box && box.querySelector('[data-rz-ritual-err]');
      var drawer = document.querySelector('cart-drawer');
      var body = { items: items };
      if (drawer && typeof drawer.getSectionsToRender === 'function') {
        body.sections = drawer.getSectionsToRender().map(function (s) { return s.id; });
        body.sections_url = window.location.pathname;
      }
      var url = ((window.routes && window.routes.cart_add_url) || '/cart/add') + '.js';
      b.disabled = true;
      if (errBox) errBox.hidden = true;
      fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(body) })
        .then(function (r) { return r.json(); })
        .then(function (res) {
          if (res.status) throw new Error(res.description || 'error');
          if (drawer && typeof drawer.renderContents === 'function' && res.sections) { drawer.classList.remove('is-empty'); drawer.renderContents(res); }
          else window.location.href = (window.routes && window.routes.cart_url) || '/cart';
          if (typeof publish === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') publish(PUB_SUB_EVENTS.cartUpdate, { source: 'rz-ritual', cartData: res });
        })
        .catch(function () { if (errBox) errBox.hidden = false; })
        .finally(function () { b.disabled = false; });
    });
  }

  function initPopup() {
    var pop = document.querySelector('[data-rz-pop]');
    if (!pop || pop.dataset.ready) return;
    pop.dataset.ready = '1';
    var KEY = 'rz-pop', CART_KEY = 'rz-pop-cart', CART_DAYS = 3;
    function read(k) { try { return JSON.parse(localStorage.getItem(k) || 'null'); } catch (e) { return null; } }
    function save(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
    var subscribed = !!(read(KEY) || {}).ok;
    var form = pop.querySelector('form');
    var err = pop.querySelector('[data-rz-pop-err]');
    var teaser = document.querySelector('[data-rz-pop-open]');
    var excluded = /\/(cart|checkouts?|account|challenge|policies)(\/|$)/.test(location.pathname);
    var lastFocus = null;
    function step(name) {
      pop.querySelectorAll('[data-rz-pop-step]').forEach(function (s) { s.hidden = s.getAttribute('data-rz-pop-step') !== name; });
    }
    function showTeaser(on) {
      if (!teaser) return;
      if (on && !subscribed && !excluded) { teaser.hidden = false; requestAnimationFrame(function () { teaser.classList.add('is-in'); }); }
      else { teaser.classList.remove('is-in'); teaser.hidden = true; }
    }
    function open(ok) {
      if (!pop.hidden) return;
      lastFocus = document.activeElement;
      step(ok ? 'ok' : 'form');
      showTeaser(false);
      pop.hidden = false;
      requestAnimationFrame(function () { pop.classList.add('is-open'); });
      var f = pop.querySelector(ok ? '.rz-pop__code' : 'input[type=email]');
      if (f) setTimeout(function () { f.focus({ preventScroll: true }); }, 300);
    }
    function close() {
      pop.classList.remove('is-open');
      setTimeout(function () { pop.hidden = true; showTeaser(true); }, 350);
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    pop.addEventListener('click', function (e) {
      if (e.target.closest('[data-rz-pop-close]')) close();
      var c = e.target.closest('[data-rz-copy]');
      if (c) {
        var code = c.getAttribute('data-rz-copy');
        var label = c.querySelector('[data-rz-copy-label]');
        var done = function () { if (label) label.textContent = c.getAttribute('data-copied'); };
        if (navigator.clipboard) navigator.clipboard.writeText(code).then(done, done); else done();
      }
    });
    if (teaser) teaser.addEventListener('click', function () { open(false); });
    // Enlaces «Apúntate y llévate un 10 %» (franja de avisos, ficha): abren la ventana; si ya se apuntó, le enseña su código
    document.addEventListener('click', function (e) {
      var l = e.target.closest('[data-rz-pop-link], a[href$="#rz-bienvenida"]');
      if (!l) return;
      e.preventDefault();
      open(subscribed);
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !pop.hidden) close(); });
    if (form) form.addEventListener('submit', function () {
      var btn = form.querySelector('[type=submit]');
      if (btn) setTimeout(function () { btn.disabled = true; }, 0);
    });
    // Al volver de enviar el formulario (Shopify recarga la página con #rz-pop-form)
    if (location.hash === '#rz-pop-form') {
      if (location.search.indexOf('customer_posted=true') > -1) { save(KEY, { ok: 1, t: Date.now() }); subscribed = true; open(true); return; }
      if (pop.querySelector('[data-rz-pop-has-error]')) { open(false); if (err) err.hidden = false; }
    }
    if (subscribed || excluded) return;
    // Botón pequeño en la esquina
    setTimeout(function () { if (pop.hidden) showTeaser(true); }, 2500);
    // Una vez, al añadir al carrito (si no hay ya un pack con descuento), cuando se cierra el carrito
    if (pop.getAttribute('data-after-cart') !== 'true' || typeof subscribe !== 'function' || typeof PUB_SUB_EVENTS === 'undefined') return;
    var pending = false;
    function canAfterCart() {
      var last = read(CART_KEY);
      try { if (sessionStorage.getItem(CART_KEY)) return false; } catch (e) {}
      return !subscribed && !(last && Date.now() - last.t < CART_DAYS * 864e5);
    }
    function markAfterCart() {
      save(CART_KEY, { t: Date.now() });
      try { sessionStorage.setItem(CART_KEY, '1'); } catch (e) {}
    }
    function waitDrawer() {
      var drawer = document.querySelector('cart-drawer');
      if (drawer && drawer.classList.contains('active')) { setTimeout(waitDrawer, 700); return; }
      setTimeout(function () {
        if (drawer && drawer.classList.contains('active')) { waitDrawer(); return; }
        pending = false;
        if (canAfterCart() && pop.hidden) { markAfterCart(); open(false); }
      }, 600);
    }
    subscribe(PUB_SUB_EVENTS.cartUpdate, function (ev) {
      if (!ev || ev.source !== 'product-form' || pending || !canAfterCart()) return;
      fetch('/cart.js', { credentials: 'same-origin' }).then(function (r) { return r.json(); }).then(function (cart) {
        if (!cart.item_count || cart.total_discount > 0) return;
        pending = true;
        setTimeout(waitDrawer, 1200);
      }).catch(function () {});
    });
  }

  function initStickyBuy() {
    var bar = document.querySelector('[data-rz-sticky]');
    var anchor = document.querySelector('[data-rz-buy-anchor]');
    if (!bar || !anchor || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      var e = entries[0];
      var on = !e.isIntersecting && e.boundingClientRect.top < 0;
      bar.classList.toggle('is-shown', on);
      document.body.classList.toggle('rz-sticky-on', on);
    }).observe(anchor);
    var btn = bar.querySelector('[data-rz-sticky-btn]');
    if (btn) btn.addEventListener('click', function () {
      var main = document.querySelector('[data-rz-main-form] [type=submit]');
      if (main) main.click();
    });
  }

  function initQuick() {
    var bar = document.querySelector('[data-rz-quick]');
    if (!bar || bar.getAttribute('data-ready')) return;
    bar.setAttribute('data-ready', '1');
    try { if (sessionStorage.getItem('rz-quick-off')) return; } catch (e) {}
    bar.hidden = false;
    var blocked = [];
    function update() {
      var on = window.scrollY > window.innerHeight * 0.85 && blocked.length === 0 && !document.body.classList.contains('rz-quick-off');
      bar.classList.toggle('is-shown', on);
      document.body.classList.toggle('rz-sticky-on', on);
    }
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          var i = blocked.indexOf(e.target);
          if (e.isIntersecting && i < 0) blocked.push(e.target);
          if (!e.isIntersecting && i >= 0) blocked.splice(i, 1);
        });
        update();
      }, { threshold: 0.12 });
      document.querySelectorAll('.rz-buy, .rz-ofertas, .rz-catalogo, .rz-footer, .footer').forEach(function (b) { io.observe(b); });
    }
    window.addEventListener('scroll', update, { passive: true });
    var close = bar.querySelector('[data-rz-quick-close]');
    if (close) close.addEventListener('click', function () {
      document.body.classList.add('rz-quick-off');
      try { sessionStorage.setItem('rz-quick-off', '1'); } catch (e) {}
      update();
    });
    update();
  }

  /* Test de gotas: 4 preguntas -> gotas, dónde, cómo, tiempo y frecuencia (textos en snippets/rz-quiz.liquid) */
  function initQuiz() {
    var m = document.querySelector('[data-rz-quiz]');
    if (!m || m.getAttribute('data-ready')) return;
    m.setAttribute('data-ready', '1');
    var T = {};
    try { T = JSON.parse(m.querySelector('[data-rz-quiz-txt]').textContent); } catch (e) {}
    var qs = m.querySelectorAll('[data-rz-quiz-q]');
    var res = m.querySelector('[data-rz-quiz-result]');
    var back = m.querySelector('[data-rz-quiz-back]');
    var stepEl = m.querySelector('[data-rz-quiz-step]');
    var bar = m.querySelector('[data-rz-quiz-bar]');
    var ans = {}, cur = 1, lastFocus = null;
    var DROP = '<svg viewBox="0 0 24 24"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg>';
    function q(sel) { return m.querySelector(sel); }
    function show(n) {
      cur = n;
      qs.forEach(function (el) {
        var k = el.getAttribute('data-rz-quiz-q');
        el.hidden = +k !== n;
        el.querySelectorAll('[data-rz-quiz-opt]').forEach(function (o) {
          var sel = ans['q' + k] === o.getAttribute('data-rz-quiz-opt');
          o.classList.toggle('is-sel', sel);
          o.setAttribute('aria-pressed', sel ? 'true' : 'false');
        });
      });
      res.hidden = n !== 5;
      back.hidden = n === 1;
      stepEl.textContent = n <= 4 ? String(T.step || '').replace('[n]', n) : '';
      bar.style.width = ((n - 1) / 4 * 100) + '%';
      var panel = q('.rz-quiz__panel'); if (panel) panel.scrollTop = 0;
      var f = n <= 4 ? q('[data-rz-quiz-q="' + n + '"] [data-rz-quiz-opt]') : q('.rz-quiz__eyebrow');
      if (f) try { f.focus({ preventScroll: true }); } catch (e) { f.focus(); }
    }
    function compute() {
      var zone = ans.q1, tipo = ans.q2, grosor = ans.q3, cuero = ans.q4;
      var local = zone === 'a' || zone === 'b' || zone === 'c';
      var g = grosor === 'a' ? 0 : (grosor === 'c' ? 2 : 1);
      var n = local ? [3, 4, 5][g] : [6, 8, 10][g];
      var suave = cuero === 'c' || cuero === 'd';
      if (suave) n = Math.max(local ? 3 : 4, n - (local ? 1 : 2));
      var how = T.how || '';
      if (tipo === 'c') how += ' ' + (T.how_curly || '');
      if (grosor === 'a') how += ' ' + (T.how_fine || '');
      q('[data-rz-quiz-drops]').textContent = String(T.drops || '[n]').replace('[n]', n);
      q('[data-rz-quiz-icons]').innerHTML = new Array(n + 1).join(DROP);
      q('[data-rz-quiz-where]').textContent = local ? String(T['where_' + zone] || '').replace('[n]', n) : (T['where_all_' + n] || '');
      q('[data-rz-quiz-how]').textContent = how;
      q('[data-rz-quiz-time]').textContent = (cuero === 'a' ? T.time_dry : (cuero === 'c' ? T.time_oily : (cuero === 'd' ? T.time_sens : T.time_normal))) || '';
      q('[data-rz-quiz-freq]').textContent = (cuero === 'd' ? T.freq_sens : T.freq_std) || '';
      q('[data-rz-quiz-sens]').hidden = cuero !== 'd';
      var err = q('[data-rz-ritual-err]'); if (err) err.hidden = true;
    }
    function open() {
      lastFocus = document.activeElement;
      ans = {};
      m.hidden = false;
      document.documentElement.classList.add('rz-quiz-open');
      show(1);
    }
    function close() {
      m.hidden = true;
      document.documentElement.classList.remove('rz-quiz-open');
      if (lastFocus && lastFocus.focus) try { lastFocus.focus({ preventScroll: true }); } catch (e) {}
    }
    document.addEventListener('click', function (e) {
      var o = e.target.closest('[data-rz-quiz-open]');
      if (o) { e.preventDefault(); open(); }
    });
    m.addEventListener('click', function (e) {
      if (e.target.closest('[data-rz-quiz-close]')) { close(); return; }
      if (e.target.closest('[data-rz-quiz-back]')) { if (cur > 1) show(cur - 1); return; }
      if (e.target.closest('[data-rz-quiz-restart]')) { ans = {}; show(1); return; }
      var opt = e.target.closest('[data-rz-quiz-opt]');
      if (opt) {
        var k = +opt.closest('[data-rz-quiz-q]').getAttribute('data-rz-quiz-q');
        ans['q' + k] = opt.getAttribute('data-rz-quiz-opt');
        if (k < 4) show(k + 1); else { compute(); show(5); }
        return;
      }
      var buy = e.target.closest('[data-rz-ritual]');
      if (buy) {
        var tries = 0;
        (function wait() {
          tries++;
          if (buy.disabled && tries < 60) { setTimeout(wait, 150); return; }
          var err = q('[data-rz-ritual-err]');
          if (!err || err.hidden) close();
        })();
      }
    });
    document.addEventListener('keydown', function (e) {
      if (m.hidden) return;
      if (e.key === 'Escape') { close(); return; }
      if (e.key === 'Tab') {
        var f = Array.prototype.filter.call(m.querySelectorAll('button, [href], [tabindex]:not([tabindex="-1"])'), function (x) { return !x.disabled && x.offsetParent !== null; });
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
  }

  /* Plazo de entrega con fechas reales (días laborables, sin fines de semana ni festivos nacionales) */
  function initEta() {
    var FEST = ['01-01', '01-06', '05-01', '08-15', '10-12', '11-01', '12-06', '12-08', '12-25'];
    function laborable(d) {
      var w = d.getDay(); if (w === 0 || w === 6) return false;
      var k = ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2);
      return FEST.indexOf(k) < 0;
    }
    function sumar(n) {
      var d = new Date(); d.setHours(12, 0, 0, 0);
      while (n > 0) { d.setDate(d.getDate() + 1); if (laborable(d)) n--; }
      return d;
    }
    document.querySelectorAll('[data-rz-eta]').forEach(function (el) {
      if (el.getAttribute('data-ready')) return;
      var tpl = el.getAttribute('data-tpl'); var span = el.querySelector('[data-rz-eta-text]') || el.querySelector('span');
      if (!tpl || !span || tpl.indexOf('[d1]') < 0) return;
      var lang = document.documentElement.lang || 'es';
      var fmt;
      try { fmt = new Intl.DateTimeFormat(lang, { weekday: 'short', day: 'numeric', month: 'short' }); } catch (e) { return; }
      function f(d) { return fmt.format(d).replace(/,/g, '').replace(/\.(?=\s|$)/g, ''); }
      var a = parseInt(el.getAttribute('data-min'), 10) || 5, b = parseInt(el.getAttribute('data-max'), 10) || 10;
      if (b < a) b = a;
      var parts = tpl.split(/\[d1\]|\[d2\]/);
      if (parts.length !== 3) return;
      span.textContent = '';
      span.appendChild(document.createTextNode(parts[0]));
      var s1 = document.createElement('strong'); s1.textContent = f(sumar(a)); span.appendChild(s1);
      span.appendChild(document.createTextNode(parts[1]));
      var s2 = document.createElement('strong'); s2.textContent = f(sumar(b)); span.appendChild(s2);
      span.appendChild(document.createTextNode(parts[2]));
      el.setAttribute('data-ready', '1');
    });
  }

  /* Black Week: oculta lo que esté fuera de fechas (por si la página viene de caché), cuenta atrás y fecha final */
  function initBf() {
    var now = Date.now();
    document.querySelectorAll('[data-rz-bf-bar]').forEach(function (el) {
      if (el.getAttribute('data-keep') === '1') return;
      var a = Date.parse(el.getAttribute('data-start')), b = Date.parse(el.getAttribute('data-end'));
      if ((a && now < a) || (b && now > b)) el.hidden = true;
      else if (el.classList.contains('rz-bfbar')) document.body.classList.add('rz-bf-on');
    });
    document.querySelectorAll('[data-rz-bf-until]').forEach(function (el) {
      var d = new Date(el.getAttribute('data-end')); var tpl = el.getAttribute('data-tpl') || '[d]';
      try { el.textContent = tpl.replace('[d]', new Intl.DateTimeFormat(document.documentElement.lang || 'es', { weekday: 'long', day: 'numeric', month: 'long' }).format(d).replace(/,/g, '')); } catch (e) {}
    });
    var counts = document.querySelectorAll('[data-rz-bf-count]');
    if (!counts.length || window.rzBfTimer) return;
    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function tick() {
      var t = Date.now();
      counts.forEach(function (el) {
        var end = Date.parse(el.getAttribute('data-end'));
        if (!end) return;
        var ms = end - t;
        if (ms <= 0) { el.textContent = ''; return; }
        var s = Math.floor(ms / 1000), d = Math.floor(s / 86400), h = Math.floor(s % 86400 / 3600), m = Math.floor(s % 3600 / 60), sec = s % 60;
        var txt = (d > 0 ? d + ' d ' : '') + pad(h) + ' h ' + pad(m) + ' min ' + pad(sec) + ' s';
        el.textContent = (el.getAttribute('data-label') || '') + ' ' + txt;
      });
    }
    tick(); window.rzBfTimer = setInterval(tick, 1000);
  }

  function init() {
    initQuick();
    initReveal(); initParallax(); initCounters(); initGallery(); initVariants(); initQty(); initPacks(); initUpsell(); initRitual(); initPopup(); initStickyBuy(); initQuiz(); initEta(); initBf();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  document.addEventListener('shopify:section:load', init);
})();
