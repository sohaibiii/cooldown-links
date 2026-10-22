# -*- coding: utf-8 -*-
"""Español neutro, para leerse con naturalidad en España y en Latinoamérica.

Tutea, como tutea la propia app. Los términos salen del catálogo de la app
(Localizable.xcstrings): «Ahorro estimado», «En pausa» (el estado de un artículo
que espera), «periodo de reflexión» (la espera en sí), «bloqueo» (el shield),
«Horas de riesgo», «Modo estricto», «Ventana de compras», «Registro de gastos»,
«Diario». Los nombres de funciones de Apple siguen los de iOS en español, como
hace la app: Ajustes, Tiempo de uso, En familia, Cuenta de Apple, Centro de
control, pantalla de inicio, pantalla bloqueada, Actividades en directo, Atajos,
Movimiento y forma física, modo de concentración.

Las etiquetas `k.*` se copian tal cual del catálogo de la app, nunca se traducen
de nuevo. «On Ice» es un nombre y no se traduce. Si esta traducción y el inglés
difieren, se aplica el inglés.
"""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Ayuda",
"nav.about": "Acerca de",
"nav.privacy": "Privacidad",
"nav.terms": "Términos",
"nav.data": "Tus datos",

"ui.skip": "Ir al contenido",
"ui.pages": "Páginas",
"ui.footer": "Pie de página",
"ui.lang": "Idioma",
"ui.toc": "En esta página",
"ui.rights": "Todos los derechos reservados.",
"ui.store_soon": "Próximamente en el App Store",
"ui.store_get": "Descárgalo en el App Store",
"ui.date": "22 de octubre de 2026",
"ui.last_updated": "Última actualización: {DATE}",

# Copiadas del catálogo de la app (y de iOS), nunca traducidas de nuevo.
"k.settings": "Ajustes",
"k.ios_settings": "Ajustes",
"k.screen_time": "Tiempo de uso",
"k.apps_with_st": "Apps con acceso a Tiempo de uso",
"k.notifications": "Notificaciones",
"k.restore": "Restaurar compras",
"k.protection_tools": "Herramientas de protección",
"k.repair": "Reparar la protección",
"k.someone_key": "Alguien guarda la llave",
"k.only_these": "Solo estas apps",
"k.ai_reflection": "Reflexión con IA",
"k.writer": "Quién escribe la reflexión",
"k.what_gets_sent": "Qué se envía",
"k.lock_journal": "Bloquear diario",
"k.export_journal": "Exportar diario",
"k.delete_entry": "Eliminar entrada",
"k.reflect_week": "Reflexionar sobre mi semana",
"k.help_privacy": "Ayuda y privacidad",
"k.email_support": "Escribir a soporte",
"k.language": "Idioma",
"k.note_it": "Anotarlo",
"k.never_mind": "Mejor no",
"k.need_to_shop": "Necesito comprar ahora",
"k.done_block": "Ya está: bloquéala otra vez",
"k.remove": "Eliminar",
"k.follow_ups": "Preguntas de seguimiento",

"meta.support.title": "On Ice — Ayuda",
"meta.support.desc": "Ayuda oficial de On Ice, la app para iPhone y iPad que pone una noche entre tú y el botón de comprar. Cómo funciona, requisitos, preguntas frecuentes y contacto.",
"meta.about.title": "On Ice — Una noche entre tú y el botón de comprar",
"meta.about.desc": "On Ice bloquea las apps y los sitios web de compras que elijas y te pide que primero lo consultes con la almohada. Sin acceso al banco, sin seguimiento de precios, sin enlaces de afiliado.",
"meta.privacy.title": "Política de Privacidad — On Ice",
"meta.privacy.desc": "On Ice no tiene cuenta, ni conexión bancaria, ni analítica. Qué se queda en tu dispositivo y qué envía exactamente la única función de IA opcional.",
"meta.terms.title": "Términos de Uso — On Ice",
"meta.terms.desc": "Términos de Uso (EULA) de On Ice: qué es la app y qué no, por qué cada cifra es una estimación, cómo se cobran Premium y los planes familiares, y qué te pide el modo estricto.",
"meta.data.title": "Eliminar tus datos — On Ice",
"meta.data.desc": "Cómo borrar lo que guarda On Ice —todo ello en tu dispositivo— y qué pasa con tu suscripción.",
"meta.nf.title": "No encontrado — On Ice",
"meta.nf.desc": "Página no encontrada.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Ayuda",
"s.h1": "Ayuda con On Ice",
"s.sub": "Una noche entre tú y el botón de comprar. On Ice bloquea las apps y los sitios web de compras que elegiste y te pide que primero lo consultes con la almohada. Esta página explica cómo funciona, qué necesita y cómo contactarnos.",
"s.cta": "Leer las preguntas frecuentes",
"s.meta": 'Sin cuenta · sin acceso al banco · <a href="{BASE}{L}/privacy/">Política de Privacidad</a>',

"s.how.h": "Cómo funciona On Ice",
"s.how.b": """
<p class="lead">On Ice pone una noche entre tú y el botón de comprar.</p>
<p>Tú eliges las apps y los sitios web de compras que más te tientan. A partir de entonces, abrir uno no te lleva directamente al pago: primero aparece el bloqueo de On Ice, <em>Pausa antes de comprar.</em> Toca {K_note_it} para dejarlo apuntado, o {K_never_mind} para irte. Nunca se compra ni se cancela nada en tu nombre.</p>
<p>Todo lo que anotas espera en tu lista: veinticuatro horas, salvo que hayas elegido otra duración. Cuando termina la espera, On Ice te hace una sola pregunta: ¿aún lo quieres? La mayoría de los antojos no sobreviven a la noche, y los que sí sobreviven eran de verdad. Cualquiera de las dos respuestas es buena.</p>
<ul class="rows">
  <li><span class="tile">{shield}</span><div><b>Protección</b><span>Un interruptor en la pantalla Inicio y otro para cada tienda. Mientras está activada, las tiendas que elegiste muestran el bloqueo de On Ice en lugar de abrirse: la app <em>y</em> el sitio web, también en Safari.</span></div></li>
  <li><span class="tile">{moon}</span><div><b>Una pausa breve</b><span>Antes de nada, un momento para respirar, escribir una frase, leer un recordatorio o decir a qué venías. Tú eliges cuál, y cuánto dura.</span></div></li>
  <li><span class="tile">{note}</span><div><b>Anótalo</b><span>Ponle nombre, toca un precio aproximado, toca cómo te sientes: aburrimiento, estrés, celebración, FOMO de oferta o «Lo necesito». Una pantalla, quince segundos.</span></div></li>
  <li><span class="tile amber">{snow}</span><div><b>En pausa</b><span>Lo que anotas espera bajo un anillo de cuenta atrás. No se compra nada mientras un artículo se enfría. Si de verdad necesitas la tienda ahora, se abre unos minutos y el bloqueo vuelve por sí solo.</span></div></li>
  <li><span class="tile green">{coin}</span><div><b>Ahorro estimado</b><span>Cada artículo que dejas ir suma a un total acumulado, hecho por completo con precios que escribiste tú: para hoy, esta semana y este mes.</span></div></li>
  <li><span class="tile amber">{clock}</span><div><b>Objetivos, límites y bloqueos</b><span>Un objetivo diario de tiempo de compras, límites diarios, bloqueos programados, bloqueos por modo de concentración y reglas para las horas que peor se te dan. El modo estricto mantiene tu configuración en su sitio.</span></div></li>
  <li><span class="tile">{book}</span><div><b>Algo distinto que hacer</b><span>Un diario privado y algunas cosas que hacer en su lugar —un paseo, un libro, una llamada— para cuando las ganas necesitan una salida.</span></div></li>
  <li><span class="tile">{widget}</span><div><b>Widgets, Actividades en directo y Atajos</b><span>El ahorro estimado y lo que está en pausa en la pantalla de inicio y en la pantalla bloqueada, una cuenta atrás mientras una tienda está abierta, y acciones de Siri y Atajos para iniciar un bloqueo.</span></div></li>
</ul>
""",

"s.requirements.h": "Requisitos",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Dispositivo</th><td>iPhone o iPad con <strong>iOS 17 o posterior</strong>. Algunos extras piden más: los controles del Centro de control necesitan iOS 18, y escribir con Apple Intelligence requiere un dispositivo y un idioma compatibles.</td></tr>
<tr><th>Permiso</th><td>Acceso a <strong>Tiempo de uso</strong>, concedido una vez durante la configuración mediante la propia solicitud de Apple. On Ice usa el framework Tiempo de uso de Apple —el mismo sistema que hay detrás de los límites de apps integrados en iOS— y es Apple, no On Ice, quien de verdad se pone delante de una tienda.</td></tr>
<tr><th>Cuenta</th><td>Ninguna. No hay registro, ni campo de correo, ni contraseña en ninguna parte de la app.</td></tr>
<tr><th>Internet</th><td>No hace falta. Cada bloqueo, pausa, lista, temporizador y total funciona sin conexión. El único tráfico de red es el de Apple cuando compras o restauras Premium, y la reflexión con IA opcional, si la activas y eliges que la escriba OpenAI.</td></tr>
<tr><th>Idiomas</th><td>English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil) y 简体中文. On Ice sigue el idioma de tu dispositivo, o el que elijas en {K_settings} → {K_language}.</td></tr>
<tr><th>Opcional</th><td><strong>Notificaciones</strong>, generadas en el dispositivo, para llevarte del bloqueo a la app y avisarte cuando termina la espera de un artículo. <strong>Movimiento y forma física</strong>, solo para mostrar los pasos en directo durante un paseo. <strong>Face ID o Touch ID</strong>, solo si bloqueas tu diario.</td></tr>
</table></div>
""",

"s.start.h": "Primeros pasos",
"s.start.b": """
<p>La configuración son unas pocas pantallas y termina con la protección ya activada.</p>
<ol class="steps">
  <li><div><b>Prueba una pausa de diez segundos</b>: el mismo momento que te dará el bloqueo más adelante.</div></li>
  <li><div><b>Permite el acceso a Tiempo de uso</b> cuando Apple lo pida. On Ice no puede funcionar sin él, y puedes retirarlo cuando quieras en {K_ios_settings} → {K_screen_time}.</div></li>
  <li><div><b>Elige tus tiendas</b> en el selector de Apple y añade los sitios web de compras que quieras bloquear. On Ice nunca llega a saber los nombres de las apps que eliges; consulta <a href="{BASE}{L}/privacy/#screentime">Privacidad</a>.</div></li>
  <li><div><b>Configura las horas de riesgo</b> si las quieres: esas horas de la noche en las que comprar suele salir peor. Es opcional, y puedes cambiarlo después.</div></li>
  <li><div><b>Listo.</b> Abre una de tus tiendas y verás el bloqueo.</div></li>
