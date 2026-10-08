"""Artículos del blog añadidos en octubre de 2026. Se cargan desde gen_blog.py."""

NOTA_DCG = '<p class="note">Basado en el Documento de Condiciones Generales (DCG) de la línea ICO Crecimiento. Las condiciones pueden cambiar y, en caso de duda, prevalece el texto oficial: compruébalo siempre en <a href="https://www.ico.es" rel="noopener">www.ico.es</a>.</p>'

NUEVOS = []

# ------------------------------------------------------------------ coste
NUEVOS.append(dict(
slug="cuanto-cuesta-ico-crecimiento",
fecha="2026-10-02",
titulo="Cuánto cuesta un préstamo ICO Crecimiento: tipo, comisiones y un ejemplo completo",
seo="Cuánto cuesta ICO Crecimiento: interés, comisiones y ejemplo",
desc="Todo lo que se paga en ICO Crecimiento: Euríbor más margen, comisión de apertura, cancelación anticipada, aval y un ejemplo de 400.000 € a 10 años.",
resumen="""<p>El coste de ICO Crecimiento tiene pocas piezas y todas están en el reglamento de la línea:</p>
<ul>
  <li><strong>Tipo de interés:</strong> Euríbor a 12 meses (mínimo 0 %) + 1,75 %, que baja al 1,25 % o al 0,75 % con aval. Se revisa cada año.</li>
  <li><strong>Comisión de apertura:</strong> 0,5 %, descontada del primer desembolso.</li>
  <li><strong>Cancelación anticipada:</strong> 0,5 % de lo que se devuelva antes de tiempo.</li>
  <li><strong>Sin comisión</strong> por la parte que no se llegue a disponer.</li>
  <li>Posible <strong>recargo de sostenibilidad</strong> del 0,25 % anual si no se cumple el Plan de Remediación.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>El tipo de interés</h2>
<p>El préstamo es a tipo variable: <strong>Euríbor a un año más un margen</strong>. Si el Euríbor fuese negativo, se toma como 0 %. El tipo se revisa una vez al año y se mantiene durante los 12 meses siguientes. El margen depende de la garantía:</p>
<div class="table-wrap">
<table>
  <thead><tr><th>Garantía</th><th>Margen</th></tr></thead>
  <tbody>
    <tr><td>Sin aval, o aval de menos del 50 %</td><td>1,75 %</td></tr>
    <tr><td>Aval del Estado o de una entidad financiera solvente entre el 50 % y el 70 %</td><td>1,25 %</td></tr>
    <tr><td>Aval del Estado o de una entidad financiera solvente entre el 70 % y el 90 %</td><td>0,75 %</td></tr>
    <tr><td>Aval del 100 % de una SGR</td><td>Según el convenio entre el ICO y esa SGR</td></tr>
  </tbody>
</table>
</div>
<p>Cuando hay aval, a ese margen hay que sumar lo que cobra el avalista. En el caso de una SGR, sus comisiones y la aportación a su capital se pueden incluir en la propia financiación.</p>

<h2>Cómo se devuelve</h2>
<p>Los intereses se pagan <strong>cada mes</strong>, el día 15. Durante la carencia solo se pagan intereses. Después, el capital se devuelve, como regla general, en <strong>cuotas mensuales de capital constantes</strong>: cada mes se amortiza lo mismo y los intereses se calculan sobre lo que queda pendiente, así que la cuota total va bajando con el tiempo.</p>

<h2>Ejemplo: 400.000 € de inversión a 10 años</h2>
<p>Una empresa financia una inversión con 400.000 € a 10 años, con 2 de carencia y sin aval. Para el ejemplo suponemos un Euríbor constante del 2 %, es decir, un tipo del 3,75 %. En la realidad el Euríbor cambiará cada año.</p>
<dl class="data-list">
  <div><dt>Comisión de apertura</dt><dd>2.000 € (0,5 %), que se descuentan del primer desembolso</dd></div>
  <div><dt>Años 1 y 2 (carencia)</dt><dd>Solo intereses: 1.250 € al mes</dd></div>
  <div><dt>Años 3 a 10</dt><dd>4.167 € de capital al mes más intereses: la primera cuota ronda los 5.417 € y la última, unos 4.180 €</dd></div>
  <div><dt>Intereses totales</dt><dd>Unos 90.600 €</dd></div>
  <div><dt>Coste financiero total</dt><dd>Unos 92.600 € (intereses + apertura)</dd></div>
</dl>

<h3>El mismo préstamo con aval del 80 %</h3>
<p>Con un aval público o de una entidad financiera solvente que cubra el 80 %, el margen bajaría al 0,75 % y el tipo quedaría en el 2,75 %. Los intereses totales bajarían a unos 66.500 €: unos 24.000 € menos, a los que habría que restar lo que cueste el aval. Por eso conviene comparar las dos opciones con números antes de presentar la solicitud.</p>

<h2>Otros costes posibles</h2>
<ul>
  <li><strong>Cancelación anticipada:</strong> 0,5 % de lo que se devuelva antes de tiempo. Si el préstamo vence anticipadamente por un incumplimiento, la comisión es del 1 % del capital pendiente.</li>
  <li><strong>Intereses de demora:</strong> el tipo ordinario más un 6 % sobre las cuotas que no se paguen a tiempo.</li>
  <li><strong>Recargo de sostenibilidad:</strong> si la empresa saca menos de 2 puntos en el cuestionario ASG y no acredita mejoras en 24 meses, 0,25 % anual sobre el importe firmado. En este ejemplo, 1.000 € al año. Lo explicamos en la guía del <a href="../../guias/cuestionario-sostenibilidad-ico-crecimiento/">cuestionario de sostenibilidad</a>.</li>
  <li><strong>Notaría:</strong> el contrato se firma en documento público.</li>
</ul>

<h2>Lo que no cuesta</h2>
<ul>
  <li>No hay comisión por la parte del préstamo que no se llegue a disponer.</li>
  <li>No hay que contratar seguros, tarjetas ni otros productos vinculados.</li>
  <li>Los gastos de consultoría para preparar la solicitud se pueden financiar dentro del propio préstamo.</li>
</ul>
""",
faqs=[
("¿Qué tipo de interés tiene ICO Crecimiento?", "Euríbor a 12 meses, con un mínimo del 0 %, más un margen del 1,75 %. El margen baja al 1,25 % o al 0,75 % si la operación lleva un aval que cubra entre el 50 % y el 70 % o entre el 70 % y el 90 %. El tipo se revisa cada año."),
("¿Qué comisiones tiene ICO Crecimiento?", "Una comisión de apertura del 0,5 %, que se descuenta del primer desembolso, y una comisión del 0,5 % sobre lo que se cancele anticipadamente. No hay comisión por la parte que no se disponga."),
("¿La cuota de ICO Crecimiento es fija?", "No. Pasada la carencia, el capital se devuelve en cuotas mensuales constantes y los intereses se calculan sobre lo pendiente, así que la cuota total baja con el tiempo. Además, el tipo se revisa cada año con el Euríbor."),
],
))

# ------------------------------------------------------------------ minimis
NUEVOS.append(dict(
slug="ayudas-de-minimis-ico-crecimiento",
fecha="2026-10-16",
titulo="Ayudas de minimis e ICO Crecimiento: por qué te preguntan por tus subvenciones",
seo="Ayudas de minimis en ICO Crecimiento: límites y declaración",
desc="Al pedir ICO Crecimiento hay que declarar las ayudas recibidas. Qué son las de minimis, el límite de 300.000 € en tres años y cómo afecta al préstamo.",
resumen="""<p>Aunque ICO Crecimiento es un préstamo, el ICO calcula la <strong>ayuda pública implícita</strong> que contiene: el ahorro frente a un préstamo a precio de mercado.</p>
<ul>
  <li>Esa ayuda se encuadra en el régimen de <strong>minimis</strong> o, en inversión, en el régimen europeo de ayudas a pymes.</li>
  <li>El límite general de <em>minimis</em> es de <strong>300.000 € por empresa en tres años</strong> (50.000 € en agricultura y 30.000 € en pesca).</li>
  <li>Por eso hay que declarar todas las ayudas de <em>minimis</em> recibidas, también las del grupo.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>¿Por qué un préstamo lleva una «ayuda»?</h2>
<p>El ICO es una entidad pública. Cuando presta a un tipo inferior al que se considera de mercado según la normativa europea, la diferencia cuenta como ayuda de Estado, aunque sea pequeña. El ICO la calcula comparando el tipo aprobado con un tipo de referencia fijado por la Comisión Europea según la solvencia de la empresa y las garantías, y la refleja en el contrato.</p>
<p>En muchas operaciones esa ayuda es pequeña o nula, pero hay que comprobar que cabe dentro de los límites europeos.</p>

<h2>Qué régimen se aplica</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Finalidad del préstamo</th><th>Régimen de ayudas</th></tr></thead>
  <tbody>
    <tr><td>Circulante</td><td>Solo <em>minimis</em> (Reglamento UE 2023/2831)</td></tr>
    <tr><td>Compra de participaciones</td><td>Solo <em>minimis</em></td></tr>
    <tr><td>Inversión</td><td>Régimen de ayudas a pymes del Reglamento UE 651/2014 o <em>minimis</em></td></tr>
  </tbody>
</table>
</div>
<p>En inversión, el régimen de ayudas a pymes permite una ayuda de hasta el 20 % de los costes en las pequeñas empresas y hasta el 10 % en las medianas. Para ese régimen se firma además una declaración específica.</p>

<h2>Los límites de minimis</h2>
<ul>
  <li><strong>300.000 €</strong> por empresa en cualquier periodo de tres años, con carácter general.</li>
  <li><strong>50.000 €</strong> para las empresas del sector agrícola.</li>
  <li><strong>30.000 €</strong> para el sector de la pesca y la acuicultura.</li>
</ul>
<p>Son importes de ayuda, no de préstamo: lo que cuenta es la ayuda implícita calculada, no el nominal. El límite se aplica a la «única empresa», es decir, sumando las empresas del mismo grupo. En fusiones y adquisiciones se suman las ayudas previas de las empresas que se unen.</p>

<h2>Qué hay que declarar</h2>
<p>La solicitud incluye una declaración de ayudas de <em>minimis</em> en la que hay que indicar las recibidas en los tres años anteriores, por la empresa y por su grupo: organismo, fecha, importe y si fue préstamo, subvención o garantía. Muchas pymes han recibido ayudas de <em>minimis</em> sin saberlo: por ejemplo, el Kit Digital se concedió en este régimen, como muchas subvenciones autonómicas y locales.</p>
<p>La empresa también se compromete a no superar el límite en los tres años siguientes, sumando la ayuda del préstamo del ICO.</p>

<h2>Qué puede pasar si te acercas al límite</h2>
<ul>
  <li>El importe o el plazo del préstamo pueden quedar limitados para no superar el tope de ayuda.</li>
  <li>La empresa puede pedir al ICO un tipo de interés más alto, precisamente para reducir la ayuda implícita y no agotar el margen de <em>minimis</em> que necesite para otras subvenciones.</li>
  <li>Un préstamo puede dividirse en tramos acogidos a regímenes distintos.</li>
</ul>

<h2>Recomendación práctica</h2>
<p>Antes de solicitar, haz una lista de todas las ayudas públicas de los últimos tres años, de la empresa y del grupo, con sus resoluciones. Si piensas pedir otras subvenciones próximamente, tenlo en cuenta: lo que consuma ICO Crecimiento del límite de <em>minimis</em> no estará disponible para ellas.</p>
""",
faqs=[
("¿ICO Crecimiento es una ayuda de minimis?", "El préstamo puede incluir una ayuda implícita: el ahorro frente a un préstamo a precio de mercado. En circulante y compra de participaciones se encuadra en el régimen de minimis; en inversión, en el régimen de ayudas a pymes del Reglamento 651/2014 o en minimis."),
("¿Cuál es el límite de las ayudas de minimis?", "Con carácter general, 300.000 € por empresa (sumando su grupo) en cualquier periodo de tres años. Para el sector agrícola el límite es de 50.000 € y para la pesca y la acuicultura, de 30.000 €."),
("¿El Kit Digital cuenta como ayuda de minimis?", "Sí, el Kit Digital se concedió en régimen de minimis, así que hay que incluirlo en la declaración si se recibió en los tres años anteriores."),
],
))

