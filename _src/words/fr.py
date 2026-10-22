# -*- coding: utf-8 -*-
"""Français. Vouvoie, comme l’app elle-même.

Traduit depuis en.py, clé par clé et dans le même ordre. Les termes suivent le
catalogue de l’app (Localizable.xcstrings) : « économies estimées », « En
attente » pour un article qui patiente, « délai de réflexion » et « durée
d’attente » pour l’attente elle-même, « écran de blocage » pour le shield,
« laisser partir », « heures sensibles », « mode strict », « créneau d’achat »,
« journal des dépenses », « réflexion IA ». Les `k.*` sont copiés tels quels
depuis les libellés de l’app et d’iOS, jamais retraduits.

Typographie française : espace insécable (U+00A0) avant « : » et à l’intérieur
des guillemets, espace fine insécable (U+202F) avant ; ? !
"""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Aide",
"nav.about": "À propos",
"nav.privacy": "Confidentialité",
"nav.terms": "Conditions",
"nav.data": "Vos données",

"ui.skip": "Aller au contenu",
"ui.pages": "Pages",
"ui.footer": "Pied de page",
"ui.lang": "Langue",
"ui.toc": "Sur cette page",
"ui.rights": "Tous droits réservés.",
"ui.store_soon": "Bientôt sur l’App Store",
"ui.store_get": "Télécharger dans l’App Store",
"ui.date": "22 octobre 2026",
"ui.last_updated": "Dernière mise à jour : {DATE}",

# Les libellés de l'app, copiés tels quels depuis Localizable.xcstrings.
"k.settings": "Réglages",
"k.ios_settings": "Réglages",
"k.screen_time": "Temps d'écran",
"k.apps_with_st": "Apps avec accès à Temps d'écran",
"k.notifications": "Notifications",
"k.restore": "Restaurer les achats",
"k.protection_tools": "Outils de protection",
"k.repair": "Réparer la protection",
"k.someone_key": "Quelqu’un détient la clé",
"k.only_these": "Seulement ces apps",
"k.ai_reflection": "Réflexion IA",
"k.writer": "Auteur de la réflexion",
"k.what_gets_sent": "Ce qui est envoyé",
"k.lock_journal": "Verrouiller le journal",
"k.export_journal": "Exporter le journal",
"k.delete_entry": "Supprimer l’entrée",
"k.reflect_week": "Faire le bilan de ma semaine",
"k.help_privacy": "Aide et confidentialité",
"k.email_support": "Écrire au support",
"k.language": "Langue",
"k.note_it": "Le noter",
"k.never_mind": "Finalement non",
"k.need_to_shop": "Je dois faire des achats maintenant",
"k.done_block": "J’ai terminé — rebloquez",
"k.remove": "Supprimer",
"k.follow_ups": "Questions de suivi",

"meta.support.title": "On Ice — Aide",
"meta.support.desc": "L’aide officielle d’On Ice, l’app pour iPhone et iPad qui place une nuit entre vous et le bouton d’achat. Fonctionnement, prérequis, FAQ et contact.",
"meta.about.title": "On Ice — Une nuit entre vous et le bouton d’achat",
"meta.about.desc": "On Ice protège les apps et sites d’achat que vous choisissez et vous demande d’abord de laisser passer une nuit. Aucun accès bancaire, aucun suivi des prix, aucun lien d’affiliation.",
"meta.privacy.title": "Politique de confidentialité — On Ice",
"meta.privacy.desc": "On Ice n’a ni compte, ni connexion bancaire, ni outil d’analyse. Ce qui reste sur votre appareil, et ce qu’envoie exactement la seule fonction IA optionnelle.",
"meta.terms.title": "Conditions d’utilisation — On Ice",
"meta.terms.desc": "Conditions d’utilisation (CLUF) d’On Ice : ce qu’est l’app et ce qu’elle n’est pas, pourquoi chaque montant est une estimation, comment Premium et les formules famille sont facturés, et ce que le mode strict vous demande.",
"meta.data.title": "Supprimer vos données — On Ice",
"meta.data.desc": "Comment effacer ce que détient On Ice — tout cela sur votre appareil — et ce qu’il advient de votre abonnement.",
"meta.nf.title": "Introuvable — On Ice",
"meta.nf.desc": "Page introuvable.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Aide",
"s.h1": "De l’aide pour On Ice",
"s.sub": "Une nuit entre vous et le bouton d’achat. On Ice protège les apps et sites d’achat que vous avez choisis et vous demande d’abord de laisser passer une nuit. Cette page explique comment il fonctionne, ce qu’il lui faut et comment nous joindre.",
"s.cta": "Lire la FAQ",
"s.meta": 'Aucun compte · aucun accès bancaire · <a href="{BASE}{L}/privacy/">Politique de confidentialité</a>',

"s.how.h": "Comment fonctionne On Ice",
"s.how.b": """
<p class="lead">On Ice place une nuit entre vous et le bouton d’achat.</p>
<p>Vous choisissez les apps et sites d’achat qui vous font craquer. Dès lors, en ouvrir un ne vous mène plus directement au paiement : l’écran de blocage d’On Ice passe d’abord — <em>Une pause avant d’acheter.</em> Touchez {K_note_it} pour noter ce qui vous tente, ou {K_never_mind} pour passer votre chemin. Rien n’est jamais acheté ni annulé à votre place.</p>
<p>Tout ce que vous notez attend sur votre liste — vingt-quatre heures, sauf si vous avez choisi une autre durée. Quand l’attente est terminée, On Ice pose une seule question : vous le voulez toujours ? La plupart des envies ne survivent pas à la nuit, et celles qui y survivent étaient réelles. Les deux réponses sont bonnes.</p>
<ul class="rows">
  <li><span class="tile">{shield}</span><div><b>Protection</b><span>Un interrupteur sur l’écran Accueil de l’app, et un pour chaque boutique. Tant qu’il est activé, les boutiques que vous avez choisies affichent l’écran de blocage d’On Ice au lieu de s’ouvrir — l’app <em>et</em> le site web, y compris dans Safari.</span></div></li>
  <li><span class="tile">{moon}</span><div><b>Une courte pause</b><span>Avant toute chose, un moment pour respirer, taper une phrase, lire un rappel ou dire ce qui vous amène. C’est vous qui choisissez lequel, et pour combien de temps.</span></div></li>
  <li><span class="tile">{note}</span><div><b>Notez-le</b><span>Nommez l’article, touchez un prix approximatif, touchez ce que vous ressentez — ennui, stress, envie de fêter, peur de rater la promo, ou « J’en ai besoin ». Un seul écran, quinze secondes.</span></div></li>
  <li><span class="tile amber">{snow}</span><div><b>En attente</b><span>Les articles notés attendent sous un anneau de compte à rebours. Rien n’est acheté pendant le délai de réflexion d’un article. Si vous avez vraiment besoin de la boutique maintenant, elle s’ouvre quelques minutes et l’écran de blocage revient tout seul.</span></div></li>
  <li><span class="tile green">{coin}</span><div><b>Économies estimées</b><span>Chaque article que vous laissez partir s’ajoute à un total cumulé, construit entièrement à partir des prix que vous avez saisis vous-même — pour aujourd’hui, cette semaine et ce mois-ci.</span></div></li>
  <li><span class="tile amber">{clock}</span><div><b>Objectifs, limites et blocages</b><span>Un objectif quotidien de temps de shopping, des limites quotidiennes, des blocages programmés, des blocages par mode de concentration, et des règles pour les heures difficiles. Le mode strict maintient votre configuration en place.</span></div></li>
  <li><span class="tile">{book}</span><div><b>Autre chose à faire</b><span>Un journal privé, et quelques choses à faire à la place — une marche, un livre, un appel — pour quand l’envie a besoin d’un exutoire.</span></div></li>
  <li><span class="tile">{widget}</span><div><b>Widgets, Activités en direct et Raccourcis</b><span>Les économies estimées et ce qui est en attente sur l’écran d’accueil et l’écran verrouillé, un compte à rebours pendant qu’une boutique est ouverte, et des actions Siri et Raccourcis pour démarrer un blocage.</span></div></li>
</ul>
""",

"s.requirements.h": "Prérequis",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Appareil</th><td>iPhone ou iPad sous <strong>iOS 17 ou version ultérieure</strong>. Quelques extras demandent davantage : les commandes du centre de contrôle nécessitent iOS 18, et l’écriture avec Apple Intelligence nécessite un appareil et une langue compatibles.</td></tr>
<tr><th>Autorisation</th><td>L’accès à <strong>Temps d’écran</strong>, accordé une fois pendant la configuration via la demande d’Apple elle-même. On Ice utilise le framework Temps d’écran d’Apple — le même système que celui des limites d’apps intégrées à iOS — et c’est Apple, pas On Ice, qui se tient réellement devant une boutique.</td></tr>
<tr><th>Compte</th><td>Aucun. Il n’y a nulle part dans l’app d’inscription, de champ e-mail ni de mot de passe.</td></tr>
<tr><th>Internet</th><td>Pas nécessaire. Chaque écran de blocage, pause, liste, minuteur et total fonctionne hors ligne. Le seul trafic réseau est celui d’Apple quand vous achetez ou restaurez Premium — et la réflexion IA optionnelle, si vous l’activez avec OpenAI comme auteur.</td></tr>
<tr><th>Langues</th><td>English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil) et 简体中文. On Ice suit la langue de votre appareil, ou celle que vous choisissez dans {K_settings} → {K_language}.</td></tr>
<tr><th>Facultatif</th><td>Les <strong>notifications</strong>, générées sur l’appareil, pour vous faire passer de l’écran de blocage à l’app et vous prévenir quand l’attente d’un article est terminée. <strong>Mouvement et forme</strong>, uniquement pour afficher vos pas en direct pendant une marche. <strong>Face ID ou Touch ID</strong>, uniquement si vous verrouillez votre journal.</td></tr>
</table></div>
""",

"s.start.h": "Premiers pas",
"s.start.b": """
<p>La configuration tient en quelques écrans et se termine avec la protection déjà activée.</p>
<ol class="steps">
  <li><div><b>Essayez une pause de dix secondes</b> — le même moment que celui que l’écran de blocage vous offrira plus tard.</div></li>
  <li><div><b>Autorisez l’accès à Temps d’écran</b> quand Apple le demande. On Ice ne peut pas fonctionner sans lui, et vous pouvez le retirer à tout moment dans {K_ios_settings} → {K_screen_time}.</div></li>
  <li><div><b>Choisissez vos boutiques</b> dans le sélecteur d’Apple, et ajoutez les sites d’achat que vous voulez protéger. On Ice n’apprend jamais le nom des apps que vous choisissez — voir <a href="{BASE}{L}/privacy/#screentime">Confidentialité</a>.</div></li>
  <li><div><b>Définissez des heures sensibles</b> si vous le souhaitez — les heures tardives où le shopping tourne mal. Facultatif, et modifiable plus tard.</div></li>
  <li><div><b>Terminé.</b> Ouvrez une de vos boutiques et découvrez l’écran de blocage.</div></li>