</ol>
<div class="callout"><span class="tile">{info}</span><div>El primer bloqueo puede parecer brusco. Ese es justo el momento para el que existe la app: toca {K_note_it} y tómate quince segundos.</div></div>
""",

"s.money.h": "Sobre la cifra de ahorro",
"s.money.b": """
<p>Cada precio en On Ice lo escribiste tú, y cada cifra de dinero que muestra la app lleva la etiqueta <strong>estimado</strong>. No es un aviso añadido a última hora: es todo el diseño.</p>
<ul>
  <li>On Ice <strong>no se conecta a tu banco</strong>, no lee tu historial de compras, no comprueba lo que cuesta realmente nada ni convierte entre monedas.</li>
  <li>Un artículo cuenta para el total <strong>una sola vez</strong>, cuando lo dejas ir tras su espera.</li>
  <li>Si nunca vuelves a un artículo, On Ice te lo recuerda, y 48 horas después de que termine su espera lo cuenta como dejado ir. Puedes decidir en cualquier momento antes de eso.</li>
  <li>Los artículos que te quedas no tocan el total, salvo que más adelante le digas a On Ice que compraste uno por menos de lo que calculabas; en ese caso, cuenta la diferencia.</li>
  <li>El <strong>registro de gastos</strong> es para las compras impulsivas que On Ice nunca vio. Se guarda aparte de tu ahorro.</li>
</ul>
<div class="callout green"><span class="tile">{coin}</span><div>La cifra es un registro de lo que decidiste no comprar, a los precios que calculaste. Es una buena cifra de la que enorgullecerse y una mala cifra para meter en una hoja de cálculo.</div></div>
""",

"s.faq.h": "Preguntas frecuentes",
"s.faq.b": """
<dl class="faq">
<dt>¿On Ice es gratis?</dt>
<dd>Sí, y la versión gratis es un producto que funciona, no una demo: <strong>una app de compras y un sitio web</strong> protegidos, el periodo de reflexión de veinticuatro horas y tu lista, tu ahorro estimado, la pausa de respiración, tres cosas que hacer en su lugar, el diario, un objetivo diario de tiempo de compras, y los bloqueos programados y por modo de concentración.</dd>
<dt>¿Qué añade Premium?</dt>
<dd>Todas las tiendas y sitios web que quieras proteger; esperas de 12, 24, 48 o 72 horas; todos los tipos de pausa, pausas que se alargan con los intentos repetidos y tus propios recordatorios; reglas de horas de riesgo y por tienda; límites diarios; modo estricto; tus patrones de compra y cómo te sentiste después de comprar; un repaso de tu diario; seis cosas que hacer en su lugar; widgets; y la reflexión con IA opcional. Premium es una suscripción mensual o anual —la anual empieza con una <strong>prueba gratuita</strong> donde se ofrezca— o una compra única de por vida, y la anual y la de por vida también existen como <strong>planes familiares</strong>. Los precios se muestran en la app para tu país, y el cobro lo gestiona Apple.</dd>
<dt>¿Cómo funcionan los planes familiares?</dt>
<dd>Premium familiar anual y Premium familiar de por vida se comparten mediante En familia de Apple con hasta otras cinco personas de tu grupo familiar: seis en total. Cada persona recibe Premium en su propia copia de On Ice, en su propio dispositivo. Nadie ve las tiendas, la lista, el diario ni el ahorro de nadie más.</dd>
<dt>¿Me impide comprar cosas?</dt>
<dd>No. Un bloqueo normal es una pausa, no un muro: toca {K_note_it}, di qué te llamó la atención, y {K_need_to_shop} abre la tienda unos minutos. {K_done_block} la vuelve a cerrar antes de tiempo. Lo único que no tiene paso es lo que configuras tú —una regla de bloqueo total, un límite diario ya alcanzado, un bloqueo programado o un bloqueo por modo de concentración—, y cada uno termina por sí solo.</dd>
<dt>¿Qué pasa si mi suscripción caduca?</dt>
<dd>No se te quita nada de lo que construiste. Tu lista, tu historial y tu ahorro estimado se quedan, las tiendas que elegiste siguen protegidas, y tus reglas, tus límites y un modo estricto en curso siguen en pie. Tu espera vuelve a 24 horas, la reflexión con IA se desactiva, y los widgets y las pantallas de patrones esperan a que vuelva Premium. Simplemente no puedes añadir más funciones Premium.</dd>
<dt>¿Puedo restaurar una compra en un dispositivo nuevo?</dt>
<dd>Sí. Abre {K_settings} y toca {K_restore}. Premium pertenece a tu Cuenta de Apple, no al dispositivo. Tu lista, tu diario y tu historial no viajan con él: viven en el dispositivo que los creó, y solo pasan a uno nuevo con una copia de seguridad de todo el dispositivo.</dd>
<dt>¿Funciona en iPad?</dt>
<dd>Sí: iPhone y iPad, con iOS 17 o posterior. Cada dispositivo guarda sus propias tiendas, su lista y su historial; nada se sincroniza entre ellos.</dd>
<dt>¿Por qué On Ice no puede decirme qué apps protegí?</dt>
<dd>Porque de verdad no lo sabe. Tiempo de uso de Apple le entrega a On Ice tokens opacos que no significan nada fuera de tu dispositivo: sin nombres de apps, sin identificadores. On Ice puede pedirle a iOS que los bloquee, e iOS te muestra sus nombres e iconos; On Ice no puede leerlos. Los sitios web que añades escribiendo una dirección son la excepción: On Ice guarda esa dirección en tu dispositivo para que iOS pueda bloquearla.</dd>
<dt>¿Bloquea sitios web, o solo apps?</dt>
<dd>Las dos cosas. Añade por separado la app de una tienda y su sitio web, y cada uno queda bloqueado; el sitio web, en Safari.</dd>
<dt>¿On Ice ve lo que compro?</dt>
<dd>No. No tiene acceso a tu banco, tus pedidos, tu navegación ni tu tarjeta. Solo registra sus propios eventos —que se mostró un bloqueo y qué elegiste— y los guarda en tu dispositivo.</dd>
<dt>¿Mi diario sale de mi dispositivo?</dt>
<dd>Nunca. Ni hacia nosotros, ni hacia OpenAI, ni con ningún ajuste. Puedes bloquearlo con Face ID, Touch ID o tu código, y su resumen semanal opcional lo escribe Apple Intelligence en tu dispositivo.</dd>
<dt>¿Adónde van mis pasos al caminar?</dt>
<dd>A ninguna parte. Durante un paseo, On Ice muestra tus pasos en directo y los olvida cuando el paseo termina. No lee ni escribe nada en la app Salud de Apple.</dd>
<dt>¿Qué es la reflexión con IA, y está activada?</dt>
<dd>Es una pregunta breve antes de las opciones, de vez en cuando, y unas frases sobre tu semana los domingos. Está <strong>desactivada hasta que la actives</strong>. Tú eliges quién la escribe: <strong>Apple Intelligence</strong>, en tu dispositivo, u <strong>OpenAI</strong>, lo único de la app que envía algo fuera del dispositivo. La <a href="{BASE}{L}/privacy/#ai">Política de Privacidad</a> enumera exactamente qué.</dd>
</dl>
""",

"s.trouble.h": "Solución de problemas",
"s.trouble.b": """
<h3>Una tienda se abre sin bloqueo</h3>
<ul>
  <li>Comprueba que la protección está activada arriba en la pantalla Inicio, y que el interruptor de esa tienda también lo está.</li>
  <li>Comprueba que el acceso a Tiempo de uso sigue concedido: {K_ios_settings} → {K_screen_time} → {K_apps_with_st}. Si se retiró, On Ice muestra una pantalla con una forma de volver a pedirlo.</li>
  <li>Puede que siga abierta una <strong>ventana de compras</strong> que abriste. Se cierra sola —o toca {K_done_block}— y el bloqueo vuelve.</li>
  <li>Si la tienda solo está cubierta por una <strong>regla</strong>, el bloqueo aparece solo durante las horas de esa regla.</li>
  <li>¿Sigue sin aparecer? {K_settings} → {K_protection_tools} → {K_repair} vuelve a aplicar todos los bloqueos y horarios.</li>