# ------------------------------------------------------------------ deuda corto plazo
NUEVOS.append(dict(
slug="cancelar-deuda-corto-plazo-ico-crecimiento",
fecha="2026-10-09",
titulo="Cancelar deuda a corto plazo con ICO Crecimiento: cuándo tiene sentido",
seo="Cancelar deuda a corto plazo con ICO Crecimiento",
desc="ICO Crecimiento permite usar el circulante para cancelar deuda a corto plazo con proveedores o bancos. Cuándo tiene sentido y qué tener en cuenta.",
resumen="""<p>Entre las finalidades de circulante de ICO Crecimiento está la <strong>cancelación de deuda a corto plazo</strong>, tanto comercial (proveedores) como financiera (bancos).</p>
<ul>
  <li>Permite pasar deuda que vence en meses a un préstamo de <strong>hasta 5 años con 1 de carencia</strong>.</li>
  <li>Tiene sentido en empresas <strong>rentables</strong> cuyo crecimiento se ha financiado con deuda demasiado corta.</li>
  <li>No sirve para empresas con pérdidas, morosidad en la CIRBE o deudas con Hacienda o la Seguridad Social: no cumplen los requisitos.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>El problema: crecer con deuda a corto</h2>
<p>Es muy habitual: una pyme crece, necesita más circulante y lo va cubriendo con lo que tiene a mano, como pólizas de crédito, descuento comercial, confirming o pagar más tarde a los proveedores. Todo es deuda que vence en meses. La empresa es rentable, pero vive pendiente de las renovaciones y cualquier recorte de una línea bancaria la pone en apuros.</p>

<h2>Qué permite ICO Crecimiento</h2>
<p>El reglamento de la línea incluye dentro del circulante la <strong>cancelación de deuda a corto plazo de naturaleza comercial y financiera</strong>. Es decir, se puede pedir un préstamo de ICO Crecimiento para pagar esas deudas y devolverlo:</p>
<ul>
  <li>en <strong>hasta 5 años</strong>,</li>
  <li>con <strong>hasta 1 año de carencia</strong>, en el que solo se pagan intereses,</li>
  <li>desde 50.000 € y hasta el 100 % de la necesidad justificada.</li>
</ul>

<h2>Ejemplo orientativo</h2>
<p>Una empresa factura 3 millones de euros, gana dinero y tiene 350.000 € dispuestos en pólizas y descuento que renueva cada año. Si pasa 250.000 € de esa deuda a ICO Crecimiento a 5 años con 1 de carencia, durante el primer año solo paga intereses y después devuelve unos 5.200 € de capital al mes, más los intereses. Las pólizas vuelven a quedar libres para los picos de tesorería.</p>

<h2>Cuándo tiene sentido</h2>
<ul>
  <li>La empresa es <strong>rentable</strong> y su problema es de plazos, no de resultados.</li>
  <li>La deuda a corto viene de <strong>financiar el crecimiento</strong>: más clientes, más stock, nuevos contratos.</li>
  <li>Los bancos han empezado a <strong>reducir o endurecer</strong> las líneas de corto plazo.</li>
  <li>Se quiere <strong>ordenar la deuda</strong> en un calendario de pagos previsible.</li>
</ul>

<h2>Cuándo no funciona</h2>
<ul>
  <li>Si la empresa ha tenido <strong>pérdidas en los dos últimos ejercicios</strong> o tiene patrimonio neto negativo: no cumple los requisitos.</li>
  <li>Si figura como <strong>morosa en la CIRBE</strong>, al pedirlo o al firmarlo.</li>
  <li>Si no está <strong>al corriente con Hacienda o la Seguridad Social</strong>: es un requisito previo, no algo que se pueda arreglar con el préstamo.</li>
  <li>Si la deuda corta tapa <strong>pérdidas recurrentes</strong>: el ICO analiza la capacidad de devolución y lo detectará.</li>
</ul>

<h2>Lo que conviene preparar</h2>
<ul>
  <li>El detalle de la deuda a corto plazo: con quién, cuánto, vencimientos y coste.</li>
  <li>Una explicación de por qué se generó esa deuda y cómo mejora la situación al alargar el plazo.</li>
  <li>Una previsión de tesorería que muestre que las cuotas son asumibles a partir del segundo año.</li>
</ul>
<p>Después habrá que justificar ante el ICO el destino de los fondos con los documentos correspondientes.</p>
<p>Ojo: la modalidad <a href="../../guias/ico-crecimiento-dana/">ICO Crecimiento DANA</a> sí excluye expresamente las refinanciaciones. Este artículo se refiere a la línea general.</p>
""",
faqs=[
("¿Se puede refinanciar deuda con ICO Crecimiento?", "La línea general permite destinar el circulante a cancelar deuda a corto plazo, tanto comercial como financiera, con un préstamo de hasta 5 años y 1 de carencia. La modalidad DANA, en cambio, excluye las refinanciaciones."),
("¿Puedo pagar deudas con Hacienda con ICO Crecimiento?", "No es el caso de uso: estar al corriente con Hacienda y la Seguridad Social es un requisito para solicitar el préstamo, no algo que se pueda resolver con él."),
("¿Conviene cancelar la póliza de crédito con ICO Crecimiento?", "Puede convenir pasar a largo plazo la parte estable de la deuda a corto y dejar la póliza libre para los picos de tesorería. Depende de cada empresa y conviene estudiarlo con números."),
],
))