</ol>
<div class="callout"><span class="tile">{info}</span><div>Le premier écran de blocage peut surprendre. C’est précisément le moment pour lequel l’app existe — touchez {K_note_it} et prenez quinze secondes.</div></div>
""",

"s.money.h": "À propos du montant des économies",
"s.money.b": """
<p>Chaque prix dans On Ice est un prix que vous avez saisi vous-même, et chaque montant affiché par l’app porte la mention <strong>estimé</strong>. Ce n’est pas une précaution ajoutée après coup — c’est tout le principe.</p>
<ul>
  <li>On Ice <strong>ne se connecte pas à votre banque</strong>, ne lit pas votre historique d’achats, ne vérifie pas ce que coûte réellement quoi que ce soit et ne convertit pas les devises.</li>
  <li>Un article compte dans le total <strong>une seule fois</strong>, quand vous le laissez partir après son attente.</li>
  <li>Si vous ne revenez jamais à un article, On Ice vous le rappelle, et 48 heures après la fin de son attente, il le compte comme laissé partir. Vous pouvez décider à tout moment d’ici là.</li>
  <li>Les articles que vous gardez ne touchent pas au total — sauf si vous indiquez plus tard à On Ice que vous en avez acheté un moins cher que vous ne l’aviez estimé, auquel cas la différence compte.</li>
  <li>Le <strong>journal des dépenses</strong> est destiné aux achats impulsifs qu’On Ice n’a jamais vus. Il est tenu à part de vos économies.</li>
</ul>
<div class="callout green"><span class="tile">{coin}</span><div>Ce montant est un registre de ce que vous avez décidé de ne pas acheter, aux prix que vous aviez estimés. C’est un bon chiffre dont être fier, et un mauvais chiffre à mettre dans un tableur.</div></div>
""",

"s.faq.h": "Questions fréquentes",
"s.faq.b": """
<dl class="faq">
<dt>On Ice est-il gratuit ?</dt>
<dd>Oui, et la version gratuite est un produit qui fonctionne, pas une démo : <strong>une app d’achat et un site web</strong> protégés, l’attente de vingt-quatre heures et votre liste, vos économies estimées, la pause respiration, trois choses à faire à la place, le journal, un objectif quotidien de temps de shopping, ainsi que les blocages programmés et par mode de concentration.</dd>
<dt>Qu’ajoute Premium ?</dt>
<dd>Toutes les boutiques et tous les sites web que vous voulez protéger ; des attentes de 12, 24, 48 ou 72 heures ; tous les types de pause, des pauses qui s’allongent avec les tentatives répétées, et vos propres rappels ; les règles des heures sensibles et par boutique ; les limites quotidiennes ; le mode strict ; vos habitudes d’achat et ce que vous avez ressenti après vos achats ; la relecture de votre journal ; six choses à faire à la place ; les widgets ; et la réflexion IA optionnelle. Premium est un abonnement mensuel ou annuel — la formule annuelle commence par un <strong>essai gratuit</strong> lorsqu’il est proposé — ou un achat unique à vie, et les formules annuelle et à vie existent aussi en <strong>formules famille</strong>. Les prix de votre pays sont affichés dans l’app, et la facturation est gérée par Apple.</dd>
<dt>Comment fonctionnent les formules famille ?</dt>
<dd>Premium famille annuel et Premium famille à vie sont partagés via le Partage familial d’Apple avec jusqu’à cinq autres personnes de votre groupe familial — six en tout. Chaque personne reçoit Premium dans sa propre copie d’On Ice, sur son propre appareil. Personne ne voit les boutiques, la liste, le journal ou les économies de quelqu’un d’autre.</dd>
<dt>Est-ce que ça m’empêche d’acheter ?</dt>
<dd>Non. Un écran de blocage ordinaire est une pause, pas un mur : touchez {K_note_it}, dites ce qui a attiré votre regard, et {K_need_to_shop} ouvre la boutique pendant quelques minutes. {K_done_block} la referme avant la fin. Les seules choses sans aucun passage sont celles que vous configurez vous-même — une règle de blocage total, une limite quotidienne atteinte, un blocage programmé ou un blocage par mode de concentration — et chacune prend fin d’elle-même.</dd>
<dt>Que se passe-t-il si mon abonnement expire ?</dt>
<dd>Rien de ce que vous avez construit ne vous est retiré. Votre liste, votre historique et vos économies estimées restent, les boutiques choisies restent protégées, et vos règles, vos limites et un mode strict en cours continuent de s’appliquer. Votre attente revient à 24 heures, la réflexion IA se désactive, et les widgets et les écrans d’habitudes attendent le retour de Premium. Vous ne pouvez simplement plus ajouter de fonctions Premium.</dd>
<dt>Puis-je restaurer un achat sur un nouvel appareil ?</dt>
<dd>Oui. Ouvrez {K_settings} et touchez {K_restore}. Premium appartient à votre compte Apple, pas à l’appareil. Votre liste, votre journal et votre historique ne le suivent pas — ils vivent sur l’appareil qui les a créés, et ne passent sur un nouvel appareil qu’avec une sauvegarde de l’appareil entier.</dd>
<dt>Est-ce que ça marche sur iPad ?</dt>
<dd>Oui — iPhone et iPad, iOS 17 ou version ultérieure. Chaque appareil garde ses propres boutiques, sa liste et son historique ; rien n’est synchronisé entre eux.</dd>
<dt>Pourquoi On Ice ne peut-il pas me dire quelles apps j’ai protégées ?</dt>
<dd>Parce qu’il ne le sait vraiment pas. Le Temps d’écran d’Apple remet à On Ice des jetons opaques qui n’ont aucun sens en dehors de votre appareil — aucun nom d’app, aucun identifiant. On Ice peut demander à iOS de les protéger, et iOS affiche pour vous leurs noms et leurs icônes ; On Ice ne peut pas les lire. Les sites web que vous ajoutez en tapant une adresse font exception : On Ice garde cette adresse sur votre appareil pour qu’iOS puisse protéger le site.</dd>
<dt>Protège-t-il les sites web, ou seulement les apps ?</dt>
<dd>Les deux. Ajoutez séparément l’app d’une boutique et son site web, et chacun est protégé — le site web dans Safari.</dd>
<dt>On Ice voit-il ce que j’achète ?</dt>
<dd>Non. Il n’a aucun accès à votre banque, à vos commandes, à votre navigation ni à votre carte. Il n’enregistre que ses propres événements — qu’un écran de blocage a été affiché, et ce que vous avez choisi — et les garde sur votre appareil.</dd>
<dt>Mon journal quitte-t-il mon appareil ?</dt>
<dd>Jamais. Ni vers nous, ni vers OpenAI, quel que soit le réglage. Vous pouvez le verrouiller avec Face ID, Touch ID ou votre code, et son résumé hebdomadaire facultatif est rédigé par Apple Intelligence sur votre appareil.</dd>
<dt>Où vont mes pas de marche ?</dt>
<dd>Nulle part. Pendant une marche, On Ice affiche vos pas en direct, et les oublie quand la marche se termine. Il ne lit ni n’écrit rien dans l’app Santé d’Apple.</dd>
<dt>Qu’est-ce que la réflexion IA, et est-elle active ?</dt>
<dd>C’est une courte question avant les choix, de temps en temps, et quelques phrases sur votre semaine le dimanche. Elle est <strong>désactivée jusqu’à ce que vous l’activiez</strong>. Vous choisissez qui l’écrit : <strong>Apple Intelligence</strong>, sur votre appareil, ou <strong>OpenAI</strong> — la seule chose dans l’app qui envoie quoi que ce soit hors de l’appareil. La <a href="{BASE}{L}/privacy/#ai">Politique de confidentialité</a> énumère exactement quoi.</dd>
</dl>
""",

"s.trouble.h": "Dépannage",
"s.trouble.b": """
<h3>Une boutique s’ouvre sans écran de blocage</h3>
<ul>
  <li>Vérifiez que la protection est activée en haut de l’écran Accueil, et que l’interrupteur de la boutique elle-même est activé.</li>
  <li>Vérifiez que l’accès à Temps d’écran est toujours accordé : {K_ios_settings} → {K_screen_time} → {K_apps_with_st}. S’il a été retiré, On Ice affiche un écran avec un moyen de le redemander.</li>
  <li>Un <strong>créneau d’achat</strong> que vous avez ouvert est peut-être encore en cours. Il se ferme tout seul — ou touchez {K_done_block} — et l’écran de blocage revient.</li>
  <li>Si la boutique n’est couverte que par une <strong>règle</strong>, l’écran de blocage n’apparaît que pendant les heures de cette règle.</li>
  <li>Toujours rien ? {K_settings} → {K_protection_tools} → {K_repair} réapplique chaque écran de blocage et chaque horaire.</li>
</ul>
<h3>Toucher « Le noter » n’ouvre pas On Ice</h3>
<ul>
  <li>Sur certaines versions d’iOS, l’écran de blocage vous passe le relais via une notification. Si les notifications sont désactivées, iOS ne peut pas la livrer — activez-les dans {K_ios_settings} → {K_notifications} → On Ice.</li>
  <li>Ouvrir On Ice vous-même reprend l’article qui attend d’être noté.</li>
