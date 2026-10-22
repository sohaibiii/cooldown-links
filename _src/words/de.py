# -*- coding: utf-8 -*-
"""Deutsch. Duzt, wie die App selbst duzt.

Die Begriffe stammen aus dem Katalog der App: Sperre (shield), Bedenkzeit und
Wartezeit (the wait, cooldown length), Auf Eis, loslassen (let go), behalten
(kept), Risikozeiten, strenger Modus, Shopping-Fenster, Tageslimit,
Ausgabenprotokoll, Tagebuch, KI-Reflexion, Wochenrückblick, Geschätzte
Ersparnis. Apple-Funktionen tragen Apples deutsche Namen: Bildschirmzeit,
Familienfreigabe, Apple Account, Bewegung & Fitness, Kontrollzentrum,
Home-Bildschirm, Sperrbildschirm, Live-Aktivitäten, Kurzbefehle, Fokus.
"""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Hilfe",
"nav.about": "Über",
"nav.privacy": "Datenschutz",
"nav.terms": "Bedingungen",
"nav.data": "Deine Daten",

"ui.skip": "Zum Inhalt springen",
"ui.pages": "Seiten",
"ui.footer": "Fußzeile",
"ui.lang": "Sprache",
"ui.toc": "Auf dieser Seite",
"ui.rights": "Alle Rechte vorbehalten.",
"ui.store_soon": "Bald im App Store",
"ui.store_get": "Im App Store laden",
"ui.date": "22. Oktober 2026",
"ui.last_updated": "Zuletzt aktualisiert: {DATE}",

# Copied from the app's Localizable.xcstrings and iOS's own German labels.
"k.settings": "Einstellungen",
"k.ios_settings": "Einstellungen",
"k.screen_time": "Bildschirmzeit",
"k.apps_with_st": "Apps mit Zugriff auf Bildschirmzeit",
"k.notifications": "Mitteilungen",
"k.restore": "Käufe wiederherstellen",
"k.protection_tools": "Schutztools",
"k.repair": "Schutz reparieren",
"k.someone_key": "Jemand verwahrt den Schlüssel",
"k.only_these": "Nur diese Apps",
"k.ai_reflection": "KI-Reflexion",
"k.writer": "Reflexion schreiben lassen von",
"k.what_gets_sent": "Was gesendet wird",
"k.lock_journal": "Tagebuch sperren",
"k.export_journal": "Tagebuch exportieren",
"k.delete_entry": "Eintrag löschen",
"k.reflect_week": "Meine Woche reflektieren",
"k.help_privacy": "Hilfe & Datenschutz",
"k.email_support": "Support per E-Mail",
"k.language": "Sprache",
"k.note_it": "Notieren",
"k.never_mind": "Doch nicht",
"k.need_to_shop": "Ich muss jetzt einkaufen",
"k.done_block": "Fertig – wieder blockieren",
"k.remove": "Entfernen",
"k.follow_ups": "Nachfragen",

"meta.support.title": "On Ice — Hilfe",
"meta.support.desc": "Offizielle Hilfe zu On Ice, der App für iPhone und iPad, die eine Nacht zwischen dich und den Kauf-Button legt. Wie es funktioniert, Voraussetzungen, FAQ und Kontakt.",
"meta.about.title": "On Ice — Eine Nacht zwischen dir und dem Kauf-Button",
"meta.about.desc": "On Ice sperrt die Shopping-Apps und Websites, die du auswählst, und bittet dich, erst eine Nacht darüber zu schlafen. Kein Bankzugriff, keine Preisverfolgung, keine Affiliate-Links.",
"meta.privacy.title": "Datenschutzerklärung — On Ice",
"meta.privacy.desc": "On Ice hat kein Konto, keine Bankverbindung und keine Analyse. Was auf deinem Gerät bleibt – und genau, was die eine optionale KI-Funktion sendet.",
"meta.terms.title": "Nutzungsbedingungen — On Ice",
"meta.terms.desc": "Nutzungsbedingungen (EULA) für On Ice: was die App ist und was nicht, warum jeder Betrag eine Schätzung ist, wie Premium und Familienpläne abgerechnet werden und worauf dich der strenge Modus festlegt.",
"meta.data.title": "Deine Daten löschen — On Ice",
"meta.data.desc": "Wie du entfernst, was On Ice speichert – alles davon auf deinem Gerät – und was mit deinem Abo passiert.",
"meta.nf.title": "Nicht gefunden — On Ice",
"meta.nf.desc": "Seite nicht gefunden.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Hilfe",
"s.h1": "Hilfe zu On Ice",
"s.sub": "Eine Nacht zwischen dir und dem Kauf-Button. On Ice sperrt die Shopping-Apps und Websites, die du ausgewählt hast, und bittet dich, erst eine Nacht darüber zu schlafen. Diese Seite erklärt, wie das funktioniert, was es braucht und wie du uns erreichst.",
"s.cta": "Zu den FAQ",
"s.meta": 'Kein Konto · kein Bankzugriff · <a href="{BASE}{L}/privacy/">Datenschutzerklärung</a>',

"s.how.h": "So funktioniert On Ice",
"s.how.b": """
<p class="lead">On Ice legt eine Nacht zwischen dich und den Kauf-Button.</p>
<p>Du wählst die Shopping-Apps und Websites, die dich am ehesten verleiten. Von da an führt dich das Öffnen einer davon nicht mehr direkt zur Kasse – zuerst kommt die Sperre von On Ice: <em>Kurz Pause vor dem Kauf.</em> Tippe auf {K_note_it}, um die Sache aufzuschreiben, oder auf {K_never_mind}, um sie sein zu lassen. Nichts wird je in deinem Namen gekauft oder storniert.</p>
<p>Alles, was du notierst, wartet auf deiner Liste – vierundzwanzig Stunden, sofern du keine andere Dauer gewählt hast. Ist die Wartezeit vorbei, stellt On Ice eine einzige Frage: Willst du es noch? Die meisten Wünsche überstehen die Nacht nicht, und die, die sie überstehen, waren echt. Beide Antworten sind gute Antworten.</p>
<ul class="rows">
  <li><span class="tile">{shield}</span><div><b>Schutz</b><span>Ein Schalter auf dem Startbildschirm und einer für jeden Shop. Solange er an ist, zeigen die Shops, die du ausgewählt hast, die Sperre von On Ice, statt sich zu öffnen – die App <em>und</em> die Website, auch in Safari.</span></div></li>
  <li><span class="tile">{moon}</span><div><b>Eine kurze Pause</b><span>Vor allem anderen ein Moment, um durchzuatmen, einen Satz zu tippen, eine Erinnerung zu lesen oder zu sagen, weswegen du gekommen bist. Du wählst, was davon, und wie lange.</span></div></li>
  <li><span class="tile">{note}</span><div><b>Notieren</b><span>Benenne die Sache, tippe einen ungefähren Preis an, tippe an, wie du dich fühlst – Langeweile, Stress, Feierlaune, Angebots-FOMO oder „Brauche ich“. Ein Bildschirm, fünfzehn Sekunden.</span></div></li>
  <li><span class="tile amber">{snow}</span><div><b>Auf Eis</b><span>Notierte Artikel warten unter einem Countdown-Ring. Solange ein Artikel abkühlt, wird nichts gekauft. Wenn du den Shop wirklich jetzt brauchst, öffnet er sich für ein paar Minuten, und die Sperre kommt von selbst zurück.</span></div></li>
  <li><span class="tile green">{coin}</span><div><b>Geschätzte Ersparnis</b><span>Jeder Artikel, den du loslässt, zählt zu einer laufenden Summe, die ganz aus Preisen besteht, die du selbst eingegeben hast – für heute, diese Woche und diesen Monat.</span></div></li>
  <li><span class="tile amber">{clock}</span><div><b>Ziele, Limits und Sperren</b><span>Ein tägliches Zeitziel fürs Shoppen, Tageslimits, zeitgesteuerte Sperren, Fokus-Sperren und Regeln für die Stunden, die schlecht laufen. Der strenge Modus hält deine Einrichtung fest.</span></div></li>
  <li><span class="tile">{book}</span><div><b>Etwas anderes tun</b><span>Ein privates Tagebuch und ein paar Alternativen – ein Spaziergang, ein Buch, ein Anruf – für die Momente, in denen das Verlangen irgendwohin muss.</span></div></li>
  <li><span class="tile">{widget}</span><div><b>Widgets, Live-Aktivitäten und Kurzbefehle</b><span>Die geschätzte Ersparnis und was auf Eis liegt auf dem Home-Bildschirm und dem Sperrbildschirm, ein Countdown, solange ein Shop offen ist, und Aktionen für Siri und Kurzbefehle, um eine Sperre zu starten.</span></div></li>
</ul>
""",

"s.requirements.h": "Voraussetzungen",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Gerät</th><td>iPhone oder iPad mit <strong>iOS 17 oder neuer</strong>. Ein paar Extras brauchen mehr: Steuerelemente im Kontrollzentrum brauchen iOS 18, und das Schreiben mit Apple Intelligence braucht ein Gerät und eine Sprache, die es unterstützen.</td></tr>
<tr><th>Berechtigung</th><td>Zugriff auf die <strong>Bildschirmzeit</strong>, einmalig bei der Einrichtung über Apples eigene Abfrage erteilt. On Ice nutzt Apples Bildschirmzeit-Framework – dasselbe System hinter den eingebauten App-Limits von iOS –, und Apple, nicht On Ice, ist das, was tatsächlich vor einem Shop steht.</td></tr>
<tr><th>Konto</th><td>Keins. Es gibt nirgends in der App eine Registrierung, ein E-Mail-Feld oder ein Passwort.</td></tr>
<tr><th>Internet</th><td>Nicht nötig. Jede Sperre, jede Pause, jede Liste, jeder Timer und jede Summe funktioniert offline. Der einzige Netzwerkverkehr ist der von Apple, wenn du Premium kaufst oder wiederherstellst – und die optionale KI-Reflexion, wenn du sie mit OpenAI als Verfasser einschaltest.</td></tr>
<tr><th>Sprachen</th><td>English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil) und 简体中文. On Ice folgt der Sprache deines Geräts oder der, die du unter {K_settings} → {K_language} wählst.</td></tr>
<tr><th>Optional</th><td><strong>Mitteilungen</strong>, auf dem Gerät erzeugt, um dich von der Sperre in die App zu übergeben und dir zu sagen, wann die Wartezeit eines Artikels vorbei ist. <strong>Bewegung &amp; Fitness</strong>, nur um während eines Spaziergangs deine Schritte live anzuzeigen. <strong>Face ID oder Touch ID</strong>, nur wenn du dein Tagebuch sperrst.</td></tr>
</table></div>
""",

"s.start.h": "Erste Schritte",
"s.start.b": """
<p>Die Einrichtung umfasst eine Handvoll Bildschirme und endet mit bereits eingeschaltetem Schutz.</p>
<ol class="steps">
  <li><div><b>Probier eine Zehn-Sekunden-Pause aus</b> – derselbe Moment, den dir die Sperre später geben wird.</div></li>
  <li><div><b>Erlaube den Zugriff auf die Bildschirmzeit</b>, wenn Apple fragt. Ohne ihn kann On Ice nicht arbeiten, und du kannst ihn jederzeit unter {K_ios_settings} → {K_screen_time} widerrufen.</div></li>
  <li><div><b>Wähle deine Shops</b> in Apples Auswahl und füge die Shopping-Websites hinzu, die du sperren willst. On Ice erfährt nie die Namen der Apps, die du auswählst – siehe <a href="{BASE}{L}/privacy/#screentime">Datenschutz</a>.</div></li>
  <li><div><b>Lege Risikozeiten fest</b>, wenn du möchtest – die späten Stunden, in denen das Shoppen schlecht läuft. Optional und später änderbar.</div></li>
  <li><div><b>Fertig.</b> Öffne einen deiner Shops und lerne die Sperre kennen.</div></li>