# ------------------------------------------------------------------ relevo generacional
NUEVOS.append(dict(
slug="relevo-generacional-ico-crecimiento",
fecha="2026-10-20",
titulo="Relevo generacional en la empresa familiar: cómo puede ayudar ICO Crecimiento",
seo="Relevo generacional en la empresa familiar con ICO Crecimiento",
desc="ICO Crecimiento puede financiar la compra de participaciones para el relevo generacional en la empresa familiar. Qué permite y qué hay que estudiar.",
resumen="""<p>Las empresas familiares que afrontan un <strong>relevo generacional</strong> son uno de los públicos a los que se dirige expresamente ICO Crecimiento. La línea permite financiar:</p>
<ul>
  <li>La <strong>compra de participaciones empresariales</strong> para facilitar el relevo de los socios mayoritarios.</li>
  <li>La <strong>adquisición de acciones o participaciones propias</strong> por la empresa familiar, hasta el límite de la Ley de Sociedades de Capital.</li>
  <li>Inversiones y gastos que acompañan al relevo, como la <strong>formación</strong> del equipo o los sistemas de gestión.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>El problema del relevo</h2>
<p>Cuando el fundador se retira, a menudo no todos los herederos quieren seguir en la empresa, o hay socios que quieren salir. Alguien tiene que comprar esas participaciones, y ni la siguiente generación ni la empresa suelen tener la liquidez necesaria. Los bancos, además, son prudentes con este tipo de operaciones porque no financian un activo productivo.</p>

<h2>Qué permite ICO Crecimiento</h2>
<p>El reglamento de la línea incluye dos finalidades pensadas para este caso:</p>
<ol class="pasos-guia">
  <li><strong>Adquisición de participaciones empresariales</strong> para facilitar el relevo generacional de los accionistas mayoritarios de la empresa familiar.</li>
  <li><strong>Adquisición de acciones propias</strong> por parte de la empresa familiar, hasta el límite que permite la Ley de Sociedades de Capital, con el mismo objetivo.</li>
</ol>
<p>Hay que tener en cuenta que el prestatario es siempre una <strong>sociedad mercantil</strong> que cumple los requisitos de la línea, no una persona física. Por eso la forma de la operación (quién compra, a quién y cómo se estructura) hay que diseñarla con cuidado, junto con el asesor legal y fiscal de la familia.</p>

<h2>Condiciones a tener en cuenta</h2>
<ul>
  <li>La compra de participaciones se financia como máximo al <strong>80 %</strong>.</li>
  <li>La ayuda implícita del préstamo en estas operaciones se encuadra solo en el régimen de <em>minimis</em>. Lo explicamos en el artículo sobre <a href="../ayudas-de-minimis-ico-crecimiento/">ayudas de minimis</a>.</li>
  <li>La compra se justifica con una nota simple actualizada del Registro Mercantil o un certificado de la sociedad que confirme la transmisión.</li>
  <li>Se aplican todos los requisitos generales: pyme con al menos 4 años, cuentas auditadas o aval, sin pérdidas en los dos últimos ejercicios, sin morosidad y al corriente de pagos. Si la empresa forma parte de un grupo, los requisitos deben cumplirse también a nivel de grupo.</li>
</ul>

<h2>Más allá de la compra</h2>
<p>Un relevo no es solo un cambio de propiedad. ICO Crecimiento también financia gastos que ayudan a que salga bien:</p>
<ul>
  <li><strong>Formación</strong> del equipo y de la nueva dirección.</li>
  <li><strong>Sistemas de gestión e informes</strong> que profesionalizan la empresa.</li>
  <li><strong>Inversiones</strong> que la nueva generación quiere acometer: digitalización, maquinaria o nuevos mercados.</li>
  <li>El <strong>circulante</strong> necesario para mantener la actividad durante la transición.</li>
</ul>

<h2>Por dónde empezar</h2>
<p>Antes de preparar la solicitud conviene tener claro el acuerdo entre la familia: quién se queda, quién sale, a qué valor y con qué calendario. Con eso definido, se puede estudiar si la operación encaja en ICO Crecimiento y cómo combinarla con otras fuentes de financiación.</p>
""",
faqs=[
("¿ICO Crecimiento financia la compra de participaciones?", "Sí, para fines concretos: facilitar el relevo generacional de los accionistas mayoritarios de la empresa familiar, ampliar la capacidad productiva, mejorar el acceso a la financiación o asegurar el suministro de insumos clave. Se financia hasta el 80 %."),
("¿Puede la empresa familiar comprar sus propias participaciones con ICO Crecimiento?", "Sí. La línea permite financiar la adquisición de acciones propias por la empresa familiar, hasta el límite de la Ley de Sociedades de Capital, para facilitar el relevo generacional de los socios mayoritarios."),
("¿Puede un heredero pedir ICO Crecimiento a título personal?", "No. El beneficiario tiene que ser una sociedad mercantil pyme que cumpla los requisitos de la línea. La estructura de la operación conviene diseñarla con el asesor legal y fiscal."),
],
))

# ------------------------------------------------------------------ después de la aprobación
NUEVOS.append(dict(
slug="despues-de-la-aprobacion-ico-crecimiento",
fecha="2026-10-13",
titulo="Me han aprobado ICO Crecimiento: firma, desembolso y justificación",
seo="ICO Crecimiento aprobado: firma, desembolso y justificación",
desc="Qué pasa cuando el ICO aprueba tu préstamo: plazo para firmar, cuándo llega el dinero, cómo se justifica el gasto y qué obligaciones tienes.",
resumen="""<p>La aprobación no es el final. Después vienen estos pasos:</p>
<ol>
  <li><strong>Aceptar</strong> las condiciones de la resolución de concesión.</li>
  <li><strong>Firmar</strong> el contrato en documento público en un máximo de 3 meses (prorrogables otros 3).</li>
  <li><strong>Recibir el dinero:</strong> el circulante, de una vez en 15 días; la inversión, en una o varias entregas antes de que acabe la carencia.</li>
  <li><strong>Justificar</strong> el destino de los fondos con facturas en ICO Online.</li>
  <li><strong>Conservar</strong> la documentación durante 10 años desde el vencimiento.</li>
</ol>""",
cuerpo=NOTA_DCG + """
<h2>1. La resolución de concesión</h2>
<p>El Comité de Operaciones del ICO aprueba la operación con una resolución que fija exactamente las condiciones: importe, plazo, carencia, tipo y garantías. La empresa tiene que <strong>aceptarlas expresamente</strong> y, a partir de ahí, ya no se pueden cambiar en la firma, salvo en los casos previstos en el reglamento.</p>

<h2>2. La firma del contrato</h2>
<p>El contrato de préstamo se formaliza en <strong>documento público</strong>, ante notario. La resolución indica el plazo máximo para firmarlo, que no puede superar <strong>3 meses</strong>, con una única prórroga de otros 3 si se justifica. En la fecha de firma, la empresa no puede figurar como morosa en la CIRBE.</p>
<p>Si la operación lleva aval de una SGR u otras garantías, tienen que estar listas para la firma.</p>

<h2>3. El desembolso</h2>
<dl class="data-list">
  <div><dt>Circulante</dt><dd>De una sola vez, en un máximo de 15 días naturales desde la firma</dd></div>
  <div><dt>Inversión</dt><dd>En una o varias entregas, siempre antes de que termine la carencia</dd></div>
  <div><dt>Comisión de apertura</dt><dd>El 0,5 % se descuenta del primer desembolso</dd></div>
  <div><dt>Lo no dispuesto</dt><dd>Si no se dispone todo en plazo, el préstamo queda en lo dispuesto, sin comisión por el resto</dd></div>
</dl>

<h2>4. La justificación</h2>
<p>La empresa tiene que justificar en qué ha gastado el dinero. Se hace en la aplicación de <strong>ICO Online</strong>, subiendo copia de las facturas, que deben cumplir el reglamento de facturación, y certificando con firma electrónica que son copia fiel de los originales. En la compra de participaciones se justifica con una nota simple del Registro Mercantil o un certificado de la sociedad, y en la compra de inmuebles hace falta un certificado de tasación.</p>
<p>No justificar, o justificar de forma insuficiente, puede provocar el <strong>vencimiento anticipado</strong> del préstamo o que no se hagan los desembolsos pendientes. Conviene tener las facturas y los justificantes de pago ordenados desde el principio.</p>

<h2>5. Durante la vida del préstamo</h2>
<ul>
  <li><strong>Pagos mensuales:</strong> intereses el día 15 de cada mes y, pasada la carencia, el capital en cuotas constantes.</li>
  <li><strong>Revisión del tipo</strong> una vez al año, con aviso previo.</li>
  <li><strong>Controles:</strong> el ICO, la Intervención General del Estado y el Tribunal de Cuentas pueden pedir información y visitar las instalaciones.</li>
  <li><strong>Plan de Remediación</strong>, si la puntuación de sostenibilidad fue inferior a 2: hay 24 meses para acreditar mejoras.</li>
  <li><strong>Desarrollar el proyecto</strong> según el plan presentado y comunicar cualquier cambio relevante.</li>
  <li><strong>Conservar los documentos</strong> justificativos durante 10 años desde el vencimiento del préstamo.</li>
</ul>

<h2>¿Se pueden cambiar las condiciones después?</h2>
<p>En algunos casos, sí: cambios de titularidad, fusiones o escisiones (si el nuevo titular cumple los requisitos), una ampliación del plazo por circunstancias imprevisibles o una ampliación del plazo de disposición. Nunca se puede aumentar el importe aprobado, y la mala situación económica de la empresa no justifica por sí sola alargar el plazo.</p>
<p>También se puede cancelar el préstamo antes de tiempo, total o parcialmente, con una comisión del 0,5 % sobre lo devuelto.</p>

<h2>Causas de vencimiento anticipado</h2>
<ul>
  <li>Dejar de pagar seis liquidaciones consecutivas.</li>
  <li>Haber obtenido el préstamo falseando u ocultando condiciones.</li>
  <li>No cumplir el objetivo o el proyecto financiado.</li>
  <li>No justificar, o justificar de forma insuficiente, el destino de los fondos.</li>
  <li>Obstaculizar los controles.</li>
</ul>
""",
faqs=[
("¿Cuánto tiempo hay para firmar ICO Crecimiento tras la aprobación?", "El plazo lo fija la resolución de concesión y no puede superar 3 meses, con una única prórroga de otros 3 meses si se justifica. El contrato se firma en documento público."),
("¿Cuándo se recibe el dinero de ICO Crecimiento?", "En circulante, de una sola vez en un máximo de 15 días naturales desde la firma. En inversión, en una o varias entregas antes de que termine el periodo de carencia."),
("¿Cómo se justifica el préstamo de ICO Crecimiento?", "Subiendo a ICO Online copia de las facturas del gasto, certificadas con firma electrónica. La compra de participaciones se justifica con nota simple o certificado de la sociedad. La documentación se conserva 10 años desde el vencimiento."),
],
))

