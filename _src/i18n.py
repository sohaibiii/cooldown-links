# -*- coding: utf-8 -*-
"""The home page in German, Japanese and Spanish.

The English home page in `site_pages.py`, its hero demo in `demo.py` and its
drawings in `art.py` wrap every visible English string in `t()`. While one of
the languages below is being built, `t()` returns its translation, and a string
with no translation stops the build, so an English sentence can never slip
onto a translated page unnoticed.

Rules, same as the support pages in `words/`:
  * the app's own words come from the app's Localizable.xcstrings, copied as
    they are (Notieren / Doch nicht, メモする / やめておく, Anotarlo / Mejor no,
    Bedenkzeit, 推定節約額, ahorro estimado...);
  * German says du, Japanese uses です・ます, Spanish is neutral and says tú;
  * money is always an estimate and says so; prices are sample figures in the
    reader's currency;
  * no long dashes.

These translations were written without a native speaker's review.
"""

# code: (URL prefix, home page path, og:locale, native name)
HOMES = {
    "en": ("", "/", "en_US"),
    "de": ("/de", "/de/home/", "de_DE"),
    "es": ("/es", "/es/home/", "es_ES"),
    "ja": ("/ja", "/ja/home/", "ja_JP"),
}
LANGS = ["de", "es", "ja"]

_state = {"lang": "en"}


def current():
    return _state["lang"]


def use(lang):
    _state["lang"] = lang


def t(s):
    lang = _state["lang"]
    if lang == "en":
        return s
    try:
        return T[lang][s]
    except KeyError:
        raise SystemExit(f"i18n: no {lang} translation for {s!r}")


def tx(key, default):
    """A translation stored under a key rather than its English text."""
    return default if _state["lang"] == "en" else t(key)


def money(amount):
    """'≈ $50' in the reader's currency. `amount` is the US dollar figure."""
    lang = _state["lang"]
    if lang == "en":
        return f"≈ ${amount}"
    if lang == "ja":
        return f"≈ ¥{YEN[amount]:,}"
    return f"≈ {amount} €"


YEN = {10: 1500, 25: 3000, 45: 6500, 50: 7000, 100: 15000, 135: 20000, 180: 26500}


# Longer words need a little less type inside the drawn phone.
DEMO_CSS = {
    "de": (".demo .s-note .dh{font-size:15px}.demo .dh.big{font-size:17px}"
           ".demo .s-ask .dh{font-size:18px}.demo .dcap{font-size:13.5px}"),
    "es": "",
    "ja": ".demo .ic em{font-size:8.5px;white-space:nowrap;letter-spacing:-.02em}",
}


def faq():
    """The home page's questions, in order, for a translated page."""
    return FAQ[_state["lang"]]


T = {}