</ul>
<h3>Un site web n’est pas protégé</h3>
<p>Les sites web sont protégés par adresse. Vérifiez que l’adresse ajoutée correspond à celle que vous ouvrez réellement, et rappelez-vous que l’app d’une boutique et son site web sont deux choses distinctes à ajouter.</p>
<h3>Mon objectif ou ma limite quotidienne affiche moins de minutes que prévu</h3>
<p>iOS n’indique pas aux apps combien de temps vous avez passé dans une autre app. Il signale seulement à On Ice quand le temps passé dans vos boutiques protégées franchit un palier — toutes les cinq minutes au début — donc On Ice affiche « au moins » ce nombre de minutes. Le chiffre réel peut être un peu plus élevé.</p>
<h3>Je ne peux pas désactiver la protection ni retirer une boutique</h3>
<p>Vérifiez si le <strong>mode strict</strong>, un <strong>blocage programmé</strong> ou un <strong>blocage par mode de concentration</strong> est en cours — l’écran Accueil l’indique. Tant que le mode strict tourne, votre configuration est maintenue en place, c’est voulu, et il se termine tout seul à l’heure que vous avez choisie. Si vous avez configuré {K_someone_key}, la personne qui détient le code PIN peut y mettre fin plus tôt.</p>
<h3>La question IA n’apparaît jamais</h3>
<p>Elle nécessite Premium, et elle est désactivée jusqu’à ce que vous l’activiez dans {K_settings} → {K_ai_reflection}. Même alors, elle ne pose une question que lorsqu’il y a une raison — un ressenti qui vous a souvent laissé des regrets, une heure sensible, ou un prix plus élevé. Avec OpenAI comme auteur, elle nécessite une connexion Internet. Si quelque chose ne va pas, elle vous montre discrètement les choix habituels à la place.</p>
<h3>Les widgets sont en retard</h3>
<p>iOS rafraîchit les widgets selon son propre calendrier. Ouvrir On Ice les met à jour. Le widget des économies et le widget « En attente » sont inclus dans Premium.</p>
<h3>Premium n’est pas reconnu</h3>
<p>Touchez {K_restore} dans {K_settings}, et vérifiez que l’appareil est connecté au même compte Apple que celui qui a effectué l’achat — ou, pour une formule famille, que vous faites partie du groupe Partage familial de l’acheteur. Les remboursements et les questions de facturation sont gérés par Apple via l’<a href="https://support.apple.com/billing">assistance Apple</a>.</p>
<h3>L’app n’est pas dans la bonne langue</h3>
<p>Choisissez-en une dans {K_settings} → {K_language}. Le sélecteur d’apps d’Apple suit à la prochaine ouverture d’On Ice.</p>
""",

"s.contact.h": "Contact",
"s.contact.b": """
<p>Une question, un bug, ou quelque chose qui devrait marcher et ne marche pas — écrivez-nous, et une personne vous répondra. Le plus rapide est {K_settings} → {K_help_privacy} → {K_email_support}, qui ajoute pour vous votre version d’On Ice, votre version d’iOS et le modèle de votre appareil.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Indiquez le modèle de votre appareil, la version d’iOS et ce que vous attendiez. Ne nous envoyez jamais votre liste, vos prix ni votre journal — nous n’en avons pas besoin et préférerions ne pas les détenir.</span></div></div>
<p class="small">La facturation, les remboursements et les changements d’abonnement sont gérés par Apple : <a href="https://apps.apple.com/account/subscriptions">gérer les abonnements</a> · <a href="https://support.apple.com/billing">demander un remboursement</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "À propos d’On Ice",
"a.h1": "Une nuit entre vous et le bouton d’achat.",
"a.sub": "Choisissez les apps et sites d’achat qui vous font craquer. Dès lors, en ouvrir un vous montre d’abord un écran de blocage — et une décision que vous prendrez demain.",
"a.cta": "Aide",
"a.meta": "Aucun compte · aucun accès bancaire · iPhone et iPad, iOS 17+ · 8 langues",
"a.lead": "On Ice place une nuit entre vous et le bouton d’achat. Ni verrou, ni leçon de morale — une courte pause, et le temps de découvrir si vous le vouliez vraiment. Rien ici ne vous reproche d’avoir des envies, et rien ne devient rouge si vous l’achetez.",

"a.f1.h": "Une pause avant d’acheter.",
"a.f1.p": "Ouvrez une boutique que vous avez choisie et On Ice intervient avant le paiement — dans l’app comme dans Safari. Prenez une grande respiration, tapez une phrase, lisez un rappel ou dites ce qui vous amène.",
"a.f2.h": "Notez-le, ne l’achetez pas.",
"a.f2.p": "Nommez l’article, touchez un prix approximatif, touchez ce que vous ressentez. Quinze secondes, un seul écran. Le noter doit être plus rapide que l’envie.",
"a.f3.h": "Une nuit en attente.",
"a.f3.p": "Les articles notés attendent sous un anneau de compte à rebours — 24 heures, ou de 12 à 72. Rien n’est acheté pendant le délai de réflexion d’un article, et c’est demain que vous décidez.",
"a.f4.h": "Voyez le total grandir.",
"a.f4.p": "Chaque article que vous laissez partir s’ajoute à vos économies estimées — vos propres estimations, pour aujourd’hui, cette semaine et ce mois-ci, à côté des heures où vous croisez le plus souvent l’écran de blocage.",
"a.f5.h": "Autre chose à faire.",
"a.f5.p": "Quand l’envie a besoin d’un exutoire : une marche avec vos pas en direct, un livre, une playlist, un appel. Choisissez ce qui vous convient et lancez-le d’un seul toucher.",
"a.f6.h": "Plus ferme quand vous le voulez.",
"a.f6.p": "Un objectif quotidien de temps de shopping, des limites quotidiennes, des blocages programmés et par mode de concentration, des règles d’heures sensibles pour les fins de soirée, et le mode strict pour maintenir le tout en place.",
"a.f7.h": "Un journal rien qu’à vous.",
"a.f7.p": "Une question par jour et un endroit pour écrire. Verrouillez-le avec Face ID. Rien de ce qu’il contient ne quitte jamais votre appareil.",
"a.f8.h": "Il ne voit jamais ce que vous achetez.",
"a.f8.p": 'Aucune connexion bancaire, aucun historique d’achats, aucun suivi des prix, aucun lien d’affiliation, aucun outil d’analyse. Apple donne à On Ice des codes, pas des noms. <a href="{BASE}{L}/privacy/">Comment cela fonctionne.</a>',

"a.price.h": "Ce que ça coûte",
"a.price.b": """
<p>La version gratuite est un produit qui fonctionne, pas une démo, et rien de ce que vous avez déjà construit ne vous est retiré si un abonnement expire.</p>
<div class="tiers">
  <div class="tier"><div class="lbl">Gratuit</div><div class="price">Sans frais</div><ul><li>Une app d’achat et un site web, protégés</li><li>L’attente de 24 heures et votre liste</li><li>Vos économies estimées</li><li>La pause respiration et trois choses à faire à la place</li><li>Le journal, un objectif quotidien, les blocages programmés et par mode de concentration</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Mensuel · Annuel · À vie</div><ul><li>Toutes les boutiques et tous les sites web que vous voulez</li><li>Des attentes de 12, 24, 48 ou 72 heures</li><li>Tous les types de pause, et vos propres rappels</li><li>Heures sensibles, règles par boutique, limites quotidiennes et mode strict</li><li>Vos habitudes d’achat, et ce que vous avez ressenti après vos achats</li><li>Les widgets, la relecture de votre journal, et la réflexion IA optionnelle</li><li>La formule annuelle commence par un essai gratuit ; les formules annuelle et à vie existent aussi en formules famille pour six personnes maximum</li></ul></div>
</div>
<p class="small">Les prix de votre pays sont affichés dans l’app et sur l’App Store. La facturation est gérée par Apple. <a href="{BASE}{L}/terms/#subscriptions">Conditions d’abonnement.</a></p>
""",

"a.st.h": "Construit sur le Temps d’écran d’Apple",
"a.st.b": """
<p>On Ice utilise le même framework que celui des limites d’apps intégrées à iOS. Apple ne l’accorde qu’aux apps qu’elle a examinées à cette fin, et c’est Apple — pas On Ice — qui se tient réellement entre vous et la boutique. C’est pour cela qu’On Ice peut protéger une app sans jamais apprendre son nom.</p>
<p>iPhone et iPad · iOS 17 ou version ultérieure · English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil), 简体中文</p>
""",