# ------------------------------------------------------------------ filtros de solvencia
NUEVOS.append(dict(
slug="por-que-deniegan-ico-crecimiento",
fecha="2026-10-02",
titulo="Por qué el ICO deniega ICO Crecimiento: los filtros de solvencia",
seo="Por qué deniegan ICO Crecimiento: rating, pérdidas y CIRBE",
desc="Rating mínimo B, pérdidas, patrimonio neto, CIRBE y empresa en crisis: los filtros del ICO antes de aprobar ICO Crecimiento y cómo comprobarlos.",
resumen="""<p>Antes de valorar el proyecto, el ICO comprueba unos filtros que, si fallan, descartan la solicitud:</p>
<ul>
  <li>Calificación crediticia mínima <strong>B</strong> (B- o inferior queda descartada).</li>
  <li><strong>Sin pérdidas</strong> en los dos últimos ejercicios cerrados y <strong>sin patrimonio neto negativo</strong>.</li>
  <li><strong>Sin morosidad en la CIRBE</strong>, al solicitar y al firmar.</li>
  <li>No ser <strong>empresa en crisis</strong>.</li>
  <li>Una <strong>pérdida esperada</strong> de la operación no superior al 1 %.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Los filtros, uno a uno</h2>

<h3>1. Calificación crediticia mínima: B</h3>
<p>El ICO calcula un rating de la empresa con su sistema interno, en la escala de Standard &amp; Poor's. El mínimo es <strong>B</strong>: las solicitudes con B- o inferior se descartan. Si la empresa pertenece a un grupo, se calcula el rating de la empresa y el del grupo, y cuenta el peor de los dos.</p>

<h3>2. Pérdidas y patrimonio neto</h3>
<p>No se admiten empresas con <strong>pérdidas en los dos últimos ejercicios cerrados</strong> ni con <strong>patrimonio neto negativo</strong> en el último. Un solo año en pérdidas no descarta por sí solo, pero pesa en el rating y conviene explicarlo bien.</p>

<h3>3. CIRBE sin morosidad</h3>
<p>La empresa no puede figurar como morosa en la Central de Información de Riesgos del Banco de España ni el día de la solicitud ni el de la firma. Un recibo devuelto o una cuota impagada que se haya olvidado puede bastar. Conviene pedir el informe CIRBE, que es gratuito, antes de presentar nada.</p>

<h3>4. Empresa en crisis</h3>
<p>Al cierre del último ejercicio, la empresa no puede estar «en crisis» según la normativa europea. En una sociedad limitada o anónima, eso ocurre, entre otros casos, cuando las pérdidas acumuladas se han comido más de la mitad del capital social suscrito, o cuando la empresa está en concurso o reúne las condiciones para estarlo.</p>

<h3>5. Pérdida esperada de la operación</h3>
<p>El ICO estima la pérdida esperada de cada operación, que combina la probabilidad de impago, la exposición y las garantías. Si supera el <strong>1 %</strong>, la operación no entra en la línea. Aquí las garantías importan: un aval puede reducir la pérdida esperada y hacer viable una operación que sin él no lo sería.</p>

<h3>6. Capacidad de devolución</h3>
<p>Con los estados financieros y las previsiones, el ICO analiza si la empresa puede pagar las cuotas. Puede pedir información adicional e incluso encargar un informe a un experto independiente.</p>

<h2>Otros motivos de exclusión</h2>
<ul>
  <li>No estar al corriente con Hacienda o la Seguridad Social, o tener pendiente el reintegro de alguna subvención.</li>
  <li>Estar en concurso de acreedores o inhabilitada.</li>
  <li>Pertenecer a un sector excluido: juego, armamento letal, medios de comunicación, intermediación financiera (salvo fintech e insurtech), actividades religiosas o políticas, entre otros.</li>
  <li>No ser pyme si se cuenta el grupo, o estar participada en un 25 % o más por organismos públicos.</li>
  <li>No cumplir los requisitos a nivel de grupo, cuando la empresa pertenece a uno.</li>
</ul>

<h2>¿Y si me lo deniegan?</h2>
<p>Contra la inadmisión o la desestimación <strong>no cabe recurso</strong> administrativo. Pero la empresa puede presentar una nueva solicitud, para otro proyecto o para el mismo una vez corregidos los defectos. Eso sí, la nueva solicitud entra al final de la cola, que se atiende por orden de llegada. Por eso es tan importante revisar estos filtros antes de la primera presentación.</p>
<p>Puedes hacer una primera comprobación con nuestro <a href="../../test-ico-crecimiento/">test de requisitos</a>. En el estudio gratuito revisamos con tus cifras los puntos que el test no puede medir, como el rating o la pérdida esperada.</p>
""",
faqs=[
("¿Qué rating mínimo exige ICO Crecimiento?", "Una calificación de B en la escala de Standard & Poor's, según el análisis interno del ICO. Las solicitudes con B- o inferior se descartan. Si la empresa pertenece a un grupo, cuenta la peor calificación entre la empresa y el grupo."),
("¿Puedo pedir ICO Crecimiento con un año en pérdidas?", "Un solo ejercicio con pérdidas no descarta automáticamente, porque el filtro es tener pérdidas en los dos últimos ejercicios cerrados. Pero afecta al rating y conviene explicarlo bien en la solicitud."),
("¿Se puede recurrir si el ICO deniega ICO Crecimiento?", "No cabe recurso administrativo, pero se puede presentar una nueva solicitud una vez corregidos los defectos. Entra de nuevo por orden de llegada."),
],
))

# ------------------------------------------------------------------ bodegas y secaderos
NUEVOS.append(dict(
slug="ico-crecimiento-bodegas-y-secaderos",
fecha="2026-10-23",
titulo="ICO Crecimiento para bodegas y secaderos: financiar el tiempo que tarda en venderse el producto",
seo="ICO Crecimiento para bodegas y secaderos de jamón",
desc="En una bodega o un secadero, el producto tarda años en venderse. Cómo financiar ese stock con ICO Crecimiento a 5 años, y barricas o naves a 10.",
resumen="""<p>Bodegas y secaderos de jamón tienen el mismo problema: <strong>el producto pasa años madurando antes de poder venderse</strong>, y ese stock hay que pagarlo desde el primer día. ICO Crecimiento encaja bien:</p>
<ul>
  <li><strong>Circulante</strong> para financiar el stock en crianza o en curación: hasta 5 años, con 1 de carencia y hasta el 100 % de la necesidad.</li>
  <li><strong>Inversión</strong> en barricas, depósitos, cámaras de secado, naves o embotelladoras: hasta 10 años, con 2 de carencia y hasta el 80 %.</li>
  <li>Al ser <strong>transformación</strong> y no producción agrícola primaria, se aplica el límite general de ayudas de <em>minimis</em>.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Un stock que tarda años en convertirse en dinero</h2>
<p>Un vino de crianza pasa al menos dos años entre barrica y botella antes de salir al mercado; un reserva, más. Un jamón ibérico de bellota puede necesitar tres años o más de curación. Durante todo ese tiempo la empresa ya ha pagado la uva o los cerdos, la mano de obra, la energía y las instalaciones, y todavía no ha cobrado nada.</p>
<p>Cuanto más crece la empresa, más producto tiene madurando y más dinero inmovilizado. Por eso muchas bodegas y secaderos rentables van justos de tesorería, y dependen de pólizas que hay que renovar cada año.</p>

<h2>Cómo encaja ICO Crecimiento</h2>
<h3>Circulante: financiar el stock</h3>
<ul>
  <li>Hasta <strong>5 años</strong>, un plazo más acorde con un producto que tarda años en venderse que una póliza anual.</li>
  <li><strong>1 año de carencia</strong>: el primer año solo se pagan intereses.</li>
  <li>Hasta el <strong>100 %</strong> de la necesidad de circulante justificada.</li>
  <li>También puede destinarse a <strong>cancelar deuda a corto plazo</strong> con proveedores o bancos.</li>
</ul>
<h3>Inversión: ampliar la capacidad</h3>
<ul>
  <li>Barricas, depósitos de acero inoxidable, prensas y líneas de embotellado.</li>
  <li>Secaderos, cámaras de frío y de curación, salas de despiece.</li>
  <li>Naves, placas solares de autoconsumo y equipos de control de temperatura y humedad.</li>
  <li>Hasta <strong>10 años</strong>, con <strong>2 de carencia</strong> y hasta el <strong>80 %</strong>. Se pueden incluir inversiones hechas o iniciadas en los 12 meses anteriores a la solicitud.</li>
</ul>

<h2>Ejemplo orientativo</h2>
<p>Un secadero de Guijuelo vende 4 millones de euros al año y quiere aumentar un 25 % la producción de ibérico. Como cada pieza tarda unos tres años en venderse, ese crecimiento le obliga a tener mucho más producto en curación antes de ingresar nada por él. Calcula que necesita 500.000 € más de circulante y 300.000 € para ampliar una cámara de secado.</p>
<p>Con ICO Crecimiento podría pedir las dos cosas en la misma solicitud: el circulante a 5 años con 1 de carencia, y la cámara como inversión a 10 años con 2 de carencia, financiando hasta el 80 % (240.000 €). El resto de la inversión lo aportaría la empresa.</p>

<h2>Lo que conviene revisar antes</h2>
<ul>
  <li><strong>La forma jurídica.</strong> La línea exige una sociedad mercantil pyme. Las cooperativas y SAT deben revisar si encajan.</li>
  <li><strong>La actividad.</strong> Elaborar vino o curar jamón es transformación, con el límite general de <em>minimis</em> de 300.000 € de ayuda en tres años. Si la empresa también cultiva viñedo o cría ganado, esa parte primaria tiene un límite mucho menor. Lo explicamos en el artículo sobre <a href="../ayudas-de-minimis-ico-crecimiento/">ayudas de minimis</a>.</li>
  <li><strong>El valor del stock en las cuentas.</strong> Un balance con mucho stock en crianza puede parecer poco líquido. Conviene explicar en la solicitud cómo y cuándo se convierte en ventas.</li>
  <li><strong>Los resultados.</strong> Una mala cosecha o una mala campaña pueden dejar pérdidas en un ejercicio. La línea no admite pérdidas en los dos últimos ejercicios cerrados ni patrimonio neto negativo.</li>
</ul>
<p>Tienes más detalle sobre el sector en la guía de <a href="../../guias/circulante-empresas-agroalimentarias/">ICO Crecimiento para empresas agroalimentarias</a>.</p>
""",
faqs=[
("¿Puede una bodega pedir ICO Crecimiento?", "Sí, si es una sociedad mercantil pyme con al menos 4 años, sin pérdidas en los dos últimos ejercicios ni patrimonio neto negativo, y cumple el resto de requisitos. Puede financiar el stock en crianza como circulante y las barricas, depósitos o naves como inversión."),
("¿ICO Crecimiento financia el stock de jamones en curación?", "Sí. El stock en curación forma parte del circulante de la empresa, que la línea financia hasta 5 años, con 1 de carencia y hasta el 100 % de la necesidad justificada."),
("¿Qué límite de ayudas tiene una bodega o un secadero?", "Elaborar vino o curar jamón es transformación, así que se aplica el límite general de minimis de 300.000 € de ayuda en tres años. La producción agrícola primaria tiene un límite de 50.000 €."),
],
))