T["de"] = {
    # page
    "Stop Impulse Buying: On Ice, the Shopping Blocker for iPhone":
        "Schluss mit Impulskäufen: On Ice, der Shopping-Blocker fürs iPhone",
    "On Ice shields the shopping apps and websites you choose, holds each want for 24 hours, and adds up what you didn't spend. Free to start, no account.":
        "On Ice sperrt die Shopping-Apps und -Websites, die du auswählst, hält jeden Wunsch 24 Stunden zurück und rechnet zusammen, was du nicht ausgegeben hast. Kostenlos starten, kein Konto.",
    "On Ice: stop impulse buying. Sleep on it first.": "On Ice: Schluss mit Impulskäufen. Erst mal drüber schlafen.",
    "A shopping blocker for iPhone and iPad that shields the shopping apps and websites you choose and holds each want for 24 hours.":
        "Ein Shopping-Blocker für iPhone und iPad, der die Shopping-Apps und -Websites sperrt, die du auswählst, und jeden Wunsch 24 Stunden zurückhält.",
    "Shopping blocker for iPhone and iPad": "Shopping-Blocker für iPhone und iPad",
    "Stop impulse buying. <em>Sleep on it first.</em>": "Schluss mit Impulskäufen. <em>Erst mal drüber schlafen.</em>",
    "On Ice pauses you when you open a shopping app or website. Note what you wanted, wait one night, then decide.":
        "On Ice hält dich kurz an, wenn du eine Shopping-App oder -Website öffnest. Notiere, was du wolltest, warte eine Nacht und entscheide dann.",
    "Free to start. No account.<br>No bank linking.": "Kostenlos starten. Kein Konto.<br>Keine Bankverbindung.",
    "Three steps. <em>One night.</em>": "Drei Schritte. <em>Eine Nacht.</em>",
    "1 · Tonight": "1 · Heute Abend",
    "A drawing of a shopping bag with a pause button on it, and the words: Pause before you buy.":
        "Eine Zeichnung einer Einkaufstasche mit Pausetaste und den Worten: Kurz Pause vor dem Kauf.",
    "On Ice pauses you": "On Ice hält dich an",
    "Open a shopping app or website and On Ice steps in before you can buy.":
        "Öffne eine Shopping-App oder -Website, und On Ice schaltet sich ein, bevor du kaufen kannst.",
    "2 · Still tonight": "2 · Noch heute Abend",
    "A drawing of a shirt frozen inside an ice cube. Under it, a line from tonight's moon to tomorrow's sun, marked 24 hours.":
        "Eine Zeichnung eines Hemds, eingefroren in einem Eiswürfel. Darunter eine Linie vom Mond heute Nacht zur Sonne morgen, beschriftet mit 24 Stunden.",
    "You wait one night": "Du wartest eine Nacht",
    "Write down what you wanted. It waits on your list for 24 hours. Nothing is bought.":
        "Schreib auf, was du wolltest. Es wartet 24 Stunden auf deiner Liste. Es wird nichts gekauft.",
    "3 · Tomorrow": "3 · Morgen",
    "A drawing of two answers. Don't want it anymore, with a savings jar: you keep the money. Or, Still want it, with a shopping bag: the shop opens.":
        "Eine Zeichnung mit zwei Antworten. Will ich nicht mehr, mit einem Sparglas: Du behältst das Geld. Oder Will ich immer noch, mit einer Einkaufstasche: Der Shop öffnet sich.",
    "You decide": "Du entscheidest",
    "Don't want it anymore? Its price joins your estimated savings. Still want it? The shop opens. Either answer is a good one.":
        "Willst du es nicht mehr? Sein Preis wandert in deine geschätzte Ersparnis. Willst du es noch? Der Shop öffnet sich. Beide Antworten sind gut.",
    "Really need to buy something now? The shop opens for 1, 5 or 15 minutes.":
        "Musst du wirklich jetzt etwas kaufen? Der Shop öffnet sich für 1, 5 oder 15 Minuten.",
    "See the real screens, step by step": "Die echten Bildschirme, Schritt für Schritt (auf Englisch)",
    "See what you <em>didn't</em> spend.": "Sieh, was du <em>nicht</em> ausgegeben hast.",
    "Every item you let go adds to a running total. It is built from prices you typed yourself, and it always says estimated.":
        "Alles, was du loslässt, kommt zu einer laufenden Summe dazu. Sie besteht aus Preisen, die du selbst eingegeben hast, und ist immer als geschätzt gekennzeichnet.",
    "No bank linking": "Keine Bankverbindung",
    "On Ice never connects to an account or reads a transaction.": "On Ice verbindet sich nie mit einem Konto und liest keine Transaktionen.",
    "No account": "Kein Konto",
    "No sign up, no email field.": "Keine Registrierung, kein E-Mail-Feld.",
    "Private": "Privat",
    "Your list stays on your device.": "Deine Liste bleibt auf deinem Gerät.",
    "How the privacy works, in full": "So funktioniert der Datenschutz, ausführlich",
    "A sample receipt of things not bought this month": "Ein Beispielbeleg mit Dingen, die diesen Monat nicht gekauft wurden",
    "THINGS YOU DIDN'T BUY": "DINGE, DIE DU NICHT GEKAUFT HAST",
    "Linen shirt": "Leinenhemd",
    "Running shoes": "Laufschuhe",
    "LET GO THIS MONTH": "DIESEN MONAT LOSGELASSEN",
    "estimated": "geschätzt",
    "Sample figures. Every amount is your own estimate.": "Beispielzahlen. Jeder Betrag ist deine eigene Schätzung.",
    "Free to start. <em>Premium if you want more.</em>": "Kostenlos starten. <em>Premium, wenn du mehr willst.</em>",
    "Free": "Kostenlos",
    "No charge, no trial clock": "Keine Kosten, keine ablaufende Testphase",
    "One shopping app and one website, shielded": "Eine Shopping-App und eine Website, gesperrt",
    "The 24 hour wait and your list": "Die 24-Stunden-Bedenkzeit und deine Liste",
    "Your estimated savings": "Deine geschätzte Ersparnis",
    "Premium": "Premium",
    "Monthly · Yearly · Lifetime · Family": "Monatlich · Jährlich · Lebenslang · Familie",
    "Every shop and website you want": "Jeder Shop und jede Website, die du willst",
    "Waits of 12, 24, 48 or 72 hours": "Bedenkzeiten von 12, 24, 48 oder 72 Stunden",
    "Daily limits, danger hours and strict mode": "Tageslimits, Risikozeiten und strenger Modus",
    "Nothing you built is taken away if a subscription lapses.": "Läuft ein Abo aus, verlierst du nichts von dem, was du aufgebaut hast.",
    "Plans and prices": "Pläne und Preise (auf Englisch)",
    "Questions people ask first": "Was die meisten zuerst fragen",
    "Something else? <a href=\"{support}\">The full support page</a> covers setup, troubleshooting and how to reach us.":
        "Noch etwas? <a href=\"{support}\">Die Hilfeseite</a> erklärt Einrichtung, Problemlösung und wie du uns erreichst.",
    "Put your next impulse buy <em>on ice.</em>": "Leg deinen nächsten Impulskauf <em>auf Eis.</em>",
    "iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.":
        "iPhone und iPad, ab iOS 17.<br>Auf Deutsch und in sieben weiteren Sprachen.",
    # the store badge and the chrome
    "Download on the": "Laden im",
    "Get the app": "App laden",
    "Skip to content": "Zum Inhalt springen",
    "Pages": "Seiten",
    "One night between you and the buy button. Made by {company}. Write to {email} and a person will reply.":
        "Eine Nacht zwischen dir und dem Kaufen-Button. Von {company}. Schreib an {email}, und ein Mensch antwortet.",
    "The app": "Die App",
    "Download on the App Store": "Im App Store laden",
    "Help and legal": "Hilfe und Rechtliches",
    "Cookie choices": "Cookie-Einstellungen",
    "Money figures on this site are sample estimates. On Ice does not connect to a bank and does not give financial advice. Apple, iPhone, iPad, Safari and App Store are trademarks of Apple Inc. Amazon is a trademark of Amazon.com, Inc. or its affiliates, and On Ice is not affiliated with it.":
        "Geldbeträge auf dieser Website sind Beispielschätzungen. On Ice verbindet sich mit keiner Bank und gibt keine Finanzberatung. Apple, iPhone, iPad, Safari und App Store sind Marken von Apple Inc. Amazon ist eine Marke von Amazon.com, Inc. oder verbundenen Unternehmen, und On Ice ist nicht mit Amazon verbunden.",
    "This page in:": "Diese Seite auf:",
    "Support in other languages:": "Hilfe in anderen Sprachen:",
    # consent banner
    "This website counts visits with Google Analytics. Is a cookie for that OK with you?":
        "Diese Website zählt Besuche mit Google Analytics. Ist ein Cookie dafür für dich in Ordnung?",
    "What it collects": "Was erfasst wird",
    "No thanks": "Nein danke",
    "OK": "OK",
    # drawings (art.py)
    "Pause before you buy.": "Kurz Pause vor dem Kauf.",
    "24 hours": "24 Stunden",
    "Tonight": "Heute Nacht",
    "Tomorrow": "Morgen",
    "or": "oder",
    "Don't want it anymore": "Will ich nicht mehr",
    "Still want it": "Will ich immer noch",
    "You keep the money": "Du behältst das Geld",
    "The shop opens": "Der Shop öffnet sich",
    # hero demo (demo.py), the app's own strings where the screen shows them
    "You open a shopping app": "Du öffnest eine Shopping-App",
    "On Ice steps in first": "On Ice schaltet sich zuerst ein",
    "You note what you wanted": "Du notierst, was du wolltest",
    "You choose to wait": "Du entscheidest dich zu warten",
    "24 hours pass. Nothing is bought.": "24 Stunden vergehen. Nichts wird gekauft.",
    "Tomorrow, On Ice asks once": "Morgen fragt On Ice einmal",
    "You let it go and keep the money": "Du lässt es los und behältst das Geld",
    "DEMO_LABEL":
        "Eine animierte Zeichnung von On Ice. Jemand öffnet Amazon auf einem iPhone. On Ice legt eine Sperre darüber: Kurz Pause vor dem Kauf. "
        "Die Person tippt auf Notieren, gibt Leinenhemd für etwa 50 Euro ein und tippt auf 24 Std. warten, dann entscheiden. Ein Tag vergeht, "
        "und nichts wird gekauft. Dann fragt On Ice einmal: Willst du das Leinenhemd immer noch? Die Person tippt auf Will ich nicht mehr, "
        "und etwa 50 Euro wandern in ihre geschätzte Ersparnis.",
    "APPS": ["Mail", "Fotos", "Karten", "Notizen", "Musik", "Amazon", "Uhr", "Wetter", "Bücher", "Health", "Dateien", "Kamera"],
    "In stock": "Auf Lager",
    "Buy now": "Jetzt kaufen",
    "In a shop you chose": "In einem Shop, den du gewählt hast",
    "Want something here? Note it in On Ice and decide later.": "Willst du hier etwas? Notiere es in On Ice und entscheide später.",
    "Note it": "Notieren",
    "Never mind": "Doch nicht",
    "What caught your eye?": "Was ist dir ins Auge gefallen?",
    "Name": "Name",
    "Roughly what does it cost?": "Was kostet es ungefähr?",
    "Optional": "Optional",
    "How are you feeling?": "Wie fühlst du dich?",
    "Bored": "Langeweile",
    "Stressed": "Stress",
    "Deal FOMO": "Angebots-FOMO",
    "Next": "Weiter",
    "Decide later?": "Später entscheiden?",
    "A linen shirt": "Ein Leinenhemd",
    "Right now": "Jetzt sofort",
    "Nothing is bought. Your note goes on the list.": "Es wird nichts gekauft. Deine Notiz kommt auf die Liste.",
    "On Ice asks once: still want it?": "On Ice fragt einmal: Willst du es noch?",
    "If you let it go": "Wenn du es loslässt",
    "{price} joins your estimated savings.": "{price} wandert in deine geschätzte Ersparnis.",
    "Wait 24h, then decide": "24 Std. warten, dann entscheiden",
    "I need to shop now": "Ich muss jetzt einkaufen",
    "1 minute": "1 Minute",
    "5 minutes": "5 Minuten",
    "15 minutes": "15 Minuten",
    "until you decide": "bis du entscheidest",
    "It's on your list": "Es steht auf deiner Liste",
    "Tomorrow at 9:41 PM": "Morgen um 21:41",
    "On Ice asks once: still want it? If you do, the shop opens for you.": "On Ice fragt einmal: Willst du es noch? Wenn ja, öffnet sich der Shop für dich.",
    "Done": "Fertig",
    "Later": "Später",
    "Still want the linen shirt?": "Willst du das Leinenhemd immer noch?",
    "You noted it yesterday · {price} estimated": "Du hast es gestern notiert · {price} geschätzt",
    "Either answer is a good one.": "Beide Antworten sind gut.",
    "Savings": "Ersparnis",
    "Today": "Heute",
    "Week": "Woche",
    "Month": "Monat",
    "Saved this month": "Diesen Monat gespart",
    "From 1 item you let go this month. Your own estimate, nothing is tracked.":
        "Aus 1 Artikel, den du diesen Monat losgelassen hast. Deine eigene Schätzung, nichts wird verfolgt.",
    "Let go today · {price} estimated": "Heute losgelassen · {price} geschätzt",
    "Pause the demo": "Demo anhalten",
    "Play the demo": "Demo abspielen",
}

