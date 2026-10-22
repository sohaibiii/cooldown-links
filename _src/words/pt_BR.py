# -*- coding: utf-8 -*-
"""Português (Brasil). Trata por “você”, como o próprio app.

Os termos seguem o catálogo do app (Localizable.xcstrings): “bloqueio” para o
shield, “no gelo”, “economia estimada”, “deixar pra lá”, “horários de risco”,
“modo rigoroso”, “janela de compras”, “registro de gastos”, “diário”. Os nomes
dos recursos do iOS são os da própria Apple em português do Brasil: Tempo de
Uso, Ajustes, Conta Apple, Compartilhamento Familiar, Tela de Início, Tela
Bloqueada, Central de Controle, Atividades ao Vivo, Atalhos, Foco e Movimento
e Preparo Físico.
"""

COPY = {

# --- chrome ---------------------------------------------------------------
"nav.support": "Ajuda",
"nav.about": "Sobre",
"nav.privacy": "Privacidade",
"nav.terms": "Termos",
"nav.data": "Seus dados",

"ui.skip": "Ir para o conteúdo",
"ui.pages": "Páginas",
"ui.footer": "Rodapé",
"ui.lang": "Idioma",
"ui.toc": "Nesta página",
"ui.rights": "Todos os direitos reservados.",
"ui.store_soon": "Em breve na App Store",
"ui.store_get": "Baixar na App Store",
"ui.date": "22 de outubro de 2026",
"ui.last_updated": "Última atualização: {DATE}",

# Copiados do Localizable.xcstrings do app e dos rótulos do próprio iOS.
"k.settings": "Ajustes",
"k.ios_settings": "Ajustes",
"k.screen_time": "Tempo de Uso",
"k.apps_with_st": "Apps com Acesso ao Tempo de Uso",
"k.notifications": "Notificações",
"k.restore": "Restaurar compras",
"k.protection_tools": "Ferramentas de proteção",
"k.repair": "Reparar a proteção",
"k.someone_key": "Alguém guarda a chave",
"k.only_these": "Só estes apps",
"k.ai_reflection": "Reflexão com IA",
"k.writer": "Quem escreve a reflexão",
"k.what_gets_sent": "O que é enviado",
"k.lock_journal": "Bloquear diário",
"k.export_journal": "Exportar diário",
"k.delete_entry": "Apagar entrada",
"k.reflect_week": "Refletir sobre minha semana",
"k.help_privacy": "Ajuda e privacidade",
"k.email_support": "Enviar e-mail ao suporte",
"k.language": "Idioma",
"k.note_it": "Anotar",
"k.never_mind": "Deixa pra lá",
"k.need_to_shop": "Preciso fazer compras agora",
"k.done_block": "Terminei — bloqueie de novo",
"k.remove": "Remover",
"k.follow_ups": "Perguntas de acompanhamento",

"meta.support.title": "On Ice — Ajuda",
"meta.support.desc": "A ajuda oficial do On Ice, o app para iPhone e iPad que põe uma noite entre você e o botão de comprar. Como funciona, requisitos, perguntas frequentes e contato.",
"meta.about.title": "On Ice — Uma noite entre você e o botão de comprar",
"meta.about.desc": "O On Ice bloqueia os apps e sites de compras que você escolher e pede que você durma com a ideia primeiro. Sem acesso ao banco, sem rastreamento de preços, sem links de afiliados.",
"meta.privacy.title": "Política de Privacidade — On Ice",
"meta.privacy.desc": "O On Ice não tem conta, nem conexão com o banco, nem análise de uso. O que fica no seu dispositivo, e exatamente o que o único recurso de IA opcional envia.",
"meta.terms.title": "Termos de Uso — On Ice",
"meta.terms.desc": "Termos de Uso (EULA) do On Ice: o que o app é e o que não é, por que todo valor é uma estimativa, como o Premium e os planos familiares são cobrados, e o que o modo rigoroso pede de você.",
"meta.data.title": "Apagar seus dados — On Ice",
"meta.data.desc": "Como remover o que o On Ice guarda — tudo no seu dispositivo — e o que acontece com a sua assinatura.",
"meta.nf.title": "Não encontrado — On Ice",
"meta.nf.desc": "Página não encontrada.",

# --- support --------------------------------------------------------------
"s.eyebrow": "Ajuda",
"s.h1": "Ajuda com o On Ice",
"s.sub": "Uma noite entre você e o botão de comprar. O On Ice bloqueia os apps e sites de compras que você escolheu e pede que você durma com a ideia primeiro. Esta página explica como funciona, do que ele precisa e como falar com a gente.",
"s.cta": "Ler as perguntas frequentes",
"s.meta": 'Sem conta · sem acesso ao banco · <a href="{BASE}{L}/privacy/">Política de Privacidade</a>',

"s.how.h": "Como o On Ice funciona",
"s.how.b": """
<p class="lead">O On Ice põe uma noite entre você e o botão de comprar.</p>
<p>Você escolhe os apps e sites de compras que mais tentam você. Daí em diante, abrir um deles não leva você direto para a finalização da compra — primeiro vem o bloqueio do On Ice: <em>Pause antes de comprar.</em> Toque em {K_note_it} para anotar o que é, ou em {K_never_mind} para ir embora. Nada é comprado nem cancelado em seu nome, nunca.</p>
<p>Tudo o que você anota espera na sua lista — vinte e quatro horas, a menos que você tenha escolhido outra duração. Quando a espera termina, o On Ice faz uma única pergunta: ainda quer? A maioria das vontades não sobrevive à noite, e as que sobrevivem eram de verdade. Qualquer uma das respostas é uma boa resposta.</p>
<ul class="rows">
  <li><span class="tile">{shield}</span><div><b>Proteção</b><span>Um interruptor na tela inicial, e um para cada loja. Enquanto ele estiver ligado, as lojas que você escolheu mostram o bloqueio do On Ice em vez de abrir — o app <em>e</em> o site, no Safari também.</span></div></li>
  <li><span class="tile">{moon}</span><div><b>Uma pausa curta</b><span>Antes de qualquer outra coisa, um momento para respirar, digitar uma frase, ler um lembrete ou dizer o que você veio buscar. Você escolhe qual, e por quanto tempo.</span></div></li>
  <li><span class="tile">{note}</span><div><b>Anotar</b><span>Dê um nome à coisa, toque num preço aproximado, toque em como você se sente — tédio, estresse, comemoração, FOMO de promoção ou “Eu preciso”. Uma tela, quinze segundos.</span></div></li>
  <li><span class="tile amber">{snow}</span><div><b>No gelo</b><span>Os itens anotados esperam sob um anel de contagem regressiva. Nada é comprado enquanto um item esfria. Se você realmente precisar da loja agora, ela abre por alguns minutos e o bloqueio volta sozinho.</span></div></li>
  <li><span class="tile green">{coin}</span><div><b>Economia estimada</b><span>Cada item que você deixa pra lá conta para um total acumulado, feito inteiramente com preços que você mesmo digitou — para hoje, esta semana e este mês.</span></div></li>
  <li><span class="tile amber">{clock}</span><div><b>Metas, limites e bloqueios</b><span>Uma meta diária de tempo para compras, limites diários, bloqueios programados, bloqueios de Foco e regras para os horários mais difíceis. O modo rigoroso mantém a sua configuração no lugar.</span></div></li>
  <li><span class="tile">{book}</span><div><b>Outra coisa para fazer</b><span>Um diário privado, e algumas coisas para fazer no lugar — uma caminhada, um livro, uma ligação — para quando a vontade precisar de um lugar para ir.</span></div></li>
  <li><span class="tile">{widget}</span><div><b>Widgets, Atividades ao Vivo e Atalhos</b><span>A economia estimada e o que está no gelo na Tela de Início e na Tela Bloqueada, uma contagem regressiva enquanto uma loja está aberta, e ações da Siri e de Atalhos para iniciar um bloqueio.</span></div></li>
</ul>
""",

"s.requirements.h": "Requisitos",
"s.requirements.b": """
<div class="table-wrap"><table>
<tr><th>Dispositivo</th><td>iPhone ou iPad com <strong>iOS 17 ou mais recente</strong>. Alguns extras precisam de mais: os controles da Central de Controle precisam do iOS 18, e escrever com o Apple Intelligence exige um dispositivo e um idioma compatíveis.</td></tr>
<tr><th>Permissão</th><td>Acesso ao <strong>Tempo de Uso</strong>, concedido uma vez durante a configuração pela solicitação da própria Apple. O On Ice usa o framework Tempo de Uso da Apple — o mesmo sistema por trás dos limites de apps embutidos no iOS — e é a Apple, não o On Ice, que de fato fica na frente de uma loja.</td></tr>
<tr><th>Conta</th><td>Nenhuma. Não há cadastro, campo de e-mail nem senha em lugar nenhum do app.</td></tr>
<tr><th>Internet</th><td>Não é necessária. Todo bloqueio, pausa, lista, timer e total funciona sem conexão. O único tráfego de rede é o da Apple quando você compra ou restaura o Premium — e a reflexão com IA opcional, se você a ativar com a OpenAI como quem escreve.</td></tr>
<tr><th>Idiomas</th><td>English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil) e 简体中文. O On Ice segue o idioma do seu dispositivo, ou o que você escolher em {K_settings} → {K_language}.</td></tr>
<tr><th>Opcional</th><td><strong>Notificações</strong>, geradas no dispositivo, para levar você do bloqueio até o app e avisar quando a espera de um item terminar. <strong>Movimento e Preparo Físico</strong>, só para mostrar os passos ao vivo durante uma caminhada. <strong>Face ID ou Touch ID</strong>, só se você bloquear o seu diário.</td></tr>
</table></div>
""",

"s.start.h": "Primeiros passos",
"s.start.b": """
<p>A configuração tem poucas telas e termina com a proteção já ligada.</p>
<ol class="steps">
  <li><div><b>Experimente uma pausa de dez segundos</b> — o mesmo momento que o bloqueio vai dar a você depois.</div></li>
  <li><div><b>Permita o acesso ao Tempo de Uso</b> quando a Apple pedir. O On Ice não funciona sem ele, e você pode revogá-lo quando quiser em {K_ios_settings} → {K_screen_time}.</div></li>
  <li><div><b>Escolha as suas lojas</b> no seletor da Apple, e adicione os sites de compras que você quer bloquear. O On Ice nunca fica sabendo os nomes dos apps que você escolhe — veja <a href="{BASE}{L}/privacy/#screentime">Privacidade</a>.</div></li>
  <li><div><b>Defina horários de risco</b> se quiser — as horas da noite em que as compras costumam dar errado. É opcional, e dá para mudar depois.</div></li>
  <li><div><b>Pronto.</b> Abra uma das suas lojas e conheça o bloqueio.</div></li>
</ol>
<div class="callout"><span class="tile">{info}</span><div>O primeiro bloqueio pode parecer abrupto. É para esse momento que o app existe — toque em {K_note_it} e tire quinze segundos.</div></div>
""",

"s.money.h": "Sobre o número da economia",
"s.money.b": """
<p>Todo preço no On Ice é um que você mesmo digitou, e todo valor em dinheiro que o app mostra traz o rótulo <strong>estimado</strong>. Isso não é um aviso colado depois — é o design inteiro.</p>
<ul>
  <li>O On Ice <strong>não se conecta ao seu banco</strong>, não lê o seu histórico de compras, não confere quanto as coisas realmente custam e não converte entre moedas.</li>
  <li>Um item conta para o total <strong>uma vez</strong>, quando você o deixa pra lá depois da espera.</li>
  <li>Se você nunca voltar a um item, o On Ice lembra você e, 48 horas depois de a espera terminar, conta o item como deixado pra lá. Você pode decidir a qualquer momento antes disso.</li>
  <li>Os itens com que você fica não mexem no total — a menos que, depois, você conte ao On Ice que comprou um por menos do que tinha imaginado; nesse caso, a diferença conta.</li>
  <li>O <strong>registro de gastos</strong> é para compras por impulso que o On Ice nunca viu. Ele fica separado da sua economia.</li>
</ul>
<div class="callout green"><span class="tile">{coin}</span><div>O número é um registro do que você decidiu não comprar, pelos preços que você imaginou. É um bom número para se orgulhar e um número ruim para pôr numa planilha.</div></div>
""",

"s.faq.h": "Perguntas frequentes",
"s.faq.b": """
<dl class="faq">
<dt>O On Ice é grátis?</dt>
<dd>Sim, e o grátis é um produto que funciona, não uma demonstração: <strong>um app de compras e um site</strong> bloqueados, a espera de vinte e quatro horas e a sua lista, a sua economia estimada, a pausa de respiração, três coisas para fazer no lugar, o diário, uma meta diária de tempo para compras, e bloqueios programados e de Foco.</dd>
<dt>O que o Premium acrescenta?</dt>
<dd>Todas as lojas e sites que você quiser bloquear; esperas de 12, 24, 48 ou 72 horas; todos os tipos de pausa, pausas que crescem com tentativas repetidas e os seus próprios lembretes; regras de horários de risco e por loja; limites diários; o modo rigoroso; os seus padrões de compra e como você se sentiu com as compras depois; revisitar o seu diário; seis coisas para fazer no lugar; widgets; e a reflexão com IA opcional. O Premium é uma assinatura mensal ou anual — a anual começa com um <strong>teste grátis</strong> quando oferecido — ou uma compra única vitalícia, e as opções anual e vitalícia também existem como <strong>planos familiares</strong>. Os preços aparecem no app para o seu país, e a cobrança é feita pela Apple.</dd>
<dt>Como funcionam os planos familiares?</dt>
<dd>O Premium família anual e o Premium família vitalício são compartilhados pelo Compartilhamento Familiar da Apple com até outras cinco pessoas do seu grupo familiar — seis no total. Cada pessoa recebe o Premium na própria cópia do On Ice, no próprio dispositivo. Ninguém vê as lojas, a lista, o diário ou a economia de mais ninguém.</dd>
<dt>Ele me impede de comprar coisas?</dt>
<dd>Não. Um bloqueio comum é uma pausa, não um muro: toque em {K_note_it}, diga o que chamou a sua atenção, e {K_need_to_shop} abre a loja por alguns minutos. {K_done_block} a fecha de novo antes da hora. As únicas coisas sem passagem são as que você mesmo configura — uma regra de bloqueio total, um limite diário que foi atingido, um bloqueio programado ou um bloqueio de Foco — e cada uma delas termina sozinha.</dd>
<dt>O que acontece se a minha assinatura vencer?</dt>
<dd>Nada do que você construiu é tirado. A sua lista, o histórico e a economia estimada ficam, as lojas que você escolheu continuam bloqueadas, e as suas regras, os seus limites e um modo rigoroso em andamento continuam valendo. O seu tempo de espera volta a 24 horas, a reflexão com IA é desativada, e os widgets e as telas de padrões esperam o Premium voltar. Você só não pode acrescentar mais recursos Premium.</dd>
<dt>Posso restaurar uma compra num aparelho novo?</dt>
<dd>Pode. Abra {K_settings} e toque em {K_restore}. O Premium pertence à sua Conta Apple, não ao aparelho. A sua lista, o diário e o histórico não vão junto — eles ficam no dispositivo que os criou, e só passam para um novo com um backup do dispositivo inteiro.</dd>
<dt>Funciona no iPad?</dt>
<dd>Sim — iPhone e iPad, iOS 17 ou mais recente. Cada dispositivo tem as próprias lojas, lista e histórico; nada é sincronizado entre eles.</dd>
<dt>Por que o On Ice não consegue me dizer quais apps eu protegi?</dt>
<dd>Porque ele realmente não sabe. O Tempo de Uso da Apple entrega ao On Ice tokens opacos que não significam nada fora do seu dispositivo — sem nomes de apps, sem identificadores. O On Ice pode pedir ao iOS que os bloqueie, e o iOS desenha os nomes e os ícones deles para você; o On Ice não consegue lê-los. Os sites que você adiciona digitando um endereço são a exceção: o On Ice guarda esse endereço no seu dispositivo para que o iOS possa bloqueá-lo.</dd>
<dt>Ele bloqueia sites, ou só apps?</dt>
<dd>Os dois. Adicione o app de uma loja e o site dela separadamente, e cada um é bloqueado — o site, no Safari.</dd>
<dt>O On Ice vê o que eu compro?</dt>
<dd>Não. Ele não tem acesso ao seu banco, aos seus pedidos, à sua navegação nem ao seu cartão. Ele registra só os próprios eventos — que um bloqueio foi mostrado, e o que você escolheu — e guarda isso no seu dispositivo.</dd>
<dt>O meu diário sai do meu dispositivo?</dt>
<dd>Nunca. Nem para nós, nem para a OpenAI, com nenhum ajuste. Você pode bloqueá-lo com Face ID, Touch ID ou o seu código, e o resumo semanal opcional dele é escrito pelo Apple Intelligence no seu dispositivo.</dd>
<dt>Para onde vão os meus passos de caminhada?</dt>
<dd>Para lugar nenhum. Durante uma caminhada, o On Ice mostra os seus passos ao vivo e os esquece quando a caminhada termina. Ele não lê nem grava nada no app Saúde da Apple.</dd>
<dt>O que é a reflexão com IA, e ela está ativada?</dt>
<dd>É uma pergunta curta antes das opções, de vez em quando, e algumas frases sobre a sua semana aos domingos. Ela fica <strong>desativada até você ativá-la</strong>. Você escolhe quem escreve: o <strong>Apple Intelligence</strong>, no seu dispositivo, ou a <strong>OpenAI</strong> — a única coisa no app que envia algo para fora do dispositivo. A <a href="{BASE}{L}/privacy/#ai">Política de Privacidade</a> lista exatamente o quê.</dd>
</dl>
""",

"s.trouble.h": "Solução de problemas",
"s.trouble.b": """
<h3>Uma loja abre sem bloqueio</h3>
<ul>
  <li>Confira se a proteção está ligada no topo da tela inicial, e se o interruptor da própria loja está ligado.</li>
  <li>Confira se o acesso ao Tempo de Uso continua concedido: {K_ios_settings} → {K_screen_time} → {K_apps_with_st}. Se ele foi revogado, o On Ice mostra uma tela com um jeito de pedir de novo.</li>
  <li>Uma <strong>janela de compras</strong> que você abriu pode ainda estar valendo. Ela fecha sozinha — ou toque em {K_done_block} — e o bloqueio volta.</li>
  <li>Se a loja só está coberta por uma <strong>regra</strong>, o bloqueio aparece apenas durante os horários dessa regra.</li>
  <li>Ainda nada? {K_settings} → {K_protection_tools} → {K_repair} aplica de novo todos os bloqueios e horários.</li>
</ul>
<h3>Tocar em “Anotar” não abre o On Ice</h3>
<ul>
  <li>Em algumas versões do iOS, o bloqueio passa você para o app por meio de uma notificação. Se as notificações estiverem desligadas, o iOS não consegue entregá-la — ligue-as em {K_ios_settings} → {K_notifications} → On Ice.</li>
  <li>Abrir o On Ice você mesmo recupera o item que estava esperando para ser anotado.</li>
</ul>
<h3>Um site não está bloqueado</h3>
<p>Os sites são bloqueados pelo endereço. Confira se o endereço que você adicionou é o mesmo que você realmente abre, e lembre que o app de uma loja e o site dela são duas coisas separadas para adicionar.</p>
<h3>A minha meta ou o meu limite diário mostra menos minutos do que eu esperava</h3>
<p>O iOS não informa aos apps quanto tempo você passou em outro app. Ele só avisa o On Ice quando o tempo nas suas lojas protegidas passa de uma etapa — a cada cinco minutos, no começo — então o On Ice mostra “pelo menos” essa quantidade de minutos. O número real pode ser um pouco maior.</p>
<h3>Não consigo desligar a proteção nem remover uma loja</h3>
<p>Veja se o <strong>modo rigoroso</strong>, um <strong>bloqueio programado</strong> ou um <strong>bloqueio de Foco</strong> está em andamento — a tela inicial avisa. Enquanto o modo rigoroso está em andamento, a sua configuração fica travada de propósito, e ele termina sozinho no horário que você escolheu. Se você configurou {K_someone_key}, a pessoa com o PIN pode encerrá-lo antes.</p>
<h3>A pergunta da IA nunca aparece</h3>
<p>Ela precisa do Premium, e fica desativada até você ativá-la em {K_settings} → {K_ai_reflection}. Mesmo assim, ela só pergunta quando há um motivo — um sentimento que muitas vezes terminou em arrependimento, um horário de risco ou um preço mais alto. Com a OpenAI como quem escreve, ela precisa de conexão com a internet. Se algo der errado, ela simplesmente mostra as opções comuns em vez disso.</p>
<h3>Os widgets estão atrasados</h3>
<p>O iOS atualiza os widgets no ritmo dele. Abrir o On Ice os coloca em dia. Os widgets de economia e “No gelo” fazem parte do Premium.</p>
<h3>O Premium não é reconhecido</h3>
<p>Toque em {K_restore} em {K_settings}, e confira se o dispositivo está conectado à mesma Conta Apple que fez a compra — ou, num plano familiar, se você está no grupo de Compartilhamento Familiar de quem comprou. Reembolsos e dúvidas de cobrança são tratados pela Apple no <a href="https://support.apple.com/billing">Suporte da Apple</a>.</p>
<h3>O app está no idioma errado</h3>
<p>Escolha um em {K_settings} → {K_language}. O seletor de apps da própria Apple acompanha na próxima vez que você abrir o On Ice.</p>
""",

"s.contact.h": "Contato",
"s.contact.b": """
<p>Dúvidas, um bug, ou algo que deveria funcionar e não funciona — escreva para a gente e uma pessoa vai responder. O jeito mais rápido é {K_settings} → {K_help_privacy} → {K_email_support}, que já inclui para você a versão do On Ice, a versão do iOS e o modelo do aparelho.</p>
<div class="callout"><span class="tile">{mail}</span><div><strong>{MAIL}</strong><br><span class="small">Inclua o modelo do seu aparelho, a versão do iOS e o que você esperava que acontecesse. Nunca nos envie a sua lista, os seus preços ou o seu diário — não precisamos deles e preferimos não guardá-los.</span></div></div>
<p class="small">Cobrança, reembolsos e mudanças de assinatura são tratados pela Apple: <a href="https://apps.apple.com/account/subscriptions">gerenciar assinaturas</a> · <a href="https://support.apple.com/billing">pedir um reembolso</a>.</p>
""",

# --- about ----------------------------------------------------------------
"a.eyebrow": "Sobre o On Ice",
"a.h1": "Uma noite entre você e o botão de comprar.",
"a.sub": "Escolha os apps e sites de compras que mais tentam você. Daí em diante, abrir um deles mostra primeiro um bloqueio — e uma decisão que fica para o seu eu de amanhã.",
"a.cta": "Ajuda",
"a.meta": "Sem conta · sem acesso ao banco · iPhone e iPad, iOS 17+ · 8 idiomas",
"a.lead": "O On Ice põe uma noite entre você e o botão de comprar. Não é uma tranca, nem um sermão — é uma pausa curta, e tempo para descobrir se você queria mesmo. Nada aqui dá bronca em você por querer coisas, e nada fica vermelho se você comprar.",

"a.f1.h": "Pause antes de comprar.",
"a.f1.p": "Abra uma loja que você escolheu e o On Ice aparece antes da finalização da compra — no app e no Safari. Respire fundo, digite uma frase, leia um lembrete ou diga o que você veio buscar.",
"a.f2.h": "Anote, não compre.",
"a.f2.p": "Dê um nome à coisa, toque num preço aproximado, toque em como você se sente. Quinze segundos, uma tela. Anotar tem que ser mais rápido do que a vontade.",
"a.f3.h": "Uma noite no gelo.",
"a.f3.p": "Os itens anotados esperam sob um anel de contagem regressiva — 24 horas, ou qualquer tempo de 12 a 72. Nada é comprado enquanto um item esfria, e a decisão fica para o seu eu de amanhã.",
"a.f4.h": "Veja somar.",
"a.f4.p": "Cada item que você deixa pra lá conta para a sua economia estimada — os seus próprios palpites, para hoje, esta semana e este mês, ao lado dos horários em que você mais esbarra nos bloqueios.",
"a.f5.h": "Outra coisa para fazer.",
"a.f5.p": "Quando a vontade precisa de um lugar para ir: uma caminhada com passos ao vivo, um livro, uma playlist, uma ligação. Escolha o que funciona para você e comece com um toque.",
"a.f6.h": "Mais firme quando você quiser.",
"a.f6.p": "Uma meta diária de tempo para compras, limites diários, bloqueios programados e de Foco, regras de horários de risco para tarde da noite, e o modo rigoroso para manter tudo no lugar.",
"a.f7.h": "Um diário só seu.",
"a.f7.p": "Uma pergunta por dia e um lugar para escrever. Bloqueie com Face ID. Nada do que está nele sai do seu dispositivo, nunca.",
"a.f8.h": "Ele nunca vê o que você compra.",
"a.f8.p": 'Sem conexão com o banco, sem histórico de compras, sem rastreamento de preços, sem links de afiliados, sem análise de uso. A Apple entrega ao On Ice códigos, não nomes. <a href="{BASE}{L}/privacy/">Como isso funciona.</a>',

"a.price.h": "Quanto custa",
"a.price.b": """
<p>O grátis é um produto que funciona, não uma demonstração, e nada do que você já construiu é tirado se uma assinatura vencer.</p>
<div class="tiers">
  <div class="tier"><div class="lbl">Grátis</div><div class="price">Sem custo</div><ul><li>Um app de compras e um site, bloqueados</li><li>A espera de 24 horas e a sua lista</li><li>A sua economia estimada</li><li>A pausa de respiração e três coisas para fazer no lugar</li><li>O diário, uma meta diária, bloqueios programados e de Foco</li></ul></div>
  <div class="tier premium"><div class="lbl">Premium</div><div class="price">Mensal · Anual · Vitalício</div><ul><li>Todas as lojas e sites que você quiser</li><li>Esperas de 12, 24, 48 ou 72 horas</li><li>Todos os tipos de pausa, e os seus próprios lembretes</li><li>Horários de risco, regras por loja, limites diários e modo rigoroso</li><li>Os seus padrões de compra, e como você se sentiu com as compras depois</li><li>Widgets, revisitar o seu diário e a reflexão com IA opcional</li><li>O anual começa com um teste grátis; o anual e o vitalício também existem como planos familiares para até seis pessoas</li></ul></div>
</div>
<p class="small">Os preços aparecem no app e na App Store do seu país. A cobrança é feita pela Apple. <a href="{BASE}{L}/terms/#subscriptions">Termos da assinatura.</a></p>
""",

"a.st.h": "Construído sobre o Tempo de Uso da Apple",
"a.st.b": """
<p>O On Ice usa o mesmo framework que move os limites de apps embutidos no iOS. A Apple só o concede a apps que ela revisou para essa finalidade, e é a Apple — não o On Ice — que de fato fica entre você e a loja. É por isso que o On Ice consegue bloquear um app sem nunca ficar sabendo o nome dele.</p>
<p>iPhone e iPad · iOS 17 ou mais recente · English, Deutsch, Español, Français, 日本語, 한국어, Português (Brasil), 简体中文</p>
""",

"a.est.h": "Todo valor é uma estimativa",
"a.est.b": """
<p>O On Ice pergunta quanto algo custa, mais ou menos, e lembra a sua resposta. Ele não se conecta a nenhum banco, não verifica nenhum preço, não converte nenhuma moeda e não dá nenhuma orientação financeira. Todo número que ele mostra traz a palavra <em class="est">estimado</em> — no app, nos widgets e neste site.</p>
""",

# --- privacy --------------------------------------------------------------
"p.eyebrow": "Política de Privacidade",
"p.h1": "Ele nunca vê o que você compra.",
"p.sub": "Sem conta, sem conexão com o banco, sem histórico de compras, sem rastreamento de preços e sem análise de uso. O que o On Ice sabe fica no seu dispositivo — com um recurso opcional, desativado até você ativá-lo, cujo conteúdo exato está listado abaixo.",
"p.meta": "Em vigor desde {DATE} · vale para o app On Ice para iPhone e iPad, e para este site",

"p.summary.h": "A versão curta",
"p.summary.b": """
<p class="lead"><strong>O On Ice não tem conta, nem análise de uso, nem publicidade, nem código de terceiros.</strong> Não há conexão com o banco, nem histórico de compras, nem rastreamento de preços, nem link de afiliado em lugar nenhum dele. Tudo o que ele sabe é gravado no seu iPhone ou iPad e fica lá.</p>
<div class="callout"><span class="tile">{eye-off}</span><div>Os apps que você escolhe no seletor do Tempo de Uso da Apple chegam ao On Ice como tokens opacos que só o seu dispositivo consegue interpretar. Não há nome de app, nem identificador, nem nada a enviar.</div></div>
<p>Há exatamente uma exceção, e ela fica desativada até você ativá-la: a <strong>reflexão com IA</strong> opcional. Com o <strong>Apple Intelligence</strong> escrevendo, ela roda no seu dispositivo e nada sai. Com a <strong>OpenAI</strong> escrevendo, sai uma lista curta e fixa de informações — listada por completo <a href="#ai">abaixo</a>. O seu diário nunca sai do dispositivo, seja quem for que escreva.</p>
<p>Esta política vale para o app On Ice para iPhone e iPad, publicado pela {COMPANY}, e para este site.</p>
""",

"p.collect.h": "O que coletamos",
"p.collect.b": """
<p>“Coletar”, no sentido da Apple e no nosso, quer dizer enviar dados para fora do dispositivo e guardá-los em algum lugar onde não sejam passageiros. Com a reflexão com IA desativada — que é como toda instalação começa — o On Ice não envia nada sobre você para lugar nenhum. A tabela mostra o que muda se você a ativar com a OpenAI escrevendo.</p>
<div class="table-wrap"><table>
<tr><th>Categoria</th><th>Enviado?</th><th>O que isso quer dizer</th></tr>
<tr><td>Informações financeiras</td><td>Só com as reflexões da OpenAI ativadas</td><td>Sem conexão com o banco, sem cartão, sem acesso a transações, sem histórico de compras. Com as reflexões da OpenAI ativadas, são enviados uma <em>faixa de preço</em> do item que está na sua frente e um total semanal arredondado da economia estimada — nunca um preço exato, uma conta ou um saldo.</td></tr>
<tr><td>Informações de contato</td><td>Não</td><td>Não há conta, login nem campo de e-mail em lugar nenhum do app.</td></tr>
<tr><td>Identificadores</td><td>Só com as reflexões da OpenAI ativadas</td><td>Sem ID de usuário, sem identificador de publicidade, e o On Ice nunca pede para rastrear você. O nosso serviço de IA vê um identificador aleatório de chave do App Attest, usado só para contar as solicitações por dispositivo por dia e apagado depois de dois dias.</td></tr>
<tr><td>Dados de uso</td><td>Só com as reflexões da OpenAI ativadas</td><td>Sem análise de uso e sem eventos de interação com o produto. Bloqueios, pausas e decisões são contados no seu dispositivo, para as suas próprias telas. Uma reflexão leva a contagem de bloqueios de hoje; o resumo semanal leva as contagens da semana.</td></tr>
<tr><td>Conteúdo do usuário</td><td>Só com as reflexões da OpenAI ativadas</td><td>A sua lista, os preços, o diário, o registro de gastos e os lembretes ficam no dispositivo. Com a OpenAI escrevendo, são enviados o nome do item que está na sua frente e o que você digita em resposta à pergunta.</td></tr>
<tr><td>Histórico de navegação</td><td>Não</td><td>O On Ice não consegue ver o que você navega. Ele só fica sabendo que o próprio bloqueio foi mostrado, e o que você escolheu nele.</td></tr>
<tr><td>Localização, saúde, condicionamento físico, contatos, buscas, diagnósticos</td><td>Não</td><td>Os passos durante uma caminhada são mostrados ao vivo e nunca guardados nem enviados. O On Ice não tem relatório próprio de falhas nem de desempenho.</td></tr>
</table></div>
<p><strong>Rastreamento:</strong> nenhum. O On Ice não vincula nada sobre você a dados de apps ou sites de outras empresas, e não compartilha nada com corretores de dados nem anunciantes. Não há <strong>links de afiliados</strong>: o On Ice não ganha nada quando você compra algo, que é o único arranjo compatível com um app cujo trabalho é ajudar você a comprar menos.</p>
""",

"p.device.h": "O que fica no seu dispositivo",
"p.device.b": """
<p>O On Ice guarda o seguinte no próprio armazenamento privado dele no seu iPhone ou iPad, protegido pelo código e pela criptografia do seu dispositivo. Nada disso é enviado, sincronizado com o iCloud, copiado em backup por nós nem fica visível para nós.</p>
<ul>
  <li><strong>As suas lojas</strong> — apps e categorias como tokens opacos do Tempo de Uso que o On Ice não consegue ler, e os sites que você adicionou pelo endereço, como esse endereço (veja abaixo).</li>
  <li><strong>A sua lista</strong> — os nomes dos itens que você digitou, os preços que você estimou, o sentimento que você tocou, e quando cada item foi anotado e decidido.</li>
  <li><strong>O que aconteceu em cada bloqueio</strong> — que ele foi mostrado, quando, e se você foi embora, esperou, abriu a loja, deixou o item pra lá ou ficou com ele, e o que você disse que veio buscar. A sua economia estimada, as sequências e os padrões são feitos disso.</li>
  <li><strong>O que você mesmo acrescenta</strong> — o registro de gastos, como você se sentiu com uma compra depois, o seu diário, os seus próprios lembretes, e as coisas que você escolheu fazer no lugar, incluindo qualquer link de app ou endereço web que você tenha dado a uma delas.</li>
  <li><strong>As suas regras e ajustes</strong> — horários de risco, regras por loja, a sua meta diária e os seus limites, bloqueios, o estado do modo rigoroso, a sua pausa, o início do seu dia, o seu idioma e quem você escolheu para escrever a reflexão com IA. Se alguém guarda a chave do seu modo rigoroso, só um hash unidirecional com salt do PIN dessa pessoa é guardado, nunca o PIN.</li>
  <li><strong>Etapas de uso</strong> — a etapa de tempo mais alta que o iOS informou hoje para as suas lojas protegidas, para a sua meta e os seus limites (veja abaixo).</li>
  <li><strong>O seu status Premium</strong> — o plano e quando ele renova ou termina, para o app saber o que liberar.</li>
  <li><strong>O resumo semanal mais recente</strong> — só enquanto a reflexão com IA estiver ativada.</li>
</ul>
<p>Se você usa o Backup do iCloud ou um backup criptografado num computador, a Apple pode incluir os dados do On Ice nesse backup, sob a sua própria Conta Apple e os termos de privacidade da Apple. Nós não temos acesso a ele.</p>
""",

"p.journal.h": "O seu diário",
"p.journal.b": """
<p>O diário é o único lugar do On Ice em que você escreve para ninguém. As entradas — e o humor, o item ou o sentimento ligado a uma delas — são guardadas no seu dispositivo e <strong>nunca saem dele</strong>: nem com a reflexão com IA, nem com a OpenAI, nem com nenhum ajuste.</p>
<ul>
  <li>A opção {K_lock_journal} pede Face ID, Touch ID ou o código do dispositivo antes de o diário abrir, e o fecha de novo quando você sai do app. Quem faz a verificação é o iOS; o On Ice nunca vê o seu rosto, a sua digital nem o seu código. A trava protege a tela; as entradas em si são protegidas pela própria criptografia do seu dispositivo, como o resto dos dados do On Ice.</li>
  <li>A opção {K_reflect_week} resume as suas entradas recentes com o Apple Intelligence, <em>no seu dispositivo</em>. Não existe versão disso num servidor.</li>
  <li>A opção {K_export_journal} cria um arquivo de texto simples e o entrega ao iOS, para você escolher onde salvá-lo. O On Ice não o envia para lugar nenhum.</li>
  <li>O widget do diário mostra só a pergunta do dia. Ele nunca lê uma entrada.</li>
</ul>
""",

"p.permissions.h": "O que o On Ice pede para usar",
"p.permissions.b": """
<p>O iOS pede cada uma destas permissões com as próprias palavras, e cada uma pode ser alterada em {K_ios_settings} a qualquer momento.</p>
<div class="table-wrap"><table>
<tr><th>Permissão</th><th>Por quê</th><th>Necessária?</th></tr>
<tr><td>Tempo de Uso</td><td>Para bloquear as lojas que você escolhe, executar os seus bloqueios, regras e limites, e receber as etapas de uso.</td><td>Sim — o On Ice não funciona sem ela.</td></tr>
<tr><td>Notificações</td><td>Para levar você do bloqueio até o app, avisar quando a espera de um item terminou ou está perto de terminar, e para perguntas de acompanhamento, timers de atividades e sugestões que você deixar ativados.</td><td>Não</td></tr>
<tr><td>Movimento e Preparo Físico</td><td>Para mostrar os seus passos ao vivo durante uma caminhada. O sensor de movimento só é usado enquanto uma caminhada está na tela, e os passos nunca são guardados nem enviados.</td><td>Não — só se você começar uma caminhada</td></tr>
<tr><td>Face ID ou Touch ID</td><td>Para desbloquear o diário, se você o bloquear.</td><td>Não</td></tr>
</table></div>
<p>Quando você escolhe o que uma “coisa para fazer no lugar” abre, o On Ice pergunta ao iOS se uma lista curta de apps está instalada — Livros, Kindle, Audible, Podcasts, Música, Spotify, Duolingo, Headspace, Calm, Notas, Mensagens e Atalhos — para poder oferecer os que você tem. A resposta é usada na hora para montar essa lista; ela não é guardada nem enviada.</p>
""",

"p.screentime.h": "O Tempo de Uso e as suas lojas",
"p.screentime.b": """
<p>O On Ice é construído sobre o framework Tempo de Uso da Apple (Family Controls, Managed Settings e Device Activity). Você concede o acesso uma vez, pela solicitação da própria Apple, e pode revogá-lo a qualquer momento em {K_ios_settings} → {K_screen_time}.</p>
<p>Quando você escolhe apps, categorias ou sites no seletor da Apple, ele devolve <strong>tokens</strong>: valores que os identificam para o iOS, mas não significam nada para o On Ice nem nada fora do seu dispositivo. O On Ice guarda esses tokens para poder pedir ao iOS que bloqueie o que você escolheu; o iOS desenha os nomes e os ícones deles para você. O On Ice nunca recebe um identificador de pacote nem um nome de app. Onde os próprios componentes dele precisam comparar tokens, eles comparam hashes unidirecionais desses tokens, nunca os tokens em si.</p>
<p><strong>Os sites que você adiciona pelo endereço são diferentes.</strong> Um site que você digita, ou escolhe entre as sugestões do On Ice, é guardado como esse endereço — <code>example.com</code> — porque o iOS precisa dele para bloquear o site. Ele fica no seu dispositivo com todo o resto e nunca é enviado.</p>
<p><strong>O uso é informado em etapas.</strong> O iOS nunca dá ao On Ice um total do seu tempo de tela. Ele só avisa o On Ice quando o tempo nas suas lojas protegidas passa de uma etapa registrada com antecedência — cinco minutos, dez, quinze… — o que basta para uma meta diária e um limite, e nada mais.</p>
<p>O On Ice não observa a sua navegação, as suas mensagens nem o que você faz dentro de nenhum app. É o próprio iOS que desenha o bloqueio e o aplica. O On Ice só fica sabendo que o próprio bloqueio foi mostrado e o que você escolheu nele.</p>
""",

"p.ai.h": "A reflexão com IA — a única coisa que pode sair",
"p.ai.b": """
<p class="lead">A reflexão com IA é um recurso Premium opcional. <strong>Ela vem desativada quando você instala o On Ice e continua desativada até você ativá-la</strong> em {K_settings} → {K_ai_reflection}.</p>
<p>Com ela ativada, alguns itens anotados recebem uma pergunta curta antes de você escolher — não todos os itens, só quando há um motivo: um sentimento que muitas vezes terminou em arrependimento, um horário de risco ou um preço mais alto. Aos domingos, ela também pode escrever algumas frases sobre a sua semana.</p>
<h3>Duas opções para escrever, e só uma delas sai do dispositivo</h3>
<ul>
  <li>O <strong>Apple Intelligence</strong> escreve no seu dispositivo. Nada é enviado para lugar nenhum. Se o Apple Intelligence ficar indisponível, o On Ice mostra as opções comuns em vez disso — <strong>ele nunca recorre a um servidor</strong>.</li>
  <li>A <strong>OpenAI</strong> escreve nos servidores da OpenAI, por meio do próprio serviço do On Ice. Só o que está listado abaixo é enviado.</li>
</ul>
<p>Você escolhe em {K_writer}. Se você ativar a reflexão com IA sem escolher, o On Ice usa o Apple Intelligence onde o seu dispositivo e o seu idioma são compatíveis, e a OpenAI onde não são.</p>
<h3>O que é enviado, com a OpenAI escrevendo</h3>
<p>Para uma pergunta:</p>
<ul>
  <li>O <strong>nome do item</strong> que você acabou de digitar, e qualquer coisa que você escreva em resposta à pergunta.</li>
  <li>Uma <strong>faixa de preço</strong> — um intervalo como “250 a 500”, nunca o valor que você digitou — e a sua moeda.</li>
  <li>O <strong>sentimento</strong> que você tocou, se tocou em algum.</li>
  <li>A <strong>hora e os minutos</strong> do seu relógio. Sem data, sem fuso horário.</li>
  <li><strong>Quantas vezes você encontrou um bloqueio de compras hoje.</strong></li>
  <li>A sua própria <strong>taxa de arrependimento para aquele sentimento</strong>, em porcentagem — só depois que você tiver avaliado pelo menos cinco compras.</li>
  <li>O seu <strong>idioma</strong>, como “Português (Brasil)”, para que a pergunta volte nele.</li>
</ul>
<p>Para o resumo semanal, <strong>só contagens e totais</strong>: bloqueios encontrados; itens postos no gelo, deixados pra lá, mantidos ou a que você resistiu; quantas vezes você abriu uma loja; a sua sequência atual e a melhor; o seu horário de maior movimento; a proporção de itens que você deixou pra lá; a sua economia estimada da semana, arredondada para um número inteiro, com a moeda; a data em que a semana começou; e o seu idioma. <strong>Nenhum nome de item e nenhum preço individual.</strong></p>
<h3>O que nunca é enviado</h3>
<ul>
  <li>Tokens do Tempo de Uso ou os hashes deles, identificadores de pacote ou endereços de sites.</li>
  <li>Quais lojas ou sites você protege, nem quantos.</li>
  <li>O preço exato que você digitou.</li>
  <li>Nada mais da sua lista — nem nomes, nem preços.</li>
  <li>O seu registro de gastos, nem o preço de qualquer compra individual.</li>
  <li>Como você avaliou qualquer compra individual.</li>
  <li>O seu diário, regras, limites, bloqueios, horários de risco ou o estado do modo rigoroso.</li>
  <li>Nenhum nome, conta, e-mail ou identificador de publicidade — nada que identifique você como pessoa.</li>
</ul>
<h3>Para onde vai, e por quanto tempo fica guardado</h3>
<p>As solicitações vão para o <strong>próprio serviço do On Ice, hospedado na Cloudflare</strong>, e de lá para a <strong>OpenAI</strong>, que roda o modelo. Não existe chave de API dentro do app para ser extraída, e o app nunca chama a OpenAI diretamente.</p>
<p>Antes de responder, o serviço usa o <strong>App Attest da Apple</strong> para verificar se a solicitação vem de uma cópia legítima do On Ice. Essa verificação se apoia numa chave criada no seu dispositivo — não no seu nome nem na sua Conta Apple. <strong>O serviço não guarda nenhuma pergunta, resposta ou detalhe de item.</strong> Ele mantém uma contagem de solicitações por dispositivo por dia, sob esse identificador aleatório de chave, e a apaga depois de dois dias; totais diários de solicitações e de uso do modelo para o serviço inteiro, que não nomeiam nenhum dispositivo, por cerca de 90 dias; e um registro de cada desafio único do App Attest até ele expirar. Os registros do serviço anotam o status de uma solicitação, quanto tempo ela levou e quantos tokens usou — nunca o conteúdo.</p>
<p><strong>A OpenAI não usa esses dados para treinar os modelos dela.</strong> Desativamos o armazenamento de respostas da OpenAI; a OpenAI ainda pode manter entradas e saídas nos registros de monitoramento de abuso dela, normalmente por até 30 dias, com exceções previstas nos termos dela. Não prometemos que o seu texto seja processado em nenhum país em particular.</p>
<p><strong>As versões anteriores do On Ice</strong> enviam os mesmos tipos de informação para o <strong>modelo Gemini do Google na Vertex AI</strong>, por meio de um serviço anterior do On Ice no Google Cloud que também não guarda nenhum conteúdo. O Google não os usa para treinar os modelos dele, pode mantê-los por até 24 horas e pode registrá-los para verificar abusos.</p>
<div class="callout"><span class="tile">{sparkle}</span><div>Desativar a reflexão com IA interrompe na hora todas as solicitações futuras, apaga o resumo semanal do seu dispositivo e remove o lembrete de domingo. O On Ice volta a não fazer nenhuma conexão de rede própria. {K_settings} → {K_ai_reflection} → {K_what_gets_sent} mostra a mesma lista dentro do app.</div></div>
""",

"p.purchases.h": "Compras e planos familiares",
"p.purchases.b": """
<p>O Premium é vendido pela App Store da Apple usando o StoreKit. A transação é entre você e a Apple, sob a <a href="https://www.apple.com/legal/privacy/">política de privacidade da Apple</a>. A Apple informa ao On Ice qual plano está ativo e quando ele renova ou termina — nada além disso — e o On Ice não informa nada à Apple sobre como você usa o app. Nós nunca vemos um cartão.</p>
<p>Com um <strong>plano familiar</strong>, o Compartilhamento Familiar da Apple dá a cada membro o Premium na própria cópia do On Ice. Nada passa entre essas cópias — nem lojas, nem lista, nem diário, nem economia, nem ajustes — e o On Ice só fica sabendo que o Premium foi compartilhado, não quem o compartilhou.</p>
""",

"p.notifications.h": "Notificações, widgets e a Tela Bloqueada",
"p.notifications.b": """
<p>As <strong>notificações</strong> são opcionais e todas são agendadas no seu dispositivo. Nenhuma é enviada de um servidor, e não existe serviço de push. O On Ice as usa para levar você do bloqueio até o app, para avisar quando a espera de um item terminou ou está perto de terminar, para perguntas de acompanhamento que você pode desligar em {K_settings} → {K_follow_ups}, para timers de atividades e sugestões que você escolher, e — só com a reflexão com IA ativada — para o resumo de domingo. Uma notificação sobre um item diz o nome do item.</p>
<p><strong>Os widgets, as Atividades ao Vivo e os controles da Central de Controle</strong> leem um pequeno instantâneo no seu dispositivo: totais, contagens, a sua sequência, e os nomes e horários de até três dos itens cuja espera termina primeiro. Eles não têm acesso ao Tempo de Uso e nunca veem quais lojas você escolheu. <strong>O widget “No gelo” e a Atividade ao Vivo de um item mostram o nome do item</strong>, então, numa Tela Bloqueada, qualquer pessoa que esteja segurando o aparelho pode lê-lo. Os valores em dinheiro ficam ocultos ali enquanto o aparelho está bloqueado. Coloque-os onde você se sinta à vontade para vê-los.</p>
""",

"p.third.h": "Terceiros",
"p.third.b": """
<p>O On Ice não contém <strong>código de terceiros</strong>: nem análise de uso, nem publicidade, nem atribuição, nem relatório de falhas, nem SDKs. Só estas partes estão envolvidas, e só da forma descrita aqui:</p>
<ul>
  <li><strong>Apple</strong> — opera a App Store e o Compartilhamento Familiar, processa as compras, aplica o bloqueio do Tempo de Uso, roda o Apple Intelligence no seu dispositivo e fornece o App Attest. Se você aceitou compartilhar com os desenvolvedores, a Apple pode compartilhar conosco registros de falhas sob a política dela.</li>
  <li><strong>Cloudflare</strong> — hospeda o serviço de IA do On Ice. Quando a reflexão com IA usa a OpenAI, as solicitações passam por ela, e ela não guarda nada do conteúdo delas.</li>
  <li><strong>OpenAI</strong> — roda o modelo por trás das reflexões da OpenAI, só enquanto essa opção de escrita estiver em uso, e recebe só o que está listado <a href="#ai">acima</a>.</li>
  <li><strong>Google Cloud</strong> — tem esse papel apenas nas versões anteriores do app.</li>
</ul>
<p>Não vendemos, alugamos nem compartilhamos dados pessoais com ninguém, e não compartilhamos nada com corretores de dados nem anunciantes. Um link que você dá a uma “coisa para fazer no lugar” abre o app ou o site que você escolheu, sob a política própria desse app ou site.</p>
""",

"p.delete.h": "Apagar os seus dados",
"p.delete.b": """
<p>Tudo o que o On Ice guarda está no seu dispositivo, então removê-lo não exige pedir nada para a gente. Você pode apagar entradas do diário, entradas do registro de gastos, regras, limites, lembretes e atividades um por um no app; desativar a reflexão com IA apaga o resumo semanal; e <strong>apagar o app remove tudo de uma vez</strong>. Não há um único botão dentro do app que apague todo o seu histórico, então apagar o app é o jeito de começar do zero. A página <a href="{BASE}{L}/delete-data/">Seus dados</a> explica cada um.</p>
<p>Do nosso lado não há nada a apagar: o serviço de IA não guarda nenhum conteúdo, e a contagem por dispositivo some sozinha depois de dois dias.</p>
""",

"p.rights.h": "Os seus direitos",
"p.rights.b": """
<p>Onde quer que você more — inclusive sob o GDPR, o GDPR do Reino Unido e a CCPA/CPRA — você tem direito de acessar, corrigir, exportar e apagar os dados pessoais que uma empresa tem sobre você, de restringir o tratamento deles e de se opor a ele, e de reclamar a uma autoridade supervisora. O On Ice não mantém nenhum perfil seu em nenhum servidor, então do nosso lado não há nada a produzir nem a apagar; os dados no seu dispositivo já estão nas suas mãos. Usar as reflexões da OpenAI é escolha sua, e desativar a reflexão com IA retira essa escolha na hora. Se você acredita que temos algo sobre você, escreva para {MAIL} e responderemos.</p>
""",

"p.children.h": "Crianças",
"p.children.b": """
<p>O On Ice é uma ferramenta autodirigida para a pessoa que usa o dispositivo. Não é um produto de controle parental e não gerencia o dispositivo de outra pessoa; um plano familiar compartilha o Premium, nunca o controle nem os dados. Ele não é dirigido a crianças menores de 13 anos (ou da idade de consentimento digital onde você mora), e não coletamos conscientemente informações pessoais de ninguém, de nenhuma idade.</p>
""",

"p.changes.h": "Mudanças nesta política",
"p.changes.b": """
<p>Podemos atualizar esta política conforme o app muda. A data no topo muda quando isso acontece, e as mudanças relevantes são anotadas nas notas de versão do app. Esta versão descreve a escolha entre o Apple Intelligence e a OpenAI para a reflexão com IA, o diário, os passos de caminhada, as etapas de uso, os planos familiares, o iPad e mais sete idiomas. Continuar usando o On Ice depois de uma mudança significa que você aceita a política revisada.</p>
<p>Esta política é publicada em oito idiomas. Se uma tradução e o inglês divergirem, vale o inglês.</p>
""",

"p.contact.h": "Contato",
"p.contact.b": """
<p>A {COMPANY}, editora do On Ice, é a controladora de tudo o que está tratado aqui. Dúvidas sobre privacidade: {MAIL}.</p>
""",

# --- terms ----------------------------------------------------------------
"t.eyebrow": "Termos de Uso",
"t.h1": "O acordo, em palavras claras.",
"t.sub": "O que o On Ice faz, o que ele não promete, por que todo valor é uma estimativa, como o Premium e os planos familiares são cobrados, e o que os bloqueios e o modo rigoroso pedem de você.",
"t.meta": "Em vigor desde {DATE} · On Ice, da {COMPANY}",

"t.acceptance.h": "1. Aceitação dos Termos",
"t.acceptance.b": """
<p>Estes Termos de Uso (“Termos”) são um acordo entre você e a {COMPANY} (“nós”), editora do app On Ice para iPhone e iPad (“On Ice” ou “o app”). Ao instalar ou usar o On Ice, você aceita estes Termos e a nossa <a href="{BASE}{L}/privacy/">Política de Privacidade</a>. Se não concordar, não use o app.</p>
<p>Estes Termos são publicados em oito idiomas. Se uma tradução e o inglês divergirem, vale o inglês.</p>
""",

"t.who.h": "2. Quem pode usar o On Ice",
"t.who.b": """
<p>Você precisa ter pelo menos 13 anos, ou a idade de consentimento digital onde mora, para usar o On Ice. O On Ice é uma ferramenta que você instala para si mesmo, no seu próprio dispositivo. Não é um produto de controle parental e não deve ser usado para gerenciar nem monitorar o dispositivo de outra pessoa. Um plano familiar compartilha o Premium com membros do seu grupo de Compartilhamento Familiar; ele não dá a ninguém controle sobre o On Ice de outro membro.</p>
""",

"t.what.h": "3. O que o On Ice é — e o que não é",
"t.what.b": """
<p>O On Ice é uma ferramenta autodirigida que bloqueia os apps e sites de compras que você escolhe, oferece uma pausa curta, deixa você anotar o que chamou a sua atenção, guarda isso por um período que você define e registra no seu dispositivo o que você decidiu. Ele também oferece um diário, coisas para fazer no lugar, metas, limites e bloqueios. Ele foi feito para transformar uma compra automática numa decisão que você realmente toma.</p>
<p>O On Ice <strong>não</strong> é um serviço médico, psicológico ou terapêutico, e nada nele — incluindo os sentimentos que você toca, as pausas, os lembretes, as perguntas do diário, as análises ou os textos escritos por IA — é orientação, diagnóstico ou tratamento. Se você está lidando com gastos compulsivos, dívidas, ansiedade ou qualquer outra coisa que afete o seu bem-estar, por favor, converse com um profissional qualificado ou com um serviço de orientação sobre dívidas. Numa emergência, ligue para o número de emergência da sua região.</p>
<p>O On Ice também <strong>não é um produto de segurança nem de controle parental</strong>. Ele foi feito para ser exatamente tão firme quanto você pedir: o app pode ser apagado, o acesso ao Tempo de Uso pode ser revogado nos Ajustes do iOS, e os bloqueios só existem enquanto o app estiver instalado e autorizado.</p>
""",

"t.money.h": "4. Estimativas, não orientação financeira",
"t.money.b": """
<p>Todo preço no On Ice é um valor que <strong>você</strong> insere. O app não se conecta a nenhum banco, provedor de pagamentos ou varejista, não lê as suas transações nem o seu histórico de pedidos, não rastreia preços, não converte moedas e não verifica quanto nada custa.</p>
<p>O valor de economia que o On Ice mostra é, portanto, uma <strong>estimativa montada a partir dos seus próprios palpites</strong>, e traz esse rótulo em todo lugar onde aparece. Ele não é uma declaração de fato sobre dinheiro que você tem, nem um registro financeiro, nem algo em que você deva se apoiar para orçamento, impostos, crédito ou qualquer outra decisão. A {COMPANY} não é consultora financeira, e nada no app nem neste site é orientação financeira, de investimento ou sobre dívidas.</p>
<div class="callout green"><span class="tile">{info}</span><div>O On Ice não tem links de afiliados e não ganha nada com o que você compra ou deixa de comprar. A única receita dele é o Premium, pago por você pela Apple.</div></div>
""",

"t.screentime.h": "5. Tempo de Uso, bloqueios e modo rigoroso",
"t.screentime.b": """
<p>O On Ice depende do framework Tempo de Uso da Apple. A Apple aplica o bloqueio; o On Ice pede por ele. Se um bloqueio aparece, com que rapidez, se uma etapa de uso é informada, e se os bloqueios se mantêm após reinícios e atualizações do iOS é, em última instância, determinado pelo iOS, e não podemos garantir isso em toda circunstância. <strong>O On Ice não consegue impedir uma compra</strong> — ele só consegue pôr uma tela na frente de uma loja que você escolheu.</p>
<p>Algumas ferramentas que você pode ativar <strong>não oferecem passagem</strong> enquanto estão em andamento: uma <strong>regra de bloqueio total</strong> durante os seus horários, um <strong>limite diário</strong> depois de atingido (até o seu próximo dia começar), um <strong>bloqueio programado</strong> até terminar, e um <strong>bloqueio de Foco</strong> enquanto esse Foco estiver ativado. Um bloqueio programado definido como {K_only_these} bloqueia <em>todos</em> os apps do seu dispositivo, exceto os apps essenciais que você escolheu. Antes de começar um, confira se você consegue acessar o que pode precisar — para ligações, mensagens, mapas, pagamentos, saúde ou trabalho.</p>
<p>O <strong>modo rigoroso</strong> é um compromisso que você assume consigo mesmo. Enquanto ele está em andamento, pelo tempo que você escolheu, a proteção continua ligada, as regras ficam como estão, lojas podem ser adicionadas mas não removidas, e os limites e o início do seu dia não podem ser alterados — <em>nem por você, nem por nós</em>. Não conseguimos encerrar antes da hora o modo rigoroso, um bloqueio ou uma regra a pedido. Se você configurou {K_someone_key}, a pessoa que guarda o PIN pode encerrar o modo rigoroso antes da hora, e você pode solicitar uma saída com espera, que o encerra 24 horas depois; não conseguimos recuperar um PIN esquecido. Não comece um compromisso que você não esteja disposto a cumprir, e não comece um num dispositivo ao qual você possa precisar de acesso irrestrito.</p>
<p>Apagar o app encerra todos os bloqueios e limites, como descrito na seção 3.</p>
""",

"t.data.h": "6. Os seus dados e o seu dispositivo",
"t.data.b": """
<p>Tudo o que o On Ice registra é guardado no seu dispositivo — veja a <a href="{BASE}{L}/privacy/">Política de Privacidade</a>. Nada é sincronizado entre dispositivos. Você é responsável pelo seu dispositivo, pelo código dele e pelos backups dele. Se você apagar o app ou perder o dispositivo sem um backup, a sua lista, o diário, as regras, o registro de gastos e o histórico de economia se perdem, e não temos cópia para restaurar. A sua compra do Premium é à parte: ela pertence à sua Conta Apple e pode ser restaurada em qualquer iPhone ou iPad conectado a ela.</p>
<p>O que você escreve no On Ice é seu. Não reivindicamos nenhum direito sobre isso e — exceto pela reflexão opcional com a OpenAI, na seção 8, que você mesmo precisa ativar — nunca o recebemos.</p>
""",

"t.subscriptions.h": "7. Premium, assinaturas e cobrança",
"t.subscriptions.b": """
<p>O On Ice é grátis para baixar e usar. O <strong>On Ice Premium</strong> libera recursos adicionais e é vendido em cinco formas, pelo preço mostrado no app e na App Store do seu país:</p>
<ul>
  <li><strong>Premium mensal</strong> — uma assinatura de renovação automática, cobrada por mês.</li>
  <li><strong>Premium anual</strong> — uma assinatura de renovação automática, cobrada por ano, que começa com um <strong>teste grátis</strong> quando oferecido.</li>
  <li><strong>Premium vitalício</strong> — uma compra única que não se renova.</li>
  <li><strong>Premium família anual</strong> — uma assinatura de renovação automática, cobrada por ano, que começa com um <strong>teste grátis</strong> quando oferecido, para até seis pessoas pelo Compartilhamento Familiar.</li>
  <li><strong>Premium família vitalício</strong> — uma compra única que não se renova, para até seis pessoas pelo Compartilhamento Familiar.</li>
</ul>
<p>Os dois planos familiares são compartilhados pelo <strong>Compartilhamento Familiar</strong> da Apple com até outros cinco membros do seu grupo familiar. Cada pessoa recebe o Premium na própria cópia do On Ice, no próprio dispositivo; nenhuma loja, lista, diário, economia ou ajuste é compartilhado entre elas. O mensal, o anual e o vitalício são só para você e não são compartilhados.</p>
<p>O pagamento é cobrado da sua Conta Apple na confirmação da compra. Um teste grátis vira uma assinatura paga, a menos que você cancele pelo menos 24 horas antes de o teste acabar. As assinaturas se renovam automaticamente pelo mesmo preço e período, a menos que a renovação automática seja desativada pelo menos 24 horas antes do fim do período atual; a renovação é cobrada nas 24 horas anteriores ao fim desse período. Você pode gerenciar ou cancelar uma assinatura nos <a href="https://apps.apple.com/account/subscriptions">ajustes de assinatura da App Store</a>; o cancelamento vale a partir do fim do período atual, e não há reembolso parcial pela parte não usada de um período. Comprar um plano vitalício, ou receber um plano familiar, não cancela uma assinatura que você já tenha — cancele-a você mesmo. Os reembolsos são tratados pela Apple, sob as políticas da Apple. Use {K_restore} no app para recuperar o Premium num dispositivo novo.</p>
<p><strong>Se uma assinatura vencer</strong>, nada do que você já construiu é removido: a sua lista, o diário, o histórico e a economia estimada ficam, as lojas que você escolheu continuam bloqueadas, e as regras e os limites existentes e um modo rigoroso em andamento continuam valendo. O seu tempo de espera volta a 24 horas, a reflexão com IA é desativada, e os widgets e as telas de padrões esperam o Premium voltar. Só a possibilidade de acrescentar mais recursos Premium se fecha. O conjunto de recursos Premium pode mudar com o tempo; não vamos remover um recurso de uma assinatura ativa sem aviso.</p>
""",

"t.ai.h": "8. A reflexão com IA",
"t.ai.b": """
<p>A reflexão com IA opcional fica <strong>desativada até você ativá-la</strong>. Com o <strong>Apple Intelligence</strong> escrevendo, o texto é gerado no seu dispositivo, sob os termos da Apple. Com a <strong>OpenAI</strong> escrevendo, as informações listadas na <a href="{BASE}{L}/privacy/#ai">Política de Privacidade</a> são enviadas ao nosso serviço e de lá à OpenAI, para que uma resposta curta possa ser gerada. As versões anteriores do app usam para isso o modelo Gemini do Google na Vertex AI. A opção {K_reflect_week} do diário usa apenas o Apple Intelligence no seu dispositivo.</p>
<p>O que um modelo de linguagem escreve é texto gerado. Ele pode estar errado, ser genérico ou pouco útil, <strong>não é orientação de espécie alguma</strong> e nunca é uma declaração de fato sobre o seu dinheiro. Não digite naquela tela nada que você não queira que seja processado por um modelo de terceiros. Se uma solicitação falhar, o app simplesmente mostra as opções comuns — nada fica na fila, é tentado de novo depois ou é guardado. Podemos limitar quantas reflexões um dispositivo pode solicitar por dia.</p>
""",

"t.licence.h": "9. Licença e propriedade intelectual",
"t.licence.b": """
<p>Concedemos a você uma licença pessoal, não exclusiva, intransferível e revogável para instalar e usar o On Ice num iPhone ou iPad que você possua ou controle, de acordo com estes Termos e as regras de uso da App Store. O On Ice, o seu nome, design, ilustrações, textos e código pertencem à {COMPANY} e são protegidos por direitos autorais e outras leis. Você não pode copiar, modificar, distribuir, vender, arrendar, fazer engenharia reversa nem criar obras derivadas do app, exceto onde a lei expressamente permitir.</p>
<p>Os nomes de varejistas, apps e sites que você escolhe bloquear, ou abrir como uma coisa para fazer no lugar, pertencem aos respectivos donos. O On Ice não é afiliado a nenhum deles, nem endossado ou patrocinado por eles, e eles são regidos pelos próprios termos.</p>
""",

"t.use.h": "10. Uso aceitável",
"t.use.b": """
<p>Você concorda em não usar o On Ice de nenhuma forma que seja ilegal, que interfira no app, no serviço de IA dele ou nos serviços da Apple, que tente contornar os mecanismos de compra da App Store ou os limites do serviço de IA, ou que o instale num dispositivo que você não tenha direito de gerenciar. Você concorda em não usá-lo para restringir ou monitorar outra pessoa sem o consentimento informado dela, e em não enviar pela reflexão com IA conteúdo que seja ilegal ou que você não tenha direito de compartilhar.</p>
""",

"t.termination.h": "11. Encerramento",
"t.termination.b": """
<p>Você pode parar de usar o On Ice a qualquer momento apagando-o. Podemos suspender ou encerrar a sua licença, ou o seu acesso ao serviço de IA, se você descumprir estes Termos. As seções 4, 6, 9, 12, 13 e 15 continuam valendo após o encerramento. Apagar o app não cancela uma assinatura ativa — cancele-a nos ajustes da App Store.</p>
""",

"t.warranty.h": "12. Garantias e responsabilidade",
"t.warranty.b": """
<p>O On Ice é fornecido “no estado em que se encontra” e “conforme disponível”, sem garantias de espécie alguma, expressas ou implícitas, incluindo a de que bloqueará qualquer app ou site em toda circunstância, a de que medirá o uso com exatidão, a de que funcionará sem interrupções ou erros, a de que qualquer valor que ele mostre seja exato, ou a de que mudará os seus gastos. Na máxima extensão permitida pela lei, a {COMPANY} não será responsável por danos indiretos, incidentais, especiais, consequentes ou punitivos, nem por perda de dados ou de dinheiro, decorrentes do seu uso ou da impossibilidade de usar o app — incluindo qualquer compra que você fez ou deixou de fazer, qualquer consequência de um bloqueio que apareceu ou não apareceu, e qualquer bloqueio, limite ou sessão de modo rigoroso que você escolheu começar. Onde a responsabilidade não puder ser excluída, ela se limita ao valor que você nos pagou pelo Premium nos doze meses anteriores à reclamação. Nada nestes Termos limita direitos que você tenha como consumidor e aos quais não se possa renunciar.</p>
""",

"t.apple.h": "13. Apple",
"t.apple.b": """
<p>O On Ice é distribuído pela App Store da Apple. Estes Termos são entre você e a {COMPANY}, não a Apple. A Apple não tem obrigação de prestar manutenção ou suporte ao app, e não é responsável por atender a qualquer reclamação relativa a ele, incluindo as de responsabilidade pelo produto, conformidade legal ou propriedade intelectual. A Apple e as suas subsidiárias são terceiros beneficiários destes Termos e podem fazê-los valer contra você. Onde estes Termos forem omissos, aplica-se o <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Contrato de Licença de Usuário Final de Aplicativo Licenciado</a> da Apple. Você declara que não está em um país sujeito a embargo do governo dos EUA nem consta como parte proibida, e deve cumprir quaisquer termos de terceiros aplicáveis ao usar o app.</p>
""",

"t.changes.h": "14. Mudanças nestes Termos",
"t.changes.b": """
<p>Podemos atualizar estes Termos de tempos em tempos. A data no topo muda quando isso acontece, e as mudanças relevantes serão anotadas nas notas de versão do app. Continuar usando o app depois de uma atualização significa que você aceita os Termos revisados.</p>
""",

"t.law.h": "15. Lei aplicável",
"t.law.b": """
<p>Estes Termos são regidos pelas leis do Paquistão, onde a {COMPANY} atua, sem consideração às regras de conflito de leis. Onde a lei do seu país de residência lhe der proteções das quais não se pode abrir mão por contrato, essas proteções se aplicam.</p>
""",

"t.contact.h": "16. Contato",
"t.contact.b": """
<p>Dúvidas sobre estes Termos: {MAIL}.</p>
""",

# --- your data ------------------------------------------------------------
"d.eyebrow": "Seus dados",
"d.h1": "Apagar seus dados",
"d.sub": "Tudo o que o On Ice sabe está no seu dispositivo. Aqui está como remover, item por item ou tudo de uma vez, o que acontece com a sua assinatura, e por que não há nada do nosso lado para pedir.",
"d.meta": 'Veja também a <a href="{BASE}{L}/privacy/">Política de Privacidade</a>',

"d.where.h": "O que é guardado, e onde",
"d.where.b": """
<p class="lead">O On Ice não tem conta e não mantém perfil de ninguém em nenhum servidor. Tudo o que ele guarda está no seu dispositivo, e você pode remover sem pedir para a gente.</p>
<div class="table-wrap"><table>
<tr><th>Dados</th><th>Onde ficam</th><th>Como remover</th></tr>
<tr><td>A sua lista, decisões, histórico de economia estimada, sequências e padrões</td><td>O armazenamento privado do app no seu dispositivo</td><td>Apague o app. O seu histórico é aquilo de que o total da economia é feito, então ele não é apagado item por item.</td></tr>
<tr><td>Entradas do diário</td><td>No seu dispositivo</td><td>{K_delete_entry} em qualquer entrada, ou apague o app</td></tr>
<tr><td>Registro de gastos, regras, limites, lembretes, atividades</td><td>No seu dispositivo</td><td>Remova cada um no app, ou apague o app</td></tr>
<tr><td>As suas lojas</td><td>Tokens do Tempo de Uso e endereços de sites no seu dispositivo</td><td>Altere-as no app; revogar o acesso ao Tempo de Uso nos Ajustes do iOS também encerra todos os bloqueios</td></tr>
<tr><td>Instantâneo dos widgets e das Atividades ao Vivo</td><td>Um arquivo pequeno no seu dispositivo</td><td>Removido com o app</td></tr>
<tr><td>O resumo semanal</td><td>No seu dispositivo, só enquanto a reflexão com IA estiver ativada</td><td>Desative a reflexão com IA</td></tr>
<tr><td>Status Premium</td><td>A sua Conta Apple (Apple), e uma cópia do status dela no seu dispositivo</td><td>Gerenciado nos ajustes da App Store — veja abaixo</td></tr>
<tr><td>O que uma reflexão da OpenAI enviou</td><td>Não no nosso serviço, que não guarda nenhum conteúdo. A OpenAI pode mantê-lo nos registros de monitoramento de abuso, normalmente por até 30 dias (o Google, nas versões anteriores: até 24 horas)</td><td>Nada para você apagar. Desative a reflexão com IA e nada mais será enviado</td></tr>
<tr><td>Uma contagem de solicitações de IA por dispositivo</td><td>O serviço de IA do On Ice, sob um identificador aleatório de chave</td><td>Apagada automaticamente depois de dois dias</td></tr>
<tr><td>Uma conta, um perfil, qualquer coisa com o seu nome</td><td>—</td><td>Não existe. Nunca tivemos uma para apagar.</td></tr>
</table></div>
""",

"d.inapp.h": "Remova no app",
"d.inapp.b": """
<ul>
  <li><strong>Entradas do diário:</strong> abra uma entrada e toque em {K_delete_entry}.</li>
  <li><strong>Registro de gastos:</strong> toque em {K_remove} numa entrada.</li>
  <li><strong>Regras, limites, lembretes e atividades:</strong> cada um tem o próprio botão de apagar ou remover.</li>
  <li><strong>Lojas:</strong> altere a sua seleção, ou desligue uma loja na tela inicial. Desligar a proteção retira todos os bloqueios de uma vez.</li>
  <li><strong>Os itens decididos ficam no seu histórico</strong> — é disso que a sua economia estimada e os seus padrões são feitos. Para remover esse histórico, apague o app.</li>
</ul>
<div class="callout amber"><span class="tile">{lock}</span><div>Enquanto o <strong>modo rigoroso</strong> está em andamento, a sua configuração fica travada — lojas não podem ser removidas, e regras e limites não podem ser apagados. Esse é o único compromisso que você pediu ao app que mantivesse por você. Ele termina sozinho no horário que você escolheu.</div></div>
""",

"d.journal.h": "O seu diário",
"d.journal.b": """
<p>As entradas do diário ficam só no seu dispositivo, e o On Ice nunca as enviou para lugar nenhum, então não há nada a remover em outro lugar. Apague-as uma de cada vez com {K_delete_entry}. Para guardar uma cópia antes de apagar o app, use {K_export_journal}: isso cria um arquivo de texto simples que você salva onde quiser.</p>
""",

"d.ai.h": "A reflexão com IA",
"d.ai.b": """
<p>Se você ativou a reflexão com IA, o On Ice guarda o resumo semanal mais recente no seu dispositivo para você poder lê-lo de novo. Desativar a reflexão com IA em {K_settings} → {K_ai_reflection} o apaga, remove o lembrete de domingo, encerra a sessão do app com o serviço e devolve o On Ice ao estado de não fazer nenhuma conexão de rede própria.</p>
<p>O serviço nunca teve uma cópia do que você enviou. Ele só mantém uma contagem por dispositivo, sob uma chave aleatória, que apaga depois de dois dias, e totais diários que não nomeiam nenhum dispositivo.</p>
""",

"d.uninstall.h": "Apague o app",
"d.uninstall.b": """
<p>Apagar o On Ice do seu iPhone ou iPad remove todos os dados dele junto — a sua lista, o histórico, o diário, os ajustes e os tokens do Tempo de Uso — e encerra na hora todos os bloqueios e limites. É o jeito de apagar tudo de uma vez. Se o app estiver incluído num backup do iCloud ou do computador, essa cópia pertence à sua Conta Apple e é regida pelos termos da Apple; nós não temos acesso a ela.</p>
""",

"d.subscription.h": "A sua assinatura",
"d.subscription.b": """
<p>Apagar o app não cancela uma assinatura — ela pertence à sua Conta Apple, não ao app. Cancele nos <a href="https://apps.apple.com/account/subscriptions">ajustes de assinatura da App Store</a>; ela continua ativa até o fim do período atual. Os reembolsos são tratados pelo <a href="https://support.apple.com/billing">Suporte da Apple</a>. Uma compra vitalícia não se renova e não precisa de nenhum cancelamento. Se você faz parte de um plano familiar, quem o gerencia é quem comprou.</p>
""",

"d.email.h": "Pergunte para a gente",
"d.email.b": """
<p>Se você quiser uma confirmação por escrito de que não temos nada sobre você, ou se acredita que temos, escreva para {MAIL} de qualquer endereço. Responderemos em até 30 dias. Por favor, não nos envie a sua lista, os seus preços, o seu diário nem capturas de tela deles — não precisamos deles para responder.</p>
""",

# --- 404 ------------------------------------------------------------------
"nf.eyebrow": "404",
"nf.h1": "Nada no gelo por aqui.",
"nf.sub": "O que, pelo menos desta vez, não é a ideia.",
"nf.cta": "Voltar para a Ajuda",
"nf.b": 'Essa página não está aqui. Tente a <a href="{BASE}/">Ajuda</a>, a <a href="{BASE}/privacy/">Política de Privacidade</a> ou os <a href="{BASE}/terms/">Termos de Uso</a>.',

}