# ------------------------------------------------------------------ CIRBE
NUEVOS.append(dict(
slug="como-leer-informe-cirbe",
fecha="2026-10-06",
titulo="Cómo leer tu informe CIRBE antes de pedir ICO Crecimiento",
seo="Cómo leer la CIRBE antes de pedir ICO Crecimiento",
desc="El ICO consulta tu CIRBE al estudiar ICO Crecimiento y antes de firmar. Cómo pedir el informe, qué significa cada dato y qué revisar antes de solicitar.",
resumen="""<p>La <strong>CIRBE</strong> es el registro del Banco de España con todas las deudas de tu empresa con bancos y entidades financieras. El ICO la consulta <strong>dos veces</strong>: al estudiar la solicitud y al firmar el préstamo.</p>
<ul>
  <li>Se pide <strong>gratis</strong> en la sede electrónica del Banco de España, con el certificado digital de la empresa.</li>
  <li>Lo primero que hay que mirar es que <strong>no aparezca nada impagado</strong>: con morosidad en la CIRBE no se puede obtener ICO Crecimiento.</li>
  <li>También conviene revisar que las cifras <strong>cuadren con el balance</strong> y que no haya avales a terceros olvidados.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Qué es la CIRBE</h2>
<p>La Central de Información de Riesgos del Banco de España recoge, mes a mes, los préstamos, créditos, avales y demás operaciones que las entidades financieras tienen con cada empresa y cada persona. Es la foto de tu deuda bancaria tal como la ven los bancos.</p>
<p>En ICO Crecimiento es especialmente importante: el reglamento de la línea exige que la empresa <strong>no figure en situación de morosidad en la CIRBE</strong> ni en la fecha de la solicitud ni en la de la firma. Además, al solicitar, la empresa autoriza al ICO a consultarla.</p>

<h2>Cómo pedir el informe</h2>
<ol class="pasos-guia">
  <li>Entra en la <strong>sede electrónica del Banco de España</strong> y busca «Solicitud de informe de riesgos (CIRBE)».</li>
  <li>Identifícate con el <strong>certificado digital de la empresa</strong> o de su representante.</li>
  <li>Descarga el informe en PDF. Es <strong>gratuito</strong>.</li>
</ol>
<p>Hazlo antes de preparar la solicitud y vuelve a pedirlo justo antes de firmar, porque el ICO lo comprobará de nuevo en ese momento.</p>

<h2>Qué significa cada dato</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Dato</th><th>Qué indica</th></tr></thead>
  <tbody>
    <tr><td>Entidad</td><td>El banco o entidad que declara la operación</td></tr>
    <tr><td>Tipo de producto</td><td>Préstamo, crédito (póliza), descuento comercial, leasing, aval…</td></tr>
    <tr><td>Riesgo directo</td><td>Deudas de la propia empresa</td></tr>
    <tr><td>Riesgo indirecto</td><td>Avales que la empresa ha dado a otros, por ejemplo a una empresa del grupo o a un socio</td></tr>
    <tr><td>Dispuesto</td><td>Lo que la empresa debe en ese momento</td></tr>
    <tr><td>Disponible</td><td>Lo que todavía podría usar de una póliza o línea de crédito</td></tr>
    <tr><td>Plazo residual</td><td>Cuánto queda hasta el vencimiento</td></tr>
    <tr><td>Garantía</td><td>Si la operación tiene garantía real (hipoteca), personal o de otro tipo</td></tr>
    <tr><td>Situación</td><td>Si la operación está al corriente o tiene importes vencidos e impagados</td></tr>
  </tbody>
</table>
</div>

<h2>Lo que hay que revisar antes de pedir ICO Crecimiento</h2>
<h3>1. Que no haya nada impagado</h3>
<p>Es el punto más importante. Cualquier operación con importes vencidos o calificada como dudosa puede hacer que el ICO descarte la solicitud. A veces es algo pequeño y olvidado: un recibo de leasing devuelto, una tarjeta de empresa o una cuota que se pagó tarde. Si aparece, hay que regularizarlo y esperar a que la entidad actualice la declaración antes de presentar nada.</p>
<h3>2. Que las cifras cuadren con el balance</h3>
<p>El ICO compara la deuda que aparece en la CIRBE con la que figura en las cuentas. Si no coinciden, por ejemplo porque un préstamo ya cancelado sigue apareciendo, conviene saberlo y explicarlo en la solicitud.</p>
<h3>3. Los avales a terceros</h3>
<p>El riesgo indirecto suele pasar desapercibido: un aval que la empresa dio hace años a una sociedad del grupo o a un socio sigue contando. El ICO lo tendrá en cuenta al analizar la capacidad de devolución.</p>
<h3>4. Cuánto se usa de las pólizas</h3>
<p>Unas pólizas dispuestas casi al máximo todos los meses indican tensión de tesorería. No descarta la solicitud, pero sí es la justificación natural de una necesidad de circulante, o de pasar parte de esa deuda corta a un préstamo a 5 años.</p>

<h2>Si encuentras un error</h2>
<p>Los datos los declara cada entidad. Si algo es incorrecto, dirígete primero a la entidad que lo declaró para que lo rectifique. Si no lo hace, puedes presentar una reclamación ante el Banco de España. La corrección puede tardar, así que revisa la CIRBE con tiempo, no el día antes de solicitar.</p>
""",
faqs=[
("¿Qué es la CIRBE?", "Es la Central de Información de Riesgos del Banco de España: un registro mensual de los préstamos, créditos, avales y demás operaciones que las entidades financieras tienen con cada empresa y persona."),
("¿Cómo se pide la CIRBE de una empresa?", "En la sede electrónica del Banco de España, con el certificado digital de la empresa o de su representante. Es gratuita."),
("¿Puedo pedir ICO Crecimiento si aparezco como moroso en la CIRBE?", "No. El reglamento de la línea exige no figurar en situación de morosidad en la CIRBE ni al solicitar ni al firmar el préstamo. Hay que regularizar la deuda y esperar a que la entidad actualice su declaración."),
],
))

# ------------------------------------------------------------------ leasing
NUEVOS.append(dict(
slug="ico-crecimiento-o-leasing-maquinaria",
fecha="2026-10-06",
titulo="ICO Crecimiento o leasing para comprar maquinaria: cuál conviene",
seo="ICO Crecimiento o leasing para maquinaria: diferencias",
desc="ICO Crecimiento financia maquinaria a 10 años con 2 de carencia. Diferencias con el leasing en plazo, propiedad, IVA y fiscalidad, y cuándo conviene cada uno.",
resumen="""<p><strong>ICO Crecimiento no ofrece leasing</strong>: es un préstamo que el ICO concede directamente a la empresa, que compra la máquina y es su propietaria desde el primer día.</p>
<ul>
  <li><strong>ICO Crecimiento:</strong> hasta el 80 % de la inversión, hasta 10 años con 2 de carencia y sin consumir tus líneas con el banco.</li>
  <li><strong>Leasing:</strong> suele financiar el 100 %, a plazos más cortos y sin carencia, con ventajas fiscales en la amortización.</li>
  <li>En muchos casos lo mejor es <strong>combinarlos</strong> o decidir con los números de cada empresa.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Dos formas de financiar la misma máquina</h2>
<p>Con un <strong>leasing</strong>, el banco o la financiera compra la máquina y te la alquila durante un plazo. Al final, puedes quedártela pagando el valor residual (la opción de compra). Con <strong>ICO Crecimiento</strong>, el ICO te presta el dinero, tú compras la máquina y es tuya desde el primer día; devuelves el préstamo en cuotas.</p>

<h2>Las diferencias principales</h2>
<div class="table-wrap">
<table>
  <thead><tr><th></th><th>ICO Crecimiento</th><th>Leasing</th></tr></thead>
  <tbody>
    <tr><td>Propiedad</td><td>De la empresa desde el inicio</td><td>De la entidad hasta ejercer la opción de compra</td></tr>
    <tr><td>Parte financiada</td><td>Hasta el 80 % de la inversión</td><td>Normalmente el 100 % del precio sin IVA</td></tr>
    <tr><td>Plazo</td><td>Hasta 10 años</td><td>Normalmente de 3 a 7 años</td></tr>
    <tr><td>Carencia</td><td>Hasta 2 años, solo intereses</td><td>Normalmente sin carencia</td></tr>
    <tr><td>IVA</td><td>Se paga entero al comprar y se recupera en el siguiente IVA</td><td>Se paga repartido en cada cuota</td></tr>
    <tr><td>Fiscalidad</td><td>Amortización normal de la máquina</td><td>Parte de la cuota puede deducirse de forma acelerada</td></tr>
    <tr><td>Relación con el banco</td><td>No consume tus líneas bancarias</td><td>Consume riesgo con esa entidad</td></tr>
  </tbody>
</table>
</div>

<h2>Cuándo conviene ICO Crecimiento</h2>
<ul>
  <li>Cuando la máquina tarda en dar resultados: la <strong>carencia de hasta 2 años</strong> da margen para instalarla y ponerla a producir.</li>
  <li>Cuando quieres <strong>cuotas más bajas</strong> gracias a un plazo de hasta 10 años.</li>
  <li>Cuando tus bancos ya tienen mucho riesgo contigo y prefieres <strong>dejar libres tus líneas</strong>.</li>
  <li>Cuando la inversión incluye cosas que un leasing no cubre bien: <strong>instalación, software, formación</strong> o reforma de la nave.</li>
  <li>Cuando además necesitas <strong>circulante</strong>: se puede pedir en la misma solicitud.</li>
</ul>

<h2>Cuándo conviene el leasing</h2>
<ul>
  <li>Cuando no puedes aportar el <strong>20 %</strong> que ICO Crecimiento no financia.</li>
  <li>Cuando el plazo de amortización acelerada te interesa fiscalmente. Consúltalo con tu asesor.</li>
  <li>Cuando la empresa tiene <strong>menos de 4 años</strong> o no cumple otros requisitos de ICO Crecimiento.</li>
  <li>Cuando se trata de <strong>camiones de transporte de mercancías por carretera</strong>, que ICO Crecimiento no financia.</li>
</ul>

<h2>Dos detalles prácticos</h2>
<h3>El IVA</h3>
<p>ICO Crecimiento no financia el IVA que la empresa puede recuperar. Si compras una máquina de 200.000 €, tendrás que adelantar 42.000 € de IVA, que recuperarás en la siguiente declaración. Conviene tenerlo previsto en la tesorería.</p>
<h3>Un leasing ya firmado</h3>
<p>ICO Crecimiento no sirve para cancelar un leasing que ya tengas: en circulante solo permite cancelar deuda a corto plazo, y un leasing de maquinaria suele ser a largo. Sí puede financiar una máquina comprada en los 12 meses anteriores a la solicitud, si se pagó al contado.</p>

<h2>Lo que no se puede financiar</h2>
<p>ICO Crecimiento sí financia vehículos industriales y elementos de transporte de la actividad, pero <strong>no</strong> los camiones de transporte de mercancías por carretera. Tampoco puede pedirlo una empresa cuyo objeto social sea alquilar esos vehículos o equipos a terceros.</p>
""",
faqs=[
("¿ICO Crecimiento ofrece leasing?", "No. ICO Crecimiento es un préstamo directo del ICO a la empresa, que compra la máquina y es su propietaria desde el primer día. Financia hasta el 80 % de la inversión, a hasta 10 años con 2 de carencia."),
("¿Qué es mejor para comprar maquinaria, ICO Crecimiento o leasing?", "Depende de cada empresa. ICO Crecimiento ofrece más plazo, carencia y no consume las líneas del banco; el leasing suele financiar el 100 % y tiene ventajas fiscales en la amortización. Conviene comparar con los números reales."),
("¿Puedo cancelar un leasing con ICO Crecimiento?", "Normalmente no. En circulante, la línea solo permite cancelar deuda a corto plazo, y un leasing de maquinaria suele ser a largo plazo."),
],
))