T["es"] = {
    "Stop Impulse Buying: On Ice, the Shopping Blocker for iPhone":
        "Deja las compras por impulso: On Ice, el bloqueador de compras para iPhone",
    "On Ice shields the shopping apps and websites you choose, holds each want for 24 hours, and adds up what you didn't spend. Free to start, no account.":
        "On Ice bloquea las apps y webs de compras que elijas, retiene cada antojo 24 horas y suma lo que no gastaste. Empieza gratis, sin cuenta.",
    "On Ice: stop impulse buying. Sleep on it first.": "On Ice: deja las compras por impulso. Consúltalo con la almohada.",
    "A shopping blocker for iPhone and iPad that shields the shopping apps and websites you choose and holds each want for 24 hours.":
        "Un bloqueador de compras para iPhone y iPad que bloquea las apps y webs de compras que elijas y retiene cada antojo 24 horas.",
    "Shopping blocker for iPhone and iPad": "Bloqueador de compras para iPhone y iPad",
    "Stop impulse buying. <em>Sleep on it first.</em>": "Deja las compras por impulso. <em>Consúltalo con la almohada.</em>",
    "On Ice pauses you when you open a shopping app or website. Note what you wanted, wait one night, then decide.":
        "On Ice te detiene un momento cuando abres una app o web de compras. Anota lo que querías, espera una noche y luego decide.",
    "Free to start. No account.<br>No bank linking.": "Empieza gratis. Sin cuenta.<br>Sin conectar el banco.",
    "Three steps. <em>One night.</em>": "Tres pasos. <em>Una noche.</em>",
    "1 · Tonight": "1 · Esta noche",
    "A drawing of a shopping bag with a pause button on it, and the words: Pause before you buy.":
        "Un dibujo de una bolsa de compras con un botón de pausa y las palabras: Pausa antes de comprar.",
    "On Ice pauses you": "On Ice te detiene",
    "Open a shopping app or website and On Ice steps in before you can buy.":
        "Abre una app o web de compras y On Ice interviene antes de que puedas comprar.",
    "2 · Still tonight": "2 · Todavía esta noche",
    "A drawing of a shirt frozen inside an ice cube. Under it, a line from tonight's moon to tomorrow's sun, marked 24 hours.":
        "Un dibujo de una camisa congelada dentro de un cubito de hielo. Debajo, una línea de la luna de esta noche al sol de mañana, marcada 24 horas.",
    "You wait one night": "Esperas una noche",
    "Write down what you wanted. It waits on your list for 24 hours. Nothing is bought.":
        "Anota lo que querías. Espera en tu lista 24 horas. No se compra nada.",
    "3 · Tomorrow": "3 · Mañana",
    "A drawing of two answers. Don't want it anymore, with a savings jar: you keep the money. Or, Still want it, with a shopping bag: the shop opens.":
        "Un dibujo de dos respuestas. Ya no lo quiero, con un frasco de ahorro: te quedas el dinero. O Todavía lo quiero, con una bolsa de compras: la tienda se abre.",
    "You decide": "Tú decides",
    "Don't want it anymore? Its price joins your estimated savings. Still want it? The shop opens. Either answer is a good one.":
        "¿Ya no lo quieres? Su precio pasa a tu ahorro estimado. ¿Todavía lo quieres? La tienda se abre. Cualquier respuesta está bien.",
    "Really need to buy something now? The shop opens for 1, 5 or 15 minutes.":
        "¿De verdad necesitas comprar algo ahora? La tienda se abre durante 1, 5 o 15 minutos.",
    "See the real screens, step by step": "Las pantallas reales, paso a paso (en inglés)",
    "See what you <em>didn't</em> spend.": "Mira lo que <em>no</em> gastaste.",
    "Every item you let go adds to a running total. It is built from prices you typed yourself, and it always says estimated.":
        "Cada artículo que dejas ir se suma a un total. Se calcula con los precios que escribiste tú y siempre dice estimado.",
    "No bank linking": "Sin conectar el banco",
    "On Ice never connects to an account or reads a transaction.": "On Ice nunca se conecta a una cuenta ni lee una transacción.",
    "No account": "Sin cuenta",
    "No sign up, no email field.": "Sin registro, sin campo de correo.",
    "Private": "Privado",
    "Your list stays on your device.": "Tu lista se queda en tu dispositivo.",
    "How the privacy works, in full": "Cómo funciona la privacidad, al completo",
    "A sample receipt of things not bought this month": "Un recibo de ejemplo de cosas que no compraste este mes",
    "THINGS YOU DIDN'T BUY": "COSAS QUE NO COMPRASTE",
    "Linen shirt": "Camisa de lino",
    "Running shoes": "Zapatillas de correr",
    "LET GO THIS MONTH": "DEJADO IR ESTE MES",
    "estimated": "estimado",
    "Sample figures. Every amount is your own estimate.": "Cifras de ejemplo. Cada importe es tu propia estimación.",
    "Free to start. <em>Premium if you want more.</em>": "Empieza gratis. <em>Premium si quieres más.</em>",
    "Free": "Gratis",
    "No charge, no trial clock": "Sin coste, sin periodo de prueba que se agote",
    "One shopping app and one website, shielded": "Una app de compras y una web, bloqueadas",
    "The 24 hour wait and your list": "El periodo de reflexión de 24 horas y tu lista",
    "Your estimated savings": "Tu ahorro estimado",
    "Premium": "Premium",
    "Monthly · Yearly · Lifetime · Family": "Mensual · Anual · De por vida · Familiar",
    "Every shop and website you want": "Todas las tiendas y webs que quieras",
    "Waits of 12, 24, 48 or 72 hours": "Esperas de 12, 24, 48 o 72 horas",
    "Daily limits, danger hours and strict mode": "Límites diarios, horas de riesgo y modo estricto",
    "Nothing you built is taken away if a subscription lapses.": "Si una suscripción caduca, no pierdes nada de lo que creaste.",
    "Plans and prices": "Planes y precios (en inglés)",
    "Questions people ask first": "Lo primero que pregunta la gente",
    "Something else? <a href=\"{support}\">The full support page</a> covers setup, troubleshooting and how to reach us.":
        "¿Algo más? <a href=\"{support}\">La página de ayuda</a> explica la configuración, la solución de problemas y cómo contactarnos.",
    "Put your next impulse buy <em>on ice.</em>": "Pon tu próxima compra por impulso <em>en pausa.</em>",
    "iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.":
        "iPhone y iPad, iOS 17 o posterior.<br>En español y en otros siete idiomas.",
    "Download on the": "Descárgalo en el",
    "Get the app": "Descargar la app",
    "Skip to content": "Ir al contenido",
    "Pages": "Páginas",
    "One night between you and the buy button. Made by {company}. Write to {email} and a person will reply.":
        "Una noche entre tú y el botón de comprar. Hecho por {company}. Escribe a {email} y te responderá una persona.",
    "The app": "La app",
    "Download on the App Store": "Descargar en el App Store",
    "Help and legal": "Ayuda y aspectos legales",
    "Cookie choices": "Opciones de cookies",
    "Money figures on this site are sample estimates. On Ice does not connect to a bank and does not give financial advice. Apple, iPhone, iPad, Safari and App Store are trademarks of Apple Inc. Amazon is a trademark of Amazon.com, Inc. or its affiliates, and On Ice is not affiliated with it.":
        "Las cifras de dinero de este sitio son estimaciones de ejemplo. On Ice no se conecta a ningún banco ni da asesoramiento financiero. Apple, iPhone, iPad, Safari y App Store son marcas de Apple Inc. Amazon es una marca de Amazon.com, Inc. o sus filiales, y On Ice no está afiliada a ella.",
    "This page in:": "Esta página en:",
    "Support in other languages:": "Ayuda en otros idiomas:",
    "This website counts visits with Google Analytics. Is a cookie for that OK with you?":
        "Este sitio cuenta las visitas con Google Analytics. ¿Te parece bien una cookie para eso?",
    "What it collects": "Qué recopila",
    "No thanks": "No, gracias",
    "OK": "OK",
    "Pause before you buy.": "Pausa antes de comprar.",
    "24 hours": "24 horas",
    "Tonight": "Esta noche",
    "Tomorrow": "Mañana",
    "or": "o",
    "Don't want it anymore": "Ya no lo quiero",
    "Still want it": "Todavía lo quiero",
    "You keep the money": "Te quedas el dinero",
    "The shop opens": "La tienda se abre",
    "You open a shopping app": "Abres una app de compras",
    "On Ice steps in first": "On Ice interviene primero",
    "You note what you wanted": "Anotas lo que querías",
    "You choose to wait": "Decides esperar",
    "24 hours pass. Nothing is bought.": "Pasan 24 horas. No se compra nada.",
    "Tomorrow, On Ice asks once": "Mañana, On Ice pregunta una vez",
    "You let it go and keep the money": "Lo dejas ir y te quedas el dinero",
    "DEMO_LABEL":
        "Un dibujo animado de On Ice en acción. Alguien abre Amazon en un iPhone. On Ice lo cubre con un bloqueo: Pausa antes de comprar. "
        "Toca Anotarlo, escribe Camisa de lino por unos 50 euros y toca Esperar 24 h y decidir. Pasa un día y no se compra nada. "
        "Luego On Ice pregunta una vez: ¿Todavía quieres la camisa de lino? Toca Ya no lo quiero, y unos 50 euros pasan a su ahorro estimado.",
    "APPS": ["Mail", "Fotos", "Mapas", "Notas", "Música", "Amazon", "Reloj", "Tiempo", "Libros", "Salud", "Archivos", "Cámara"],
    "In stock": "En stock",
    "Buy now": "Comprar ahora",
    "In a shop you chose": "En una tienda que elegiste",
    "Want something here? Note it in On Ice and decide later.": "¿Quieres algo de aquí? Anótalo en On Ice y decide después.",
    "Note it": "Anotarlo",
    "Never mind": "Mejor no",
    "What caught your eye?": "¿Qué te llamó la atención?",
    "Name": "Nombre",
    "Roughly what does it cost?": "¿Cuánto cuesta más o menos?",
    "Optional": "Opcional",
    "How are you feeling?": "¿Cómo te sientes?",
    "Bored": "Aburrimiento",
    "Stressed": "Estrés",
    "Deal FOMO": "FOMO de oferta",
    "Next": "Siguiente",
    "Decide later?": "¿Decidir después?",
    "A linen shirt": "Una camisa de lino",
    "Right now": "Ahora mismo",
    "Nothing is bought. Your note goes on the list.": "No se compra nada. Tu nota va a la lista.",
    "On Ice asks once: still want it?": "On Ice te pregunta una vez: ¿todavía lo quieres?",
    "If you let it go": "Si lo dejas ir",
    "{price} joins your estimated savings.": "{price} pasa a tu ahorro estimado.",
    "Wait 24h, then decide": "Esperar 24 h y decidir",
    "I need to shop now": "Necesito comprar ahora",
    "1 minute": "1 minuto",
    "5 minutes": "5 minutos",
    "15 minutes": "15 minutos",
    "until you decide": "hasta que decidas",
    "It's on your list": "Ya está en tu lista",
    "Tomorrow at 9:41 PM": "Mañana a las 21:41",
    "On Ice asks once: still want it? If you do, the shop opens for you.": "On Ice te pregunta una vez: ¿todavía lo quieres? Si es así, la tienda se abre para ti.",
    "Done": "Listo",
    "Later": "Más tarde",
    "Still want the linen shirt?": "¿Todavía quieres la camisa de lino?",
    "You noted it yesterday · {price} estimated": "Lo anotaste ayer · {price} estimado",
    "Either answer is a good one.": "Cualquier respuesta está bien.",
    "Savings": "Ahorro",
    "Today": "Hoy",
    "Week": "Semana",
    "Month": "Mes",
    "Saved this month": "Ahorrado este mes",
    "From 1 item you let go this month. Your own estimate, nothing is tracked.":
        "De 1 artículo que dejaste ir este mes. Tu propia estimación: no se rastrea nada.",
    "Let go today · {price} estimated": "Dejado ir hoy · {price} estimado",
    "Pause the demo": "Pausar la demo",
    "Play the demo": "Reproducir la demo",
}