"a.est.h": "Chaque montant est une estimation",
"a.est.b": """
<p>On Ice vous demande ce que coûte à peu près quelque chose et retient votre réponse. Il ne se connecte à aucune banque, ne vérifie aucun prix, ne convertit aucune devise et ne donne aucun conseil financier. Chaque montant qu’il affiche porte la mention <em class="est">estimé</em> — dans l’app, dans les widgets et sur ce site.</p>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Politique de confidentialité",
"p.h1": "Il ne voit jamais ce que vous achetez.",
"p.sub": "Aucun compte, aucune connexion bancaire, aucun historique d’achats, aucun suivi des prix et aucun outil d’analyse. Ce que sait On Ice reste sur votre appareil — avec une fonction optionnelle, désactivée jusqu’à ce que vous l’activiez, dont le contenu exact est détaillé ci-dessous.",
"p.meta": "En vigueur au {DATE} · s’applique à l’app On Ice pour iPhone et iPad, et à ce site",

"p.summary.h": "La version courte",
"p.summary.b": """
<p class="lead"><strong>On Ice n’a aucun compte, aucun outil d’analyse, aucune publicité et aucun code tiers.</strong> Il n’y a nulle part de connexion bancaire, d’historique d’achats, de suivi des prix ni de lien d’affiliation. Tout ce qu’il sait est écrit sur votre iPhone ou votre iPad et y reste.</p>
<div class="callout"><span class="tile">{eye-off}</span><div>Les apps que vous choisissez dans le sélecteur Temps d’écran d’Apple parviennent à On Ice sous forme de jetons opaques que seul votre appareil sait interpréter. Il n’y a ni nom d’app, ni identifiant, ni rien à envoyer.</div></div>
<p>Il y a exactement une exception, et elle est désactivée jusqu’à ce que vous l’activiez : la <strong>réflexion IA</strong> optionnelle. Avec <strong>Apple Intelligence</strong> comme auteur, elle tourne sur votre appareil et rien ne sort. Avec <strong>OpenAI</strong> comme auteur, une courte liste fixe de détails sort — énumérée en entier <a href="#ai">ci-dessous</a>. Votre journal ne quitte jamais l’appareil, quel que soit l’auteur choisi.</p>
<p>Cette politique s’applique à l’app On Ice pour iPhone et iPad, publiée par {COMPANY}, et à ce site web.</p>
""",

"p.collect.h": "Ce que nous collectons",
"p.collect.b": """
<p>« Collecter », au sens d’Apple comme au nôtre, signifie transmettre des données hors de l’appareil et les conserver quelque part de façon non transitoire. Avec la réflexion IA désactivée — et c’est ainsi que commence chaque installation — On Ice n’envoie rien vous concernant, nulle part. Le tableau montre ce qui change si vous l’activez avec OpenAI comme auteur.</p>
<div class="table-wrap"><table>
<tr><th>Catégorie</th><th>Envoyé ?</th><th>Ce que cela veut dire</th></tr>
<tr><td>Informations financières</td><td>Seulement avec les réflexions OpenAI activées</td><td>Aucune connexion bancaire, aucune carte, aucun accès aux transactions, aucun historique d’achats. Avec les réflexions OpenAI activées, une <em>tranche de prix</em> pour l’article devant vous et un total hebdomadaire arrondi des économies estimées sont envoyés — jamais un prix exact, un compte ou un solde.</td></tr>
<tr><td>Coordonnées</td><td>Non</td><td>Il n’y a nulle part dans l’app de compte, de connexion ni de champ e-mail.</td></tr>
<tr><td>Identifiants</td><td>Seulement avec les réflexions OpenAI activées</td><td>Aucun identifiant utilisateur, aucun identifiant publicitaire, et On Ice ne demande jamais à vous suivre. Notre service IA voit un identifiant de clé App Attest aléatoire, utilisé uniquement pour compter les requêtes par appareil et par jour, et supprimé au bout de deux jours.</td></tr>
<tr><td>Données d’utilisation</td><td>Seulement avec les réflexions OpenAI activées</td><td>Aucun outil d’analyse et aucun événement d’interaction avec le produit. Les écrans de blocage, les pauses et les décisions sont comptés sur votre appareil, pour vos propres écrans. Une réflexion contient le nombre d’écrans de blocage du jour ; le bilan hebdomadaire contient les décomptes de la semaine.</td></tr>
<tr><td>Contenu utilisateur</td><td>Seulement avec les réflexions OpenAI activées</td><td>Votre liste, vos prix, votre journal, votre journal des dépenses et vos rappels restent sur l’appareil. Avec OpenAI comme auteur, le nom de l’article devant vous et ce que vous tapez en réponse à la question sont envoyés.</td></tr>
<tr><td>Historique de navigation</td><td>Non</td><td>On Ice ne peut pas voir ce que vous consultez en ligne. Il apprend seulement que son propre écran de blocage a été affiché, et ce que vous y avez choisi.</td></tr>
<tr><td>Localisation, santé, forme, contacts, recherches, diagnostics</td><td>Non</td><td>Les pas pendant une marche sont affichés en direct et ne sont jamais stockés ni envoyés. On Ice n’a aucun outil propre de rapport de plantage ou de performances.</td></tr>
</table></div>
<p><strong>Suivi :</strong> aucun. On Ice ne lie rien vous concernant à des données provenant des apps ou des sites web d’autres entreprises, et ne partage rien avec des courtiers en données ou des annonceurs. Il n’y a <strong>aucun lien d’affiliation</strong> : On Ice ne gagne rien quand vous achetez quelque chose, ce qui est le seul arrangement compatible avec une app dont le rôle est de vous aider à acheter moins.</p>
""",

"p.device.h": "Ce qui reste sur votre appareil",
"p.device.b": """
<p>On Ice conserve ce qui suit dans son propre espace privé sur votre iPhone ou votre iPad, protégé par le code et le chiffrement de votre appareil. Rien de tout cela n’est téléversé, synchronisé avec iCloud, sauvegardé par nous ni visible pour nous.</p>
<ul>
  <li><strong>Vos boutiques</strong> — les apps et catégories sous forme de jetons Temps d’écran opaques qu’On Ice ne peut pas lire, et les sites web que vous avez ajoutés par adresse sous forme de cette adresse (voir plus bas).</li>
  <li><strong>Votre liste</strong> — les noms d’articles que vous avez saisis, les prix que vous avez estimés, le ressenti que vous avez sélectionné, et quand chaque article a été noté puis décidé.</li>
  <li><strong>Ce qui s’est passé à chaque écran de blocage</strong> — qu’il a été affiché, quand, et si vous avez renoncé, attendu, ouvert la boutique, laissé partir l’article ou l’avez gardé, et ce que vous avez dit être venu chercher. Vos économies estimées, vos séries et vos habitudes en sont faites.</li>
  <li><strong>Ce que vous ajoutez vous-même</strong> — le journal des dépenses, ce que vous avez ressenti après un achat, votre journal, vos propres rappels, et les choses que vous avez choisi de faire à la place, y compris tout lien d’app ou toute adresse web que vous avez associé à l’une d’elles.</li>
  <li><strong>Vos règles et réglages</strong> — heures sensibles, règles par boutique, votre objectif quotidien et vos limites, blocages, état du mode strict, votre pause, le début de votre journée, votre langue et l’auteur IA que vous avez choisi. Si quelqu’un détient la clé de votre mode strict, seule une empreinte à sens unique salée de son code PIN est stockée, jamais le code PIN lui-même.</li>
  <li><strong>Paliers d’utilisation</strong> — le palier de temps le plus élevé signalé aujourd’hui par iOS pour vos boutiques protégées, pour votre objectif et vos limites (voir plus bas).</li>
  <li><strong>Votre statut Premium</strong> — la formule et la date de son renouvellement ou de sa fin, pour que l’app sache quoi déverrouiller.</li>
  <li><strong>Le dernier bilan hebdomadaire</strong> — uniquement tant que la réflexion IA est activée.</li>
</ul>
<p>Si vous utilisez la sauvegarde iCloud ou une sauvegarde chiffrée sur un ordinateur, Apple peut inclure les données d’On Ice dans cette sauvegarde, sous votre propre compte Apple et selon les conditions de confidentialité d’Apple. Nous n’y avons aucun accès.</p>
""",

"p.journal.h": "Votre journal",
"p.journal.b": """
<p>Le journal est le seul endroit d’On Ice où vous écrivez pour personne. Les entrées — et l’humeur, l’article ou le ressenti qui y est associé — sont stockées sur votre appareil et <strong>ne le quittent jamais</strong> : ni avec la réflexion IA, ni avec OpenAI, quel que soit le réglage.</p>
<ul>
  <li>{K_lock_journal} demande Face ID, Touch ID ou le code de votre appareil avant l’ouverture du journal, et le referme quand vous quittez l’app. C’est iOS qui effectue la vérification ; On Ice ne voit jamais votre visage, votre empreinte digitale ni votre code. Le verrou protège l’écran ; les entrées elles-mêmes sont protégées par le chiffrement propre de votre appareil, comme le reste des données d’On Ice.</li>
  <li>{K_reflect_week} résume vos entrées récentes avec Apple Intelligence, <em>sur votre appareil</em>. Il n’en existe aucune version serveur.</li>
  <li>{K_export_journal} crée un fichier texte brut et le confie à iOS, pour que vous choisissiez où l’enregistrer. On Ice ne l’envoie nulle part.</li>
  <li>Le widget du journal n’affiche que la question du jour. Il ne lit jamais une entrée.</li>
