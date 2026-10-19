/* Origen de la visita para las consultas de itacacrecimiento.com.
   Al entrar, se anota de dónde viene el visitante (folleto, Google Ads, Google, correo…) en
   sessionStorage (sin cookies; se borra al cerrar la pestaña). Al enviar un formulario, ese origen
   viaja en los campos ocultos «origen» y «pagina_entrada», y llega con la consulta al correo.
   No se envía nada a terceros: solo sale si el visitante envía el formulario. */
(function () {
  var KEY = 'itaca-origen';

  function leer() {
    try { return JSON.parse(sessionStorage.getItem(KEY) || 'null'); } catch (e) { return null; }
  }
  function guardar(o) {
    try { sessionStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {}
  }

  function host(url) {
    try { return new URL(url).hostname.replace(/^www\./, ''); } catch (e) { return ''; }
  }

  function detectar() {
    var q = new URLSearchParams(location.search);
    var src = (q.get('utm_source') || '').toLowerCase();
    var med = (q.get('utm_medium') || '').toLowerCase();
    var camp = q.get('utm_campaign') || '';

    if (q.get('gclid') || q.get('gbraid') || q.get('wbraid')) return 'Google Ads';
    if (src === 'folleto') return 'Folleto' + (camp ? ' (' + camp + ')' : '');
    if (src.indexOf('brevo') > -1 || med === 'email') return 'Correo (Brevo)' + (camp ? ' · ' + camp : '');
    if (src.indexOf('linkedin') > -1) return 'LinkedIn';
    if (src) return src + (med ? ' / ' + med : '') + (camp ? ' · ' + camp : '');

    var ref = host(document.referrer);
    if (!ref || ref === location.hostname.replace(/^www\./, '')) return null;
    if (/(^|\.)google\./.test(ref)) return 'Google (orgánico)';
    if (/(^|\.)(bing\.com|duckduckgo\.com|yahoo\.|ecosia\.org|qwant\.com)/.test(ref)) return 'Buscador (' + ref + ')';
    if (/(chatgpt\.com|openai\.com|perplexity\.ai|gemini\.google|copilot\.microsoft|claude\.ai)/.test(ref)) return 'Asistente de IA (' + ref + ')';
    if (/(sendibm|brevo|sendinblue)/.test(ref)) return 'Correo (Brevo)';
    if (/(linkedin\.com|lnkd\.in)/.test(ref)) return 'LinkedIn';
    if (/(facebook\.com|instagram\.com|t\.co|twitter\.com|x\.com)/.test(ref)) return 'Redes sociales (' + ref + ')';
    return 'Otra web (' + ref + ')';
  }

  // Una llegada con etiqueta (QR, anuncio, correo) o desde otra web manda; la navegación
  // interna conserva el origen con el que empezó la visita.
  var actual = leer();
  var nuevo = detectar();
  if (nuevo || !actual) {
    actual = { origen: nuevo || 'Directo (sin origen identificado)', entrada: location.pathname };
    guardar(actual);
  }

  function rellenar() {
    var o = leer() || actual;
    document.querySelectorAll('form[data-endpoint]').forEach(function (f) {
      [['origen', o.origen], ['pagina_entrada', o.entrada]].forEach(function (c) {
        var el = f.querySelector('input[name="' + c[0] + '"]');
        if (!el) {
          el = document.createElement('input');
          el.type = 'hidden';
          el.name = c[0];
          f.appendChild(el);
        }
        el.value = c[1];
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', rellenar);
  else rellenar();
})();