T["ja"] = {
    "Stop Impulse Buying: On Ice, the Shopping Blocker for iPhone": "衝動買いをやめる：On Ice、iPhone用の買い物ブロッカー",
    "On Ice shields the shopping apps and websites you choose, holds each want for 24 hours, and adds up what you didn't spend. Free to start, no account.":
        "On Ice は選んだショッピングアプリとサイトをブロックし、欲しいものを24時間保留して、使わなかった金額を合計します。無料で始められ、アカウントは不要です。",
    "On Ice: stop impulse buying. Sleep on it first.": "On Ice：衝動買いをやめる。まずは一晩寝かせて。",
    "A shopping blocker for iPhone and iPad that shields the shopping apps and websites you choose and holds each want for 24 hours.":
        "選んだショッピングアプリとサイトをブロックし、欲しいものを24時間保留する、iPhone・iPad用の買い物ブロッカー。",
    "Shopping blocker for iPhone and iPad": "iPhone・iPad用の買い物ブロッカー",
    "Stop impulse buying. <em>Sleep on it first.</em>": "衝動買いをやめる。<em>まずは一晩寝かせて。</em>",
    "On Ice pauses you when you open a shopping app or website. Note what you wanted, wait one night, then decide.":
        "ショッピングアプリやサイトを開くと、On Ice がひと呼吸おかせます。欲しかったものをメモして、一晩待ってから決めましょう。",
    "Free to start. No account.<br>No bank linking.": "無料で始められます。アカウント不要。<br>銀行連携なし。",
    "Three steps. <em>One night.</em>": "3つのステップ。<em>一晩だけ。</em>",
    "1 · Tonight": "1 · 今夜",
    "A drawing of a shopping bag with a pause button on it, and the words: Pause before you buy.":
        "一時停止ボタンのついた買い物袋のイラストと「買う前にひと呼吸。」の文字。",
    "On Ice pauses you": "On Ice がひと呼吸おかせる",
    "Open a shopping app or website and On Ice steps in before you can buy.":
        "ショッピングアプリやサイトを開くと、買う前に On Ice が割って入ります。",
    "2 · Still tonight": "2 · 同じ夜に",
    "A drawing of a shirt frozen inside an ice cube. Under it, a line from tonight's moon to tomorrow's sun, marked 24 hours.":
        "氷の中に閉じ込められたシャツのイラスト。その下に、今夜の月から明日の太陽まで「24時間」と書かれた線。",
    "You wait one night": "一晩待つ",
    "Write down what you wanted. It waits on your list for 24 hours. Nothing is bought.":
        "欲しかったものを書き留めます。24時間リストで待機します。何も購入されません。",
    "3 · Tomorrow": "3 · 明日",
    "A drawing of two answers. Don't want it anymore, with a savings jar: you keep the money. Or, Still want it, with a shopping bag: the shop opens.":
        "2つの答えのイラスト。「もう欲しくない」と貯金瓶：お金は手元に残ります。または「まだ欲しい」と買い物袋：ショップが開きます。",
    "You decide": "あなたが決める",
    "Don't want it anymore? Its price joins your estimated savings. Still want it? The shop opens. Either answer is a good one.":
        "もう欲しくない？その価格が推定節約額に加わります。まだ欲しい？ショップが開きます。どちらの答えでも大丈夫です。",
    "Really need to buy something now? The shop opens for 1, 5 or 15 minutes.":
        "本当に今すぐ買う必要がある？ショップが1分、5分、15分のいずれかだけ開きます。",
    "See the real screens, step by step": "実際の画面をステップごとに見る（英語）",
    "See what you <em>didn't</em> spend.": "<em>使わなかった</em>お金が見える。",
    "Every item you let go adds to a running total. It is built from prices you typed yourself, and it always says estimated.":
        "手放したものはすべて合計に加わります。合計はあなたが入力した価格から計算され、常に「推定」と表示されます。",
    "No bank linking": "銀行連携なし",
    "On Ice never connects to an account or reads a transaction.": "On Ice は口座に接続することも、取引を読み取ることもありません。",
    "No account": "アカウント不要",
    "No sign up, no email field.": "登録もメールアドレスの入力もありません。",
    "Private": "プライベート",
    "Your list stays on your device.": "リストはあなたのデバイスに保存されます。",
    "How the privacy works, in full": "プライバシーの詳しい仕組み",
    "A sample receipt of things not bought this month": "今月買わなかったもののレシート（例）",
    "THINGS YOU DIDN'T BUY": "買わなかったもの",
    "Linen shirt": "リネンシャツ",
    "Running shoes": "ランニングシューズ",
    "LET GO THIS MONTH": "今月手放した分",
    "estimated": "推定",
    "Sample figures. Every amount is your own estimate.": "数字は例です。金額はすべてご自身の見積もりです。",
    "Free to start. <em>Premium if you want more.</em>": "無料で始める。<em>もっと使いたければ Premium。</em>",
    "Free": "無料",
    "No charge, no trial clock": "料金なし、試用期限なし",
    "One shopping app and one website, shielded": "ショッピングアプリ1つとサイト1つをブロック",
    "The 24 hour wait and your list": "24時間のクールダウンとリスト",
    "Your estimated savings": "推定節約額",
    "Premium": "Premium",
    "Monthly · Yearly · Lifetime · Family": "月額・年額・買い切り・ファミリー",
    "Every shop and website you want": "好きなだけショップとサイトを",
    "Waits of 12, 24, 48 or 72 hours": "12・24・48・72時間のクールダウン",
    "Daily limits, danger hours and strict mode": "1日の上限、危ない時間帯、厳格モード",
    "Nothing you built is taken away if a subscription lapses.": "サブスクリプションが切れても、作ったものが消えることはありません。",
    "Plans and prices": "プランと価格（英語）",
    "Questions people ask first": "よくある質問",
    "Something else? <a href=\"{support}\">The full support page</a> covers setup, troubleshooting and how to reach us.":
        "ほかにご質問は？<a href=\"{support}\">ヘルプページ</a>で、設定方法、トラブルの対処、お問い合わせ方法をご案内しています。",
    "Put your next impulse buy <em>on ice.</em>": "次の衝動買いは、<em>いったん保留に。</em>",
    "iPhone and iPad, iOS 17 or newer.<br>English and seven other languages.":
        "iPhone・iPad、iOS 17以降。<br>日本語を含む8言語に対応。",
    "Download on the": "ダウンロード",
    "Get the app": "アプリを入手",
    "Skip to content": "本文へスキップ",
    "Pages": "ページ",
    "One night between you and the buy button. Made by {company}. Write to {email} and a person will reply.":
        "あなたと購入ボタンのあいだに、一晩を。開発：{company}。{email} までご連絡いただければ、担当者が返信します。",
    "The app": "アプリ",
    "Download on the App Store": "App Storeからダウンロード",
    "Help and legal": "ヘルプと規約",
    "Cookie choices": "Cookieの設定",
    "Money figures on this site are sample estimates. On Ice does not connect to a bank and does not give financial advice. Apple, iPhone, iPad, Safari and App Store are trademarks of Apple Inc. Amazon is a trademark of Amazon.com, Inc. or its affiliates, and On Ice is not affiliated with it.":
        "このサイトの金額は見積もりの例です。On Ice は銀行に接続せず、金融に関する助言も行いません。Apple、iPhone、iPad、Safari、App Store は Apple Inc. の商標です。Amazon は Amazon.com, Inc. またはその関連会社の商標であり、On Ice は同社と提携していません。",
    "This page in:": "このページの他の言語：",
    "Support in other languages:": "他の言語のヘルプ：",
    "This website counts visits with Google Analytics. Is a cookie for that OK with you?":
        "このサイトは Google Analytics で訪問数を数えています。そのための Cookie を使ってもよろしいですか？",
    "What it collects": "収集する内容",
    "No thanks": "同意しない",
    "OK": "OK",
    "Pause before you buy.": "買う前にひと呼吸。",
    "24 hours": "24時間",
    "Tonight": "今夜",
    "Tomorrow": "明日",
    "or": "または",
    "Don't want it anymore": "もう欲しくない",
    "Still want it": "まだ欲しい",
    "You keep the money": "お金は手元に",
    "The shop opens": "ショップが開く",
    "You open a shopping app": "ショッピングアプリを開く",
    "On Ice steps in first": "まず On Ice が割って入る",
    "You note what you wanted": "欲しかったものをメモする",
    "You choose to wait": "待つことを選ぶ",
    "24 hours pass. Nothing is bought.": "24時間が過ぎる。何も買っていない。",
    "Tomorrow, On Ice asks once": "明日、On Ice が一度だけ聞く",
    "You let it go and keep the money": "手放して、お金を残す",
    "DEMO_LABEL":
        "On Ice が動くようすのアニメーション。iPhoneで Amazon を開くと、On Ice がブロック画面で覆います：買う前にひと呼吸。"
        "「メモする」をタップし、リネンシャツを約7,000円と入力して「24時間待ってから決める」をタップ。一日が過ぎ、何も買われません。"
        "そのあと On Ice が一度だけ聞きます：リネンシャツ、まだ欲しいですか？「もう欲しくない」をタップすると、約7,000円が推定節約額に加わります。",
    "APPS": ["メール", "写真", "マップ", "メモ", "ミュージック", "Amazon", "時計", "天気", "ブック", "ヘルスケア", "ファイル", "カメラ"],
    "In stock": "在庫あり",
    "Buy now": "今すぐ購入",
    "In a shop you chose": "選んだショップで",
    "Want something here? Note it in On Ice and decide later.": "欲しいものがありますか？On Ice にメモして、あとで決めましょう。",
    "Note it": "メモする",
    "Never mind": "やめておく",
    "What caught your eye?": "何が気になりましたか？",
    "Name": "名前",
    "Roughly what does it cost?": "だいたいいくらですか？",
    "Optional": "任意",
    "How are you feeling?": "今の気分は？",
    "Bored": "退屈",
    "Stressed": "ストレス",
    "Deal FOMO": "買い逃したくない",
    "Next": "次へ",
    "Decide later?": "あとで決めますか？",
    "A linen shirt": "リネンシャツ",
    "Right now": "今すぐ",
    "Nothing is bought. Your note goes on the list.": "何も購入されません。メモはリストに入ります。",
    "On Ice asks once: still want it?": "On Iceが一度だけ「まだ欲しいですか？」と聞きます。",
    "If you let it go": "手放したら",
    "{price} joins your estimated savings.": "{price}が推定節約額に加わります。",
    "Wait 24h, then decide": "24時間待ってから決める",
    "I need to shop now": "今すぐ買い物をしたい",
    "1 minute": "1分",
    "5 minutes": "5分",
    "15 minutes": "15分",
    "until you decide": "決めるまで",
    "It's on your list": "リストに入りました",
    "Tomorrow at 9:41 PM": "明日 21:41",
    "On Ice asks once: still want it? If you do, the shop opens for you.": "On Iceが一度だけ「まだ欲しいですか？」と聞きます。欲しければショップが開きます。",
    "Done": "完了",
    "Later": "あとで",
    "Still want the linen shirt?": "リネンシャツ、まだ欲しいですか？",
    "You noted it yesterday · {price} estimated": "昨日に記録しました · {price} 推定",
    "Either answer is a good one.": "どちらの答えでも大丈夫です。",
    "Savings": "節約",
    "Today": "今日",
    "Week": "週",
    "Month": "月",
    "Saved this month": "今月の節約額",
    "From 1 item you let go this month. Your own estimate, nothing is tracked.":
        "今月手放した1件から。あなた自身の見積もりで、何も追跡されていません。",
    "Let go today · {price} estimated": "今日手放しました · {price} 推定",
    "Pause the demo": "デモを一時停止",
    "Play the demo": "デモを再生",
}