</ul>
""",

"p.permissions.h": "Ce qu’On Ice demande à utiliser",
"p.permissions.b": """
<p>iOS demande chacune de ces autorisations avec ses propres mots, et chacune peut être modifiée à tout moment dans {K_ios_settings}.</p>
<div class="table-wrap"><table>
<tr><th>Autorisation</th><th>Pourquoi</th><th>Nécessaire ?</th></tr>
<tr><td>Temps d’écran</td><td>Pour protéger les boutiques que vous choisissez, appliquer vos blocages, règles et limites, et recevoir les paliers d’utilisation.</td><td>Oui — On Ice ne peut pas fonctionner sans.</td></tr>
<tr><td>Notifications</td><td>Pour vous faire passer de l’écran de blocage à l’app, pour vous dire quand l’attente d’un article est terminée ou presque, et pour les questions de suivi, minuteurs d’activité et suggestions que vous laissez activés.</td><td>Non</td></tr>
<tr><td>Mouvement et forme</td><td>Pour afficher vos pas en direct pendant une marche. Le capteur de mouvement n’est utilisé que lorsqu’une marche est à l’écran, et les pas ne sont jamais stockés ni envoyés.</td><td>Non — seulement si vous démarrez une marche</td></tr>
<tr><td>Face ID ou Touch ID</td><td>Pour déverrouiller le journal, si vous le verrouillez.</td><td>Non</td></tr>
</table></div>
<p>Quand vous choisissez ce qu’ouvre une « chose à faire à la place », On Ice demande à iOS si une courte liste d’apps est installée — Livres, Kindle, Audible, Podcasts, Musique, Spotify, Duolingo, Headspace, Calm, Notes, Messages et Raccourcis — pour pouvoir proposer celles que vous avez. La réponse sert sur le moment à construire cette liste ; elle n’est ni stockée ni envoyée.</p>
""",

"p.screentime.h": "Temps d’écran et vos boutiques",
"p.screentime.b": """
<p>On Ice repose sur le framework Temps d’écran d’Apple (Family Controls, Managed Settings et Device Activity). Vous lui accordez l’accès une fois, via la demande d’Apple elle-même, et pouvez le retirer à tout moment dans {K_ios_settings} → {K_screen_time}.</p>
<p>Quand vous choisissez des apps, des catégories ou des sites web dans le sélecteur d’Apple, celui-ci renvoie des <strong>jetons</strong> : des valeurs qui les identifient auprès d’iOS mais ne signifient rien pour On Ice et rien en dehors de votre appareil. On Ice stocke ces jetons pour pouvoir demander à iOS de protéger ce que vous avez choisi ; iOS affiche pour vous leurs noms et leurs icônes. On Ice ne reçoit jamais d’identifiant de bundle ni de nom d’app. Là où ses propres composants doivent comparer des jetons, ils comparent des empreintes à sens unique de ceux-ci, jamais les jetons eux-mêmes.</p>
<p><strong>Les sites web ajoutés par adresse sont différents.</strong> Un site que vous tapez, ou que vous choisissez parmi les suggestions d’On Ice, est stocké sous forme de cette adresse — <code>example.com</code> — parce qu’iOS en a besoin pour protéger le site. Elle reste sur votre appareil avec tout le reste et n’est jamais envoyée.</p>
<p><strong>L’utilisation est signalée par paliers.</strong> iOS ne donne jamais à On Ice le total de votre temps d’écran. Il indique seulement à On Ice quand le temps passé dans vos boutiques protégées franchit un palier enregistré à l’avance — cinq minutes, dix, quinze… — ce qui suffit pour un objectif quotidien et une limite, et rien de plus.</p>
<p>On Ice n’observe ni votre navigation, ni vos messages, ni ce que vous faites dans une app. C’est iOS lui-même qui affiche l’écran de blocage et l’applique. On Ice apprend seulement que son propre écran de blocage a été affiché et ce que vous y avez choisi.</p>
""",

"p.ai.h": "La réflexion IA — la seule chose qui peut sortir",
"p.ai.b": """
<p class="lead">La réflexion IA est une fonction Premium optionnelle. <strong>Elle est désactivée quand vous installez On Ice et le reste jusqu’à ce que vous l’activiez</strong> dans {K_settings} → {K_ai_reflection}.</p>
<p>Quand elle est activée, certains articles notés reçoivent une courte question avant que vous choisissiez — pas chaque article, seulement lorsqu’il y a une raison : un ressenti qui vous a souvent laissé des regrets, une heure sensible, ou un prix plus élevé. Le dimanche, elle peut aussi écrire quelques phrases sur votre semaine.</p>
<h3>Deux auteurs, et un seul d’entre eux quitte l’appareil</h3>
<ul>
  <li><strong>Apple Intelligence</strong> écrit sur votre appareil. Rien n’est envoyé nulle part. Si Apple Intelligence devient indisponible, On Ice vous montre les choix habituels à la place — <strong>il ne bascule jamais vers un serveur</strong>.</li>
  <li><strong>OpenAI</strong> écrit sur les serveurs d’OpenAI, via le propre service d’On Ice. Seul ce qui est énuméré ci-dessous est envoyé.</li>
</ul>
<p>Vous choisissez sous {K_writer}. Si vous activez la réflexion IA sans choisir, On Ice utilise Apple Intelligence là où votre appareil et votre langue le permettent, et OpenAI là où ce n’est pas le cas.</p>
<h3>Ce qui est envoyé, avec OpenAI comme auteur</h3>
<p>Pour une question :</p>
<ul>
  <li>Le <strong>nom de l’article</strong> que vous venez de saisir, et tout ce que vous écrivez en réponse à la question.</li>
  <li>Une <strong>tranche de prix</strong> — une fourchette comme « 250 à 500 », jamais le montant que vous avez saisi — et votre devise.</li>
  <li>Le <strong>ressenti</strong> que vous avez sélectionné, si vous en avez sélectionné un.</li>
  <li>L’<strong>heure et les minutes</strong> de votre horloge. Ni date, ni fuseau horaire.</li>
  <li><strong>Le nombre d’écrans de blocage d’achat que vous avez rencontrés aujourd’hui.</strong></li>
  <li>Votre propre <strong>taux de regret pour ce seul ressenti</strong>, en pourcentage — seulement une fois que vous avez évalué au moins cinq achats.</li>
  <li>Votre <strong>langue</strong>, par exemple « Français (France) », pour que la question vous revienne dans celle-ci.</li>
</ul>
<p>Pour le bilan hebdomadaire, <strong>uniquement des décomptes et des totaux</strong> : les écrans de blocage rencontrés, les articles mis en attente, laissés partir, gardés ou auxquels vous avez renoncé, le nombre de fois où vous avez ouvert une boutique, votre série actuelle et votre meilleure série, votre heure la plus chargée, la part des articles laissés partir, vos économies estimées de la semaine arrondies à l’unité avec leur devise, la date de début de la semaine, et votre langue. <strong>Aucun nom d’article et aucun prix individuel.</strong></p>
<h3>Ce qui n’est jamais envoyé</h3>
<ul>
  <li>Les jetons Temps d’écran ou leurs empreintes, les identifiants de bundle ou les adresses de sites web.</li>
  <li>Quelles boutiques ou quels sites web vous protégez, ni combien.</li>
  <li>Le prix exact que vous avez saisi.</li>
  <li>Quoi que ce soit d’autre de votre liste — ni noms, ni prix.</li>
  <li>Votre journal des dépenses, ni aucun prix d’achat individuel.</li>
  <li>La façon dont vous avez évalué un achat en particulier.</li>
  <li>Votre journal, vos règles, vos limites, vos blocages, vos heures sensibles ou l’état du mode strict.</li>
  <li>Un nom, un compte, une adresse e-mail ou un identifiant publicitaire — rien qui vous identifie en tant que personne.</li>
</ul>
<h3>Où cela va, et combien de temps c’est conservé</h3>
<p>Les requêtes vont au <strong>propre service d’On Ice, hébergé sur Cloudflare</strong>, puis à <strong>OpenAI</strong>, qui fait tourner le modèle. Il n’y a dans l’app aucune clé d’API à extraire, et l’app n’appelle jamais OpenAI directement.</p>
<p>Avant de répondre, le service utilise <strong>App Attest d’Apple</strong> pour vérifier que la requête provient d’une copie authentique d’On Ice. Cette vérification repose sur une clé créée sur votre appareil — pas sur votre nom ni sur votre compte Apple. <strong>Le service ne stocke aucune question, aucune réponse ni aucun détail d’article.</strong> Il conserve un décompte des requêtes par appareil et par jour, sous cet identifiant de clé aléatoire, et le supprime au bout de deux jours ; des totaux quotidiens de requêtes et d’utilisation du modèle pour l’ensemble du service, qui ne nomment aucun appareil, pendant environ 90 jours ; et une trace de chaque défi App Attest à usage unique jusqu’à son expiration. Ses journaux enregistrent le statut d’une requête, sa durée et le nombre de tokens qu’elle a utilisés — jamais son contenu.</p>
<p><strong>OpenAI n’utilise pas ces données pour entraîner ses modèles.</strong> Nous désactivons le stockage des réponses chez OpenAI ; OpenAI peut néanmoins conserver les entrées et les sorties dans ses journaux de surveillance des abus, normalement jusqu’à 30 jours, avec des exceptions prévues par ses propres conditions. Nous ne promettons pas que votre texte soit traité dans un pays en particulier.</p>
<p><strong>Les versions précédentes d’On Ice</strong> envoient les mêmes types de détails au <strong>modèle Gemini de Google sur Vertex AI</strong> à la place, via un ancien service d’On Ice sur Google Cloud qui ne stocke lui non plus aucun contenu. Google ne les utilise pas pour entraîner ses modèles, peut les conserver jusqu’à 24 heures, et peut les journaliser pour détecter des abus.</p>
<div class="callout"><span class="tile">{sparkle}</span><div>Désactiver la réflexion IA arrête immédiatement toute requête future, supprime le bilan hebdomadaire de votre appareil et retire le rappel du dimanche. On Ice ne fait alors plus aucun appel réseau de lui-même. {K_settings} → {K_ai_reflection} → {K_what_gets_sent} affiche la même liste dans l’app.</div></div>
""",

"p.purchases.h": "Achats et formules famille",
"p.purchases.b": """
<p>Premium est vendu via l’App Store d’Apple avec StoreKit. La transaction est entre vous et Apple, sous la <a href="https://www.apple.com/legal/privacy/">politique de confidentialité d’Apple</a>. Apple indique à On Ice quelle formule est active et quand elle se renouvelle ou prend fin — rien d’autre — et On Ice n’indique rien à Apple sur votre usage de l’app. Nous ne voyons jamais aucune carte.</p>
<p>Avec une <strong>formule famille</strong>, le Partage familial d’Apple donne à chaque membre Premium dans sa propre copie d’On Ice. Rien ne circule entre ces copies — ni boutiques, ni liste, ni journal, ni économies, ni réglages — et On Ice apprend seulement que Premium a été partagé, pas qui l’a partagé.</p>
""",

"p.notifications.h": "Notifications, widgets et écran verrouillé",
"p.notifications.b": """
<p>Les <strong>notifications</strong> sont facultatives et toutes programmées sur votre appareil. Aucune n’est envoyée depuis un serveur, et il n’y a aucun service de notifications push. On Ice les utilise pour vous faire passer de l’écran de blocage à l’app, pour vous dire quand l’attente d’un article est terminée ou presque, pour les questions de suivi que vous pouvez désactiver dans {K_settings} → {K_follow_ups}, pour les minuteurs d’activité et les suggestions que vous choisissez, et — uniquement avec la réflexion IA activée — pour le bilan du dimanche. Une notification concernant un article nomme cet article.</p>
<p>Les <strong>widgets, les Activités en direct et les commandes du centre de contrôle</strong> lisent un petit instantané sur votre appareil : totaux, décomptes, votre série, ainsi que les noms et les échéances de trois articles au plus parmi ceux qui arrivent le plus tôt à terme. Ils n’ont aucun accès à Temps d’écran et ne voient jamais quelles boutiques vous avez choisies. <strong>Le widget « En attente » et l’Activité en direct d’un article affichent le nom de l’article</strong> : sur un écran verrouillé, quiconque tient l’appareil peut donc le lire. Les montants y sont masqués tant que l’appareil est verrouillé. Placez-les là où vous êtes à l’aise de les voir.</p>
""",

"p.third.h": "Tiers",
"p.third.b": """
<p>On Ice ne contient <strong>aucun code tiers</strong> : ni outil d’analyse, ni publicité, ni attribution, ni rapport de plantage, ni SDK. Seules ces parties interviennent, et seulement de la manière décrite ici :</p>
<ul>
  <li><strong>Apple</strong> — exploite l’App Store et le Partage familial, traite les achats, applique l’écran de blocage de Temps d’écran, fait tourner Apple Intelligence sur votre appareil et fournit App Attest. Si vous avez accepté le partage avec les développeurs, Apple peut nous transmettre des rapports de plantage selon sa propre politique.</li>
  <li><strong>Cloudflare</strong> — héberge le service IA d’On Ice. Quand la réflexion IA utilise OpenAI, les requêtes y transitent, et il n’en stocke aucun contenu.</li>
  <li><strong>OpenAI</strong> — fait tourner le modèle derrière les réflexions OpenAI, uniquement tant que cet auteur est utilisé, et ne reçoit que ce qui est énuméré <a href="#ai">plus haut</a>.</li>
  <li><strong>Google Cloud</strong> — joue ce rôle pour les versions précédentes de l’app uniquement.</li>
