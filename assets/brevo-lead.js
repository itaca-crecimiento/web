/* Copia cada lead de los formularios de la web en la lista «Leads web» de Brevo,
   que dispara la automatización de bienvenida y seguimiento.
   Se llama después de que Formspree confirme el envío: si Brevo falla, el lead
   ya ha llegado por correo y el visitante no ve ningún error. */
(function () {
  var URL = 'https://96999149.sibforms.com/serve/MUIFAE4LcFaOvwjOjpXXUozBnRYlgNQe1_ldV8M9CyAoPpZWUM__EiHtlfBcpF1jesdYSPlDtePMqG4m5oCNHkX9LiGb388kU5EtCwqu_bo9BMSMQYH7IwsudDGGt4BRSBqsS11sZpM2tNKGxPV2PXteabXiHtumXaTzluTmFJ4fuek8Qo5VpqMsgEHibWh74cfyYwPDTSXbB75KIA==';

  window.itacaBrevoLead = function (campos) {
    try {
      var d = new FormData();
      Object.keys(campos).forEach(function (k) {
        var v = campos[k];
        if (v) d.append(k, String(v).slice(0, 200));
      });
      d.append('email_address_check', '');
      d.append('locale', 'es');
      d.append('html_type', 'simple');
      fetch(URL, { method: 'POST', body: d, mode: 'no-cors', keepalive: true }).catch(function () {});
    } catch (e) {}
  };
})();