# ------------------------------------------------------------------ autónomos
NUEVOS.append(dict(
slug="ico-crecimiento-autonomos",
fecha="2026-10-27",
titulo="¿Puede un autónomo pedir ICO Crecimiento? Respuesta y alternativas",
seo="¿Puede un autónomo pedir ICO Crecimiento? No, y alternativas",
desc="ICO Crecimiento es solo para sociedades pyme con 4 años de antigüedad: un autónomo no puede pedirlo. Por qué, qué pasa si creas una SL y qué alternativas hay.",
resumen="""<p><strong>No.</strong> ICO Crecimiento solo admite <strong>sociedades mercantiles pyme</strong> (SL, SA…) con al menos <strong>4 años de antigüedad</strong>. Los autónomos y las comunidades de bienes no pueden ser beneficiarios.</p>
<ul>
  <li>Crear ahora una sociedad <strong>no sirve</strong> para pedirlo: la antigüedad exigida es la de la sociedad que solicita.</li>
  <li>Si eres autónomo, las alternativas son las <strong>líneas ICO de mediación</strong> que se piden en el banco, el aval de una SGR o la financiación bancaria tradicional.</li>
  <li>Si tu negocio ya funciona como sociedad desde hace 4 años o más, entonces sí puede encajar.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Por qué un autónomo no puede pedirlo</h2>
<p>Las condiciones de ICO Crecimiento definen como beneficiarias a las <strong>pymes constituidas como sociedad mercantil</strong>, con actividad en España y con al menos cuatro años de antigüedad. Además, piden cuentas anuales de los dos últimos ejercicios, auditadas o respaldadas por un aval. Un autónomo no deposita cuentas anuales en el Registro Mercantil, así que no encaja en la estructura de la línea.</p>
<p>Esta es una de las confusiones más habituales, también en las respuestas de los asistentes de IA. Muchas líneas ICO <em>sí</em> admiten autónomos, como ICO Empresas y Emprendedores, y es fácil generalizar. ICO Crecimiento no es una de ellas.</p>

<h2>¿Y si creo una sociedad?</h2>
<p>Para esta línea no resuelve el problema a corto plazo. La antigüedad mínima de cuatro años se refiere a la <strong>sociedad que presenta la solicitud</strong>. Una SL recién constituida no la cumple, aunque el negocio lleve años funcionando como autónomo. Convertirse en sociedad puede tener sentido por otros motivos (fiscalidad, responsabilidad, crecimiento), pero consúltalo con tu asesor fiscal y no lo plantees solo para pedir ICO Crecimiento.</p>

<h2>Alternativas si eres autónomo</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Opción</th><th>Cómo se pide</th><th>Para qué encaja</th></tr></thead>
  <tbody>
    <tr><td>Líneas ICO de mediación (por ejemplo, ICO Empresas y Emprendedores)</td><td>En tu banco, si está adherido</td><td>Inversión y liquidez, con condiciones fijadas por el ICO; decide el banco</td></tr>
    <tr><td>Aval de una SGR</td><td>En la SGR de tu comunidad autónoma</td><td>Conseguir un préstamo bancario que solo no te darían, o en mejores condiciones</td></tr>
    <tr><td>Préstamo o póliza bancaria</td><td>En tu banco</td><td>Necesidades puntuales; plazos más cortos</td></tr>
    <tr><td>Ayudas autonómicas</td><td>En el organismo de tu comunidad</td><td>Depende de la convocatoria vigente</td></tr>
  </tbody>
</table>
</div>
<p>Explicamos la diferencia entre las líneas que se piden en el banco y ICO Crecimiento en <a href="../../guias/como-solicitar-un-prestamo-ico/">cómo solicitar un préstamo ICO paso a paso</a>, y cómo funciona una SGR en nuestra <a href="../../guias/aval-sgr/">guía del aval de SGR</a>.</p>

<h2>Si tu negocio ya es una sociedad</h2>
<p>Si facturas a través de una SL o SA con cuatro años o más, ICO Crecimiento puede ser una opción muy interesante: hasta 5 años para circulante o 10 para inversión, sin pasar por el banco. Comprueba en un minuto si cumples el resto de requisitos con nuestro <a href="../../test-ico-crecimiento/">test gratuito</a>.</p>
""",
faqs=[
("¿Un autónomo puede pedir ICO Crecimiento?", "No. ICO Crecimiento solo admite pymes constituidas como sociedad mercantil, con actividad en España y al menos cuatro años de antigüedad. Los autónomos y las comunidades de bienes no pueden ser beneficiarios."),
("Si constituyo una SL, ¿puedo pedir ICO Crecimiento?", "No de inmediato: la antigüedad mínima de cuatro años se exige a la sociedad que solicita, así que una SL recién creada no la cumple aunque el negocio venga de antes."),
("¿Qué préstamos ICO puede pedir un autónomo?", "Las líneas ICO de mediación, como ICO Empresas y Emprendedores, que se solicitan en un banco adherido. En ellas es el banco quien analiza y decide."),
],
))

# ------------------------------------------------------------------ requerimientos
NUEVOS.append(dict(
slug="requerimientos-ico-crecimiento",
fecha="2026-10-30",
titulo="Requerimientos del ICO en ICO Crecimiento: el plazo de 5 días hábiles",
seo="Requerimientos de ICO Crecimiento: plazo de 5 días hábiles",
desc="Tras solicitar ICO Crecimiento, el ICO puede pedir documentos o aclaraciones. Hay 5 días hábiles para responder o la solicitud se da por desistida. Cómo prepararse.",
resumen="""<p>Durante el análisis, el ICO puede enviar <strong>requerimientos</strong>: peticiones de documentos o aclaraciones sobre la solicitud.</p>
<ul>
  <li>Hay <strong>5 días hábiles</strong> para contestarlos.</li>
  <li>Si no se contestan, <strong>o si la notificación electrónica no se abre</strong> en ese plazo, la solicitud se da por <strong>desistida</strong>.</li>
  <li>Si te lo deniegan o desistes, puedes volver a presentarla, pero <strong>entras al final de la cola</strong>, que se atiende por orden de llegada.</li>
  <li>La mejor defensa es un expediente completo desde el primer día.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Qué es un requerimiento</h2>
<p>Una vez presentada la solicitud en ICO Online, el analista del ICO revisa la documentación y la información financiera. Si falta algo o algo no cuadra, envía un requerimiento a través de la plataforma: por ejemplo, unas cuentas de otro ejercicio, el detalle de una partida, la explicación de una caída de ventas o información adicional sobre el proyecto. El ICO puede incluso encargar un informe a un experto independiente.</p>

<h2>El plazo: 5 días hábiles</h2>
<p>Según las condiciones de la línea, los requerimientos se contestan en <strong>5 días hábiles</strong>. Si no se atienden en ese plazo, o si la notificación electrónica no se abre, la solicitud se da por <strong>desistida</strong>. Es uno de los motivos más tontos, y más evitables, por los que se pierde una operación.</p>
<p>Cinco días hábiles es poco tiempo si el documento que piden lo tiene la gestoría, el auditor o el banco, o si coincide con unas vacaciones.</p>

<h2>Cómo prepararse</h2>
<ol class="pasos-guia">
  <li><strong>Designa a un responsable</strong> que revise ICO Online y el correo cada día mientras dure el análisis.</li>
  <li><strong>Ten a mano el «paquete de respaldo»</strong>: cuentas de los últimos ejercicios, impuestos, informe CIRBE reciente, pool bancario, detalle de la deuda y presupuestos de la inversión. La lista está en nuestra <a href="../../guias/documentacion-prestamo-ico/">guía de documentación</a>.</li>
  <li><strong>Haz que las cifras cuadren</strong> entre la memoria, las cuentas y las previsiones. La mayoría de requerimientos nacen de incoherencias.</li>
  <li><strong>Explica de antemano lo que llamará la atención</strong>: un año flojo, una deuda alta o un cambio de actividad. Mejor contarlo en la memoria que esperar a que lo pregunten.</li>
  <li><strong>Evita presentar justo antes de vacaciones</strong> si no vas a poder responder.</li>
</ol>

<h2>Si la solicitud se da por desistida o se deniega</h2>
<p>No cabe recurso administrativo, pero se puede presentar una nueva solicitud una vez corregidos los defectos. El problema es el tiempo: la nueva solicitud entra al final de la cola. Con más de 3.000 solicitudes recibidas (dato de julio de 2026, ver <a href="../../guias/novedades-ico-crecimiento/">novedades</a>), cada vuelta atrás cuenta. Lo explicamos en <a href="../por-que-deniegan-ico-crecimiento/">por qué deniegan ICO Crecimiento</a> y en <a href="../errores-al-solicitar-ico-crecimiento/">los 9 errores más frecuentes</a>.</p>
""",
faqs=[
("¿Cuánto tiempo hay para responder a un requerimiento del ICO?", "Cinco días hábiles. Si no se responde en ese plazo, o si la notificación electrónica no se abre, la solicitud de ICO Crecimiento se da por desistida."),
("¿Qué pasa si mi solicitud de ICO Crecimiento se da por desistida?", "Se puede presentar una nueva solicitud una vez corregidos los defectos, pero entra al final de la cola, que se atiende por orden de llegada."),
("¿Qué suele pedir el ICO en un requerimiento?", "Documentos que faltan o aclaraciones sobre la información financiera y el proyecto: cuentas, detalle de deuda, explicación de variaciones o información adicional sobre la inversión o el circulante."),
],
))