# The home page's questions (FAQ in site_pages.py, without the two about Premium
# and deleting the app), in the same order.
FAQ = {
    "de": [
        ("Sperrt mich On Ice aus meinen Shopping-Apps aus?",
         "Nein. Eine normale Sperre ist eine Pause, keine Mauer. Tippe auf <kbd>Notieren</kbd>, sag, was dir ins Auge gefallen ist, und "
         "<kbd>Ich muss jetzt einkaufen</kbd> öffnet den Shop für 1, 5 oder 15 Minuten. Ganz ohne Ausweg sind nur Dinge, die du selbst "
         "eingerichtet hast, etwa ein erreichtes Tageslimit, eine zeitgesteuerte Sperre oder eine feste Regel für einen Shop. Jede davon endet von selbst."),
        ("Sperrt es Shopping-Websites oder nur Apps?",
         "Beides. Füge die App eines Shops und seine Website getrennt hinzu, dann ist beides gesperrt, die Website in Safari."),
        ("Funktioniert es mit Amazon, Temu, Shein und den anderen?",
         "Du wählst die Apps in Apples eigener Bildschirmzeit-Auswahl und fügst Websites per Adresse hinzu. So funktioniert es mit genau den "
         "Shops, die dich verführen. On Ice erfährt nie die Namen der Apps, die du auswählst. Apple gibt stattdessen private Codes weiter."),
        ("Sieht On Ice, was ich kaufe?",
         "Nein. On Ice hat keinen Zugriff auf deine Bank, deine Bestellungen, deinen Browserverlauf oder deine Karte. Es speichert nur seine "
         "eigenen Ereignisse: dass eine Sperre angezeigt wurde und was du gewählt hast. Diese bleiben auf deinem Gerät."),
        ("Was passiert mit dem, was ich notiert habe?",
         "Es wartet 24 Stunden auf deiner Liste. Dann fragt On Ice einmal: Willst du es noch? Lässt du es los, wandert der Preis, den du "
         "geschätzt hast, in deine geschätzte Ersparnis. Willst du es noch, öffnet sich der Shop für dich. Beide Antworten sind gut."),
        ("Ist On Ice kostenlos?",
         "Ja, und kostenlos ist ein funktionierendes Produkt, keine Demo: eine Shopping-App und eine Website gesperrt, die 24-Stunden-Bedenkzeit "
         "und deine Liste, deine geschätzte Ersparnis, die Atempause, drei Alternativen, das Tagebuch, ein tägliches Zeitziel fürs Shoppen "
         "und zeitgesteuerte Sperren."),
        ("Welche Geräte brauche ich?",
         "Ein iPhone oder iPad mit iOS 17 oder neuer. Es gibt kein Konto. Jedes Gerät hat seine eigenen Shops, seine eigene Liste und seinen "
         "eigenen Verlauf, und nichts wird zwischen ihnen synchronisiert."),
    ],
    "es": [
        ("¿On Ice me bloqueará el acceso a mis apps de compras?",
         "No. Un bloqueo normal es una pausa, no un muro. Toca <kbd>Anotarlo</kbd>, di qué te llamó la atención y "
         "<kbd>Necesito comprar ahora</kbd> abre la tienda durante 1, 5 o 15 minutos. Lo único sin salida es lo que tú mismo configuras, "
         "como un límite diario que ya alcanzaste, un bloqueo programado o una regla estricta para una tienda. Todo eso termina solo."),
        ("¿Bloquea webs de compras o solo apps?",
         "Ambas. Añade por separado la app de una tienda y su web, y cada una queda bloqueada; la web, en Safari."),
        ("¿Funciona con Amazon, Temu, Shein y las demás?",
         "Eliges las apps en el selector de Tiempo de uso de Apple y añades webs por su dirección, así que funciona con las tiendas que te "
         "tientan a ti. On Ice nunca conoce los nombres de las apps que eliges. Apple le pasa códigos privados en su lugar."),
        ("¿On Ice ve lo que compro?",
         "No. No tiene acceso a tu banco, tus pedidos, tu navegación ni tu tarjeta. Solo registra sus propios eventos: que se mostró un "
         "bloqueo y qué elegiste. Eso se queda en tu dispositivo."),
        ("¿Qué pasa con lo que anoté?",
         "Espera en tu lista 24 horas. Luego On Ice te pregunta una vez: ¿todavía lo quieres? Si lo dejas ir, el precio que calculaste pasa "
         "a tu ahorro estimado. Si todavía lo quieres, la tienda se abre para ti. Cualquier respuesta está bien."),
        ("¿On Ice es gratis?",
         "Sí, y la versión gratis es un producto que funciona, no una demo: una app de compras y una web bloqueadas, el periodo de reflexión "
         "de 24 horas y tu lista, tu ahorro estimado, la pausa de respiración, tres cosas que hacer en su lugar, el diario, un objetivo "
         "diario de tiempo de compras y los bloqueos programados."),
        ("¿Qué dispositivos necesito?",
         "Un iPhone o iPad con iOS 17 o posterior. No hay cuenta. Cada dispositivo guarda sus propias tiendas, lista e historial, y nada se "
         "sincroniza entre ellos."),
    ],
    "ja": [
        ("On Ice でショッピングアプリが使えなくなりますか？",
         "いいえ。通常のブロック画面は壁ではなく、ひと呼吸です。<kbd>メモする</kbd>をタップして気になったものを書けば、"
         "<kbd>今すぐ買い物をしたい</kbd>でショップが1分、5分、15分のいずれかだけ開きます。抜け道がないのは、達した1日の上限、"
         "時間指定ブロック、特定のショップの厳しいルールなど、あなた自身が設定したものだけです。どれも時間が来れば終わります。"),
        ("ショッピングサイトもブロックできますか？アプリだけですか？",
         "両方できます。ショップのアプリとWebサイトを別々に追加すると、それぞれがブロックされます。WebサイトはSafariでブロックされます。"),
        ("Amazon、Temu、SHEIN などでも使えますか？",
         "アプリはApple純正のスクリーンタイムの選択画面で選び、WebサイトはURLで追加します。だから、あなたがつい開いてしまうショップなら"
         "どれでも使えます。On Ice が選んだアプリの名前を知ることはありません。Appleは代わりに非公開のコードを渡します。"),
        ("On Ice は私が買ったものを見ますか？",
         "いいえ。銀行、注文、閲覧履歴、カードにはアクセスしません。記録するのは自分自身のイベント、つまりブロック画面が表示されたことと、"
         "あなたが何を選んだかだけです。それらはデバイスに保存されます。"),
        ("メモしたものはどうなりますか？",
         "24時間リストで待機します。そのあと On Ice が一度だけ「まだ欲しいですか？」と聞きます。手放せば、見積もった価格が推定節約額に"
         "加わります。まだ欲しければ、ショップが開きます。どちらの答えでも大丈夫です。"),
        ("On Ice は無料ですか？",
         "はい。無料版はお試し版ではなく、ちゃんと使える製品です。ショッピングアプリ1つとサイト1つのブロック、24時間のクールダウンと"
         "リスト、推定節約額、呼吸のひと休み、代わりにできる3つのこと、日記、1日の買い物時間の目標、時間指定ブロックが使えます。"),
        ("必要なデバイスは？",
         "iOS 17以降のiPhoneまたはiPadです。アカウントはありません。ショップ、リスト、履歴はデバイスごとに保存され、デバイス間で"
         "同期されることはありません。"),
    ],
}