</ul>
<h3>Tocar «Anotarlo» no abre On Ice</h3>
<ul>
  <li>En algunas versiones de iOS, el bloqueo te pasa a la app mediante una notificación. Si las notificaciones están desactivadas, iOS no puede entregarla: actívalas en {K_ios_settings} → {K_notifications} → On Ice.</li>
  <li>Abrir On Ice directamente también recoge el artículo que está pendiente de anotar.</li>
</ul>
<h3>Un sitio web no está bloqueado</h3>
<p>Los sitios web se bloquean por dirección. Asegúrate de que la dirección que añadiste coincide con la que abres de verdad, y recuerda que la app de una tienda y su sitio web son dos cosas distintas que hay que añadir.</p>
<h3>Mi objetivo o mi límite diario muestra menos minutos de los que esperaba</h3>
<p>iOS no les dice a las apps cuánto tiempo pasaste en otra app. Solo le avisa a On Ice cuando el tiempo en tus tiendas protegidas supera un tramo —cada cinco minutos al principio—, así que On Ice muestra «al menos» esos minutos. La cifra real puede ser un poco mayor.</p>
<h3>No puedo desactivar la protección ni quitar una tienda</h3>
<p>Comprueba si está en marcha el <strong>modo estricto</strong>, un <strong>bloqueo programado</strong> o un <strong>bloqueo por modo de concentración</strong>: la pantalla Inicio lo indica. Mientras el modo estricto está en marcha, tu configuración se mantiene en su sitio a propósito, y el modo estricto termina por sí solo a la hora que elegiste. Si configuraste {K_someone_key}, la persona que tiene el PIN puede terminarlo antes.</p>
<h3>La pregunta de IA nunca aparece</h3>
<p>Necesita Premium, y está desactivada hasta que la actives en {K_settings} → {K_ai_reflection}. Aun así, solo pregunta cuando hay un motivo: una emoción que a menudo ha acabado en arrepentimiento, una hora de riesgo o un precio más alto. Si la escribe OpenAI, necesita conexión a internet. Si algo falla, te muestra sin más las opciones habituales.</p>
<h3>Los widgets van con retraso</h3>
<p>iOS actualiza los widgets según su propio calendario. Abrir On Ice los pone al día. Los widgets de ahorro y «En pausa» vienen con Premium.</p>
<h3>Premium no se reconoce</h3>
<p>Toca {K_restore} en {K_settings}, y asegúrate de que el dispositivo tiene iniciada la sesión con la misma Cuenta de Apple que hizo la compra o, si es un plan familiar, de que estás en el grupo de En familia de quien lo compró. Los reembolsos y las dudas de facturación los gestiona Apple a través del <a href="https://support.apple.com/billing">Soporte de Apple</a>.</p>
<h3>La app está en el idioma equivocado</h3>
<p>Elige uno en {K_settings} → {K_language}. El selector de apps de Apple se actualiza la próxima vez que abras On Ice.</p>
""",

"s.contact.h": "Contacto",
"s.contact.b": """
<p>Dudas, un fallo, o algo que debería funcionar y no funciona: escríbenos y te responderá una persona. Lo más rápido es {K_settings} → {K_help_privacy} → {K_email_support}, que añade por ti la versión de On Ice, la versión de iOS y el modelo de tu dispositivo.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Incluye el modelo de tu dispositivo, la versión de iOS y qué esperabas que pasara. Nunca nos envíes tu lista, tus precios ni tu diario: no los necesitamos y preferimos no tenerlos.</span></div></div>
<p class="small">La facturación, los reembolsos y los cambios de suscripción los gestiona Apple: <a href="https://apps.apple.com/account/subscriptions">gestionar suscripciones</a> · <a href="https://support.apple.com/billing">solicitar un reembolso</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "Acerca de On Ice",
"a.h1": "Una noche entre tú y el botón de comprar.",
"a.sub": "Elige las apps y los sitios web de compras que más te tientan. A partir de entonces, al abrir uno te encuentras primero con un bloqueo, y con una decisión que le toca tomar a tu yo de mañana.",
"a.cta": "Ayuda",
"a.meta": "Sin cuenta · sin acceso al banco · iPhone y iPad, iOS 17+ · 8 idiomas",
"a.lead": "On Ice pone una noche entre tú y el botón de comprar. No es un cerrojo ni un sermón: es una pausa breve, y tiempo para descubrir si de verdad lo querías. Aquí nada te regaña por querer cosas, y nada se pone en rojo si lo compras.",

"a.f1.h": "Pausa antes de comprar.",
"a.f1.p": "Abre una tienda que hayas elegido y On Ice interviene antes de que llegues al pago, en la app y en Safari. Respira hondo, escribe una frase, lee un recordatorio o di a qué venías.",
"a.f2.h": "Anótalo, no lo compres.",
"a.f2.p": "Ponle nombre, toca un precio aproximado, toca cómo te sientes. Quince segundos, una pantalla. Anotarlo tiene que ser más rápido que el antojo.",
"a.f3.h": "Una noche en pausa.",
"a.f3.p": "Lo que anotas espera bajo un anillo de cuenta atrás: 24 horas, o lo que quieras entre 12 y 72. No se compra nada mientras un artículo se enfría, y la decisión es de tu yo de mañana.",
"a.f4.h": "Mira cómo suma.",
"a.f4.p": "Cada artículo que dejas ir suma a tu ahorro estimado —tus propios cálculos, para hoy, esta semana y este mes—, junto a las horas en las que más te encuentras con los bloqueos.",
"a.f5.h": "Algo distinto que hacer.",
"a.f5.p": "Cuando las ganas necesitan una salida: un paseo con los pasos en directo, un libro, una lista de reproducción, una llamada. Elige lo que te funcione y empiézalo con un toque.",
"a.f6.h": "Más firme cuando lo quieras.",
"a.f6.p": "Un objetivo diario de tiempo de compras, límites diarios, bloqueos programados y por modo de concentración, reglas de horas de riesgo para altas horas de la noche, y el modo estricto para mantenerlo todo en su sitio.",
"a.f7.h": "Un diario solo para ti.",
"a.f7.p": "Una pregunta al día y un lugar donde escribir. Bloquéalo con Face ID. Nada de lo que contiene sale nunca de tu dispositivo.",
"a.f8.h": "Nunca ve lo que compras.",
"a.f8.p": 'Sin vinculación bancaria, sin historial de compras, sin seguimiento de precios, sin enlaces de afiliado, sin analítica. Apple le da a On Ice códigos, no nombres. <a href="{BASE}{L}/privacy/">Cómo funciona eso.</a>',

"a.price.h": "Lo que cuesta",
"a.price.b": """
<p>La versión gratis es un producto que funciona, no una demo, y no se te quita nada de lo que ya hayas construido si una suscripción caduca.</p>
<div class="tiers">
  <div class="tier"><div class="lbl">Gratis</div><div class="price">Sin cargo</div><ul><li>Una app de compras y un sitio web, protegidos</li><li>El periodo de reflexión de 24 horas y tu lista</li><li>Tu ahorro estimado</li><li>La pausa de respiración y tres cosas que hacer en su lugar</li><li>El diario, un objetivo diario, y bloqueos programados y por modo de concentración</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Mensual · Anual · De por vida</div><ul><li>Todas las tiendas y sitios web que quieras</li><li>Esperas de 12, 24, 48 o 72 horas</li><li>Todos los tipos de pausa, y tus propios recordatorios</li><li>Horas de riesgo, reglas por tienda, límites diarios y modo estricto</li><li>Tus patrones de compra, y cómo te sentiste después de comprar</li><li>Widgets, un repaso de tu diario y la reflexión con IA opcional</li><li>El plan anual empieza con una prueba gratuita; el anual y el de por vida también existen como planes familiares para hasta seis personas</li></ul></div>
</div>
<p class="small">Los precios se muestran en la app y en el App Store para tu país. El cobro lo gestiona Apple. <a href="{BASE}{L}/terms/#subscriptions">Condiciones de la suscripción.</a></p>
""",

"a.st.h": "Construido sobre Tiempo de uso de Apple",
"a.st.b": """
<p>On Ice usa el mismo framework que hace funcionar los límites de apps integrados en iOS. Apple solo se lo concede a apps que ha revisado para ese fin, y es Apple —no On Ice— quien de verdad se interpone entre tú y la tienda. Por eso On Ice puede bloquear una app sin llegar a saber nunca su nombre.</p>
<p>iPhone y iPad · iOS 17 o posterior · English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil), 简体中文</p>
""",