</ol>
<div class="callout"><span class="tile">{info}</span><div>Die erste Sperre kann abrupt wirken. Genau für diesen Moment gibt es die App – tippe auf {K_note_it} und nimm dir fünfzehn Sekunden.</div></div>
""",

"s.money.h": "Zur Ersparnis-Zahl",
"s.money.b": """
<p>Jeder Preis in On Ice ist einer, den du selbst eingegeben hast, und jeder Geldbetrag, den die App zeigt, ist als <strong>geschätzt</strong> gekennzeichnet. Das ist kein nachträglich angeschraubter Haftungsausschluss – es ist das ganze Konzept.</p>
<ul>
  <li>On Ice <strong>verbindet sich nicht mit deiner Bank</strong>, liest nicht deinen Kaufverlauf, prüft nicht, was etwas tatsächlich kostet, und rechnet nicht zwischen Währungen um.</li>
  <li>Ein Artikel zählt <strong>einmal</strong> zur Summe, wenn du ihn nach seiner Wartezeit loslässt.</li>
  <li>Kommst du nie auf einen Artikel zurück, erinnert dich On Ice daran, und 48 Stunden nach dem Ende seiner Wartezeit zählt es den Artikel als losgelassen. Bis dahin kannst du jederzeit entscheiden.</li>
  <li>Artikel, die du behältst, berühren die Summe nicht – es sei denn, du sagst On Ice später, dass du einen günstiger gekauft hast als geschätzt; dann zählt die Differenz.</li>
  <li>Das <strong>Ausgabenprotokoll</strong> ist für Spontankäufe, die On Ice nie gesehen hat. Es wird getrennt von deiner Ersparnis geführt.</li>
</ul>
<div class="callout green"><span class="tile">{coin}</span><div>Die Zahl ist eine Aufzeichnung dessen, was du beschlossen hast, nicht zu kaufen, zu den Preisen, die du geschätzt hast. Es ist eine gute Zahl, um stolz darauf zu sein, und eine schlechte Zahl für eine Tabellenkalkulation.</div></div>
""",

"s.faq.h": "Häufige Fragen",
"s.faq.b": """
<dl class="faq">
<dt>Ist On Ice kostenlos?</dt>
<dd>Ja, und kostenlos ist ein funktionierendes Produkt, keine Demo: <strong>eine Shopping-App und eine Website</strong> gesperrt, die 24-Stunden-Bedenkzeit und deine Liste, deine geschätzte Ersparnis, die Atempause, drei Alternativen, das Tagebuch, ein tägliches Zeitziel fürs Shoppen sowie zeitgesteuerte Sperren und Fokus-Sperren.</dd>
<dt>Was kommt mit Premium dazu?</dt>
<dd>Jeder Shop und jede Website, die du sperren willst; Wartezeiten von 12, 24, 48 oder 72 Stunden; jede Art von Pause, Pausen, die bei wiederholten Versuchen länger werden, und deine eigenen Erinnerungen; Risikozeiten-Regeln und Regeln pro Shop; Tageslimits; der strenge Modus; deine Einkaufsmuster und wie sich Käufe danach angefühlt haben; ein Rückblick auf dein Tagebuch; sechs Alternativen; Widgets; und die optionale KI-Reflexion. Premium ist ein Monats- oder Jahresabo – das Jahresabo beginnt mit einer <strong>kostenlosen Testphase</strong>, wo eine angeboten wird – oder ein einmaliger Kauf für immer, und Jährlich und Einmalkauf gibt es auch als <strong>Familienpläne</strong>. Die Preise für dein Land stehen in der App, und die Abrechnung übernimmt Apple.</dd>
<dt>Wie funktionieren die Familienpläne?</dt>
<dd>Premium Familie – jährlich und Premium Familie – lebenslang werden über Apples Familienfreigabe mit bis zu fünf weiteren Personen deiner Familiengruppe geteilt – sechs insgesamt. Jede Person bekommt Premium in ihrer eigenen Kopie von On Ice, auf ihrem eigenen Gerät. Niemand sieht die Shops, die Liste, das Tagebuch oder die Ersparnis einer anderen Person.</dd>
<dt>Hindert es mich am Kaufen?</dt>
<dd>Nein. Eine gewöhnliche Sperre ist eine Pause, keine Mauer: Tippe auf {K_note_it}, sag, was dir ins Auge gefallen ist, und {K_need_to_shop} öffnet den Shop für ein paar Minuten. {K_done_block} schließt ihn vorzeitig wieder. Kein Durchkommen gibt es nur bei dem, was du selbst eingerichtet hast – einer Regel mit Komplettsperre, einem erreichten Tageslimit, einer zeitgesteuerten Sperre oder einer Fokus-Sperre –, und jede davon endet von selbst.</dd>
<dt>Was passiert, wenn mein Abo ausläuft?</dt>
<dd>Nichts, was du aufgebaut hast, wird dir weggenommen. Deine Liste, dein Verlauf und deine geschätzte Ersparnis bleiben, die Shops, die du ausgewählt hast, bleiben gesperrt, und deine Regeln, Limits und ein laufender strenger Modus halten weiter. Deine Bedenkzeit geht auf 24 Stunden zurück, die KI-Reflexion schaltet sich aus, und Widgets und die Muster-Bildschirme warten, bis Premium zurückkommt. Du kannst nur keine weiteren Premium-Funktionen hinzufügen.</dd>
<dt>Kann ich einen Kauf auf einem neuen Gerät wiederherstellen?</dt>
<dd>Ja. Öffne {K_settings} und tippe auf {K_restore}. Premium gehört zu deinem Apple Account, nicht zum Gerät. Deine Liste, dein Tagebuch und dein Verlauf reisen nicht mit – sie liegen auf dem Gerät, auf dem sie entstanden sind, und kommen nur mit einem Backup des ganzen Geräts auf ein neues.</dd>
<dt>Funktioniert es auf dem iPad?</dt>
<dd>Ja – iPhone und iPad, iOS 17 oder neuer. Jedes Gerät hat seine eigenen Shops, seine eigene Liste und seinen eigenen Verlauf; nichts wird zwischen ihnen synchronisiert.</dd>
<dt>Warum kann On Ice mir nicht sagen, welche Apps ich geschützt habe?</dt>
<dd>Weil es das wirklich nicht weiß. Apples Bildschirmzeit übergibt On Ice undurchsichtige Tokens, die außerhalb deines Geräts bedeutungslos sind – keine App-Namen, keine Kennungen. On Ice kann iOS bitten, sie zu sperren, und iOS zeichnet ihre Namen und Symbole für dich; lesen kann On Ice sie nicht. Websites, die du durch Eintippen einer Adresse hinzufügst, sind die Ausnahme: On Ice behält diese Adresse auf deinem Gerät, damit iOS sie sperren kann.</dd>
<dt>Sperrt es Websites oder nur Apps?</dt>
<dd>Beides. Füge die App eines Shops und seine Website getrennt hinzu, und beide werden gesperrt – die Website in Safari.</dd>
<dt>Sieht On Ice, was ich kaufe?</dt>
<dd>Nein. Es hat keinen Zugriff auf deine Bank, deine Bestellungen, dein Surfen oder deine Karte. Es hält nur seine eigenen Ereignisse fest – dass eine Sperre gezeigt wurde und wofür du dich entschieden hast – und behält sie auf deinem Gerät.</dd>
<dt>Verlässt mein Tagebuch mein Gerät?</dt>
<dd>Niemals. Nicht zu uns, nicht zu OpenAI, mit keiner Einstellung. Du kannst es mit Face ID, Touch ID oder deinem Code sperren, und seine optionale Wochenzusammenfassung schreibt Apple Intelligence auf deinem Gerät.</dd>
<dt>Wohin gehen meine Schritte beim Spazierengehen?</dt>
<dd>Nirgendwohin. Während eines Spaziergangs zeigt On Ice deine Schritte live an und vergisst sie, wenn der Spaziergang endet. Es liest nichts aus Apple Health und schreibt nichts hinein.</dd>
<dt>Was ist die KI-Reflexion, und ist sie an?</dt>
<dd>Ab und zu eine kurze Frage vor den Auswahlmöglichkeiten und sonntags ein paar Sätze über deine Woche. Sie ist <strong>aus, bis du sie einschaltest</strong>. Du wählst, wer sie schreibt: <strong>Apple Intelligence</strong>, auf deinem Gerät, oder <strong>OpenAI</strong> – das Einzige in der App, das überhaupt etwas vom Gerät sendet. Die <a href="{BASE}{L}/privacy/#ai">Datenschutzerklärung</a> listet genau auf, was.</dd>
</dl>
""",

"s.trouble.h": "Fehlerbehebung",
"s.trouble.b": """
<h3>Ein Shop öffnet sich ohne Sperre</h3>
<ul>
  <li>Prüfe, ob der Schutz oben auf dem Startbildschirm an ist und ob der eigene Schalter des Shops an ist.</li>
  <li>Prüfe, ob der Zugriff auf die Bildschirmzeit noch erteilt ist: {K_ios_settings} → {K_screen_time} → {K_apps_with_st}. Wurde er widerrufen, zeigt On Ice einen Bildschirm mit einer Möglichkeit, erneut zu fragen.</li>
  <li>Ein <strong>Shopping-Fenster</strong>, das du geöffnet hast, läuft vielleicht noch. Es schließt sich von selbst – oder tippe auf {K_done_block} –, und die Sperre kommt zurück.</li>
  <li>Wird der Shop nur von einer <strong>Regel</strong> abgedeckt, erscheint die Sperre nur während der Zeiten dieser Regel.</li>
  <li>Immer noch nichts? {K_settings} → {K_protection_tools} → {K_repair} wendet jede Sperre und jeden Zeitplan erneut an.</li>
</ul>
<h3>Ein Tippen auf „Notieren“ öffnet On Ice nicht</h3>
<ul>
  <li>Bei manchen iOS-Versionen übergibt dich die Sperre mit einer Mitteilung. Sind Mitteilungen aus, kann iOS sie nicht zustellen – schalte sie unter {K_ios_settings} → {K_notifications} → On Ice ein.</li>
  <li>Wenn du On Ice selbst öffnest, wird der Artikel übernommen, der darauf wartet, notiert zu werden.</li>