# ------------------------------------------------------------------ software e intangibles
NUEVOS.append(dict(
slug="ico-crecimiento-software-intangibles",
fecha="2026-11-03",
titulo="ICO Crecimiento para software, I+D e intangibles: qué se puede financiar",
seo="ICO Crecimiento para software, I+D e intangibles",
desc="ICO Crecimiento financia intangibles (software, I+D, marca, formación, nuevos mercados) hasta el 80 % a 10 años con 2 de carencia. Qué entra y cómo justificarlo.",
resumen="""<p>Los <strong>intangibles</strong> son una de las grandes diferencias de ICO Crecimiento frente al préstamo bancario: la línea se pensó para empresas viables cuyo valor está en activos que un banco no acepta como garantía.</p>
<ul>
  <li>Financia <strong>software, desarrollo tecnológico, I+D, marcas, formación y apertura de nuevos mercados</strong>.</li>
  <li>Como inversión: <strong>hasta el 80 %</strong>, a <strong>hasta 10 años con 2 de carencia</strong>.</li>
  <li>Se pueden incluir gastos realizados en los <strong>12 meses anteriores</strong> a la solicitud.</li>
  <li>La clave es explicar <strong>qué retorno genera</strong> el intangible y cómo se devolverá el préstamo.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Por qué los intangibles encajan en ICO Crecimiento</h2>
<p>El ICO presentó la línea como una herramienta para pymes con potencial de crecimiento que tienen difícil la financiación bancaria, entre otras razones, por su <strong>perfil innovador o por invertir en intangibles</strong>. Un banco suele pedir garantías sobre lo que financia, y un software a medida o una marca no sirven de garantía. El ICO, en cambio, analiza la viabilidad del proyecto y la capacidad de devolución de la empresa.</p>

<h2>Qué se puede financiar</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Intangible</th><th>Ejemplos</th></tr></thead>
  <tbody>
    <tr><td>Software y digitalización</td><td>ERP, desarrollo de una plataforma propia, comercio electrónico, automatización</td></tr>
    <tr><td>I+D y desarrollo tecnológico</td><td>Desarrollo de nuevos productos o procesos</td></tr>
    <tr><td>Marca y propiedad industrial</td><td>Registro y desarrollo de marca</td></tr>
    <tr><td>Formación</td><td>Capacitación del equipo vinculada al proyecto</td></tr>
    <tr><td>Nuevos mercados</td><td>Apertura comercial en nuevas zonas o canales</td></tr>
  </tbody>
</table>
</div>
<p>Si el proyecto necesita además más equipo o más stock, se puede combinar inversión y <a href="../../guias/ico-crecimiento-circulante/">circulante</a> en la misma solicitud. Tienes más ejemplos en <a href="../que-se-puede-financiar-con-ico-crecimiento/">qué se puede financiar con ICO Crecimiento</a>.</p>

<h2>Ejemplo orientativo</h2>
<p><em>Ejemplo ilustrativo, no es un cliente real.</em> Una empresa de servicios factura 2,5 millones de euros, tiene beneficios y quiere invertir 300.000 € en una plataforma propia que automatice su operación. ICO Crecimiento podría financiar hasta el 80 % (240.000 €) a 10 años, con 2 de carencia mientras la plataforma se desarrolla y empieza a dar resultados. La empresa aporta el 20 % restante. Si parte de la inversión se pagó en los 12 meses anteriores, también puede incluirse.</p>

<h2>Cómo justificarlo bien</h2>
<ul>
  <li><strong>Presupuestos detallados</strong> de proveedores o del equipo interno (horas y coste).</li>
  <li><strong>El retorno esperado</strong>: ahorro de costes, nuevas ventas o margen, con cifras.</li>
  <li><strong>El calendario</strong>: cuándo se desarrolla y cuándo empieza a generar caja, que es la base para pedir la carencia.</li>
  <li><strong>Coherencia con las cuentas</strong>: si la inversión se activa como inmovilizado intangible, cómo y cuándo.</li>
</ul>
<p>Recuerda que hay que cumplir los filtros de solvencia: <a href="../por-que-deniegan-ico-crecimiento/">rating mínimo, sin pérdidas y CIRBE limpia</a>.</p>
""",
faqs=[
("¿ICO Crecimiento financia software?", "Sí. La línea financia intangibles como software, desarrollo tecnológico, I+D, marcas, formación o apertura de nuevos mercados, como inversión de hasta el 80 % a un plazo de hasta 10 años con hasta 2 de carencia."),
("¿Puedo financiar con ICO Crecimiento un software que ya pagué?", "Se pueden incluir inversiones y gastos realizados o iniciados en los 12 meses anteriores a la solicitud, siempre que se justifiquen."),
("¿Necesito garantías para financiar intangibles con ICO Crecimiento?", "La línea no se basa en garantías sobre el activo, sino en la viabilidad del proyecto y la solvencia de la empresa. Si las cuentas no están auditadas, hará falta un aval, normalmente de una SGR."),
],
))

# ------------------------------------------------------------------ ENISA
NUEVOS.append(dict(
slug="ico-crecimiento-o-enisa",
fecha="2026-11-06",
titulo="ICO Crecimiento o ENISA: diferencias y cuál encaja con tu empresa",
seo="ICO Crecimiento o ENISA: diferencias y cuál te conviene",
desc="ICO Crecimiento es un préstamo ordinario para pymes con 4 años y beneficios; ENISA, un préstamo participativo para empresas innovadoras. Diferencias y cuándo elegir cada uno.",
resumen="""<p>Las dos son financiación pública para pymes sin pasar por el banco, pero sirven a empresas distintas:</p>
<ul>
  <li><strong>ICO Crecimiento</strong>: préstamo ordinario del ICO para <strong>sociedades con al menos 4 años</strong>, sin pérdidas y con capacidad de devolución. Circulante e inversión.</li>
  <li><strong>ENISA</strong>: <strong>préstamo participativo</strong> para empresas innovadoras, incluidas jóvenes, con un interés que depende en parte de los resultados.</li>
  <li>En general: empresa consolidada y rentable → ICO Crecimiento; empresa innovadora en fase temprana → ENISA.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Qué es cada una</h2>
<p><strong>ICO Crecimiento</strong> es la línea de financiación directa del Instituto de Crédito Oficial para pymes viables con potencial de crecimiento: desde 50.000 €, circulante hasta 5 años e inversión hasta 10, con un tipo de Euríbor + 1,75 % que baja con aval. Se pide en ICO Online. Todos los detalles están en nuestra <a href="../../guias/ico-crecimiento/">guía de ICO Crecimiento</a>.</p>
<p><strong>ENISA</strong> (Empresa Nacional de Innovación, del Ministerio de Industria) concede <strong>préstamos participativos</strong>: un tipo de préstamo a medio camino entre la deuda y el capital, normalmente sin avales personales, con un interés en parte fijo y en parte ligado a la rentabilidad de la empresa. Se dirige a pymes con proyectos innovadores, incluidas empresas jóvenes. Consulta las líneas y condiciones vigentes en <a href="https://www.enisa.es" rel="noopener">enisa.es</a>.</p>

<h2>Comparativa</h2>
<div class="table-wrap">
<table>
  <thead><tr><th></th><th>ICO Crecimiento</th><th>ENISA</th></tr></thead>
  <tbody>
    <tr><td>Tipo de préstamo</td><td>Ordinario</td><td>Participativo</td></tr>
    <tr><td>Antigüedad</td><td>Sociedad con al menos 4 años</td><td>Admite empresas jóvenes, según la línea</td></tr>
    <tr><td>Resultados</td><td>Sin pérdidas en los dos últimos ejercicios</td><td>Se valora el proyecto innovador y el plan de negocio</td></tr>
    <tr><td>Interés</td><td>Euríbor + 1,75 % (menos con aval)</td><td>Tramo fijo más un tramo variable según resultados</td></tr>
    <tr><td>Finalidad</td><td>Circulante e inversión, incluidos intangibles</td><td>Proyectos de crecimiento e innovación</td></tr>
    <tr><td>Fondos propios</td><td>Patrimonio neto positivo</td><td>Suele exigir fondos propios en proporción al préstamo</td></tr>
    <tr><td>Dónde se pide</td><td>ICO Online</td><td>Web de ENISA</td></tr>
  </tbody>
</table>
</div>
<p class="note">Las condiciones de ENISA varían según la línea y la convocatoria. Compruébalas siempre en su web oficial.</p>

<h2>Cuándo elegir cada una</h2>
<ul>
  <li><strong>ICO Crecimiento</strong> si la empresa tiene trayectoria, gana dinero y necesita circulante o inversión a largo plazo, incluidos <a href="../ico-crecimiento-software-intangibles/">software e intangibles</a>.</li>
  <li><strong>ENISA</strong> si es una empresa innovadora que aún no cumple los requisitos de antigüedad o de resultados de ICO Crecimiento, o si prefiere un préstamo cuyo coste dependa en parte de los resultados.</li>
  <li>Combinar ambas puede ser posible si el proyecto lo justifica. Analízalo caso por caso, porque cada línea tiene sus límites y compatibilidades.</li>
</ul>
<p>Si dudas, el <a href="../../test-ico-crecimiento/">test de requisitos</a> te dice en un minuto si encajas en ICO Crecimiento.</p>
""",
faqs=[
("¿Qué diferencia hay entre ICO Crecimiento y ENISA?", "ICO Crecimiento es un préstamo ordinario para sociedades pyme con al menos cuatro años, sin pérdidas y con capacidad de devolución. ENISA concede préstamos participativos a empresas innovadoras, incluidas jóvenes, con un interés en parte ligado a los resultados."),
("¿Una startup puede pedir ICO Crecimiento?", "Solo si es una sociedad con al menos cuatro años de antigüedad y cumple el resto de requisitos. Para empresas innovadoras más jóvenes, ENISA suele encajar mejor."),
("¿Se pueden pedir ICO Crecimiento y ENISA a la vez?", "Puede ser posible si el proyecto lo justifica, pero hay que revisar los límites y compatibilidades de cada línea en sus condiciones vigentes."),
],
))