</ul>
<p>Nous ne vendons, ne louons ni ne partageons de données personnelles avec quiconque, et nous ne partageons rien avec des courtiers en données ou des annonceurs. Un lien que vous associez à une « chose à faire à la place » ouvre l’app ou le site web que vous avez choisi, selon la politique propre de cette app ou de ce site.</p>
""",

"p.delete.h": "Supprimer vos données",
"p.delete.b": """
<p>Tout ce que détient On Ice se trouve sur votre appareil : l’effacer ne nécessite donc pas de nous le demander. Vous pouvez supprimer une à une dans l’app les entrées du journal, les entrées du journal des dépenses, les règles, les limites, les rappels et les activités ; désactiver la réflexion IA supprime le bilan hebdomadaire ; et <strong>supprimer l’app efface tout d’un coup</strong>. Il n’y a dans l’app aucun bouton unique qui efface tout votre historique : supprimer l’app est donc la façon de repartir de zéro. La page <a href="{BASE}{L}/delete-data/">Vos données</a> détaille chaque cas.</p>
<p>De notre côté, il n’y a rien à supprimer : le service IA ne conserve aucun contenu, et son décompte par appareil disparaît de lui-même au bout de deux jours.</p>
""",

"p.rights.h": "Vos droits",
"p.rights.b": """
<p>Où que vous viviez — y compris sous le RGPD (GDPR), le RGPD britannique (UK GDPR) et le CCPA/CPRA — vous avez le droit d’accéder aux données personnelles qu’une entreprise détient sur vous, de les corriger, de les exporter, d’en limiter le traitement, de vous y opposer et de les effacer, ainsi que de saisir une autorité de contrôle. On Ice ne conserve aucun profil de vous sur aucun serveur : il n’y a donc, de notre côté, rien à produire ni à supprimer ; les données sur votre appareil sont déjà entre vos mains. Utiliser les réflexions OpenAI est votre choix, et désactiver la réflexion IA retire ce choix immédiatement. Si vous pensez que nous détenons quelque chose vous concernant, écrivez à {MAIL} et nous vous répondrons.</p>
""",

"p.children.h": "Enfants",
"p.children.b": """
<p>On Ice est un outil autodirigé, destiné à la personne qui utilise l’appareil. Ce n’est pas un produit de contrôle parental et il ne gère pas l’appareil d’une autre personne ; une formule famille partage Premium, jamais le contrôle ni les données. Il ne s’adresse pas aux enfants de moins de 13 ans (ou de l’âge du consentement numérique là où vous vivez), et nous ne collectons sciemment d’informations personnelles de personne, à aucun âge.</p>
""",

"p.changes.h": "Modifications de cette politique",
"p.changes.b": """
<p>Nous pouvons mettre à jour cette politique à mesure que l’app évolue. La date en haut change quand nous le faisons, et les changements importants sont signalés dans les notes de version de l’app. Cette version décrit le choix entre Apple Intelligence et OpenAI pour la réflexion IA, le journal, les pas de marche, les paliers d’utilisation, les formules famille, l’iPad, et sept langues supplémentaires. Continuer à utiliser On Ice après un changement signifie que vous acceptez la politique révisée.</p>
<p>Cette politique est publiée en huit langues. En cas de divergence entre une traduction et la version anglaise, la version anglaise prévaut.</p>
""",

"p.contact.h": "Contact",
"p.contact.b": """
<p>{COMPANY}, l’éditeur d’On Ice, est le responsable du traitement pour tout ce qui est couvert ici. Questions sur la confidentialité : {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Conditions d’utilisation",
"t.h1": "L’accord, en mots simples.",
"t.sub": "Ce que fait On Ice, ce qu’il ne promet pas, pourquoi chaque montant est une estimation, comment Premium et les formules famille sont facturés, et ce que les blocages et le mode strict vous demandent.",
"t.meta": "En vigueur au {DATE} · On Ice par {COMPANY}",

"t.acceptance.h": "1. Acceptation des Conditions",
"t.acceptance.b": """
<p>Les présentes Conditions d’utilisation (« Conditions ») constituent un accord entre vous et {COMPANY} (« nous »), l’éditeur de l’app On Ice pour iPhone et iPad (« On Ice » ou « l’app »). En installant ou en utilisant On Ice, vous acceptez ces Conditions et notre <a href="{BASE}{L}/privacy/">Politique de confidentialité</a>. Si vous n’êtes pas d’accord, n’utilisez pas l’app.</p>
<p>Ces Conditions sont publiées en huit langues. En cas de divergence entre une traduction et la version anglaise, la version anglaise prévaut.</p>
""",

"t.who.h": "2. Qui peut utiliser On Ice",
"t.who.b": """
<p>Vous devez avoir au moins 13 ans, ou l’âge du consentement numérique là où vous vivez, pour utiliser On Ice. On Ice est un outil que vous installez pour vous-même, sur votre propre appareil. Ce n’est pas un produit de contrôle parental et il ne doit pas servir à gérer ni à surveiller l’appareil d’une autre personne. Une formule famille partage Premium avec les membres de votre groupe Partage familial ; elle ne donne à personne le contrôle de l’app On Ice d’un autre membre.</p>
""",

"t.what.h": "3. Ce qu’est On Ice — et ce qu’il n’est pas",
"t.what.b": """
<p>On Ice est un outil autodirigé qui protège les apps et sites d’achat que vous choisissez, propose une courte pause, vous permet de noter ce qui a attiré votre regard, le met en attente pendant une durée que vous fixez, et enregistre sur votre appareil ce que vous avez décidé. Il propose aussi un journal, des choses à faire à la place, des objectifs, des limites et des blocages. Il est conçu pour transformer un achat automatique en une décision que vous prenez vraiment.</p>
<p>On Ice n’est <strong>pas</strong> un service médical, psychologique ou thérapeutique, et rien de ce qu’il contient — y compris les ressentis que vous sélectionnez, les pauses, les rappels, les questions du journal, les analyses ou les textes rédigés par l’IA — ne constitue un conseil, un diagnostic ou un traitement. Si vous êtes aux prises avec des achats compulsifs, des dettes, de l’anxiété ou toute autre chose qui affecte votre bien-être, parlez-en à un professionnel qualifié ou à un service de conseil en endettement. En cas d’urgence, appelez le numéro d’urgence local.</p>
<p>On Ice n’est pas non plus <strong>un produit de sécurité ou de contrôle parental</strong>. Il est conçu pour être exactement aussi ferme que vous le lui demandez : l’app peut être supprimée, l’accès à Temps d’écran peut être retiré dans les Réglages d’iOS, et les écrans de blocage n’existent que tant que l’app est installée et autorisée.</p>
""",

"t.money.h": "4. Des estimations, pas des conseils financiers",
"t.money.b": """
<p>Chaque prix dans On Ice est un montant que <strong>vous</strong> saisissez. L’app ne se connecte à aucune banque, aucun prestataire de paiement ni aucun commerçant, ne lit pas vos transactions ni votre historique de commandes, ne suit pas les prix, ne convertit pas les devises et ne vérifie pas ce que coûte quoi que ce soit.</p>
<p>Le montant d’économies affiché par On Ice est donc une <strong>estimation construite à partir de vos propres suppositions</strong>, et il est présenté comme tel partout où il apparaît. Ce n’est ni une déclaration factuelle sur l’argent dont vous disposez, ni un document financier, ni quoi que ce soit sur lequel vous devriez vous appuyer pour un budget, des impôts, un crédit ou toute autre décision. {COMPANY} n’est pas un conseiller financier, et rien dans l’app ni sur ce site ne constitue un conseil financier, en investissement ou en endettement.</p>
<div class="callout green"><span class="tile">{info}</span><div>On Ice ne contient aucun lien d’affiliation et ne gagne rien sur ce que vous achetez ou n’achetez pas. Son seul revenu est Premium, payé par vous via Apple.</div></div>
""",

"t.screentime.h": "5. Temps d’écran, blocages et mode strict",
"t.screentime.b": """
<p>On Ice s’appuie sur le framework Temps d’écran d’Apple. Apple applique l’écran de blocage ; On Ice le demande. Qu’un écran de blocage apparaisse, à quelle vitesse, qu’un palier d’utilisation soit signalé, et que les écrans de blocage persistent après les redémarrages et les mises à jour d’iOS relève en dernier ressort d’iOS, et nous ne pouvons pas le garantir en toute circonstance. <strong>On Ice ne peut pas empêcher un achat</strong> — il peut seulement placer un écran devant une boutique que vous avez choisie.</p>
<p>Certains outils que vous pouvez activer n’offrent <strong>aucun passage</strong> tant qu’ils sont en cours : une <strong>règle de blocage total</strong> pendant ses heures, une <strong>limite quotidienne</strong> une fois atteinte (jusqu’au début de votre journée suivante), un <strong>blocage programmé</strong> jusqu’à sa fin, et un <strong>blocage par mode de concentration</strong> tant que ce mode de concentration est activé. Un blocage programmé réglé sur {K_only_these} bloque <em>toutes</em> les apps de votre appareil, sauf les apps essentielles que vous avez choisies. Avant d’en démarrer un, assurez-vous de pouvoir accéder à ce dont vous pourriez avoir besoin — pour les appels, les messages, les cartes, les paiements, la santé ou le travail.</p>
<p>Le <strong>mode strict</strong> est un engagement que vous prenez envers vous-même. Tant qu’il tourne, pour la durée que vous avez choisie, la protection reste activée, les règles restent telles quelles, des boutiques peuvent être ajoutées mais pas retirées, et les limites et le début de votre journée ne peuvent pas être modifiés — <em>y compris par vous, et y compris par nous</em>. Nous ne pouvons pas, sur demande, mettre fin par anticipation au mode strict, à un blocage ou à une règle. Si vous avez configuré {K_someone_key}, la personne qui détient le code PIN peut mettre fin au mode strict plus tôt, et vous pouvez demander une sortie différée qui y met fin 24 heures plus tard ; nous ne pouvons pas récupérer un code PIN oublié. Ne prenez pas un engagement que vous n’êtes pas prêt à tenir, et n’en prenez pas sur un appareil auquel vous pourriez avoir besoin d’un accès sans restriction.</p>
<p>Supprimer l’app met fin à tout écran de blocage, blocage et limite, comme décrit à la section 3.</p>
""",

"t.data.h": "6. Vos données et votre appareil",
"t.data.b": """
<p>Tout ce qu’On Ice enregistre est stocké sur votre appareil — voir la <a href="{BASE}{L}/privacy/">Politique de confidentialité</a>. Rien n’est synchronisé entre appareils. Vous êtes responsable de votre appareil, de son code et de ses sauvegardes. Si vous supprimez l’app ou perdez l’appareil sans sauvegarde, votre liste, votre journal, vos règles, votre journal des dépenses et votre historique d’économies sont perdus, et nous n’avons aucune copie à restaurer. Votre achat Premium est distinct : il appartient à votre compte Apple et peut être restauré sur tout iPhone ou iPad connecté à celui-ci.</p>
<p>Ce que vous écrivez dans On Ice vous appartient. Nous ne revendiquons aucun droit dessus et — à l’exception de la réflexion OpenAI optionnelle décrite à la section 8, que vous devez activer vous-même — nous ne le recevons jamais.</p>
""",

"t.subscriptions.h": "7. Premium, abonnements et facturation",
"t.subscriptions.b": """
<p>On Ice est gratuit à télécharger et à utiliser. <strong>On Ice Premium</strong> débloque des fonctions supplémentaires et est vendu sous cinq formes, au prix affiché dans l’app et sur l’App Store de votre pays :</p>
<ul>
  <li><strong>Premium mensuel</strong> — un abonnement à renouvellement automatique, facturé chaque mois.</li>
  <li><strong>Premium annuel</strong> — un abonnement à renouvellement automatique, facturé chaque année, commençant par un <strong>essai gratuit</strong> lorsqu’il est proposé.</li>
  <li><strong>Premium à vie</strong> — un achat unique qui ne se renouvelle pas.</li>
  <li><strong>Premium famille annuel</strong> — un abonnement à renouvellement automatique, facturé chaque année, commençant par un <strong>essai gratuit</strong> lorsqu’il est proposé, pour six personnes maximum via le Partage familial.</li>
  <li><strong>Premium famille à vie</strong> — un achat unique qui ne se renouvelle pas, pour six personnes maximum via le Partage familial.</li>
</ul>
<p>Les deux formules famille sont partagées via le <strong>Partage familial</strong> d’Apple avec jusqu’à cinq autres membres de votre groupe familial. Chacun reçoit Premium dans sa propre copie d’On Ice, sur son propre appareil ; ni les boutiques, ni les listes, ni les journaux, ni les économies, ni les réglages ne sont partagés entre eux. Premium mensuel, Premium annuel et Premium à vie sont réservés à votre usage personnel et ne sont pas partagés.</p>
<p>Le paiement est prélevé sur votre compte Apple à la confirmation de l’achat. Un essai gratuit se transforme en abonnement payant sauf si vous le résiliez au moins 24 heures avant la fin de l’essai. Les abonnements se renouvellent automatiquement au même prix et pour la même période, sauf si le renouvellement automatique est désactivé au moins 24 heures avant la fin de la période en cours ; le renouvellement est facturé dans les 24 heures qui précèdent la fin de cette période. Vous pouvez gérer ou résilier un abonnement dans vos <a href="https://apps.apple.com/account/subscriptions">réglages d’abonnements App Store</a> ; la résiliation prend effet à la fin de la période en cours, et aucun remboursement partiel n’est accordé pour la partie inutilisée d’une période. Acheter une formule à vie, ou recevoir une formule famille, ne résilie pas un abonnement que vous avez déjà — résiliez-le vous-même. Les remboursements sont gérés par Apple selon ses politiques. Utilisez {K_restore} dans l’app pour retrouver Premium sur un nouvel appareil.</p>
<p><strong>Si un abonnement expire</strong>, rien de ce que vous avez déjà construit n’est supprimé : votre liste, votre journal, votre historique et vos économies estimées restent, les boutiques choisies restent protégées, et les règles et limites existantes ainsi qu’un mode strict en cours continuent de s’appliquer. Votre attente revient à 24 heures, la réflexion IA se désactive, et les widgets et les écrans d’habitudes attendent le retour de Premium. Seule la possibilité d’ajouter davantage de fonctions Premium se ferme. L’ensemble des fonctions Premium peut évoluer ; nous ne retirerons pas une fonction d’un abonnement actif sans préavis.</p>
""",

"t.ai.h": "8. La réflexion IA",
"t.ai.b": """
<p>La réflexion IA optionnelle est <strong>désactivée jusqu’à ce que vous l’activiez</strong>. Avec <strong>Apple Intelligence</strong> comme auteur, le texte est généré sur votre appareil selon les conditions d’Apple. Avec <strong>OpenAI</strong> comme auteur, les détails énumérés dans la <a href="{BASE}{L}/privacy/#ai">Politique de confidentialité</a> sont envoyés à notre service puis à OpenAI pour qu’une courte réponse puisse être générée. Les versions précédentes de l’app utilisent à la place le modèle Gemini de Google sur Vertex AI. La fonction {K_reflect_week} du journal utilise uniquement Apple Intelligence, sur votre appareil.</p>
<p>Ce qu’écrit un modèle de langage est un texte généré. Il peut être erroné, générique ou inutile, il ne constitue <strong>aucun conseil d’aucune sorte</strong>, et ce n’est jamais une déclaration factuelle sur votre argent. Ne tapez rien dans cet écran que vous ne voudriez pas voir traité par un modèle tiers. Si une requête échoue, l’app vous montre simplement les choix habituels — rien n’est mis en file d’attente, réessayé plus tard ni stocké. Nous pouvons limiter le nombre de réflexions qu’un appareil peut demander chaque jour.</p>
""",

"t.licence.h": "9. Licence et propriété intellectuelle",
"t.licence.b": """
<p>Nous vous accordons une licence personnelle, non exclusive, non transférable et révocable pour installer et utiliser On Ice sur un iPhone ou un iPad que vous possédez ou contrôlez, conformément à ces Conditions et aux règles d’utilisation de l’App Store. On Ice, son nom, son design, ses illustrations, ses textes et son code appartiennent à {COMPANY} et sont protégés par le droit d’auteur et d’autres lois. Vous ne pouvez pas copier, modifier, distribuer, vendre, louer, désosser ni créer d’œuvres dérivées de l’app, sauf là où la loi l’autorise expressément.</p>
<p>Les noms des commerçants, apps et sites web que vous choisissez de protéger, ou d’ouvrir comme chose à faire à la place, appartiennent à leurs propriétaires respectifs. On Ice n’est affilié à aucun d’entre eux, ni approuvé ou parrainé par l’un d’eux, et ils sont régis par leurs propres conditions.</p>
""",

"t.use.h": "10. Usage acceptable",
"t.use.b": """
<p>Vous vous engagez à ne pas utiliser On Ice d’une manière illicite, qui perturbe l’app, son service IA ou les services d’Apple, qui tente de contourner les mécanismes d’achat de l’App Store ou les limites du service IA, ou qui l’installe sur un appareil que vous n’avez pas le droit de gérer. Vous vous engagez à ne pas l’utiliser pour restreindre ou surveiller une autre personne sans son consentement éclairé, et à ne pas soumettre via la réflexion IA de contenu illicite ou que vous n’avez pas le droit de partager.</p>
""",

"t.termination.h": "11. Résiliation",
"t.termination.b": """
<p>Vous pouvez cesser d’utiliser On Ice à tout moment en le supprimant. Nous pouvons suspendre ou mettre fin à votre licence, ou à votre accès au service IA, en cas de manquement à ces Conditions. Les sections 4, 6, 9, 12, 13 et 15 survivent à la résiliation. Supprimer l’app ne résilie pas un abonnement actif — résiliez-le dans vos réglages App Store.</p>
""",

"t.warranty.h": "12. Garanties et responsabilité",
"t.warranty.b": """
<p>On Ice est fourni « en l’état » et « selon disponibilité », sans garantie d’aucune sorte, expresse ou implicite, notamment qu’il protégera une app ou un site web en toute circonstance, qu’il mesurera l’utilisation avec exactitude, qu’il fonctionnera sans interruption ni erreur, que tout chiffre qu’il affiche est exact, ou qu’il changera vos dépenses. Dans toute la mesure permise par la loi, {COMPANY} ne saurait être tenu responsable de dommages indirects, accessoires, spéciaux, consécutifs ou punitifs, ni d’une perte de données ou d’argent, découlant de votre usage de l’app ou de votre impossibilité de l’utiliser — y compris de tout achat que vous avez fait ou non, de toute conséquence d’un écran de blocage qui est apparu ou non, et de tout blocage, limite ou session de mode strict que vous avez choisi de démarrer. Là où la responsabilité ne peut être exclue, elle est limitée au montant que vous nous avez versé pour Premium au cours des douze mois précédant la réclamation. Rien dans ces Conditions ne limite les droits dont vous disposez en tant que consommateur et auxquels il ne peut être renoncé.</p>
""",

"t.apple.h": "13. Apple",
"t.apple.b": """
<p>On Ice est distribué via l’App Store d’Apple. Ces Conditions sont conclues entre vous et {COMPANY}, et non avec Apple. Apple n’a aucune obligation d’assurer la maintenance ou l’assistance de l’app, et n’est pas responsable du traitement d’une quelconque réclamation la concernant, y compris en matière de responsabilité du fait des produits, de conformité légale ou de propriété intellectuelle. Apple et ses filiales sont tiers bénéficiaires de ces Conditions et peuvent les faire valoir à votre encontre. Là où ces Conditions sont muettes, le <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrat de licence utilisateur final d’application sous licence</a> d’Apple s’applique. Vous déclarez ne pas vous trouver dans un pays soumis à un embargo du gouvernement des États-Unis ni figurer sur une liste de parties interdites, et vous devez respecter toutes conditions tierces applicables lors de l’usage de l’app.</p>
""",

"t.changes.h": "14. Modifications de ces Conditions",
"t.changes.b": """
<p>Nous pouvons mettre à jour ces Conditions de temps à autre. La date en haut changera quand nous le ferons, et les changements importants seront signalés dans les notes de version de l’app. Continuer à utiliser l’app après une mise à jour signifie que vous acceptez les Conditions révisées.</p>
""",

"t.law.h": "15. Droit applicable",
"t.law.b": """
<p>Ces Conditions sont régies par le droit du Pakistan, où {COMPANY} exerce ses activités, sans égard aux règles de conflit de lois. Là où le droit de votre pays de résidence vous accorde des protections auxquelles il ne peut être dérogé par contrat, ces protections s’appliquent.</p>
""",

"t.contact.h": "16. Contact",
"t.contact.b": """
<p>Questions sur ces Conditions : {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Vos données",
"d.h1": "Supprimer vos données",
"d.sub": "Tout ce que sait On Ice est sur votre appareil. Voici comment l’effacer, élément par élément ou d’un seul coup, ce qu’il advient de votre abonnement, et pourquoi il n’y a rien à nous demander de notre côté.",
"d.meta": 'Voir aussi la <a href="{BASE}{L}/privacy/">Politique de confidentialité</a>',

"d.where.h": "Ce qui est stocké, et où",
"d.where.b": """
<p class="lead">On Ice n’a aucun compte et ne conserve de profil de personne sur aucun serveur. Tout ce qu’il détient est sur votre appareil, et vous pouvez l’effacer sans nous le demander.</p>
<div class="table-wrap"><table>
<tr><th>Données</th><th>Où elles se trouvent</th><th>Comment les supprimer</th></tr>
<tr><td>Votre liste, vos décisions, l’historique de vos économies estimées, vos séries et vos habitudes</td><td>L’espace privé de l’app sur votre appareil</td><td>Supprimez l’app. Votre historique est ce dont est fait le total des économies : il n’est donc pas effacé article par article.</td></tr>
<tr><td>Entrées du journal</td><td>Sur votre appareil</td><td>{K_delete_entry} sur n’importe quelle entrée, ou supprimez l’app</td></tr>
<tr><td>Journal des dépenses, règles, limites, rappels, activités</td><td>Sur votre appareil</td><td>Supprimez chaque élément dans l’app, ou supprimez l’app</td></tr>
<tr><td>Vos boutiques</td><td>Jetons Temps d’écran et adresses de sites web sur votre appareil</td><td>Modifiez-les dans l’app ; retirer l’accès à Temps d’écran dans les Réglages d’iOS met aussi fin à tout écran de blocage</td></tr>
<tr><td>Instantané des widgets et des Activités en direct</td><td>Un petit fichier sur votre appareil</td><td>Supprimé avec l’app</td></tr>
<tr><td>Le bilan hebdomadaire</td><td>Sur votre appareil, uniquement tant que la réflexion IA est activée</td><td>Désactivez la réflexion IA</td></tr>
<tr><td>Statut Premium</td><td>Votre compte Apple (Apple), et une copie de son statut sur votre appareil</td><td>Géré dans vos réglages App Store — voir plus bas</td></tr>
<tr><td>Ce qu’une réflexion OpenAI a envoyé</td><td>Pas sur notre service, qui ne conserve aucun contenu. OpenAI peut le conserver dans ses journaux de surveillance des abus, normalement jusqu’à 30 jours (Google, pour les versions précédentes : jusqu’à 24 heures)</td><td>Rien à supprimer de votre part. Désactivez la réflexion IA et plus rien ne sera envoyé</td></tr>
<tr><td>Un décompte des requêtes IA par appareil</td><td>Le service IA d’On Ice, sous un identifiant de clé aléatoire</td><td>Supprimé automatiquement au bout de deux jours</td></tr>
<tr><td>Un compte, un profil, quoi que ce soit à votre nom</td><td>—</td><td>Il n’y en a pas. Nous n’en avons jamais eu à supprimer.</td></tr>
</table></div>
""",

"d.inapp.h": "L’effacer dans l’app",
"d.inapp.b": """
<ul>
  <li><strong>Entrées du journal :</strong> ouvrez une entrée et touchez {K_delete_entry}.</li>
  <li><strong>Journal des dépenses :</strong> touchez {K_remove} sur une entrée.</li>
  <li><strong>Règles, limites, rappels et activités :</strong> chacun a son propre bouton de suppression.</li>
  <li><strong>Boutiques :</strong> modifiez votre sélection, ou désactivez une boutique sur l’écran Accueil. Désactiver la protection retire d’un coup tous les écrans de blocage.</li>
  <li><strong>Les articles décidés restent dans votre historique</strong> — c’est de cela que sont faites vos économies estimées et vos habitudes. Pour effacer cet historique, supprimez l’app.</li>
</ul>
<div class="callout amber"><span class="tile">{lock}</span><div>Tant que le <strong>mode strict</strong> tourne, votre configuration est maintenue en place — les boutiques ne peuvent pas être retirées, et les règles et les limites ne peuvent pas être supprimées. C’est le seul engagement que vous avez demandé à l’app de tenir pour vous. Il se termine tout seul à l’heure que vous avez choisie.</div></div>
""",

"d.journal.h": "Votre journal",
"d.journal.b": """
<p>Les entrées du journal ne se trouvent que sur votre appareil, et On Ice ne les a jamais envoyées nulle part : il n’y a donc rien à supprimer ailleurs. Supprimez-les une par une avec {K_delete_entry}. Pour en garder une copie avant de supprimer l’app, utilisez {K_export_journal} : cela crée un fichier texte brut que vous enregistrez où vous le souhaitez.</p>
""",

"d.ai.h": "La réflexion IA",
"d.ai.b": """
<p>Si vous avez activé la réflexion IA, On Ice garde le dernier bilan hebdomadaire sur votre appareil pour que vous puissiez le relire. Désactiver la réflexion IA dans {K_settings} → {K_ai_reflection} le supprime, retire le rappel du dimanche, met fin à la session de l’app avec le service, et ramène On Ice à ne faire aucun appel réseau de lui-même.</p>
<p>Le service n’a jamais détenu de copie de ce que vous avez envoyé. Il ne conserve qu’un décompte par appareil sous une clé aléatoire, qu’il supprime au bout de deux jours, et des totaux quotidiens qui ne nomment aucun appareil.</p>
""",

"d.uninstall.h": "Supprimer l’app",
"d.uninstall.b": """
<p>Supprimer On Ice de votre iPhone ou de votre iPad emporte avec lui toutes ses données — votre liste, votre historique, votre journal, vos réglages et les jetons Temps d’écran — et met fin immédiatement à tout écran de blocage, blocage et limite. C’est la façon de tout effacer d’un coup. Si l’app est incluse dans une sauvegarde iCloud ou sur ordinateur, cette copie appartient à votre compte Apple et relève des conditions d’Apple ; nous n’y avons aucun accès.</p>
""",

"d.subscription.h": "Votre abonnement",
"d.subscription.b": """
<p>Supprimer l’app ne résilie pas un abonnement — il appartient à votre compte Apple, pas à l’app. Résiliez-le dans les <a href="https://apps.apple.com/account/subscriptions">réglages d’abonnements App Store</a> ; il reste actif jusqu’à la fin de la période en cours. Les remboursements sont gérés par l’<a href="https://support.apple.com/billing">assistance Apple</a>. Un achat à vie ne se renouvelle pas et n’a rien à résilier. Si vous faites partie d’une formule famille, c’est l’acheteur qui la gère.</p>
""",

"d.email.h": "Demandez-nous",
"d.email.b": """
<p>Si vous souhaitez une confirmation écrite que nous ne détenons rien sur vous, ou si vous pensez le contraire, écrivez à {MAIL} depuis n’importe quelle adresse. Nous répondrons sous 30 jours. Merci de ne pas nous envoyer votre liste, vos prix, votre journal ni des captures d’écran de ceux-ci — nous n’en avons pas besoin pour répondre.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Rien en attente ici.",
"nf.sub": "Ce qui, pour une fois, n’est pas le but.",
"nf.cta": "Retour à l’aide",
"nf.b": 'Cette page n’est pas ici. Essayez l’<a href="{BASE}/">aide</a>, la <a href="{BASE}/privacy/">Politique de confidentialité</a> ou les <a href="{BASE}/terms/">Conditions d’utilisation</a>.',

}