</ul>
<h3>Eine Website wird nicht gesperrt</h3>
<p>Websites werden über ihre Adresse gesperrt. Achte darauf, dass die Adresse, die du hinzugefügt hast, zu der passt, die du tatsächlich öffnest, und denk daran, dass die App eines Shops und seine Website zwei getrennte Dinge zum Hinzufügen sind.</p>
<h3>Mein Tagesziel oder Limit zeigt weniger Minuten als erwartet</h3>
<p>iOS sagt Apps nicht, wie lange du in einer anderen App warst. Es sagt On Ice nur, wann die Zeit in deinen geschützten Shops eine Stufe überschreitet – anfangs alle fünf Minuten –, deshalb zeigt On Ice „mindestens“ so viele Minuten. Der echte Wert kann etwas höher sein.</p>
<h3>Ich kann den Schutz nicht abschalten oder einen Shop nicht entfernen</h3>
<p>Prüfe, ob der <strong>strenge Modus</strong>, eine <strong>zeitgesteuerte Sperre</strong> oder eine <strong>Fokus-Sperre</strong> läuft – der Startbildschirm zeigt es an. Solange der strenge Modus läuft, ist deine Einrichtung bewusst festgehalten, und er endet von selbst zu der Zeit, die du gewählt hast. Wenn du {K_someone_key} eingerichtet hast, kann die Person mit der PIN ihn vorzeitig beenden.</p>
<h3>Die KI-Frage erscheint nie</h3>
<p>Sie braucht Premium und ist aus, bis du sie unter {K_settings} → {K_ai_reflection} einschaltest. Selbst dann fragt sie nur, wenn es einen Grund gibt – ein Gefühl, bei dem du Käufe oft bereut hast, eine Risikozeit oder ein höherer Preis. Mit OpenAI als Verfasser braucht sie eine Internetverbindung. Wenn etwas schiefgeht, zeigt sie dir stattdessen still die normalen Auswahlmöglichkeiten.</p>
<h3>Widgets hinken hinterher</h3>
<p>iOS aktualisiert Widgets nach seinem eigenen Zeitplan. Wenn du On Ice öffnest, sind sie wieder auf dem neuesten Stand. Die Widgets für die Ersparnis und „Auf Eis“ gibt es mit Premium.</p>
<h3>Premium wird nicht erkannt</h3>
<p>Tippe in {K_settings} auf {K_restore} und achte darauf, dass das Gerät mit demselben Apple Account angemeldet ist, mit dem der Kauf getätigt wurde – oder, bei einem Familienplan, dass du in der Familienfreigabe-Gruppe der Person bist, die ihn gekauft hat. Rückerstattungen und Abrechnungsfragen übernimmt Apple über den <a href="https://support.apple.com/billing">Apple Support</a>.</p>
<h3>Die App ist in der falschen Sprache</h3>
<p>Wähle eine unter {K_settings} → {K_language}. Apples eigene App-Auswahl zieht beim nächsten Öffnen von On Ice nach.</p>
""",

"s.contact.h": "Kontakt",
"s.contact.b": """
<p>Fragen, ein Fehler oder etwas, das funktionieren sollte und es nicht tut – schreib uns, und ein Mensch antwortet. Am schnellsten geht es über {K_settings} → {K_help_privacy} → {K_email_support}; das fügt deine Version von On Ice, deine iOS-Version und dein Gerätemodell für dich hinzu.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Nenne dein Gerätemodell, die iOS-Version und was du erwartet hättest. Schick uns nie deine Liste, deine Preise oder dein Tagebuch – wir brauchen sie nicht und hätten sie lieber nicht.</span></div></div>
<p class="small">Abrechnung, Rückerstattungen und Abo-Änderungen übernimmt Apple: <a href="https://apps.apple.com/account/subscriptions">Abos verwalten</a> · <a href="https://support.apple.com/billing">Rückerstattung anfordern</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "Über On Ice",
"a.h1": "Eine Nacht zwischen dir und dem Kauf-Button.",
"a.sub": "Wähle die Shopping-Apps und Websites, die dich am ehesten verleiten. Von da an bekommst du beim Öffnen zuerst eine Sperre – und eine Entscheidung, die dein Ich von morgen treffen darf.",
"a.cta": "Hilfe",
"a.meta": "Kein Konto · kein Bankzugriff · iPhone und iPad, iOS 17+ · 8 Sprachen",
"a.lead": "On Ice legt eine Nacht zwischen dich und den Kauf-Button. Keine Aussperrung, keine Belehrung – eine kurze Pause und Zeit, herauszufinden, ob du es wirklich wolltest. Nichts hier tadelt dich dafür, dass du Dinge willst, und nichts wird rot, wenn du es kaufst.",

"a.f1.h": "Kurz Pause vor dem Kauf.",
"a.f1.p": "Öffne einen Shop, den du ausgewählt hast, und On Ice kommt vor der Kasse – in der App und in Safari. Atme kurz durch, tippe einen Satz, lies eine Erinnerung oder sag, weswegen du gekommen bist.",
"a.f2.h": "Notieren statt kaufen.",
"a.f2.p": "Benenne die Sache, tippe einen ungefähren Preis an, tippe an, wie du dich fühlst. Fünfzehn Sekunden, ein Bildschirm. Notieren muss schneller gehen als das Verlangen.",
"a.f3.h": "Eine Nacht auf Eis.",
"a.f3.p": "Notierte Artikel warten unter einem Countdown-Ring – 24 Stunden oder irgendwo zwischen 12 und 72. Solange ein Artikel abkühlt, wird nichts gekauft, und dein Ich von morgen trifft die Entscheidung.",
"a.f4.h": "Sieh zu, wie es sich summiert.",
"a.f4.p": "Jeder Artikel, den du loslässt, zählt zu deiner geschätzten Ersparnis – deine eigenen Schätzungen, für heute, diese Woche und diesen Monat, neben den Stunden, in denen dir die Sperren immer wieder begegnen.",
"a.f5.h": "Etwas anderes tun.",
"a.f5.p": "Wenn das Verlangen irgendwohin muss: ein Spaziergang mit Schritten live, ein Buch, eine Playlist, ein Anruf. Wähle, was für dich funktioniert, und starte es mit einem Tippen.",
"a.f6.h": "Fester, wenn du es willst.",
"a.f6.p": "Ein tägliches Zeitziel fürs Shoppen, Tageslimits, zeitgesteuerte Sperren und Fokus-Sperren, Risikozeiten-Regeln für späte Abende und der strenge Modus, der alles festhält.",
"a.f7.h": "Ein Tagebuch nur für dich.",
"a.f7.p": "Eine Frage am Tag und ein Ort zum Schreiben. Sperr es mit Face ID. Nichts darin verlässt je dein Gerät.",
"a.f8.h": "Es sieht nie, was du kaufst.",
"a.f8.p": 'Keine Bankverbindung, kein Kaufverlauf, keine Preisverfolgung, keine Affiliate-Links, keine Analyse. Apple gibt On Ice Codes, keine Namen. <a href="{BASE}{L}/privacy/">So funktioniert das.</a>',

"a.price.h": "Was es kostet",
"a.price.b": """
<p>Kostenlos ist ein funktionierendes Produkt, keine Demo, und nichts, was du schon aufgebaut hast, wird dir weggenommen, wenn ein Abo ausläuft.</p>
<div class="tiers">
  <div class="tier"><div class="lbl">Kostenlos</div><div class="price">Gratis</div><ul><li>Eine Shopping-App und eine Website, gesperrt</li><li>Die 24-Stunden-Bedenkzeit und deine Liste</li><li>Deine geschätzte Ersparnis</li><li>Die Atempause und drei Alternativen</li><li>Das Tagebuch, ein Tagesziel, zeitgesteuerte Sperren und Fokus-Sperren</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Monatlich · Jährlich · Einmalkauf</div><ul><li>Jeder Shop und jede Website, die du willst</li><li>Wartezeiten von 12, 24, 48 oder 72 Stunden</li><li>Jede Art von Pause und deine eigenen Erinnerungen</li><li>Risikozeiten, Regeln pro Shop, Tageslimits und strenger Modus</li><li>Deine Einkaufsmuster und wie sich Käufe danach angefühlt haben</li><li>Widgets, ein Rückblick auf dein Tagebuch und die optionale KI-Reflexion</li><li>Jährlich beginnt mit einer kostenlosen Testphase; Jährlich und Einmalkauf gibt es auch als Familienpläne für bis zu sechs Personen</li></ul></div>
</div>
<p class="small">Die Preise für dein Land stehen in der App und im App Store. Die Abrechnung übernimmt Apple. <a href="{BASE}{L}/terms/#subscriptions">Abo-Bedingungen.</a></p>
""",

"a.st.h": "Auf Apples Bildschirmzeit gebaut",
"a.st.b": """
<p>On Ice nutzt dasselbe Framework, das hinter den eingebauten App-Limits von iOS steckt. Apple gibt es nur an Apps, die es für diesen Zweck geprüft hat, und Apple – nicht On Ice – ist das, was tatsächlich zwischen dir und dem Shop steht. Deshalb kann On Ice eine App sperren, ohne je ihren Namen zu erfahren.</p>
<p>iPhone und iPad · iOS 17 oder neuer · English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil), 简体中文</p>
""",