# ------------------------------------------------------------------ renovables
NUEVOS.append(dict(
slug="ico-crecimiento-placas-solares-autoconsumo",
fecha="2026-11-10",
titulo="ICO Crecimiento para placas solares y autoconsumo en la empresa",
seo="ICO Crecimiento para placas solares y autoconsumo",
desc="ICO Crecimiento financia instalaciones de renovables para autoconsumo como inversión: hasta el 80 % a 10 años con 2 de carencia. Cómo plantearlo y qué tener en cuenta.",
resumen="""<p>Las <strong>instalaciones de energías renovables para autoconsumo</strong>, como las placas solares en la cubierta de la nave, están entre las inversiones que financia ICO Crecimiento.</p>
<ul>
  <li>Como inversión: <strong>hasta el 80 %</strong>, a <strong>hasta 10 años con 2 de carencia</strong>.</li>
  <li>El ahorro en la factura eléctrica ayuda a <strong>justificar la devolución</strong>.</li>
  <li>El ICO cita la <strong>transición energética</strong> entre los sectores que más solicitudes generan.</li>
  <li>El IVA recuperable no se financia y hay que adelantarlo.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Por qué encaja</h2>
<p>Una instalación de autoconsumo tiene un perfil muy adecuado para ICO Crecimiento: es una inversión con un <strong>ahorro medible</strong> desde el primer mes, una vida útil larga y un retorno que suele cubrir buena parte de la cuota. Con un plazo de hasta 10 años, el ahorro puede igualar o superar lo que se paga cada mes. En julio de 2026 el ICO destacó la transición energética entre los sectores más presentes en las solicitudes (ver <a href="../../guias/novedades-ico-crecimiento/">novedades</a>).</p>

<h2>Ejemplo orientativo</h2>
<p><em>Ejemplo ilustrativo con cifras redondas, no es un cliente real.</em> Una industria invierte 180.000 € en una instalación fotovoltaica en su cubierta. ICO Crecimiento podría financiar hasta el 80 % (144.000 €) a 10 años con 1 o 2 de carencia. La empresa aporta el 20 % y el IVA, que recupera después. Si la instalación ahorra, por ejemplo, 2.000 € al mes en electricidad, ese ahorro es el argumento central de la memoria: demuestra que la inversión se paga sola.</p>

<h2>Qué conviene preparar</h2>
<ul>
  <li><strong>Presupuesto del instalador</strong> con potencia, equipos y plazos.</li>
  <li><strong>Estudio de ahorro</strong> basado en el consumo real de la empresa (facturas de los últimos 12 meses).</li>
  <li><strong>Licencias y permisos</strong> previstos.</li>
  <li><strong>Encaje con el resto del proyecto de crecimiento</strong>: la línea valora el crecimiento y el empleo, no solo el ahorro.</li>
</ul>

<h2>Lo que hay que tener en cuenta</h2>
<ul>
  <li>Hay que cumplir los requisitos generales: sociedad con 4 años, sin pérdidas, patrimonio neto positivo y CIRBE limpia. Revisa <a href="../por-que-deniegan-ico-crecimiento/">los filtros del ICO</a>.</li>
  <li>Si la instalación ya está pagada, se pueden incluir gastos de los <strong>12 meses anteriores</strong> a la solicitud.</li>
  <li>Las ayudas públicas recibidas para la misma instalación deben declararse; lo explicamos en el artículo sobre <a href="../ayudas-de-minimis-ico-crecimiento/">ayudas de minimis</a>.</li>
  <li>Compara con un leasing o renting energético: lo analizamos en <a href="../ico-crecimiento-o-leasing-maquinaria/">ICO Crecimiento o leasing</a>.</li>
</ul>
""",
faqs=[
("¿ICO Crecimiento financia placas solares?", "Sí. Las instalaciones de energías renovables para autoconsumo están entre las inversiones financiables, hasta el 80 % a un plazo de hasta 10 años con hasta 2 de carencia."),
("¿Puedo financiar con ICO Crecimiento una instalación solar que ya hice?", "Se pueden incluir inversiones realizadas o iniciadas en los 12 meses anteriores a la solicitud, siempre que se justifiquen."),
("¿Se financia el IVA de la instalación?", "No se financia el IVA que la empresa puede recuperar: hay que adelantarlo y se recupera en las declaraciones."),
],
))

# ------------------------------------------------------------------ factoring y confirming
NUEVOS.append(dict(
slug="ico-crecimiento-o-factoring-confirming",
fecha="2026-11-13",
titulo="ICO Crecimiento, factoring o confirming: cómo financiar el circulante",
seo="ICO Crecimiento, factoring o confirming para el circulante",
desc="Factoring y confirming financian facturas concretas a corto plazo; ICO Crecimiento financia la necesidad estable de circulante a 5 años. Diferencias y cuándo usar cada uno.",
resumen="""<p>Las tres herramientas financian circulante, pero resuelven problemas distintos:</p>
<ul>
  <li><strong>Factoring</strong>: adelanta el cobro de facturas a clientes. Corto plazo, factura a factura.</li>
  <li><strong>Confirming</strong>: el banco paga a tus proveedores y tú le pagas después. Corto plazo.</li>
  <li><strong>ICO Crecimiento</strong>: un préstamo de <strong>hasta 5 años con 1 de carencia</strong> para la <strong>parte estable</strong> del circulante, la que siempre necesitas para crecer.</li>
  <li>Lo habitual es combinarlas: ICO Crecimiento para la base y factoring o confirming para los picos.</li>
</ul>""",
cuerpo=NOTA_DCG + """
<h2>Tres herramientas, tres problemas</h2>
<div class="table-wrap">
<table>
  <thead><tr><th></th><th>Factoring</th><th>Confirming</th><th>ICO Crecimiento (circulante)</th></tr></thead>
  <tbody>
    <tr><td>Qué financia</td><td>Facturas emitidas a clientes</td><td>Pagos a proveedores</td><td>La necesidad de circulante del negocio</td></tr>
    <tr><td>Plazo</td><td>Días o meses (lo que tarda en cobrarse la factura)</td><td>Días o meses</td><td>Hasta 5 años, con hasta 1 de carencia</td></tr>
    <tr><td>Quién decide</td><td>Banco o entidad de factoring</td><td>Banco</td><td>El ICO</td></tr>
    <tr><td>Consume riesgo bancario</td><td>Sí</td><td>Sí</td><td>No con tus bancos</td></tr>
    <tr><td>Coste</td><td>Comisión + interés por factura</td><td>Normalmente sin coste para quien paga; el proveedor paga si adelanta</td><td>Euríbor + 1,75 % (menos con aval), comisión de apertura del 0,5 %</td></tr>
  </tbody>
</table>
</div>

<h2>El error típico: financiar una necesidad estable con herramientas de corto plazo</h2>
<p>Cuando una empresa crece, necesita <strong>de forma permanente</strong> más stock y más crédito a clientes. Si eso se cubre solo con factoring, confirming y pólizas, la empresa vive renovando líneas cada año y depende de que el banco no las recorte. ICO Crecimiento permite pasar esa base estable a un préstamo de 5 años e, incluso, <a href="../cancelar-deuda-corto-plazo-ico-crecimiento/">cancelar deuda a corto plazo</a>.</p>

<h2>Ejemplo orientativo</h2>
<p><em>Ejemplo ilustrativo, no es un cliente real.</em> Una distribuidora cobra a 90 días y paga a 30. Al crecer un 25 %, su necesidad de circulante sube 300.000 € y la cubre con factoring a coste creciente. Con ICO Crecimiento podría financiar esos 300.000 € a 5 años con 1 de carencia y dejar el factoring solo para los meses de más ventas. Lo desarrollamos en la guía de <a href="../../guias/circulante-distribucion-mayoristas/">circulante para distribución</a>.</p>

<h2>Cuándo usar cada una</h2>
<ul>
  <li><strong>ICO Crecimiento</strong>: para la necesidad de circulante que se mantiene en el tiempo, si la empresa cumple los <a href="../../guias/ico-crecimiento/">requisitos</a>.</li>
  <li><strong>Factoring</strong>: para picos de facturación o clientes grandes que pagan tarde.</li>
  <li><strong>Confirming</strong>: para ordenar los pagos a proveedores y negociar plazos.</li>
</ul>
""",
faqs=[
("¿Es mejor ICO Crecimiento o factoring para el circulante?", "Depende de la necesidad. El factoring adelanta facturas concretas a corto plazo; ICO Crecimiento financia la necesidad estable de circulante con un préstamo de hasta 5 años y 1 de carencia, sin consumir líneas bancarias. Muchas empresas combinan ambos."),
("¿Puedo cancelar líneas de factoring con ICO Crecimiento?", "ICO Crecimiento permite destinar el circulante a cancelar deuda a corto plazo de naturaleza comercial y financiera. Conviene analizar qué parte de la financiación a corto es estable y cuál es estacional."),
("¿ICO Crecimiento consume riesgo con mis bancos?", "No: es un préstamo directo del ICO, así que no utiliza tus líneas bancarias, aunque aparecerá en la CIRBE como cualquier otra deuda."),
],
))
