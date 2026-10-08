/* Aviso de cookies de itacacrecimiento.com.
   La etiqueta de Google (en el <head> de cada página) arranca con el consentimiento denegado:
   no se instalan cookies publicitarias hasta que el visitante pulsa «Aceptar».
   La elección se guarda en el navegador (localStorage, clave «itaca-cookies»). */
(function () {
  var KEY = 'itaca-cookies';
  var GRANTED = { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'granted' };
  var DENIED = { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' };
  var box = null;

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function consent(v) { if (typeof window.gtag === 'function') window.gtag('consent', 'update', v); }

  function css() {
    if (document.getElementById('itaca-cookies-css')) return;
    var s = document.createElement('style');
    s.id = 'itaca-cookies-css';
    s.textContent =
      '.ck{position:fixed;left:20px;bottom:20px;z-index:1000;max-width:420px;box-sizing:border-box;padding:22px 24px;background:#0E2A47;color:#F3EEE4;border-radius:4px;box-shadow:0 12px 40px rgba(10,31,53,.28);font-family:inherit;font-size:14px;line-height:1.6}' +
      '.ck p{margin:0 0 16px;color:#F3EEE4}' +
      '.ck a{color:#F3EEE4;text-decoration:underline;text-underline-offset:3px}' +
      '.ck-b{display:flex;gap:10px;flex-wrap:wrap}' +
      '.ck button{flex:1 1 120px;min-height:44px;padding:10px 16px;border:1px solid #F3EEE4;border-radius:2px;background:transparent;color:#F3EEE4;font:inherit;font-weight:600;cursor:pointer}' +
      '.ck button:hover{background:#F3EEE4;color:#0E2A47}' +
      '.ck button:focus-visible{outline:2px solid #D9774C;outline-offset:2px}' +
      '@media (max-width:560px){.ck{left:12px;right:12px;bottom:12px;max-width:none}}';
    document.head.appendChild(s);
  }

  function close() { if (box) { box.remove(); box = null; } }

  function choose(v) {
    save(v);
    consent(v === 'aceptadas' ? GRANTED : DENIED);
    close();
  }

  function open() {
    if (box) return;
    css();
    box = document.createElement('div');
    box.className = 'ck';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Aviso de cookies');
    box.innerHTML =
      '<p>Usamos cookies de Google para medir las visitas a la web y la eficacia de nuestros anuncios. Solo se activan si las aceptas. <a href="/cookies.html">Más información</a></p>' +
      '<div class="ck-b"><button type="button" data-ck="rechazadas">Rechazar</button><button type="button" data-ck="aceptadas">Aceptar</button></div>';
    box.addEventListener('click', function (e) {
      var v = e.target && e.target.getAttribute && e.target.getAttribute('data-ck');
      if (v) choose(v);
    });
    document.body.appendChild(box);
  }

  window.itacaCookies = { open: open };

  function init() {
    document.querySelectorAll('[data-cookies-config]').forEach(function (el) {
      el.addEventListener('click', function (e) { e.preventDefault(); open(); });
    });
    if (!read()) open();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