"a.est.h": "Jeder Betrag ist eine Schätzung",
"a.est.b": """
<p>On Ice fragt dich, was etwas ungefähr kostet, und merkt sich deine Antwort. Es verbindet sich mit keiner Bank, prüft keinen Preis, rechnet keine Währung um und gibt keine Finanzberatung. Jede Zahl, die es zeigt, trägt das Wort <em class="est">geschätzt</em> – in der App, in den Widgets und auf dieser Website.</p>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Datenschutzerklärung",
"p.h1": "Es sieht nie, was du kaufst.",
"p.sub": "Kein Konto, keine Bankverbindung, kein Kaufverlauf, keine Preisverfolgung und keine Analyse. Was On Ice weiß, bleibt auf deinem Gerät – mit einer optionalen Funktion, die aus ist, bis du sie einschaltest, und deren genauer Inhalt unten aufgeführt ist.",
"p.meta": "Gültig ab {DATE} · gilt für die App On Ice für iPhone und iPad und für diese Website",

"p.summary.h": "Die kurze Fassung",
"p.summary.b": """
<p class="lead"><strong>On Ice hat kein Konto, keine Analyse, keine Werbung und keinen fremden Code.</strong> Es gibt darin nirgends eine Bankverbindung, einen Kaufverlauf, eine Preisverfolgung oder einen Affiliate-Link. Alles, was es weiß, wird auf dein iPhone oder iPad geschrieben und bleibt dort.</p>
<div class="callout"><span class="tile">{eye-off}</span><div>Die Apps, die du in Apples Bildschirmzeit-Auswahl auswählst, erreichen On Ice als undurchsichtige Tokens, die nur dein Gerät deuten kann. Es gibt keinen App-Namen, keine Kennung und nichts zu senden.</div></div>
<p>Es gibt genau eine Ausnahme, und sie ist aus, bis du sie einschaltest: die optionale <strong>KI-Reflexion</strong>. Mit <strong>Apple Intelligence</strong> als Verfasser läuft sie auf deinem Gerät, und nichts geht hinaus. Mit <strong>OpenAI</strong> als Verfasser geht eine kurze, feste Liste von Angaben hinaus – vollständig aufgeführt <a href="#ai">unten</a>. Dein Tagebuch verlässt das Gerät nie, egal welchen Verfasser du wählst.</p>
<p>Diese Erklärung gilt für die App On Ice für iPhone und iPad, herausgegeben von {COMPANY}, und für diese Website.</p>
""",

"p.collect.h": "Was wir erfassen",
"p.collect.b": """
<p>„Erfassen“ heißt in Apples Sinn und in unserem: Daten vom Gerät zu senden und irgendwo zu behalten, das nicht flüchtig ist. Mit ausgeschalteter KI-Reflexion – so beginnt jede Installation – sendet On Ice nichts über dich irgendwohin. Die Tabelle zeigt, was sich ändert, wenn du sie mit OpenAI als Verfasser einschaltest.</p>
<div class="table-wrap"><table>
<tr><th>Kategorie</th><th>Gesendet?</th><th>Was das heißt</th></tr>
<tr><td>Finanzinformationen</td><td>Nur bei eingeschalteten OpenAI-Reflexionen</td><td>Keine Bankverbindung, keine Karte, kein Zugriff auf Transaktionen, kein Kaufverlauf. Bei eingeschalteten OpenAI-Reflexionen werden eine <em>Preisspanne</em> für den Artikel vor dir und eine gerundete geschätzte Ersparnis der Woche gesendet – nie ein genauer Preis, ein Konto oder ein Kontostand.</td></tr>
<tr><td>Kontaktinformationen</td><td>Nein</td><td>Es gibt nirgends in der App ein Konto, eine Anmeldung oder ein E-Mail-Feld.</td></tr>
<tr><td>Kennungen</td><td>Nur bei eingeschalteten OpenAI-Reflexionen</td><td>Keine Nutzer-ID, keine Werbekennung, und On Ice fragt nie, ob es dich tracken darf. Unser KI-Dienst sieht eine zufällige App-Attest-Schlüsselkennung, die nur dazu dient, Anfragen pro Gerät und Tag zu zählen, und nach zwei Tagen gelöscht wird.</td></tr>
<tr><td>Nutzungsdaten</td><td>Nur bei eingeschalteten OpenAI-Reflexionen</td><td>Keine Analyse und keine Ereignisse zur Produktinteraktion. Sperren, Pausen und Entscheidungen werden auf deinem Gerät gezählt, für deine eigenen Bildschirme. Eine Reflexion enthält die heutige Anzahl der Sperren; der Wochenrückblick enthält die Anzahlen der Woche.</td></tr>
<tr><td>Benutzerinhalte</td><td>Nur bei eingeschalteten OpenAI-Reflexionen</td><td>Deine Liste, deine Preise, dein Tagebuch, dein Ausgabenprotokoll und deine Erinnerungen bleiben auf dem Gerät. Mit OpenAI als Verfasser werden der Name des Artikels vor dir und das, was du als Antwort auf die Frage tippst, gesendet.</td></tr>
<tr><td>Browserverlauf</td><td>Nein</td><td>On Ice kann nicht sehen, was du im Web aufrufst. Es erfährt nur, dass seine eigene Sperre gezeigt wurde und wofür du dich darauf entschieden hast.</td></tr>
<tr><td>Standort, Gesundheit, Fitness, Kontakte, Suche, Diagnose</td><td>Nein</td><td>Schritte während eines Spaziergangs werden live angezeigt und nie gespeichert oder gesendet. On Ice hat keinen eigenen Absturz- oder Leistungsbericht.</td></tr>
</table></div>
<p><strong>Tracking:</strong> keins. On Ice verknüpft nichts über dich mit Daten aus Apps oder Websites anderer Unternehmen und teilt nichts mit Datenhändlern oder Werbetreibenden. Es gibt <strong>keine Affiliate-Links</strong>: On Ice verdient nichts, wenn du etwas kaufst – die einzige Regelung, die zu einer App passt, deren Aufgabe es ist, dir zu helfen, weniger zu kaufen.</p>
""",

"p.device.h": "Was auf deinem Gerät bleibt",
"p.device.b": """
<p>On Ice speichert das Folgende in seinem eigenen privaten Speicher auf deinem iPhone oder iPad, geschützt durch den Code und die Verschlüsselung deines Geräts. Nichts davon wird hochgeladen, mit iCloud synchronisiert, von uns gesichert oder ist für uns sichtbar.</p>
<ul>
  <li><strong>Deine Shops</strong> – Apps und Kategorien als undurchsichtige Bildschirmzeit-Tokens, die On Ice nicht lesen kann, und Websites, die du über ihre Adresse hinzugefügt hast, als diese Adresse (siehe unten).</li>
  <li><strong>Deine Liste</strong> – die Artikelnamen, die du getippt hast, die Preise, die du geschätzt hast, das Gefühl, das du angetippt hast, und wann jeder Artikel notiert und entschieden wurde.</li>
  <li><strong>Was an jeder Sperre passiert ist</strong> – dass sie gezeigt wurde, wann, und ob du widerstanden, gewartet, den Shop geöffnet, den Artikel losgelassen oder behalten hast, und was du gesagt hast, weswegen du gekommen bist. Daraus bestehen deine geschätzte Ersparnis, deine Serien und deine Muster.</li>
  <li><strong>Was du selbst hinzufügst</strong> – das Ausgabenprotokoll, wie sich ein Kauf danach angefühlt hat, dein Tagebuch, deine eigenen Erinnerungen und die Alternativen, die du gewählt hast, einschließlich eines App-Links oder einer Webadresse, die du einer davon gegeben hast.</li>
  <li><strong>Deine Regeln und Einstellungen</strong> – Risikozeiten, Regeln pro Shop, dein Tagesziel und deine Limits, Sperren, der Zustand des strengen Modus, deine Pause, dein Tagesbeginn, deine Sprache und der KI-Verfasser, den du gewählt hast. Wenn jemand den Schlüssel für deinen strengen Modus verwahrt, wird nur ein gesalzener Einweg-Hash der PIN dieser Person gespeichert, nie die PIN.</li>
  <li><strong>Nutzungsstufen</strong> – die höchste Zeitstufe, die iOS heute für deine geschützten Shops gemeldet hat, für dein Ziel und deine Limits (siehe unten).</li>
  <li><strong>Dein Premium-Status</strong> – der Plan und wann er sich verlängert oder endet, damit die App weiß, was sie freischalten soll.</li>
  <li><strong>Der letzte Wochenrückblick</strong> – nur solange die KI-Reflexion an ist.</li>
</ul>
<p>Wenn du iCloud-Backup oder ein verschlüsseltes Backup auf einem Computer nutzt, nimmt Apple die Daten von On Ice möglicherweise in dieses Backup auf, unter deinem eigenen Apple Account und nach Apples Datenschutzbedingungen. Wir haben keinen Zugriff darauf.</p>
""",

"p.journal.h": "Dein Tagebuch",
"p.journal.b": """
<p>Das Tagebuch ist der eine Ort in On Ice, an dem du für niemanden schreibst. Einträge – und die Stimmung, der Artikel oder das Gefühl, die an einem hängen – werden auf deinem Gerät gespeichert und <strong>verlassen es nie</strong>: nicht mit der KI-Reflexion, nicht mit OpenAI, mit keiner Einstellung.</p>
<ul>
  <li>{K_lock_journal} verlangt Face ID, Touch ID oder deinen Gerätecode, bevor sich das Tagebuch öffnet, und schließt es wieder, wenn du die App verlässt. iOS führt die Prüfung durch; On Ice sieht nie dein Gesicht, deinen Fingerabdruck oder deinen Code. Die Sperre schützt den Bildschirm; die Einträge selbst sind durch die eigene Verschlüsselung deines Geräts geschützt, wie die übrigen Daten von On Ice.</li>
  <li>{K_reflect_week} fasst deine letzten Einträge mit Apple Intelligence zusammen, <em>auf deinem Gerät</em>. Eine Server-Version davon gibt es nicht.</li>
  <li>{K_export_journal} erstellt eine reine Textdatei und übergibt sie an iOS, sodass du wählst, wo sie gespeichert wird. On Ice sendet sie nirgendwohin.</li>
  <li>Das Tagebuch-Widget zeigt nur die Frage des Tages. Es liest nie einen Eintrag.</li>