"a.est.h": "Cada cifra es una estimación",
"a.est.b": """
<p>On Ice te pregunta cuánto cuesta algo más o menos y recuerda tu respuesta. No se conecta a ningún banco, no verifica ningún precio, no convierte ninguna moneda y no da ningún consejo financiero. Cada número que muestra lleva la palabra <em class="est">estimado</em>: en la app, en los widgets y en este sitio.</p>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Política de Privacidad",
"p.h1": "Nunca ve lo que compras.",
"p.sub": "Sin cuenta, sin vinculación bancaria, sin historial de compras, sin seguimiento de precios y sin analítica. Lo que On Ice sabe se queda en tu dispositivo, con una función opcional, desactivada hasta que la actives, cuyo contenido exacto se detalla más abajo.",
"p.meta": "En vigor desde el {DATE} · se aplica a la app On Ice para iPhone y iPad, y a este sitio",

"p.summary.h": "La versión corta",
"p.summary.b": """
<p class="lead"><strong>On Ice no tiene cuenta, ni analítica, ni publicidad, ni código de terceros.</strong> No hay conexión bancaria, ni historial de compras, ni seguimiento de precios, ni enlaces de afiliado en ninguna parte. Todo lo que sabe se escribe en tu iPhone o iPad y se queda ahí.</p>
<div class="callout"><span class="tile">{eye-off}</span><div>Las apps que eliges en el selector de Tiempo de uso de Apple le llegan a On Ice como tokens opacos que solo tu dispositivo puede interpretar. No hay nombre de app, ni identificador, ni nada que enviar.</div></div>
<p>Hay exactamente una excepción, y está desactivada hasta que la actives: la <strong>reflexión con IA</strong> opcional. Si la escribe <strong>Apple Intelligence</strong>, se ejecuta en tu dispositivo y no sale nada. Si la escribe <strong>OpenAI</strong>, sale una lista breve y fija de datos, que se detalla por completo <a href="#ai">más abajo</a>. Tu diario nunca sale del dispositivo, elijas la opción que elijas para escribirla.</p>
<p>Esta política se aplica a la app On Ice para iPhone y iPad, publicada por {COMPANY}, y a este sitio web.</p>
""",

"p.collect.h": "Qué recopilamos",
"p.collect.b": """
<p>«Recopilar», en el sentido de Apple y en el nuestro, significa enviar datos fuera del dispositivo y guardarlos en algún sitio de forma no pasajera. Con la reflexión con IA desactivada —que es como empieza cada instalación—, On Ice no envía nada sobre ti a ninguna parte. La tabla muestra qué cambia si la activas y eliges que la escriba OpenAI.</p>
<div class="table-wrap"><table>
<tr><th>Categoría</th><th>¿Se envía?</th><th>Qué significa</th></tr>
<tr><td>Información financiera</td><td>Solo con las reflexiones de OpenAI activadas</td><td>Sin conexión bancaria, sin tarjeta, sin acceso a transacciones, sin historial de compras. Con las reflexiones de OpenAI activadas, se envían un <em>rango de precio</em> del artículo que tienes delante y un total semanal redondeado de ahorro estimado; nunca un precio exacto, una cuenta ni un saldo.</td></tr>
<tr><td>Datos de contacto</td><td>No</td><td>No hay cuenta, ni inicio de sesión, ni campo de correo en ninguna parte de la app.</td></tr>
<tr><td>Identificadores</td><td>Solo con las reflexiones de OpenAI activadas</td><td>Sin ID de usuario, sin identificador de publicidad, y On Ice nunca te pide permiso para rastrearte. Nuestro servicio de IA ve un identificador aleatorio de clave de App Attest, que se usa solo para contar las solicitudes por dispositivo y día, y se borra a los dos días.</td></tr>
<tr><td>Datos de uso</td><td>Solo con las reflexiones de OpenAI activadas</td><td>Sin analítica y sin eventos de interacción con el producto. Los bloqueos, las pausas y las decisiones se cuentan en tu dispositivo, para tus propias pantallas. Una reflexión incluye el recuento de bloqueos de hoy; el resumen semanal incluye los recuentos de la semana.</td></tr>
<tr><td>Contenido del usuario</td><td>Solo con las reflexiones de OpenAI activadas</td><td>Tu lista, tus precios, tu diario, tu registro de gastos y tus recordatorios se quedan en el dispositivo. Si la reflexión la escribe OpenAI, se envían el nombre del artículo que tienes delante y lo que escribas como respuesta a la pregunta.</td></tr>
<tr><td>Historial de navegación</td><td>No</td><td>On Ice no puede ver lo que navegas. Solo sabe que se mostró su propio bloqueo y qué elegiste en él.</td></tr>
<tr><td>Ubicación, salud, forma física, contactos, búsquedas, diagnósticos</td><td>No</td><td>Los pasos durante un paseo se muestran en directo y nunca se guardan ni se envían. On Ice no tiene ningún informe propio de fallos ni de rendimiento.</td></tr>
</table></div>
<p><strong>Seguimiento:</strong> ninguno. On Ice no vincula nada sobre ti con datos de apps o sitios web de otras empresas, y no comparte nada con intermediarios de datos ni anunciantes. <strong>No hay enlaces de afiliado</strong>: On Ice no gana nada cuando compras algo, que es el único acuerdo compatible con una app cuyo trabajo es ayudarte a comprar menos.</p>
""",

"p.device.h": "Qué se queda en tu dispositivo",
"p.device.b": """
<p>On Ice guarda lo siguiente en su propio almacenamiento privado de tu iPhone o iPad, protegido por el código y el cifrado de tu dispositivo. Nada de ello se sube, ni se sincroniza con iCloud, ni lo respaldamos nosotros, ni es visible para nosotros.</p>
<ul>
  <li><strong>Tus tiendas</strong>: las apps y categorías, como tokens opacos de Tiempo de uso que On Ice no puede leer, y los sitios web que añadiste por dirección, como esa dirección (ver más abajo).</li>
  <li><strong>Tu lista</strong>: los nombres de artículos que escribiste, los precios que estimaste, la emoción que tocaste, y cuándo se anotó y se decidió cada artículo.</li>
  <li><strong>Lo que pasó en cada bloqueo</strong>: que se mostró, cuándo, y si te fuiste, esperaste, abriste la tienda, dejaste ir el artículo o te lo quedaste, y a qué dijiste que venías. De esto están hechos tu ahorro estimado, tus rachas y tus patrones.</li>
  <li><strong>Lo que añades tú</strong>: el registro de gastos, cómo te sentiste después de una compra, tu diario, tus propios recordatorios y las cosas que elegiste hacer en su lugar, incluido cualquier enlace a una app o dirección web que le hayas asignado a alguna.</li>
  <li><strong>Tus reglas y ajustes</strong>: horas de riesgo, reglas por tienda, tu objetivo diario y tus límites, bloqueos, el estado del modo estricto, tu pausa, la hora a la que empieza tu día, tu idioma y quién elegiste que escriba la reflexión con IA. Si alguien guarda la llave de tu modo estricto, solo se almacena un hash unidireccional con sal de su PIN, nunca el PIN.</li>
  <li><strong>Tramos de uso</strong>: el tramo de tiempo más alto que iOS ha informado hoy para tus tiendas protegidas, para tu objetivo y tus límites (ver más abajo).</li>
  <li><strong>Tu estado de Premium</strong>: el plan y cuándo se renueva o termina, para que la app sepa qué desbloquear.</li>
  <li><strong>El último resumen semanal</strong>: solo mientras la reflexión con IA está activada.</li>
</ul>
<p>Si usas la copia de seguridad de iCloud o una copia de seguridad local cifrada, Apple puede incluir los datos de On Ice en esa copia bajo tu propia Cuenta de Apple y las condiciones de privacidad de Apple. Nosotros no tenemos acceso a ella.</p>
""",

"p.journal.h": "Tu diario",
"p.journal.b": """
<p>El diario es el único lugar de On Ice donde escribes para nadie. Las entradas —y el estado de ánimo, el artículo o la emoción que tengan asociados— se guardan en tu dispositivo y <strong>nunca salen de él</strong>: ni con la reflexión con IA, ni con OpenAI, ni con ningún ajuste.</p>
<ul>
  <li>{K_lock_journal} pide Face ID, Touch ID o el código de tu dispositivo antes de abrir el diario, y lo vuelve a cerrar cuando sales de la app. Es iOS quien hace la comprobación; On Ice nunca ve tu cara, tu huella ni tu código. El bloqueo protege la pantalla; las entradas en sí están protegidas por el propio cifrado de tu dispositivo, como el resto de los datos de On Ice.</li>
  <li>{K_reflect_week} resume tus entradas recientes con Apple Intelligence, <em>en tu dispositivo</em>. No existe una versión en servidor.</li>
  <li>{K_export_journal} crea un archivo de texto sin formato y se lo entrega a iOS, para que elijas dónde guardarlo. On Ice no lo envía a ninguna parte.</li>
  <li>El widget del diario solo muestra la pregunta del día. Nunca lee una entrada.</li>