</ul>
""",

"p.permissions.h": "Was On Ice nutzen möchte",
"p.permissions.b": """
<p>iOS fragt nach jeder dieser Berechtigungen mit eigenen Worten, und jede lässt sich jederzeit in {K_ios_settings} ändern.</p>
<div class="table-wrap"><table>
<tr><th>Berechtigung</th><th>Warum</th><th>Nötig?</th></tr>
<tr><td>Bildschirmzeit</td><td>Um die Shops zu sperren, die du auswählst, deine Sperren, Regeln und Limits auszuführen und Nutzungsstufen zu empfangen.</td><td>Ja – ohne sie kann On Ice nicht arbeiten.</td></tr>
<tr><td>Mitteilungen</td><td>Um dich von der Sperre in die App zu übergeben, um zu sagen, wann die Wartezeit eines Artikels vorbei oder fast vorbei ist, und für Nachfragen, Aktivitäts-Timer und Vorschläge, die du eingeschaltet lässt.</td><td>Nein</td></tr>
<tr><td>Bewegung &amp; Fitness</td><td>Um deine Schritte während eines Spaziergangs live anzuzeigen. Der Bewegungssensor wird nur genutzt, solange ein Spaziergang auf dem Bildschirm ist, und Schritte werden nie gespeichert oder gesendet.</td><td>Nein – nur wenn du einen Spaziergang startest</td></tr>
<tr><td>Face ID oder Touch ID</td><td>Um das Tagebuch zu entsperren, wenn du es sperrst.</td><td>Nein</td></tr>
</table></div>
<p>Wenn du wählst, was eine „Alternative“ öffnet, fragt On Ice iOS, ob eine kurze Liste von Apps installiert ist – Bücher, Kindle, Audible, Podcasts, Musik, Spotify, Duolingo, Headspace, Calm, Notizen, Nachrichten und Kurzbefehle –, damit es dir die anbieten kann, die du hast. Die Antwort wird sofort verwendet, um diese Liste zu erstellen; sie wird weder gespeichert noch gesendet.</p>
""",

"p.screentime.h": "Bildschirmzeit und deine Shops",
"p.screentime.b": """
<p>On Ice baut auf Apples Bildschirmzeit-Framework auf (Family Controls, Managed Settings und Device Activity). Du erteilst den Zugriff einmal, über Apples eigene Abfrage, und kannst ihn jederzeit unter {K_ios_settings} → {K_screen_time} widerrufen.</p>
<p>Wenn du in Apples Auswahl Apps, Kategorien oder Websites auswählst, gibt sie <strong>Tokens</strong> zurück: Werte, die sie gegenüber iOS bezeichnen, für On Ice aber nichts bedeuten und außerhalb deines Geräts nichts. On Ice speichert diese Tokens, um iOS bitten zu können, das zu sperren, was du ausgewählt hast; iOS zeichnet ihre Namen und Symbole für dich. On Ice bekommt nie eine Bundle-Kennung oder einen App-Namen. Wo seine eigenen Bestandteile Tokens vergleichen müssen, vergleichen sie Einweg-Hashes davon, nie die Tokens selbst.</p>
<p><strong>Websites, die du über ihre Adresse hinzufügst, sind etwas anderes.</strong> Eine Website, die du eintippst oder aus den Vorschlägen von On Ice auswählst, wird als diese Adresse gespeichert – <code>example.com</code> –, weil iOS sie braucht, um die Website zu sperren. Sie bleibt mit allem anderen auf deinem Gerät und wird nie gesendet.</p>
<p><strong>Die Nutzung wird in Stufen gemeldet.</strong> iOS gibt On Ice nie eine Gesamtsumme deiner Bildschirmzeit. Es sagt On Ice nur, wann die Zeit in deinen geschützten Shops eine im Voraus registrierte Stufe überschreitet – fünf Minuten, zehn, fünfzehn … –, was für ein Tagesziel und ein Limit reicht, und für nichts weiter.</p>
<p>On Ice beobachtet weder dein Surfen noch deine Nachrichten noch das, was du in irgendeiner App tust. iOS selbst zeichnet die Sperre und setzt sie durch. On Ice erfährt nur, dass seine eigene Sperre gezeigt wurde und wofür du dich darauf entschieden hast.</p>
""",

"p.ai.h": "Die KI-Reflexion – das Einzige, was hinausgehen kann",
"p.ai.b": """
<p class="lead">Die KI-Reflexion ist eine optionale Premium-Funktion. <strong>Sie ist aus, wenn du On Ice installierst, und bleibt aus, bis du sie einschaltest</strong>, unter {K_settings} → {K_ai_reflection}.</p>
<p>Ist sie an, bekommen manche notierten Artikel eine kurze Frage, bevor du wählst – nicht jeder Artikel, nur wenn es einen Grund gibt: ein Gefühl, bei dem du Käufe oft bereut hast, eine Risikozeit oder ein höherer Preis. Sonntags kann sie außerdem ein paar Sätze über deine Woche schreiben.</p>
<h3>Zwei Verfasser, und nur einer davon verlässt das Gerät</h3>
<ul>
  <li><strong>Apple Intelligence</strong> schreibt auf deinem Gerät. Nichts wird irgendwohin gesendet. Wenn Apple Intelligence nicht mehr verfügbar ist, zeigt dir On Ice stattdessen die normalen Auswahlmöglichkeiten – <strong>es weicht nie auf einen Server aus</strong>.</li>
  <li><strong>OpenAI</strong> schreibt auf den Servern von OpenAI, über den eigenen Dienst von On Ice. Gesendet wird nur, was unten aufgeführt ist.</li>
</ul>
<p>Du wählst unter {K_writer}. Wenn du die KI-Reflexion einschaltest, ohne zu wählen, nutzt On Ice Apple Intelligence, wo dein Gerät und deine Sprache es unterstützen, und OpenAI, wo nicht.</p>
<h3>Was gesendet wird, mit OpenAI als Verfasser</h3>
<p>Für eine Frage:</p>
<ul>
  <li>Der <strong>Name des Artikels</strong>, den du gerade getippt hast, und alles, was du als Antwort auf die Frage schreibst.</li>
  <li>Eine <strong>Preisspanne</strong> – eine Spanne wie „250 bis 500“, nie der Betrag, den du eingegeben hast – und deine Währung.</li>
  <li>Das <strong>Gefühl</strong>, das du angetippt hast, falls du eins angetippt hast.</li>
  <li><strong>Stunde und Minute</strong> auf deiner Uhr. Kein Datum, keine Zeitzone.</li>
  <li><strong>Wie vielen Shopping-Sperren du heute begegnet bist.</strong></li>
  <li>Deine eigene <strong>Bereuensquote für genau dieses Gefühl</strong>, als Prozentsatz – erst wenn du mindestens fünf Käufe bewertet hast.</li>
  <li>Deine <strong>Sprache</strong>, etwa „Deutsch (Deutschland)“, damit die Frage darin zurückkommt.</li>
</ul>
<p>Für den Wochenrückblick <strong>nur Anzahlen und Summen</strong>: begegnete Sperren; Artikel, auf die du gewartet, die du losgelassen oder behalten hast oder bei denen du widerstanden hast; wie oft du einen Shop geöffnet hast; deine aktuelle und deine beste Serie; deine geschäftigste Stunde; der Anteil der Artikel, die du losgelassen hast; deine geschätzte Ersparnis der Woche, auf eine ganze Zahl gerundet, mit ihrer Währung; das Datum, an dem die Woche begann; und deine Sprache. <strong>Keine Artikelnamen und keine Einzelpreise.</strong></p>
<h3>Was nie gesendet wird</h3>
<ul>
  <li>Bildschirmzeit-Tokens oder ihre Hashes, Bundle-Kennungen oder Website-Adressen.</li>
  <li>Welche Shops oder Websites du schützt, oder wie viele.</li>
  <li>Der genaue Preis, den du eingegeben hast.</li>
  <li>Irgendetwas anderes auf deiner Liste – keine Namen, keine Preise.</li>
  <li>Dein Ausgabenprotokoll oder irgendein einzelner Kaufpreis.</li>
  <li>Wie du einen einzelnen Kauf bewertet hast.</li>
  <li>Dein Tagebuch, deine Regeln, Limits, Sperren, Risikozeiten oder der Zustand des strengen Modus.</li>
  <li>Irgendein Name, Konto, eine E-Mail-Adresse oder Werbekennung – nichts, was dich als Person identifiziert.</li>
</ul>
<h3>Wohin es geht und wie lange es aufbewahrt wird</h3>
<p>Anfragen gehen an den <strong>eigenen Dienst von On Ice, gehostet bei Cloudflare</strong>, und weiter an <strong>OpenAI</strong>, das das Modell betreibt. In der App steckt kein API-Schlüssel, den man herausziehen könnte, und die App ruft OpenAI nie direkt auf.</p>
<p>Bevor er antwortet, prüft der Dienst mit <strong>Apples App Attest</strong>, ob die Anfrage von einer echten Kopie von On Ice kommt. Diese Prüfung stützt sich auf einen Schlüssel, der auf deinem Gerät erzeugt wurde – nicht auf deinen Namen oder deinen Apple Account. <strong>Der Dienst speichert keine Frage, keine Antwort und keine Artikeldetails.</strong> Er behält eine Zählung der Anfragen pro Gerät und Tag, unter dieser zufälligen Schlüsselkennung, und löscht sie nach zwei Tagen; tägliche Summen der Anfragen und der Modellnutzung für den gesamten Dienst, die kein Gerät nennen, für etwa 90 Tage; und einen Eintrag zu jeder einmaligen App-Attest-Challenge, bis sie abläuft. Seine Protokolle halten den Status einer Anfrage fest, wie lange sie dauerte und wie viele Tokens sie verbraucht hat – nie ihren Inhalt.</p>
<p><strong>OpenAI verwendet diese Daten nicht, um seine Modelle zu trainieren.</strong> Wir schalten die gespeicherten Antworten von OpenAI ab; OpenAI kann Ein- und Ausgaben dennoch in seinen Protokollen zur Missbrauchsüberwachung behalten, normalerweise bis zu 30 Tage, mit Ausnahmen nach seinen eigenen Bedingungen. Wir versprechen nicht, dass dein Text in einem bestimmten Land verarbeitet wird.</p>
<p><strong>Frühere Versionen von On Ice</strong> senden dieselben Arten von Angaben stattdessen an <strong>Googles Gemini-Modell auf Vertex AI</strong>, über einen früheren Dienst von On Ice auf Google Cloud, der ebenfalls keine Inhalte speichert. Google verwendet sie nicht, um seine Modelle zu trainieren, kann sie bis zu 24 Stunden aufbewahren und kann sie protokollieren, um auf Missbrauch zu prüfen.</p>
<div class="callout"><span class="tile">{sparkle}</span><div>Wenn du die KI-Reflexion ausschaltest, stoppt das sofort jede künftige Anfrage, löscht den Wochenrückblick von deinem Gerät und entfernt die Sonntagserinnerung. On Ice stellt dann wieder keine eigenen Netzwerkverbindungen mehr her. {K_settings} → {K_ai_reflection} → {K_what_gets_sent} zeigt dieselbe Liste in der App.</div></div>
""",

"p.purchases.h": "Käufe und Familienpläne",
"p.purchases.b": """
<p>Premium wird über Apples App Store mit StoreKit verkauft. Das Geschäft besteht zwischen dir und Apple, nach <a href="https://www.apple.com/legal/privacy/">Apples Datenschutzrichtlinie</a>. Apple sagt On Ice, welcher Plan aktiv ist und wann er sich verlängert oder endet – sonst nichts –, und On Ice sagt Apple nichts darüber, wie du die App benutzt. Wir sehen nie eine Karte.</p>
<p>Bei einem <strong>Familienplan</strong> gibt Apples Familienfreigabe jedem Mitglied Premium in seiner eigenen Kopie von On Ice. Zwischen diesen Kopien wird nichts übertragen – keine Shops, keine Liste, kein Tagebuch, keine Ersparnis und keine Einstellungen –, und On Ice erfährt nur, dass Premium geteilt wurde, nicht, wer es geteilt hat.</p>
""",

"p.notifications.h": "Mitteilungen, Widgets und der Sperrbildschirm",
"p.notifications.b": """
<p><strong>Mitteilungen</strong> sind optional und werden alle auf deinem Gerät geplant. Keine wird von einem Server gesendet, und es gibt keinen Push-Dienst. On Ice nutzt sie, um dich von der Sperre in die App zu übergeben, um zu sagen, wann die Wartezeit eines Artikels vorbei oder fast vorbei ist, für Nachfragen, die du unter {K_settings} → {K_follow_ups} abschalten kannst, für Aktivitäts-Timer und Vorschläge, die du wählst, und – nur bei eingeschalteter KI-Reflexion – für den Wochenrückblick am Sonntag. Eine Mitteilung zu einem Artikel nennt den Artikel.</p>
<p><strong>Widgets, Live-Aktivitäten und Steuerelemente im Kontrollzentrum</strong> lesen eine kleine Momentaufnahme auf deinem Gerät: Summen, Anzahlen, deine Serie sowie die Namen und Zeiten von bis zu drei der als Nächstes fälligen Artikel. Sie haben keinen Bildschirmzeit-Zugriff und sehen nie, welche Shops du ausgewählt hast. <strong>Das Widget „Auf Eis“ und die Live-Aktivität eines Artikels zeigen den Namen des Artikels</strong>, sodass ihn auf einem Sperrbildschirm jeder lesen kann, der das Gerät in der Hand hält. Geldbeträge sind dort ausgeblendet, solange das Gerät gesperrt ist. Platziere sie dort, wo es dir recht ist, sie zu sehen.</p>
""",

"p.third.h": "Dritte",
"p.third.b": """
<p>On Ice enthält <strong>keinen fremden Code</strong>: keine Analyse, keine Werbung, keine Attribution, keinen Absturzbericht, keine SDKs. Nur diese Parteien sind beteiligt, und nur so, wie hier beschrieben:</p>
<ul>
  <li><strong>Apple</strong> – betreibt den App Store und die Familienfreigabe, wickelt Käufe ab, setzt die Bildschirmzeit-Sperre durch, führt Apple Intelligence auf deinem Gerät aus und stellt App Attest bereit. Wenn du dem Teilen mit Entwicklern zugestimmt hast, kann Apple uns nach seiner eigenen Richtlinie Absturzprotokolle weitergeben.</li>
  <li><strong>Cloudflare</strong> – hostet den KI-Dienst von On Ice. Wenn die KI-Reflexion OpenAI nutzt, laufen Anfragen durch ihn, und er speichert nichts von ihrem Inhalt.</li>
  <li><strong>OpenAI</strong> – betreibt das Modell hinter den OpenAI-Reflexionen, nur solange dieser Verfasser genutzt wird, und bekommt nur, was <a href="#ai">oben</a> aufgeführt ist.</li>
  <li><strong>Google Cloud</strong> – übernimmt diese Rolle nur für frühere Versionen der App.</li>
</ul>
<p>Wir verkaufen, vermieten oder teilen personenbezogene Daten mit niemandem, und wir teilen nichts mit Datenhändlern oder Werbetreibenden. Ein Link, den du einer „Alternative“ gibst, öffnet die App oder Website, die du gewählt hast, nach deren eigener Richtlinie.</p>
""",

"p.delete.h": "Deine Daten löschen",
"p.delete.b": """
<p>Alles, was On Ice speichert, liegt auf deinem Gerät, deshalb musst du uns nicht fragen, um es zu entfernen. Du kannst Tagebucheinträge, Einträge im Ausgabenprotokoll, Regeln, Limits, Erinnerungen und Aktivitäten einzeln in der App löschen; das Ausschalten der KI-Reflexion löscht den Wochenrückblick; und <strong>das Löschen der App entfernt alles auf einmal</strong>. Es gibt in der App keine einzelne Taste, die deinen ganzen Verlauf löscht, deshalb ist das Löschen der App der Weg, neu anzufangen. Die Seite <a href="{BASE}{L}/delete-data/">Deine Daten</a> geht jeden Punkt durch.</p>
<p>Auf unserer Seite gibt es nichts zu löschen: Der KI-Dienst behält keine Inhalte, und seine Zählung pro Gerät verschwindet nach zwei Tagen von selbst.</p>
""",

"p.rights.h": "Deine Rechte",
"p.rights.b": """
<p>Wo immer du lebst – auch nach DSGVO, UK GDPR und CCPA/CPRA –, hast du das Recht auf Auskunft, Berichtigung, Export, Einschränkung der Verarbeitung, Widerspruch gegen die Verarbeitung und Löschung personenbezogener Daten, die ein Unternehmen über dich hält, sowie das Recht, dich bei einer Aufsichtsbehörde zu beschweren. On Ice führt auf keinem Server ein Profil von dir, also gibt es auf unserer Seite nichts herauszugeben oder zu löschen; die Daten auf deinem Gerät sind schon in deiner Hand. OpenAI-Reflexionen zu nutzen ist deine Entscheidung, und wenn du die KI-Reflexion ausschaltest, widerrufst du diese Entscheidung sofort. Wenn du glaubst, dass wir etwas über dich haben, schreib an {MAIL}, und wir antworten.</p>
""",

"p.children.h": "Kinder",
"p.children.b": """
<p>On Ice ist ein selbstbestimmtes Werkzeug für die Person, die das Gerät benutzt. Es ist kein Kindersicherungs-Produkt und verwaltet nicht das Gerät einer anderen Person; ein Familienplan teilt Premium, nie Kontrolle oder Daten. Es richtet sich nicht an Kinder unter 13 Jahren (oder unter dem Alter der digitalen Einwilligung an deinem Wohnort), und wir erfassen wissentlich von niemandem personenbezogene Daten, gleich welchen Alters.</p>
""",

"p.changes.h": "Änderungen an dieser Erklärung",
"p.changes.b": """
<p>Wir können diese Erklärung aktualisieren, wenn sich die App ändert. Das Datum oben ändert sich dann mit, und wesentliche Änderungen werden in den Versionshinweisen der App vermerkt. Diese Fassung beschreibt die Wahl zwischen Apple Intelligence und OpenAI für die KI-Reflexion, das Tagebuch, Schritte beim Spazierengehen, Nutzungsstufen, Familienpläne, das iPad und sieben weitere Sprachen. Wenn du On Ice nach einer Änderung weiter nutzt, nimmst du die geänderte Erklärung an.</p>
<p>Diese Erklärung wird in acht Sprachen veröffentlicht. Wenn eine Übersetzung und die englische Fassung voneinander abweichen, gilt die englische Fassung.</p>
""",

"p.contact.h": "Kontakt",
"p.contact.b": """
<p>{COMPANY}, der Herausgeber von On Ice, ist die verantwortliche Stelle für alles hier Behandelte. Fragen zum Datenschutz: {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Nutzungsbedingungen",
"t.h1": "Die Vereinbarung, in klaren Worten.",
"t.sub": "Was On Ice tut, was es nicht verspricht, warum jeder Betrag eine Schätzung ist, wie Premium und Familienpläne abgerechnet werden und worauf dich Sperren und der strenge Modus festlegen.",
"t.meta": "Gültig ab {DATE} · On Ice von {COMPANY}",

"t.acceptance.h": "1. Annahme der Bedingungen",
"t.acceptance.b": """
<p>Diese Nutzungsbedingungen („Bedingungen“) sind eine Vereinbarung zwischen dir und {COMPANY} („wir“, „uns“), dem Herausgeber der App On Ice für iPhone und iPad („On Ice“ oder „die App“). Indem du On Ice installierst oder benutzt, nimmst du diese Bedingungen und unsere <a href="{BASE}{L}/privacy/">Datenschutzerklärung</a> an. Wenn du nicht einverstanden bist, benutze die App nicht.</p>
<p>Diese Bedingungen werden in acht Sprachen veröffentlicht. Wenn eine Übersetzung und die englische Fassung voneinander abweichen, gilt die englische Fassung.</p>
""",

"t.who.h": "2. Wer On Ice benutzen darf",
"t.who.b": """
<p>Du musst mindestens 13 Jahre alt sein oder das Alter der digitalen Einwilligung an deinem Wohnort erreicht haben, um On Ice zu benutzen. On Ice ist ein Werkzeug, das du für dich selbst installierst, auf deinem eigenen Gerät. Es ist kein Kindersicherungs-Produkt und darf nicht dazu verwendet werden, das Gerät einer anderen Person zu verwalten oder zu überwachen. Ein Familienplan teilt Premium mit Mitgliedern deiner Familienfreigabe-Gruppe; er gibt niemandem Kontrolle über das On Ice eines anderen Mitglieds.</p>
""",

"t.what.h": "3. Was On Ice ist – und was nicht",
"t.what.b": """
<p>On Ice ist ein selbstbestimmtes Werkzeug, das Shopping-Apps und Websites deiner Wahl sperrt, eine kurze Pause anbietet, dich notieren lässt, was dir ins Auge gefallen ist, es für einen von dir festgelegten Zeitraum zurückhält und auf deinem Gerät festhält, wie du dich entschieden hast. Es bietet außerdem ein Tagebuch, Alternativen, Ziele, Limits und Sperren. Es ist dafür gemacht, aus einem automatischen Kauf eine Entscheidung zu machen, die du wirklich triffst.</p>
<p>On Ice ist <strong>kein</strong> medizinischer, psychologischer oder therapeutischer Dienst, und nichts darin – auch keine Gefühle, die du antippst, Pausen, Erinnerungen, Tagebuchfragen, Auswertungen oder von KI geschriebener Text – ist Beratung, Diagnose oder Behandlung. Wenn du mit zwanghaftem Geldausgeben, Schulden, Angst oder irgendetwas anderem kämpfst, das dein Wohlbefinden beeinträchtigt, sprich bitte mit einer qualifizierten Fachperson oder einer Schuldnerberatung. Im Notfall wähle die örtliche Notrufnummer.</p>
<p>On Ice ist außerdem <strong>kein Sicherheits- oder Kindersicherungs-Produkt</strong>. Es ist dafür gemacht, genau so stark zu sein, wie du es verlangst: Die App kann gelöscht werden, der Bildschirmzeit-Zugriff kann in den iOS-Einstellungen widerrufen werden, und Sperren bestehen nur, solange die App installiert und berechtigt ist.</p>
""",

"t.money.h": "4. Schätzungen, keine Finanzberatung",
"t.money.b": """
<p>Jeder Preis in On Ice ist ein Betrag, den <strong>du</strong> eingibst. Die App verbindet sich mit keiner Bank, keinem Zahlungsanbieter und keinem Händler, liest weder deine Transaktionen noch deinen Bestellverlauf, verfolgt keine Preise, rechnet keine Währungen um und prüft nicht, was etwas kostet.</p>
<p>Die Ersparnis, die On Ice anzeigt, ist daher eine <strong>Schätzung, zusammengesetzt aus deinen eigenen Annahmen</strong>, und ist überall, wo sie erscheint, als solche gekennzeichnet. Sie ist keine Tatsachenaussage über Geld, das du hast, kein Finanzbeleg und nichts, worauf du dich bei Budget, Steuern, Krediten oder irgendeiner anderen Entscheidung verlassen solltest. {COMPANY} ist kein Finanzberater, und nichts in der App oder auf dieser Website ist Finanz-, Anlage- oder Schuldenberatung.</p>
<div class="callout green"><span class="tile">{info}</span><div>On Ice enthält keine Affiliate-Links und verdient nichts an dem, was du kaufst oder nicht kaufst. Seine einzige Einnahme ist Premium, von dir über Apple bezahlt.</div></div>
""",

"t.screentime.h": "5. Bildschirmzeit, Sperren und strenger Modus",
"t.screentime.b": """
<p>On Ice stützt sich auf Apples Bildschirmzeit-Framework. Apple setzt die Sperre durch; On Ice bittet darum. Ob eine Sperre erscheint, wie schnell, ob eine Nutzungsstufe gemeldet wird und ob Sperren Neustarts und iOS-Updates überstehen, entscheidet letztlich iOS, und wir können es nicht in jedem Fall garantieren. <strong>On Ice kann keinen Kauf verhindern</strong> – es kann nur einen Bildschirm vor einen Shop stellen, den du ausgewählt hast.</p>
<p>Manche Werkzeuge, die du einschalten kannst, bieten <strong>kein Durchkommen</strong>, solange sie laufen: eine <strong>Regel mit Komplettsperre</strong> während ihrer Zeiten, ein <strong>Tageslimit</strong>, sobald es erreicht ist (bis dein nächster Tag beginnt), eine <strong>zeitgesteuerte Sperre</strong>, bis sie endet, und eine <strong>Fokus-Sperre</strong>, solange dieser Fokus aktiviert ist. Eine zeitgesteuerte Sperre mit der Einstellung {K_only_these} sperrt <em>jede</em> App auf deinem Gerät außer den wichtigen Apps, die du ausgewählt hast. Bevor du eine startest, stell sicher, dass du erreichst, was du brauchen könntest – für Anrufe, Nachrichten, Karten, Zahlungen, Gesundheit oder Arbeit.</p>
<p>Der <strong>strenge Modus</strong> ist eine Zusage, die du dir selbst gibst. Solange er läuft, für die von dir gewählte Dauer, bleibt der Schutz an, Regeln bleiben, wie sie sind, Shops können hinzugefügt, aber nicht entfernt werden, und Limits und dein Tagesbeginn lassen sich nicht ändern – <em>auch nicht von dir und auch nicht von uns</em>. Wir können den strengen Modus, eine Sperre oder eine Regel auf Wunsch nicht vorzeitig beenden. Wenn du {K_someone_key} eingerichtet hast, kann die Person mit der PIN den strengen Modus vorzeitig beenden, und du kannst eine verzögerte Umgehung anfordern, die ihn 24 Stunden später beendet; eine vergessene PIN können wir nicht wiederherstellen. Beginne keine Zusage, die du nicht einzuhalten bereit bist, und beginne keine auf einem Gerät, auf das du womöglich uneingeschränkten Zugriff brauchst.</p>
<p>Das Löschen der App beendet jede Sperre, jede Blockierung und jedes Limit, wie in Abschnitt 3 beschrieben.</p>
""",

"t.data.h": "6. Deine Daten und dein Gerät",
"t.data.b": """
<p>Alles, was On Ice aufzeichnet, wird auf deinem Gerät gespeichert – siehe die <a href="{BASE}{L}/privacy/">Datenschutzerklärung</a>. Nichts wird zwischen Geräten synchronisiert. Du bist für dein Gerät, seinen Code und seine Backups verantwortlich. Wenn du die App löschst oder das Gerät ohne Backup verlierst, sind deine Liste, dein Tagebuch, deine Regeln, dein Ausgabenprotokoll und dein Ersparnisverlauf weg, und wir haben keine Kopie zum Wiederherstellen. Dein Premium-Kauf ist davon getrennt: Er gehört zu deinem Apple Account und lässt sich auf jedem iPhone oder iPad wiederherstellen, das damit angemeldet ist.</p>
<p>Was du in On Ice schreibst, gehört dir. Wir erheben keine Rechte daran, und – abgesehen von der optionalen OpenAI-Reflexion in Abschnitt 8, die du selbst einschalten musst – erhalten wir es nie.</p>
""",

"t.subscriptions.h": "7. Premium, Abos und Abrechnung",
"t.subscriptions.b": """
<p>On Ice ist kostenlos zum Laden und Benutzen. <strong>On Ice Premium</strong> schaltet weitere Funktionen frei und wird in fünf Formen verkauft, zu dem Preis, der in der App und im App Store für dein Land angezeigt wird:</p>
<ul>
  <li><strong>Premium Monatlich</strong>: ein sich automatisch verlängerndes Abo, monatlich abgerechnet.</li>
  <li><strong>Premium Jährlich</strong>: ein sich automatisch verlängerndes Abo, jährlich abgerechnet, beginnend mit einer <strong>kostenlosen Testphase</strong>, wo eine angeboten wird.</li>
  <li><strong>Premium für immer</strong>: ein einmaliger Kauf, der sich nicht verlängert.</li>
  <li><strong>Premium Familie – jährlich</strong>: ein sich automatisch verlängerndes Abo, jährlich abgerechnet, beginnend mit einer <strong>kostenlosen Testphase</strong>, wo eine angeboten wird, für bis zu sechs Personen über die Familienfreigabe.</li>
  <li><strong>Premium Familie – lebenslang</strong>: ein einmaliger Kauf, der sich nicht verlängert, für bis zu sechs Personen über die Familienfreigabe.</li>
</ul>
<p>Die beiden Familienpläne werden über Apples <strong>Familienfreigabe</strong> mit bis zu fünf weiteren Mitgliedern deiner Familiengruppe geteilt. Jede Person bekommt Premium in ihrer eigenen Kopie von On Ice, auf ihrem eigenen Gerät; Shops, Listen, Tagebücher, Ersparnisse und Einstellungen werden nicht zwischen ihnen geteilt. Premium Monatlich, Premium Jährlich und Premium für immer gelten nur für dich und werden nicht geteilt.</p>
<p>Die Zahlung wird deinem Apple Account mit der Kaufbestätigung belastet. Eine kostenlose Testphase geht in ein kostenpflichtiges Abo über, sofern du nicht mindestens 24 Stunden vor Ende der Testphase kündigst. Abos verlängern sich automatisch zum selben Preis und für denselben Zeitraum, sofern die automatische Verlängerung nicht mindestens 24 Stunden vor Ende des laufenden Zeitraums abgeschaltet wird; die Verlängerung wird innerhalb der 24 Stunden vor dessen Ende berechnet. Du kannst ein Abo in deinen <a href="https://apps.apple.com/account/subscriptions">App-Store-Aboeinstellungen</a> verwalten oder kündigen; die Kündigung wirkt zum Ende des laufenden Zeitraums, und für den ungenutzten Teil eines Zeitraums gibt es keine anteilige Erstattung. Der Kauf eines lebenslangen Plans oder der Erhalt eines Familienplans kündigt kein Abo, das du bereits hast – kündige es selbst. Rückerstattungen übernimmt Apple nach Apples Richtlinien. Nutze {K_restore} in der App, um Premium auf einem neuen Gerät zurückzuholen.</p>
<p><strong>Läuft ein Abo aus</strong>, wird nichts entfernt, was du bereits aufgebaut hast: Deine Liste, dein Tagebuch, dein Verlauf und deine geschätzte Ersparnis bleiben, die Shops, die du ausgewählt hast, bleiben gesperrt, und bestehende Regeln, Limits und ein laufender strenger Modus halten weiter. Deine Bedenkzeit geht auf 24 Stunden zurück, die KI-Reflexion schaltet sich aus, und Widgets und Muster-Bildschirme warten, bis Premium zurückkommt. Nur die Möglichkeit, weitere Premium-Funktionen hinzuzufügen, schließt sich. Der Umfang der Premium-Funktionen kann sich mit der Zeit ändern; wir entfernen keine Funktion aus einem laufenden Abo, ohne das anzukündigen.</p>
""",

"t.ai.h": "8. Die KI-Reflexion",
"t.ai.b": """
<p>Die optionale KI-Reflexion ist <strong>aus, bis du sie einschaltest</strong>. Mit <strong>Apple Intelligence</strong> als Verfasser wird Text auf deinem Gerät erzeugt, nach Apples Bedingungen. Mit <strong>OpenAI</strong> als Verfasser werden die in der <a href="{BASE}{L}/privacy/#ai">Datenschutzerklärung</a> aufgeführten Angaben an unseren Dienst und weiter an OpenAI gesendet, damit eine kurze Antwort erzeugt werden kann. Frühere Versionen der App nutzen dafür stattdessen Googles Gemini-Modell auf Vertex AI. {K_reflect_week} im Tagebuch nutzt ausschließlich Apple Intelligence auf deinem Gerät.</p>
<p>Was ein Sprachmodell schreibt, ist erzeugter Text. Er kann falsch, allgemein oder nicht hilfreich sein, er ist <strong>keinerlei Beratung</strong>, und er ist nie eine Tatsachenaussage über dein Geld. Tippe nichts in diesen Bildschirm, von dem du nicht möchtest, dass ein Modell eines Drittanbieters es verarbeitet. Schlägt eine Anfrage fehl, zeigt dir die App einfach die normalen Auswahlmöglichkeiten – nichts wird in eine Warteschlange gestellt, später erneut versucht oder gespeichert. Wir können begrenzen, wie viele Reflexionen ein Gerät pro Tag anfragen kann.</p>
""",

"t.licence.h": "9. Lizenz und geistiges Eigentum",
"t.licence.b": """
<p>Wir gewähren dir eine persönliche, nicht ausschließliche, nicht übertragbare, widerrufliche Lizenz, On Ice auf einem iPhone oder iPad, das dir gehört oder das du kontrollierst, zu installieren und zu benutzen, im Einklang mit diesen Bedingungen und den Nutzungsregeln des App Store. On Ice, sein Name, sein Design, seine Grafiken, Texte und sein Code gehören {COMPANY} und sind durch das Urheberrecht und weitere Gesetze geschützt. Du darfst die App nicht kopieren, verändern, verbreiten, verkaufen, vermieten, zurückentwickeln oder abgeleitete Werke daraus erstellen, außer wo das Gesetz es ausdrücklich erlaubt.</p>
<p>Namen von Händlern, Apps und Websites, die du sperren oder als Alternative öffnen lässt, gehören ihren jeweiligen Inhabern. On Ice ist mit keinem von ihnen verbunden und wird von keinem von ihnen unterstützt oder gesponsert, und für sie gelten ihre eigenen Bedingungen.</p>
""",

"t.use.h": "10. Zulässige Nutzung",
"t.use.b": """
<p>Du verpflichtest dich, On Ice nicht auf eine Weise zu nutzen, die rechtswidrig ist, die die App, ihren KI-Dienst oder Apples Dienste stört, die versucht, die Kaufmechanismen des App Store oder die Limits des KI-Dienstes zu umgehen, oder die es auf einem Gerät installiert, zu dessen Verwaltung du nicht berechtigt bist. Du verpflichtest dich, es nicht zu nutzen, um eine andere Person ohne deren informierte Einwilligung einzuschränken oder zu überwachen, und über die KI-Reflexion keine Inhalte einzureichen, die rechtswidrig sind oder die du nicht teilen darfst.</p>
""",

"t.termination.h": "11. Beendigung",
"t.termination.b": """
<p>Du kannst die Nutzung von On Ice jederzeit beenden, indem du es löschst. Wir können deine Lizenz oder deinen Zugang zum KI-Dienst aussetzen oder beenden, wenn du gegen diese Bedingungen verstößt. Die Abschnitte 4, 6, 9, 12, 13 und 15 gelten über die Beendigung hinaus. Das Löschen der App kündigt kein laufendes Abo – kündige es in deinen App-Store-Einstellungen.</p>
""",

"t.warranty.h": "12. Gewährleistung und Haftung",
"t.warranty.b": """
<p>On Ice wird „wie besehen“ und „wie verfügbar“ bereitgestellt, ohne Gewährleistungen irgendeiner Art, ausdrücklich oder stillschweigend, einschließlich dessen, dass es jede App oder Website in jedem Fall sperrt, dass es die Nutzung genau misst, dass es ununterbrochen oder fehlerfrei läuft, dass irgendein Betrag, den es anzeigt, zutreffend ist, oder dass es dein Ausgabeverhalten ändert. Im größtmöglichen gesetzlich zulässigen Umfang haftet {COMPANY} nicht für mittelbare, zufällige, besondere, Folge- oder Strafschäden oder für Daten- oder Geldverluste, die aus deiner Nutzung oder Nichtnutzbarkeit der App entstehen – einschließlich jedes Kaufs, den du getätigt oder nicht getätigt hast, jeder Folge einer Sperre, die erschien oder nicht erschien, und jeder Blockierung, jedes Limits oder jeder Sitzung im strengen Modus, die du zu starten beschlossen hast. Wo die Haftung nicht ausgeschlossen werden kann, ist sie auf den Betrag begrenzt, den du uns in den zwölf Monaten vor dem Anspruch für Premium gezahlt hast. Nichts in diesen Bedingungen beschränkt Rechte, die dir als Verbraucher zustehen und auf die nicht verzichtet werden kann.</p>
""",

"t.apple.h": "13. Apple",
"t.apple.b": """
<p>On Ice wird über den Apple App Store vertrieben. Diese Bedingungen bestehen zwischen dir und {COMPANY}, nicht Apple. Apple ist nicht verpflichtet, Wartung oder Support für die App zu leisten, und ist nicht dafür verantwortlich, Ansprüche in Bezug auf sie zu behandeln, einschließlich Produkthaftungs-, Rechtskonformitäts- oder Schutzrechtsansprüchen. Apple und seine Tochtergesellschaften sind Drittbegünstigte dieser Bedingungen und können sie dir gegenüber durchsetzen. Wo diese Bedingungen schweigen, gilt Apples <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Lizenzvereinbarung für Endbenutzer</a>. Du versicherst, dass du dich nicht in einem Land befindest, das einem Embargo der US-Regierung unterliegt, und nicht als verbotene Partei gelistet bist, und du musst bei der Nutzung der App alle geltenden Bedingungen Dritter einhalten.</p>
""",

"t.changes.h": "14. Änderungen an diesen Bedingungen",
"t.changes.b": """
<p>Wir können diese Bedingungen von Zeit zu Zeit aktualisieren. Das Datum oben ändert sich dann, und wesentliche Änderungen werden in den Versionshinweisen der App vermerkt. Wenn du die App nach einer Aktualisierung weiter nutzt, nimmst du die geänderten Bedingungen an.</p>
""",

"t.law.h": "15. Anwendbares Recht",
"t.law.b": """
<p>Diese Bedingungen unterliegen dem Recht Pakistans, wo {COMPANY} tätig ist, ohne Rücksicht auf Kollisionsnormen. Wo das Recht deines Wohnsitzlandes dir Schutz gibt, auf den vertraglich nicht verzichtet werden kann, gilt dieser Schutz.</p>
""",

"t.contact.h": "16. Kontakt",
"t.contact.b": """
<p>Fragen zu diesen Bedingungen: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Deine Daten",
"d.h1": "Deine Daten löschen",
"d.sub": "Alles, was On Ice weiß, liegt auf deinem Gerät. Hier steht, wie du es entfernst – Stück für Stück oder alles auf einmal –, was mit deinem Abo passiert und warum es auf unserer Seite nichts anzufragen gibt.",
"d.meta": 'Siehe auch die <a href="{BASE}{L}/privacy/">Datenschutzerklärung</a>',

"d.where.h": "Was wo gespeichert ist",
"d.where.b": """
<p class="lead">On Ice hat kein Konto und führt auf keinem Server ein Profil über irgendjemanden. Alles, was es speichert, liegt auf deinem Gerät, und du kannst es entfernen, ohne uns zu fragen.</p>
<div class="table-wrap"><table>
<tr><th>Daten</th><th>Wo sie liegen</th><th>Wie du sie entfernst</th></tr>
<tr><td>Deine Liste, Entscheidungen, der Verlauf deiner geschätzten Ersparnis, Serien und Muster</td><td>Der private Speicher der App auf deinem Gerät</td><td>Lösche die App. Aus deinem Verlauf besteht die Ersparnis-Summe, deshalb wird er nicht Artikel für Artikel gelöscht.</td></tr>
<tr><td>Tagebucheinträge</td><td>Auf deinem Gerät</td><td>{K_delete_entry} bei jedem Eintrag, oder die App löschen</td></tr>
<tr><td>Ausgabenprotokoll, Regeln, Limits, Erinnerungen, Aktivitäten</td><td>Auf deinem Gerät</td><td>Jedes einzeln in der App entfernen, oder die App löschen</td></tr>
<tr><td>Deine Shops</td><td>Bildschirmzeit-Tokens und Website-Adressen auf deinem Gerät</td><td>In der App ändern; den Bildschirmzeit-Zugriff in den iOS-Einstellungen zu widerrufen, beendet außerdem jede Sperre</td></tr>
<tr><td>Momentaufnahme für Widgets und Live-Aktivitäten</td><td>Eine kleine Datei auf deinem Gerät</td><td>Wird mit der App entfernt</td></tr>
<tr><td>Der Wochenrückblick</td><td>Auf deinem Gerät, nur solange die KI-Reflexion an ist</td><td>Die KI-Reflexion ausschalten</td></tr>
<tr><td>Premium-Status</td><td>Dein Apple Account (Apple) und eine Kopie des Status auf deinem Gerät</td><td>In deinen App-Store-Einstellungen verwaltet – siehe unten</td></tr>
<tr><td>Was eine OpenAI-Reflexion gesendet hat</td><td>Nicht in unserem Dienst, der keine Inhalte behält. OpenAI kann es in Protokollen zur Missbrauchsüberwachung behalten, normalerweise bis zu 30 Tage (Google, bei früheren Versionen: bis zu 24 Stunden)</td><td>Für dich gibt es nichts zu löschen. Schalte die KI-Reflexion aus, und es wird nichts mehr gesendet</td></tr>
<tr><td>Eine Zählung der KI-Anfragen pro Gerät</td><td>Der KI-Dienst von On Ice, unter einer zufälligen Schlüsselkennung</td><td>Wird nach zwei Tagen automatisch gelöscht</td></tr>
<tr><td>Ein Konto, ein Profil, irgendetwas mit deinem Namen darauf</td><td>—</td><td>Gibt es nicht. Wir hatten nie eins zum Löschen.</td></tr>
</table></div>
""",

"d.inapp.h": "In der App entfernen",
"d.inapp.b": """
<ul>
  <li><strong>Tagebucheinträge:</strong> Öffne einen Eintrag und tippe auf {K_delete_entry}.</li>
  <li><strong>Ausgabenprotokoll:</strong> Tippe bei einem Eintrag auf {K_remove}.</li>
  <li><strong>Regeln, Limits, Erinnerungen und Aktivitäten:</strong> Jedes davon hat eine eigene Taste zum Löschen oder Entfernen.</li>
  <li><strong>Shops:</strong> Ändere deine Auswahl oder schalte einen Shop auf dem Startbildschirm aus. Wenn du den Schutz ausschaltest, kommen alle Sperren auf einmal herunter.</li>
  <li><strong>Entschiedene Artikel bleiben in deinem Verlauf</strong> – daraus bestehen deine geschätzte Ersparnis und deine Muster. Um diesen Verlauf zu entfernen, lösche die App.</li>
</ul>
<div class="callout amber"><span class="tile">{lock}</span><div>Solange der <strong>strenge Modus</strong> läuft, ist deine Einrichtung festgehalten – Shops lassen sich nicht entfernen, und Regeln und Limits lassen sich nicht löschen. Das ist die eine Zusage, um deren Einhaltung du die App gebeten hast. Er endet von selbst zu der Zeit, die du gewählt hast.</div></div>
""",

"d.journal.h": "Dein Tagebuch",
"d.journal.b": """
<p>Tagebucheinträge liegen nur auf deinem Gerät, und On Ice hat sie nie irgendwohin gesendet, also gibt es anderswo nichts zu entfernen. Lösche sie einzeln mit {K_delete_entry}. Um eine Kopie zu behalten, bevor du die App löschst, nutze {K_export_journal}: Das erstellt eine reine Textdatei, die du speicherst, wo du willst.</p>
""",

"d.ai.h": "Die KI-Reflexion",
"d.ai.b": """
<p>Wenn du die KI-Reflexion eingeschaltet hast, behält On Ice den letzten Wochenrückblick auf deinem Gerät, damit du ihn noch einmal lesen kannst. Wenn du die KI-Reflexion unter {K_settings} → {K_ai_reflection} ausschaltest, wird er gelöscht, die Sonntagserinnerung entfernt und die Sitzung der App mit dem Dienst beendet, und On Ice stellt wieder keine eigenen Netzwerkverbindungen mehr her.</p>
<p>Der Dienst hatte nie eine Kopie dessen, was du gesendet hast. Er behält nur eine Zählung pro Gerät unter einem zufälligen Schlüssel, die er nach zwei Tagen löscht, und tägliche Summen, die kein Gerät nennen.</p>
""",

"d.uninstall.h": "Die App löschen",
"d.uninstall.b": """
<p>Wenn du On Ice von deinem iPhone oder iPad löschst, werden alle seine Daten mit entfernt – deine Liste, dein Verlauf, dein Tagebuch, deine Einstellungen und die Bildschirmzeit-Tokens –, und jede Sperre, jede Blockierung und jedes Limit endet sofort. Das ist der Weg, alles auf einmal zu löschen. Ist die App in einem iCloud- oder Computer-Backup enthalten, gehört diese Kopie zu deinem Apple Account und unterliegt Apples Bedingungen; wir haben keinen Zugriff darauf.</p>
""",

"d.subscription.h": "Dein Abo",
"d.subscription.b": """
<p>Das Löschen der App kündigt kein Abo – es gehört zu deinem Apple Account, nicht zur App. Kündige es in den <a href="https://apps.apple.com/account/subscriptions">App-Store-Aboeinstellungen</a>; es bleibt bis zum Ende des laufenden Zeitraums aktiv. Rückerstattungen übernimmt der <a href="https://support.apple.com/billing">Apple Support</a>. Ein Einmalkauf verlängert sich nicht, und es muss nichts gekündigt werden. Wenn du zu einem Familienplan gehörst, verwaltet ihn die Person, die ihn gekauft hat.</p>
""",

"d.email.h": "Frag uns",
"d.email.b": """
<p>Wenn du eine schriftliche Bestätigung möchtest, dass wir nichts über dich haben, oder wenn du glaubst, dass wir doch etwas haben, schreib von einer beliebigen Adresse an {MAIL}. Wir antworten innerhalb von 30 Tagen. Bitte schick uns nicht deine Liste, deine Preise, dein Tagebuch oder Bildschirmfotos davon – wir brauchen sie nicht, um zu antworten.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Hier liegt nichts auf Eis.",
"nf.sub": "Was ausnahmsweise nicht der Sinn der Sache ist.",
"nf.cta": "Zurück zur Hilfe",
"nf.b": 'Diese Seite gibt es hier nicht. Versuch es mit <a href="{BASE}/">Hilfe</a>, der <a href="{BASE}/privacy/">Datenschutzerklärung</a> oder den <a href="{BASE}/terms/">Nutzungsbedingungen</a>.',

}