</ul>
""",

"p.permissions.h": "Lo que On Ice pide usar",
"p.permissions.b": """
<p>iOS pide cada uno de estos permisos con sus propias palabras, y cada uno se puede cambiar en {K_ios_settings} cuando quieras.</p>
<div class="table-wrap"><table>
<tr><th>Permiso</th><th>Por qué</th><th>¿Hace falta?</th></tr>
<tr><td>Tiempo de uso</td><td>Para bloquear las tiendas que elijas, aplicar tus bloqueos, reglas y límites, y recibir los tramos de uso.</td><td>Sí: On Ice no puede funcionar sin él.</td></tr>
<tr><td>Notificaciones</td><td>Para llevarte del bloqueo a la app, para avisarte cuando la espera de un artículo ha terminado o está a punto de terminar, y para las preguntas de seguimiento, los temporizadores de actividades y las sugerencias que dejes activados.</td><td>No</td></tr>
<tr><td>Movimiento y forma física</td><td>Para mostrar tus pasos en directo durante un paseo. El sensor de movimiento solo se usa mientras hay un paseo en pantalla, y los pasos nunca se guardan ni se envían.</td><td>No; solo si empiezas un paseo</td></tr>
<tr><td>Face ID o Touch ID</td><td>Para desbloquear el diario, si lo bloqueas.</td><td>No</td></tr>
</table></div>
<p>Cuando eliges qué abre una «cosa que hacer en su lugar», On Ice le pregunta a iOS si están instaladas las apps de una lista breve —Libros, Kindle, Audible, Podcasts, Música, Spotify, Duolingo, Headspace, Calm, Notas, Mensajes y Atajos— para poder ofrecerte las que tienes. La respuesta se usa en el momento para crear esa lista; ni se guarda ni se envía.</p>
""",

"p.screentime.h": "Tiempo de uso y tus tiendas",
"p.screentime.b": """
<p>On Ice está construido sobre el framework Tiempo de uso de Apple (Family Controls, Managed Settings y Device Activity). Le concedes acceso una vez, mediante la propia solicitud de Apple, y puedes retirarlo cuando quieras en {K_ios_settings} → {K_screen_time}.</p>
<p>Cuando eliges apps, categorías o sitios web en el selector de Apple, este devuelve <strong>tokens</strong>: valores que los identifican ante iOS pero que no significan nada para On Ice ni fuera de tu dispositivo. On Ice guarda esos tokens para poder pedirle a iOS que bloquee lo que elegiste; iOS te muestra sus nombres e iconos. On Ice nunca recibe un identificador de paquete ni un nombre de app. Cuando sus propios componentes necesitan comparar tokens, comparan hashes unidireccionales de ellos, nunca los tokens en sí.</p>
<p><strong>Los sitios web que añades por dirección son distintos.</strong> Un sitio que escribes, o que eliges entre las sugerencias de On Ice, se guarda como esa dirección —<code>example.com</code>— porque iOS la necesita para bloquear el sitio. Se queda en tu dispositivo con todo lo demás y nunca se envía.</p>
<p><strong>El uso se informa por tramos.</strong> iOS nunca le da a On Ice un total de tu tiempo de uso. Solo le avisa cuando el tiempo en tus tiendas protegidas supera un tramo registrado de antemano —cinco minutos, diez, quince…—, lo que basta para un objetivo diario y un límite, y nada más.</p>
<p>On Ice no observa tu navegación, tus mensajes ni lo que haces dentro de ninguna app. Es iOS quien muestra el bloqueo y lo aplica. On Ice solo sabe que se mostró su propio bloqueo y qué elegiste en él.</p>
""",

"p.ai.h": "La reflexión con IA: lo único que puede salir",
"p.ai.b": """
<p class="lead">La reflexión con IA es una función Premium opcional. <strong>Está desactivada cuando instalas On Ice y sigue desactivada hasta que la actives</strong> en {K_settings} → {K_ai_reflection}.</p>
<p>Con ella activada, algunos artículos anotados reciben una pregunta breve antes de que elijas; no todos, solo cuando hay un motivo: una emoción que a menudo ha acabado en arrepentimiento, una hora de riesgo o un precio más alto. Los domingos también puede escribir unas frases sobre tu semana.</p>
<h3>Dos opciones para escribirla, y solo una sale del dispositivo</h3>
<ul>
  <li><strong>Apple Intelligence</strong> escribe en tu dispositivo. No se envía nada a ninguna parte. Si Apple Intelligence deja de estar disponible, On Ice te muestra las opciones habituales; <strong>nunca recurre a un servidor</strong>.</li>
  <li><strong>OpenAI</strong> escribe en los servidores de OpenAI, a través del servicio propio de On Ice. Solo se envía lo que se detalla abajo.</li>
</ul>
<p>Lo eliges en {K_writer}. Si activas la reflexión con IA sin elegir, On Ice usa Apple Intelligence donde tu dispositivo y tu idioma lo admiten, y OpenAI donde no.</p>
<h3>Qué se envía si la escribe OpenAI</h3>
<p>Para una pregunta:</p>
<ul>
  <li>El <strong>nombre del artículo</strong> que acabas de escribir, y lo que escribas como respuesta a la pregunta.</li>
  <li>Un <strong>rango de precio</strong> —un rango como «250 a 500», nunca la cantidad que escribiste— y tu moneda.</li>
  <li>La <strong>emoción</strong> que tocaste, si tocaste alguna.</li>
  <li>La <strong>hora y los minutos</strong> de tu reloj. Sin fecha ni zona horaria.</li>
  <li><strong>Cuántas veces te has encontrado hoy con un bloqueo de compras.</strong></li>
  <li>Tu propia <strong>tasa de arrepentimiento para esa emoción</strong>, como porcentaje, y solo cuando hayas valorado al menos cinco compras.</li>
  <li>Tu <strong>idioma</strong>, por ejemplo «Español (España)», para que la pregunta llegue en él.</li>
</ul>
<p>Para el resumen semanal, <strong>solo recuentos y totales</strong>: los bloqueos que encontraste; los artículos que pusiste en espera, que dejaste ir o que te quedaste, y aquellos a los que te resististe; cuántas veces abriste una tienda; tu racha actual y tu mejor racha; tu hora más concurrida; la proporción de artículos que dejaste ir; tu ahorro estimado de la semana, redondeado a un número entero y con su moneda; la fecha en que empezó la semana, y tu idioma. <strong>Ni nombres de artículos ni precios individuales.</strong></p>
<h3>Qué no se envía nunca</h3>
<ul>
  <li>Tokens de Tiempo de uso ni sus hashes, identificadores de paquete ni direcciones de sitios web.</li>
  <li>Qué tiendas o sitios web proteges, ni cuántos.</li>
  <li>El precio exacto que escribiste.</li>
  <li>Nada más de tu lista: ni nombres ni precios.</li>
  <li>Tu registro de gastos, ni el precio de ninguna compra individual.</li>
  <li>Cómo valoraste ninguna compra individual.</li>
  <li>Tu diario, tus reglas, límites, bloqueos, horas de riesgo ni el estado del modo estricto.</li>
  <li>Ningún nombre, cuenta, correo ni identificador de publicidad: nada que te identifique como persona.</li>
</ul>
<h3>Adónde va y cuánto tiempo se guarda</h3>
<p>Las solicitudes van al <strong>servicio propio de On Ice, alojado en Cloudflare</strong>, y de ahí a <strong>OpenAI</strong>, que ejecuta el modelo. Dentro de la app no hay ninguna clave de API que se pueda extraer, y la app nunca llama directamente a OpenAI.</p>
<p>Antes de responder, el servicio usa <strong>App Attest de Apple</strong> para comprobar que la solicitud viene de una copia auténtica de On Ice. Esa comprobación se basa en una clave creada en tu dispositivo, no en tu nombre ni en tu Cuenta de Apple. <strong>El servicio no guarda ninguna pregunta, respuesta ni dato de ningún artículo.</strong> Guarda un recuento de solicitudes por dispositivo y día, bajo ese identificador de clave aleatorio, y lo borra a los dos días; totales diarios de solicitudes y de uso del modelo para todo el servicio, que no nombran ningún dispositivo, durante unos 90 días; y un registro de cada desafío de App Attest de un solo uso hasta que caduca. Sus registros anotan el estado de una solicitud, cuánto tardó y cuántos tokens usó, nunca su contenido.</p>
<p><strong>OpenAI no usa estos datos para entrenar sus modelos.</strong> Desactivamos el almacenamiento de respuestas de OpenAI; aun así, OpenAI puede conservar entradas y salidas en sus registros de supervisión de abusos, normalmente hasta 30 días, con excepciones según sus propias condiciones. No prometemos que tu texto se procese en ningún país en concreto.</p>
<p><strong>Las versiones anteriores de On Ice</strong> envían, en su lugar, los mismos tipos de datos al <strong>modelo Gemini de Google en Vertex AI</strong>, a través de un servicio anterior de On Ice en Google Cloud que tampoco guarda contenido. Google no los usa para entrenar sus modelos, puede conservarlos hasta 24 horas y puede registrarlos para comprobar si hay abusos.</p>
<div class="callout"><span class="tile">{sparkle}</span><div>Desactivar la reflexión con IA detiene al instante cualquier solicitud futura, borra el resumen semanal de tu dispositivo y quita el recordatorio del domingo. On Ice vuelve a no hacer ninguna conexión de red por su cuenta. {K_settings} → {K_ai_reflection} → {K_what_gets_sent} muestra la misma lista dentro de la app.</div></div>
""",

"p.purchases.h": "Compras y planes familiares",
"p.purchases.b": """
<p>Premium se vende a través del App Store de Apple con StoreKit. La transacción es entre tú y Apple, bajo la <a href="https://www.apple.com/legal/privacy/">política de privacidad de Apple</a>. Apple le dice a On Ice qué plan está activo y cuándo se renueva o termina —nada más—, y On Ice no le dice a Apple nada sobre cómo usas la app. Nunca vemos una tarjeta.</p>
<p>Con un <strong>plan familiar</strong>, En familia de Apple le da Premium a cada miembro en su propia copia de On Ice. Nada pasa entre esas copias —ni tiendas, ni lista, ni diario, ni ahorro, ni ajustes—, y On Ice solo sabe que Premium se compartió, no quién lo compartió.</p>
""",

"p.notifications.h": "Notificaciones, widgets y pantalla bloqueada",
"p.notifications.b": """
<p>Las <strong>notificaciones</strong> son opcionales y todas se programan en tu dispositivo. Ninguna se envía desde un servidor, y no hay servicio push. On Ice las usa para llevarte del bloqueo a la app, para avisarte cuando la espera de un artículo ha terminado o está a punto de terminar, para las preguntas de seguimiento, que puedes desactivar en {K_settings} → {K_follow_ups}, para los temporizadores de actividades y las sugerencias que elijas y, solo con la reflexión con IA activada, para el resumen del domingo. Una notificación sobre un artículo menciona el nombre del artículo.</p>
<p>Los <strong>widgets, las Actividades en directo y los controles del Centro de control</strong> leen una pequeña instantánea en tu dispositivo: totales, recuentos, tu racha, y los nombres y las horas de hasta tres de los artículos que terminan antes. No tienen acceso a Tiempo de uso y nunca ven qué tiendas elegiste. <strong>El widget «En pausa» y la Actividad en directo de un artículo muestran el nombre del artículo</strong>, así que, en la pantalla bloqueada, cualquiera que tenga el dispositivo en la mano puede leerlo. Los importes de dinero se ocultan ahí mientras el dispositivo está bloqueado. Colócalos donde te resulte cómodo verlos.</p>
""",

"p.third.h": "Terceros",
"p.third.b": """
<p>On Ice no contiene <strong>código de terceros</strong>: ni analítica, ni publicidad, ni atribución, ni informes de fallos, ni SDK. Solo intervienen estas partes, y solo como se describe aquí:</p>
<ul>
  <li><strong>Apple</strong>: gestiona el App Store y En familia, procesa las compras, aplica el bloqueo de Tiempo de uso, ejecuta Apple Intelligence en tu dispositivo y proporciona App Attest. Si has aceptado compartir datos con los desarrolladores, Apple puede compartir con nosotros registros de fallos según su propia política.</li>
  <li><strong>Cloudflare</strong>: aloja el servicio de IA de On Ice. Cuando la reflexión con IA usa OpenAI, las solicitudes pasan por él, y no guarda nada de su contenido.</li>
  <li><strong>OpenAI</strong>: ejecuta el modelo que hay detrás de las reflexiones de OpenAI, solo mientras esa opción está en uso, y recibe únicamente lo que se detalla <a href="#ai">arriba</a>.</li>
  <li><strong>Google Cloud</strong>: cumple esa misma función, solo para las versiones anteriores de la app.</li>
</ul>
<p>No vendemos, alquilamos ni compartimos datos personales con nadie, y no compartimos nada con intermediarios de datos ni anunciantes. Un enlace que le asignas a una «cosa que hacer en su lugar» abre la app o el sitio web que elegiste, bajo la política propia de esa app o de ese sitio.</p>
""",

"p.delete.h": "Eliminar tus datos",
"p.delete.b": """
<p>Todo lo que guarda On Ice está en tu dispositivo, así que borrarlo no requiere pedírnoslo. Puedes eliminar una a una en la app las entradas del diario, las entradas del registro de gastos, las reglas, los límites, los recordatorios y las actividades; desactivar la reflexión con IA borra el resumen semanal; y <strong>eliminar la app lo borra todo a la vez</strong>. No hay un único botón dentro de la app que borre todo tu historial, así que eliminar la app es la forma de empezar de cero. La página <a href="{BASE}{L}/delete-data/">Tus datos</a> explica cada caso paso a paso.</p>
<p>De nuestro lado no hay nada que borrar: el servicio de IA no guarda contenido, y su recuento por dispositivo desaparece por sí solo a los dos días.</p>
""",

"p.rights.h": "Tus derechos",
"p.rights.b": """
<p>Vivas donde vivas —incluido bajo el RGPD (GDPR), el UK GDPR y la CCPA/CPRA—, tienes derecho a acceder a los datos personales que una empresa tenga sobre ti, a corregirlos, exportarlos y suprimirlos, a restringir su tratamiento y a oponerte a él, y a presentar una reclamación ante una autoridad de control. On Ice no guarda ningún perfil tuyo en ningún servidor, así que de nuestro lado no hay nada que entregar ni que borrar; los datos de tu dispositivo ya están en tus manos. Usar las reflexiones de OpenAI es decisión tuya, y desactivar la reflexión con IA retira esa decisión al instante. Si crees que tenemos algo sobre ti, escribe a {MAIL} y te responderemos.</p>
""",

"p.children.h": "Menores",
"p.children.b": """
<p>On Ice es una herramienta autodirigida para la persona que usa el dispositivo. No es un producto de control parental y no gestiona el dispositivo de otra persona; un plan familiar comparte Premium, nunca control ni datos. No está dirigida a menores de 13 años (o de la edad de consentimiento digital donde vivas), y no recopilamos a sabiendas información personal de nadie, de ninguna edad.</p>
""",

"p.changes.h": "Cambios en esta política",
"p.changes.b": """
<p>Podemos actualizar esta política a medida que cambie la app. La fecha de arriba cambia cuando lo hacemos, y los cambios importantes se indican en las notas de la versión de la app. Esta versión describe la elección entre Apple Intelligence y OpenAI para la reflexión con IA, el diario, los pasos al caminar, los tramos de uso, los planes familiares, el iPad y siete idiomas más. Seguir usando On Ice después de un cambio significa que aceptas la política revisada.</p>
<p>Esta política se publica en ocho idiomas. Si una traducción y la versión en inglés difieren, se aplica la versión en inglés.</p>
""",

"p.contact.h": "Contacto",
"p.contact.b": """
<p>{COMPANY}, la editora de On Ice, es la responsable del tratamiento de todo lo que se describe aquí. Dudas sobre privacidad: {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Términos de Uso",
"t.h1": "El acuerdo, en palabras claras.",
"t.sub": "Qué hace On Ice, qué no promete, por qué cada cifra es una estimación, cómo se cobran Premium y los planes familiares, y qué te piden los bloqueos y el modo estricto.",
"t.meta": "En vigor desde el {DATE} · On Ice de {COMPANY}",

"t.acceptance.h": "1. Aceptación de los Términos",
"t.acceptance.b": """
<p>Estos Términos de Uso («Términos») son un acuerdo entre tú y {COMPANY} («nosotros»), la editora de la app On Ice para iPhone y iPad («On Ice» o «la app»). Al instalar o usar On Ice, aceptas estos Términos y nuestra <a href="{BASE}{L}/privacy/">Política de Privacidad</a>. Si no estás de acuerdo, no uses la app.</p>
<p>Estos Términos se publican en ocho idiomas. Si una traducción y la versión en inglés difieren, se aplica la versión en inglés.</p>
""",

"t.who.h": "2. Quién puede usar On Ice",
"t.who.b": """
<p>Debes tener al menos 13 años, o la edad de consentimiento digital donde vivas, para usar On Ice. On Ice es una herramienta que instalas para ti, en tu propio dispositivo. No es un producto de control parental y no debe usarse para gestionar ni vigilar el dispositivo de otra persona. Un plan familiar comparte Premium con los miembros de tu grupo de En familia; no le da a nadie control sobre el On Ice de otro miembro.</p>
""",

"t.what.h": "3. Qué es On Ice y qué no es",
"t.what.b": """
<p>On Ice es una herramienta autodirigida que bloquea las apps y los sitios web de compras que eliges, ofrece una pausa breve, te permite anotar lo que te llamó la atención, lo guarda durante el periodo que fijes y registra en tu dispositivo lo que decidiste. También ofrece un diario, cosas que hacer en su lugar, objetivos, límites y bloqueos. Está diseñada para convertir una compra automática en una decisión que tomas de verdad.</p>
<p>On Ice <strong>no</strong> es un servicio médico, psicológico ni terapéutico, y nada de lo que contiene —incluidas las emociones que tocas, las pausas, los recordatorios, las preguntas del diario, las observaciones o los textos escritos por IA— es consejo, diagnóstico ni tratamiento. Si estás lidiando con gastos compulsivos, deudas, ansiedad o cualquier otra cosa que afecte a tu bienestar, por favor, habla con un profesional cualificado o con un servicio de asesoramiento sobre deudas. En una emergencia, llama al número de emergencias de tu zona.</p>
<p>On Ice tampoco es <strong>un producto de seguridad ni de control parental</strong>. Está diseñada para ser exactamente tan firme como le pidas: la app se puede eliminar, el acceso a Tiempo de uso se puede retirar en los Ajustes de iOS, y los bloqueos solo existen mientras la app está instalada y autorizada.</p>
""",

"t.money.h": "4. Estimaciones, no asesoramiento financiero",
"t.money.b": """
<p>Cada precio en On Ice es una cifra que introduces <strong>tú</strong>. La app no se conecta a ningún banco, proveedor de pagos ni comercio, no lee tus transacciones ni tu historial de pedidos, no hace seguimiento de precios, no convierte monedas y no verifica lo que cuesta nada.</p>
<p>Por tanto, la cifra de ahorro que muestra On Ice es una <strong>estimación construida a partir de tus propios cálculos</strong>, y se identifica como tal en todos los lugares donde aparece. No es una declaración de hecho sobre dinero que tengas, ni un registro financiero, ni algo en lo que debas basarte para presupuestos, impuestos, crédito ni ninguna otra decisión. {COMPANY} no es un asesor financiero, y nada de lo que hay en la app o en este sitio es asesoramiento financiero, de inversión ni sobre deudas.</p>
<div class="callout green"><span class="tile">{info}</span><div>On Ice no incluye enlaces de afiliado y no gana nada con lo que compres o dejes de comprar. Sus únicos ingresos son Premium, que pagas tú a través de Apple.</div></div>
""",

"t.screentime.h": "5. Tiempo de uso, bloqueos y modo estricto",
"t.screentime.b": """
<p>On Ice depende del framework Tiempo de uso de Apple. Apple aplica el bloqueo; On Ice lo solicita. Si un bloqueo aparece, con qué rapidez, si se informa un tramo de uso y si los bloqueos se mantienen tras reinicios y actualizaciones de iOS lo determina en último término iOS, y no podemos garantizarlo en todas las circunstancias. <strong>On Ice no puede impedir una compra</strong>: solo puede poner una pantalla delante de una tienda que elegiste.</p>
<p>Algunas herramientas que puedes activar <strong>no ofrecen ninguna salida</strong> mientras están en marcha: una <strong>regla de bloqueo total</strong> durante sus horas, un <strong>límite diario</strong> una vez alcanzado (hasta que empiece tu siguiente día), un <strong>bloqueo programado</strong> hasta que termine y un <strong>bloqueo por modo de concentración</strong> mientras ese modo de concentración esté activado. Un bloqueo programado configurado en {K_only_these} bloquea <em>todas</em> las apps de tu dispositivo salvo las apps esenciales que elegiste. Antes de iniciar uno, asegúrate de poder acceder a lo que puedas necesitar: llamadas, mensajes, mapas, pagos, salud o trabajo.</p>
<p>El <strong>modo estricto</strong> es un compromiso que haces contigo. Mientras está en marcha, durante el tiempo que elegiste, la protección sigue activada, las reglas se quedan como están, se pueden añadir tiendas pero no quitarlas, y los límites y la hora a la que empieza tu día no se pueden cambiar, <em>ni siquiera por ti, ni siquiera por nosotros</em>. No podemos terminar antes de tiempo el modo estricto, un bloqueo ni una regla a petición. Si configuras {K_someone_key}, la persona que tiene el PIN puede terminar antes el modo estricto, y tú puedes solicitar una salida con demora que lo termina 24 horas después; no podemos recuperar un PIN olvidado. No empieces un compromiso que no tengas intención de cumplir, y no lo empieces en un dispositivo al que puedas necesitar acceso sin restricciones.</p>
<p>Eliminar la app pone fin a toda protección, bloqueo y límite, como se describe en la sección 3.</p>
""",

"t.data.h": "6. Tus datos y tu dispositivo",
"t.data.b": """
<p>Todo lo que registra On Ice se guarda en tu dispositivo; consulta la <a href="{BASE}{L}/privacy/">Política de Privacidad</a>. Nada se sincroniza entre dispositivos. Eres responsable de tu dispositivo, de su código y de sus copias de seguridad. Si eliminas la app o pierdes el dispositivo sin una copia de seguridad, tu lista, tu diario, tus reglas, tu registro de gastos y tu historial de ahorro desaparecen, y no tenemos ninguna copia que restaurar. Tu compra de Premium es aparte: pertenece a tu Cuenta de Apple y se puede restaurar en cualquier iPhone o iPad que tenga iniciada la sesión con ella.</p>
<p>Lo que escribes en On Ice es tuyo. No reclamamos ningún derecho sobre ello y, salvo en el caso de la reflexión opcional con OpenAI de la sección 8, que debes activar tú, nunca lo recibimos.</p>
""",

"t.subscriptions.h": "7. Premium, suscripciones y facturación",
"t.subscriptions.b": """
<p>On Ice es gratis de descargar y de usar. <strong>On Ice Premium</strong> desbloquea funciones adicionales y se vende en cinco formas, al precio que se muestra en la app y en el App Store para tu país:</p>
<ul>
  <li><strong>Premium mensual</strong>: una suscripción de renovación automática, facturada cada mes.</li>
  <li><strong>Premium anual</strong>: una suscripción de renovación automática, facturada cada año, que empieza con una <strong>prueba gratuita</strong> donde se ofrezca.</li>
  <li><strong>Premium de por vida</strong>: una compra única que no se renueva.</li>
  <li><strong>Premium familiar anual</strong>: una suscripción de renovación automática, facturada cada año, que empieza con una <strong>prueba gratuita</strong> donde se ofrezca, para hasta seis personas mediante En familia.</li>
  <li><strong>Premium familiar de por vida</strong>: una compra única que no se renueva, para hasta seis personas mediante En familia.</li>
</ul>
<p>Los dos planes familiares se comparten mediante <strong>En familia</strong> de Apple con hasta otros cinco miembros de tu grupo familiar. Cada persona recibe Premium en su propia copia de On Ice, en su propio dispositivo; no se comparten tiendas, listas, diarios, ahorros ni ajustes entre ellas. Premium mensual, Premium anual y Premium de por vida son solo para ti y no se comparten.</p>
<p>El pago se carga a tu Cuenta de Apple al confirmar la compra. Una prueba gratuita se convierte en una suscripción de pago salvo que canceles al menos 24 horas antes de que termine la prueba. Las suscripciones se renuevan automáticamente al mismo precio y por el mismo periodo salvo que la renovación automática se desactive al menos 24 horas antes del final del periodo en curso; la renovación se cobra dentro de las 24 horas anteriores al final de ese periodo. Puedes gestionar o cancelar una suscripción en los <a href="https://apps.apple.com/account/subscriptions">ajustes de suscripciones del App Store</a>; la cancelación surte efecto al final del periodo en curso, y no se concede ningún reembolso parcial por la parte no usada de un periodo. Comprar un plan de por vida, o recibir un plan familiar, no cancela una suscripción que ya tengas: cancélala tú. Los reembolsos los gestiona Apple según sus políticas. Usa {K_restore} en la app para recuperar Premium en un dispositivo nuevo.</p>
<p><strong>Si una suscripción caduca</strong>, no se elimina nada de lo que ya hayas construido: tu lista, tu diario, tu historial y tu ahorro estimado se quedan, las tiendas que elegiste siguen protegidas, y las reglas y los límites existentes y un modo estricto en curso siguen en pie. Tu espera vuelve a 24 horas, la reflexión con IA se desactiva, y los widgets y las pantallas de patrones esperan a que vuelva Premium. Solo se cierra la posibilidad de añadir más funciones Premium. El conjunto de funciones Premium puede cambiar con el tiempo; no quitaremos una función de una suscripción activa sin avisar.</p>
""",

"t.ai.h": "8. La reflexión con IA",
"t.ai.b": """
<p>La reflexión con IA opcional está <strong>desactivada hasta que la actives</strong>. Si la escribe <strong>Apple Intelligence</strong>, el texto se genera en tu dispositivo según las condiciones de Apple. Si la escribe <strong>OpenAI</strong>, los datos que se detallan en la <a href="{BASE}{L}/privacy/#ai">Política de Privacidad</a> se envían a nuestro servicio y de ahí a OpenAI para que se pueda generar una respuesta breve. Las versiones anteriores de la app usan para esto, en su lugar, el modelo Gemini de Google en Vertex AI. La opción {K_reflect_week} del diario usa Apple Intelligence únicamente en tu dispositivo.</p>
<p>Lo que escribe un modelo de lenguaje es texto generado. Puede ser incorrecto, genérico o poco útil, <strong>no es consejo de ningún tipo</strong> y nunca es una declaración de hecho sobre tu dinero. No escribas en esa pantalla nada que no quieras que procese un modelo de terceros. Si una solicitud falla, la app simplemente te muestra las opciones habituales: nada se pone en cola, se reintenta más tarde ni se guarda. Podemos limitar cuántas reflexiones puede solicitar un dispositivo cada día.</p>
""",

"t.licence.h": "9. Licencia y propiedad intelectual",
"t.licence.b": """
<p>Te concedemos una licencia personal, no exclusiva, intransferible y revocable para instalar y usar On Ice en un iPhone o iPad de tu propiedad o bajo tu control, conforme a estos Términos y a las normas de uso del App Store. On Ice, su nombre, diseño, ilustraciones, textos y código son propiedad de {COMPANY} y están protegidos por derechos de autor y otras leyes. No puedes copiar, modificar, distribuir, vender, arrendar, aplicar ingeniería inversa ni crear obras derivadas de la app, salvo donde la ley lo permita expresamente.</p>
<p>Los nombres de los comercios, apps y sitios web que eliges bloquear, o abrir como cosa que hacer en su lugar, pertenecen a sus respectivos propietarios. On Ice no está afiliada a ninguno de ellos ni cuenta con su respaldo o patrocinio, y estos se rigen por sus propias condiciones.</p>
""",

"t.use.h": "10. Uso aceptable",
"t.use.b": """
<p>Te comprometes a no usar On Ice de ninguna forma que sea ilícita, que interfiera con la app, con su servicio de IA o con los servicios de Apple, que intente eludir los mecanismos de compra del App Store o los límites del servicio de IA, o que la instale en un dispositivo que no tengas derecho a gestionar. Te comprometes a no usarla para restringir ni vigilar a otra persona sin su consentimiento informado, y a no enviar mediante la reflexión con IA contenido ilícito o que no tengas derecho a compartir.</p>
""",

"t.termination.h": "11. Terminación",
"t.termination.b": """
<p>Puedes dejar de usar On Ice en cualquier momento eliminándola. Podemos suspender o terminar tu licencia, o tu acceso al servicio de IA, si incumples estos Términos. Las secciones 4, 6, 9, 12, 13 y 15 siguen vigentes tras la terminación. Eliminar la app no cancela una suscripción activa: cancélala en los ajustes del App Store.</p>
""",

"t.warranty.h": "12. Garantías y responsabilidad",
"t.warranty.b": """
<p>On Ice se ofrece «tal cual» y «según disponibilidad», sin garantías de ningún tipo, expresas o implícitas, incluidas las de que bloqueará cualquier app o sitio web en todas las circunstancias, de que medirá el uso con exactitud, de que funcionará sin interrupciones ni errores, de que cualquier cifra que muestre será exacta o de que cambiará tu forma de gastar. En la máxima medida permitida por la ley, {COMPANY} no será responsable de ningún daño indirecto, incidental, especial, consecuente o punitivo, ni de ninguna pérdida de datos o de dinero, derivados de tu uso o de tu imposibilidad de usar la app, incluida cualquier compra que hicieras o no hicieras, cualquier consecuencia de un bloqueo que apareciera o no apareciera, y cualquier bloqueo, límite o sesión de modo estricto que decidieras iniciar. Cuando la responsabilidad no pueda excluirse, se limita al importe que nos hayas pagado por Premium en los doce meses anteriores a la reclamación. Nada en estos Términos limita los derechos que tengas como consumidor y a los que no se pueda renunciar.</p>
""",

"t.apple.h": "13. Apple",
"t.apple.b": """
<p>On Ice se distribuye a través del App Store de Apple. Estos Términos son entre tú y {COMPANY}, no Apple. Apple no tiene ninguna obligación de prestar mantenimiento ni soporte para la app, y no es responsable de atender ninguna reclamación relacionada con ella, incluidas las de responsabilidad por productos, cumplimiento normativo o propiedad intelectual. Apple y sus filiales son terceros beneficiarios de estos Términos y pueden hacerlos valer frente a ti. Cuando estos Términos no digan nada, se aplica el <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de Licencia de Usuario Final de Aplicación Licenciada</a> de Apple. Declaras que no te encuentras en un país sujeto a un embargo del gobierno de EE. UU. ni figuras como parte prohibida, y debes cumplir las condiciones de terceros aplicables cuando uses la app.</p>
""",

"t.changes.h": "14. Cambios en estos Términos",
"t.changes.b": """
<p>Podemos actualizar estos Términos de vez en cuando. La fecha de arriba cambiará cuando lo hagamos, y los cambios importantes se indicarán en las notas de la versión de la app. Seguir usándola después de una actualización significa que aceptas los Términos revisados.</p>
""",

"t.law.h": "15. Ley aplicable",
"t.law.b": """
<p>Estos Términos se rigen por las leyes de Pakistán, donde opera {COMPANY}, sin atender a las normas sobre conflicto de leyes. Cuando la ley de tu país de residencia te otorgue protecciones que no puedan excluirse por contrato, se aplican esas protecciones.</p>
""",

"t.contact.h": "16. Contacto",
"t.contact.b": """
<p>Dudas sobre estos Términos: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Tus datos",
"d.h1": "Eliminar tus datos",
"d.sub": "Todo lo que On Ice sabe está en tu dispositivo. Aquí tienes cómo borrarlo, por partes o todo a la vez, qué pasa con tu suscripción y por qué de nuestro lado no hay nada que pedir.",
"d.meta": 'Consulta también la <a href="{BASE}{L}/privacy/">Política de Privacidad</a>',

"d.where.h": "Qué se guarda y dónde",
"d.where.b": """
<p class="lead">On Ice no tiene cuenta y no guarda ningún perfil de nadie en un servidor. Todo lo que tiene está en tu dispositivo, y puedes borrarlo sin pedírnoslo.</p>
<div class="table-wrap"><table>
<tr><th>Datos</th><th>Dónde están</th><th>Cómo borrarlos</th></tr>
<tr><td>Tu lista, tus decisiones, tu historial de ahorro estimado, tus rachas y tus patrones</td><td>El almacenamiento privado de la app en tu dispositivo</td><td>Elimina la app. Tu historial es de lo que está hecho el total de ahorro, así que no se borra artículo por artículo.</td></tr>
<tr><td>Entradas del diario</td><td>En tu dispositivo</td><td>{K_delete_entry} en cualquier entrada, o elimina la app</td></tr>
<tr><td>Registro de gastos, reglas, límites, recordatorios, actividades</td><td>En tu dispositivo</td><td>Quita cada uno en la app, o elimina la app</td></tr>
<tr><td>Tus tiendas</td><td>Tokens de Tiempo de uso y direcciones de sitios web en tu dispositivo</td><td>Cámbialas en la app; retirar el acceso a Tiempo de uso en los Ajustes de iOS también pone fin a todos los bloqueos</td></tr>
<tr><td>Instantánea de los widgets y las Actividades en directo</td><td>Un archivo pequeño en tu dispositivo</td><td>Se borra con la app</td></tr>
<tr><td>El resumen semanal</td><td>En tu dispositivo, solo mientras la reflexión con IA está activada</td><td>Desactiva la reflexión con IA</td></tr>
<tr><td>Estado de Premium</td><td>Tu Cuenta de Apple (Apple), y una copia de su estado en tu dispositivo</td><td>Se gestiona en los ajustes del App Store; ver más abajo</td></tr>
<tr><td>Lo que envió una reflexión de OpenAI</td><td>No está en nuestro servicio, que no guarda contenido. OpenAI puede conservarlo en sus registros de supervisión de abusos, normalmente hasta 30 días (Google, en versiones anteriores: hasta 24 horas)</td><td>No tienes nada que borrar. Desactiva la reflexión con IA y no se enviará nada más</td></tr>
<tr><td>Un recuento de solicitudes de IA por dispositivo</td><td>El servicio de IA de On Ice, bajo un identificador de clave aleatorio</td><td>Se borra automáticamente a los dos días</td></tr>
<tr><td>Una cuenta, un perfil, algo con tu nombre</td><td>—</td><td>No existe. Nunca tuvimos nada de eso que borrar.</td></tr>
</table></div>
""",

"d.inapp.h": "Bórralo en la app",
"d.inapp.b": """
<ul>
  <li><strong>Entradas del diario:</strong> abre una entrada y toca {K_delete_entry}.</li>
  <li><strong>Registro de gastos:</strong> toca {K_remove} en una entrada.</li>
  <li><strong>Reglas, límites, recordatorios y actividades:</strong> cada uno tiene su propio botón para eliminarlo o quitarlo.</li>
  <li><strong>Tiendas:</strong> cambia tu selección o desactiva una tienda en la pantalla Inicio. Desactivar la protección retira todos los bloqueos a la vez.</li>
  <li><strong>Los artículos ya decididos se quedan en tu historial</strong>: de eso están hechos tu ahorro estimado y tus patrones. Para borrar ese historial, elimina la app.</li>
</ul>
<div class="callout amber"><span class="tile">{lock}</span><div>Mientras el <strong>modo estricto</strong> está en marcha, tu configuración se mantiene en su sitio: no se pueden quitar tiendas, ni eliminar reglas ni límites. Ese es el único compromiso que le pediste a la app que mantuviera por ti. Termina por sí solo a la hora que elegiste.</div></div>
""",

"d.journal.h": "Tu diario",
"d.journal.b": """
<p>Las entradas del diario solo están en tu dispositivo, y On Ice nunca las envió a ninguna parte, así que no hay nada que borrar en otro sitio. Elimínalas una a una con {K_delete_entry}. Para guardar una copia antes de eliminar la app, usa {K_export_journal}: crea un archivo de texto sin formato que puedes guardar donde quieras.</p>
""",

"d.ai.h": "La reflexión con IA",
"d.ai.b": """
<p>Si activaste la reflexión con IA, On Ice guarda el último resumen semanal en tu dispositivo para que puedas volver a leerlo. Desactivar la reflexión con IA en {K_settings} → {K_ai_reflection} lo borra, quita el recordatorio del domingo, cierra la sesión de la app con el servicio y hace que On Ice vuelva a no hacer ninguna conexión de red por su cuenta.</p>
<p>El servicio nunca tuvo una copia de lo que enviaste. Solo guarda un recuento por dispositivo bajo una clave aleatoria, que borra a los dos días, y totales diarios que no nombran ningún dispositivo.</p>
""",

"d.uninstall.h": "Eliminar la app",
"d.uninstall.b": """
<p>Eliminar On Ice de tu iPhone o iPad borra con ella todos sus datos —tu lista, tu historial, tu diario, tus ajustes y los tokens de Tiempo de uso— y pone fin de inmediato a toda protección, bloqueo y límite. Es la forma de borrarlo todo a la vez. Si la app está incluida en una copia de seguridad de iCloud o local, esa copia pertenece a tu Cuenta de Apple y se rige por las condiciones de Apple; nosotros no tenemos acceso a ella.</p>
""",

"d.subscription.h": "Tu suscripción",
"d.subscription.b": """
<p>Eliminar la app no cancela una suscripción: pertenece a tu Cuenta de Apple, no a la app. Cancélala en los <a href="https://apps.apple.com/account/subscriptions">ajustes de suscripciones del App Store</a>; sigue activa hasta el final del periodo en curso. Los reembolsos los gestiona el <a href="https://support.apple.com/billing">Soporte de Apple</a>. Una compra de por vida no se renueva y no hay que cancelar nada. Si perteneces a un plan familiar, lo gestiona quien lo compró.</p>
""",

"d.email.h": "Pregúntanos",
"d.email.b": """
<p>Si quieres una confirmación por escrito de que no tenemos nada sobre ti, o crees que sí lo tenemos, escribe a {MAIL} desde cualquier dirección. Responderemos en un plazo de 30 días. Por favor, no nos envíes tu lista, tus precios, tu diario ni capturas de pantalla de ellos: no los necesitamos para responder.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Aquí no hay nada en pausa.",
"nf.sub": "Lo cual, por una vez, no es la idea.",
"nf.cta": "Volver a Ayuda",
"nf.b": 'Esa página no está aquí. Prueba con <a href="{BASE}/">Ayuda</a>, la <a href="{BASE}/privacy/">Política de Privacidad</a> o los <a href="{BASE}/terms/">Términos de Uso</a>.',

}
