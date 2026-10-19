# Resolução de Exercícios — Inteligência Artificial (Russell & Norvig)

---

## Exercício 2.3

### a. Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional.
* **Julgamento:** F
* **Justificativa:** Ser racional não é saber de tudo (onisciência), mas sim tomar a melhor decisão com o que você consegue enxergar e com o que você já sabe.
* **Exemplo ou contraexemplo:** No Pôquer, você não vê a mão do adversário, mas pode jogar de forma perfeitamente racional calculando as chances.
* **Hipóteses:** Racionalidade depende do desempenho esperado com base nas percepções disponíveis, não de ter informação perfeita.

---

### b. Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente.
* **Julgamento:** V
* **Justificativa:** Agentes reativos só olham o momento atual e não têm memória. Se o ambiente exige lembrar do passado para tomar a decisão certa, ele vai falhar ou ficar preso em loop.
* **Exemplo ou contraexemplo:** Um aspirador que não sabe em qual sala está porque só olha o chão de agora e não tem memória de onde veio.
* **Hipóteses:** O ambiente é parcialmente observável e exige memória para decidir a melhor ação.

---

### c. Existe um ambiente de tarefa em que todo agente é racional.
* **Julgamento:** V
* **Justificativa:** Se a nota/pontuação dada pelo ambiente for a mesma para qualquer coisa que o agente fizer, qualquer ação dele vai ser considerada "a melhor possível".
* **Exemplo ou contraexemplo:** Um ambiente em que qualquer ação sempre dá 100 pontos de nota.
* **Hipóteses:** A medida de desempenho é constante e não muda independente da ação escolhida.

---

### d. A entrada para o programa de agente é a mesma que a entrada para a função de agente.
* **Julgamento:** F
* **Justificativa:** A função de agente recebe todo o histórico de percepções desde o começo. O programa de agente roda passo a passo e recebe só a percepção atual do instante.
* **Exemplo ou contraexemplo:** Função recebe `[sala limpa no t1, sala suja no t2]`, enquanto o programa recebe apenas `[sala suja no t2]`.
* **Hipóteses:** A definição padrão do livro (Russell & Norvig) onde o programa roda em ciclos no hardware.

---

### e. Toda função de agente é implementável por uma combinação de programa/máquina.
* **Julgamento:** F
* **Justificativa:** Existem funções que exigem memória ou tempo de processamento infinitos, o que é impossível em computadores reais.
* **Exemplo ou contraexemplo:** Uma função que precisasse resolver o Problema da Parada de Turing ou analisar infinitos estados de um jogo.
* **Hipóteses:** Computadores reais têm limitações físicas e de computabilidade.

---

### f. Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional.
* **Julgamento:** V
* **Justificativa:** Se todas as ações disponíveis levarem ao mesmo resultado e à nota máxima, escolher qualquer uma no chute/carrocel vai dar certo.
* **Exemplo ou contraexemplo:** O ambiente já está perfeito (ex: tudo limpo) e qualquer movimento ganha a pontuação máxima.
* **Hipóteses:** A pontuação obtida é idêntica para todas as opções de ação.

---

### g. É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos.
* **Julgamento:** V
* **Justificativa:** Se dois ambientes exigirem as mesmas regras de decisão para atingir o objetivo, a mesma lógica de agente funciona perfeitamente nos dois.
* **Exemplo ou contraexemplo:** O código de um aspirador que limpa se tiver sujeira e anda se estiver limpo funciona em uma casa de 2 cômodos e em uma de 5 cômodos.
* **Hipóteses:** A regra de ação necessária para pontuar bem é a mesma em ambos os ambientes.

---

### h. Todo agente é racional em um ambiente não observável.
* **Julgamento:** F
* **Justificativa:** Mesmo sem enxergar nada (sem sensores), um agente racional precisa tentar a estratégia com maior chance de dar certo. Se ele agir de forma burra, ele continua sendo irracional.
* **Exemplo ou contraexemplo:** Um aspirador no escuro que fica parado para sempre em vez de andar tentando limpar às cegas.
* **Hipóteses:** O agente possui um conhecimento prévio sobre as ações que pode usar a seu favor.

---

### i. Um agente jogador de pôquer perfeitamente racional nunca perde.
* **Julgamento:** F
* **Justificativa:** O pôquer depende da sorte das cartas jogadas. O agente racional faz a jogada com maior chance de vitória, mas ainda assim pode dar azar e perder.
* **Exemplo ou contraexemplo:** O agente joga com 95% de chance de ganhar na última carta, mas sai justamente os 5% do adversário.
* **Hipóteses:** O ambiente envolve azar/probabilidade (estocástico).

---

## Exercício 2.4

### Caso 1 — Jogar futebol.
* **Agente analisado:** Robô jogador de futebol (ou software de controle do robô).
* **Objetivo e hipóteses:** Marcar gols no time adversário, defender a própria meta e vencer a partida respeitando as regras.
* **P — Medida de desempenho:** Gols marcados, gols sofridos, precisão de passes, posse de bola, resultado final (vitória/derrota).
* **E — Ambiente:** Campo de futebol, bola, companheiros de equipe, adversários, condições do gramado/clima.
* **A — Atuadores:** Motores das rodas/pernas articuladas, atuador de chute, direcionamento do corpo.
* **S — Sensores:** Câmeras, sensores ultrassônicos/LIDAR, giroscópio, acelerômetro, GPS local.

| Propriedade | Classificação | Justificativa |
| :--- | :--- | :--- |
| **Observabilidade** | Parcialmente observável | O robô tem campo de visão limitado; não consegue enxergar o campo inteiro atrás dele ao mesmo tempo. |
| **Número de agentes** | Multiagente (cooperativo e competitivo) | Coopera com os colegas do mesmo time e compete contra os jogadores do time adversário. |
| **Previsibilidade** | Estocástico | O comportamento dos outros jogadores é imprevisível e há derrapagens ou rebotes da bola. |
| **Dependência entre decisões** | Sequencial | As decisões atuais (como dar um passe) afetam diretamente as oportunidades e escolhas futuras no jogo. |
| **Mudança durante a decisão** | Dinâmico | O jogo, a bola e os jogadores continuam se movendo enquanto o robô calcula qual ação tomar. |
| **Natureza dos elementos** | Contínuo | Posições, velocidade, trajetória da bola e tempo mudam de forma contínua. |
| **Conhecimento do funcionamento** | Conhecido | As regras do futebol e as físicas básicas de movimento são conhecidas pelo agente. |

---

### Caso 2 — Explorar os oceanos subterrâneos de Titã.
* **Agente analisado:** Sonda robótica submarina autônoma.
* **Objetivo e hipóteses:** Mapear o oceano subterrâneo de Titã, coletar dados químicos/físicos e procurar sinais de vida sem colidir.
* **P — Medida de desempenho:** Área mapeada, volume de dados científicos coletados, integridade do robô, eficiência energética.
* **E — Ambiente:** Oceanos subterrâneos de metano/etano/água de Titã, crosta de gelo, correntes aquáticas profundas, rochas.
* **A — Atuadores:** Hélices/propulsores marinhos, iluminação, braço robótico para coleta de amostras, leme.
* **S — Sensores:** Sonar, sensores de temperatura/pressão/densidade, espectrômetro, câmeras com iluminação própria, giroscópio.

| Propriedade | Classificação | Justificativa |
| :--- | :--- | :--- |
| **Observabilidade** | Parcialmente observável | Sensores ópticos e sonares possuem alcance limitado na escuridão e densidade do oceano de Titã. |
| **Número de agentes** | Agente único | A sonda opera sozinha no ambiente sem interação com outros agentes tomadores de decisão. |
| **Previsibilidade** | Estocástico | Correntes subterrâneas imprevistas, falhas de terreno ou turbulências tornam os resultados incertos. |
| **Dependência entre decisões** | Sequencial | Escolher um trajeto inicial condiciona quais áreas a sonda conseguirá explorar antes do fim da bateria. |
| **Mudança durante a decisão** | Dinâmico | Correntes marítimas e movimentações de fluidos continuam acontecendo enquanto o robô processa. |
| **Natureza dos elementos** | Contínuo | Pressão, profundidade, temperatura, coordenadas e níveis de bateria variam de forma contínua. |
| **Conhecimento do funcionamento** | Desconhecido | As condições exatas do oceano subterrâneo de Titã são hipotéticas e não foram totalmente mapeadas. |

---

### Caso 3 — Comprar livros usados de IA na Internet.
* **Agente analisado:** Bot/Software de compras automatizadas.
* **Objetivo e hipóteses:** Encontrar e comprar edições específicas de livros de IA pelo menor preço, considerando frete e estado de conservação.
* **P — Medida de desempenho:** Custo total pago (livro + frete), tempo gasto para encontrar, qualidade do estado do livro, cumprimento do orçamento.
* **E — Ambiente:** Sites de e-commerce, APIs de sebos virtuais, servidores na internet, vendedores online.
* **A — Atuadores:** Envio de requisições HTTP (adicionar ao carrinho, preencher dados, confirmar compra/pagamento).
* **S — Sensores:** Leitura de código HTML/JSON dos sites, chamadas de API, consultas de preços e fretes.

| Propriedade | Classificação | Justificativa |
| :--- | :--- | :--- |
| **Observabilidade** | Parcialmente observável | O agente não consegue ver o estado físico real do livro usado (apenas descrições/fotos) nem ofertas privadas fora da rede. |
| **Número de agentes** | Multiagente (competitivo) | Compete com outros compradores e bots por poucas unidades do mesmo livro usado. |
| **Previsibilidade** | Estocástico | Um anúncio pode sumir repentinamente, ou o vendedor pode cancelar a venda por falta de estoque. |
| **Dependência entre decisões** | Sequencial | Fazer uma reserva ou gastar parte do orçamento limita as compras de outros livros disponíveis no futuro. |
| **Mudança durante a decisão** | Semidinâmico | O ambiente em si não muda continuamente, mas os preços e estoques podem mudar enquanto o bot decide. |
| **Natureza dos elementos** | Discreto | Preços, número de páginas, quantidade em estoque e cliques/comandos são valores discretos. |
| **Conhecimento do funcionamento** | Conhecido | O agente conhece o funcionamento das APIs e regras de compra dos sites de e-commerce. |

---

### Caso 4 — Jogar uma partida de tênis.
* **Agente analisado:** Robô tenista em quadra.
* **Objetivo e hipóteses:** Rebater a bolinha para a quadra adversária respeitando as linhas para marcar pontos e vencer o jogo.
* **P — Medida de desempenho:** Pontos e sets conquistados, taxa de acerto de saques, erros não forçados.
* **E — Ambiente:** Quadra de tênis, rede, bolinha, vento, adversário.
* **A — Atuadores:** Braço robótico articulado para empunhar a raquete, sistema de locomoção nas pernas/rodas.
* **S — Sensores:** Câmeras de alta velocidade, sensores de rastreamento de impacto, giroscópios, sensores de linha.

| Propriedade | Classificação | Justificativa |
| :--- | :--- | :--- |
| **Observabilidade** | Completamente observável | O agente tem visão total do seu lado da quadra, da rede, da bolinha e do adversário. |
| **Número de agentes** | Multiagente (competitivo) | Compete diretamente contra outro jogador/agente que tenta dificultar suas rebatidas. |
| **Previsibilidade** | Estocástico | Rajadas de vento e as escolhas estratégicas do oponente tornam o resultado dos lances incerto. |
| **Dependência entre decisões** | Sequencial | Cada rebatida posiciona o agente para a devolução seguinte, encadeando a jogada. |
| **Mudança durante a decisão** | Dinâmico | A bolinha e o oponente se movem continuamente enquanto o robô decide o ângulo do golpe. |
| **Natureza dos elementos** | Contínuo | Ângulo de rebatida, velocidade, trajetória e posição são variáveis contínuas. |
| **Conhecimento do funcionamento** | Conhecido | As regras do tênis e as leis da física clássica aplicadas à bola são totalmente conhecidas. |

---

### Caso 5 — Praticar tênis contra uma parede.
* **Agente analisado:** Robô tenista treinando solo.
* **Objetivo e hipóteses:** Rebater a bolinha continuamente contra a parede sem deixá-la cair mais de um quique no chão.
* **P — Medida de desempenho:** Quantidade de rebatidas consecutivas bem-sucedidas, precisão do alvo na parede, controle de ritmo.
* **E — Ambiente:** Quadra/parede de treino, bolinha de tênis, superfície do piso, vento.
* **A — Atuadores:** Braço robótico (movimento da raquete) e sistema de locomoção corporal.
* **S — Sensores:** Câmeras de rastreamento visual da bola, acelerômetro, sensores de impacto.

| Propriedade | Classificação | Justificativa |
| :--- | :--- | :--- |
| **Observabilidade** | Completamente observável | O robô consegue enxergar todo o espaço de treino, a parede e a bolinha sem obstáculos. |
| **Número de agentes** | Agente único | A parede é apenas um elemento estático do ambiente, não um outro agente com objetivos próprios. |
| **Previsibilidade** | Determinístico (ou ligeiramente estocástico se houver vento/imperfeição na parede) | O quique da bola na parede obedece a leis físicas bem previsíveis em ambiente controlado. |
| **Dependência entre decisões** | Sequencial | O local onde o agente devolve a bola na parede determina onde ele terá que recebê-la na jogada seguinte. |
| **Mudança durante a decisão** | Dinâmico | A bola continua em movimento pelo ar enquanto o agente calcula a trajetória. |
| **Natureza dos elementos** | Contínuo | Velocidades, forças aplicadas, posições e tempos são contínuos. |
| **Conhecimento do funcionamento** | Conhecido | O comportamento elástico do choque da bola com a parede é totalmente conhecido pela física. |

---

### Caso 6 — Realizar um salto de altura.
* **Agente analisado:** Robô atleta de salto em altura.
* **Objetivo e hipóteses:** Correr e saltar sobre o sarrafo sem derrubá-lo, caindo na área do colchão de proteção.
* **P — Medida de desempenho:** Altura máxima superada com sucesso (em metros), número de tentativas utilizadas, não derrubar o sarrafo.
* **E — Ambiente:** Pista de corrida, sarrafo, suportes laterais, colchão de queda, vento.
* **A — Atuadores:** Perna(s) mecânicas articuladas para corrida e impulsão, controle de rotação do tronco no ar.
* **S — Sensores:** Telemetria a laser/LIDAR para medir a distância até o sarrafo, giroscópio, acelerômetros, sensores de pressão nos pés.

| Propriedade | Classificação | Justificativa |
| :--- | :--- | :--- |
| **Observabilidade** | Completamente observável | A pista, o sarrafo e a área de queda estão totalmente visíveis para os sensores do robô. |
| **Número de agentes** | Agente único | Durante a execução do salto em si, apenas o robô atua na pista (a disputa contra outros atletas ocorre em turnos isolados). |
| **Previsibilidade** | Determinístico (ou levemente estocástico em caso de vento forte) | Em ambiente coberto, os resultados dependem quase que exclusivamente da mecânica física da impulsão do próprio robô. |
| **Dependência entre decisões** | Sequencial | A passada da corrida e a escolha do ponto da impulsão determinam diretamente o sucesso da passagem por cima da barra. |
| **Mudança durante a decisão** | Dinâmico | Enquanto o robô corre e se aproxima do salto, o tempo e a posição mudam continuamente. |
| **Natureza dos elementos** | Contínuo | Velocidade de corrida, ângulo de salto, aceleração e altura da barra variam de forma contínua. |
| **Conhecimento do funcionamento** | Conhecido | As regras da modalidade e as equações da física parabólica do salto são amplamente conhecidas. |

---

### Caso 7 — Participar de um leilão de um item, realizando lances.
* **Agente analisado:** Bot/Agente comprador de leilão.
* **Objetivo e hipóteses:** Arrematar o item leiloado pelo menor preço possível, sem ultrapassar o valor limite preestabelecido.
* **P — Medida de desempenho:** Obtenção do item (sucesso na compra), margem de economia em relação ao limite estipulado, custo do lance final.
* **E — Ambiente:** Plataforma/sala de leilão, cronômetro do lote, lances concorrentes, leiloeiro.
* **A — Atuadores:** Envio de comandos digitais para cobrir lances ("Dar lance de $X$").
* **S — Sensores:** Monitoramento de eventos de rede (recebimento do valor atual do lote, tempo restante, notificação de novos lances).

| Propriedade | Classificação | Justificativa |
| :--- | :--- | :--- |
| **Observabilidade** | Parcialmente observável | O agente sabe qual é o lance atual, mas não sabe qual é o valor limite máximo dos outros participantes. |
| **Número de agentes** | Multiagente (competitivo) | Compete contra outros participantes dispostos a dar lances maiores para arrematar o mesmo item. |
| **Previsibilidade** | Estocástico | O comportamento de lance dos adversários é imprevisível e pode envolver blefes no último segundo. |
| **Dependência entre decisões** | Sequencial | Um lance dado agora aumenta a oferta atual e força os concorrentes a tomarem novas decisões no próximo turno. |
| **Mudança durante a decisão** | Semidinâmico | O preço não muda sozinho continuamente, mas o relógio corre e os adversários podem enviar lances a qualquer instante. |
| **Natureza dos elementos** | Discreto | Os valores de lances, número de participantes, tempo restante em segundos e estados ("vencendo"/"perdendo") são discretos. |
| **Conhecimento do funcionamento** | Conhecido | As regras do leilão (ex: incremento mínimo, prazo final) são explicitadas pela plataforma. |

---

### Comparação final

* **O que muda entre jogar tênis contra outra pessoa e praticar contra uma parede?**  
  A principal mudança está no **número de agentes** e na **previsibilidade/complexidade do ambiente**. Contra uma pessoa, o ambiente é **multiagente e altamente estocástico**, pois o adversário usa estratégias imprevisíveis e adapta as jogadas para explorar os pontos fracos do robô. Contra a parede, o ambiente passa a ser de **agente único e praticamente determinístico**, pois a resposta da parede segue estritamente as leis de reflexão física, eliminando o fator tático do oponente.

* **Por que comprar livros usados pode exigir decisões com informações incompletas?**  
  Porque o ambiente é **parcialmente observável**. O agente não tem acesso ao estado físico real e minucioso da mercadoria (rasuras escondidas, páginas amareladas ou rasgadas não fotografadas), não conhece o estoque real não atualizado do vendedor, nem consegue prever se outro comprador fechará o pedido segundos antes dele.

* **Como outros agentes influenciam futebol e leilões?**  
  Nos dois cenários, a presença de outros agentes transforma o ambiente em um jogo **multiagente interativo**:
  1. No **futebol**, a influência ocorre em tempo real via **cooperação e competição física**: colegas exigem coordenação tática para passes, enquanto adversários bloqueiam caminhos e tentam roubar a bola, alterando constantemente o estado do mundo.
  2. Nos **leilões**, a influência é **estratégica e competitiva**: os adversários ocultam seu limite de orçamento e reagem aos lances do bot, podendo forçar o preço para cima ou realizar lances no último segundo (*sniping*), o que exige que o bot recalcule se vale a pena cobrir a oferta ou desistir.

---

## Exercício 2.5

### Agente
* **Definição:** Qualquer entidade capaz de perceber o ambiente por meio de sensores e atuar sobre esse ambiente por meio de atuadores. Ele toma decisões para mapear suas sequências de percepção em ações.
* **Exemplo:** Um robô aspirador de pó que percebe sujeira no chão através de sensores infravermelhos e atua ativando suas rodas e seu motor de sucção.

### Função de agente
* **Definição:** Uma descrição matemática abstrata que mapeia qualquer sequência de percepções recebidas pelo agente até o momento para uma ação correspondente a ser executada.
* **Exemplo:** Uma tabela formal que define que, se a sequência de percepções for `[Sala A, Suja]`, a ação associada será `Limpar`.

### Programa de agente
* **Definição:** A implementação concreta em software ou código computacional da função de agente, projetada para rodar em uma arquitetura física ou computador real.
* **Exemplo:** Um script escrito em Python executado dentro do microcontrolador do robô aspirador que lê as variáveis dos sensores e envia sinais elétricos para os motores.

### Racionalidade
* **Definição:** A propriedade de um agente em escolher ações que maximizem o valor esperado de sua medida de desempenho, considerando seu histórico de percepções e o conhecimento prévio do ambiente.
* **Exemplo:** Um carro autônomo acionar os freios de emergência ao detectar um pedestre atravessando a rua para evitar um atropelamento.

### Autonomia
* **Definição:** A capacidade de um agente de operar com base na sua própria experiência e aprendizado no ambiente, sem depender exclusivamente de conhecimentos pré-programados ou intervenção humana externa.
* **Exemplo:** Uma sonda espacial que aprende a recalibrar suas rotas de navegação analisando o terreno e desviando de obstáculos por conta própria.

### Agente reativo
* **Definição:** Um agente simples que escolhe suas ações baseando-se apenas na percepção do estado atual do ambiente, ignorando completamente o histórico de percepções passadas.
* **Exemplo:** Um termostato que liga o ar-condicionado imediatamente quando a temperatura atual detectada ultrapassa 25 °C.

### Agente baseado em modelo
* **Definição:** Um agente que mantém um estado interno para rastrear aspectos não observáveis do ambiente atual, atualizando seu modelo do mundo com base na história de como o mundo evolui.
* **Exemplo:** Um robô aspirador que guarda na memória o mapa das salas já limpas para não ficar rodando no mesmo lugar.

### Agente baseado em objetivos
* **Definição:** Um agente que combina a representação do estado do mundo com informações sobre suas metas para avaliar quais ações possíveis permitirão alcançar o resultado desejado.
* **Exemplo:** Um aplicativo de navegação (como o Waze) que calcula a melhor rota combinando o mapa da cidade com a meta de chegar a um endereço específico.

### Agente baseado em utilidade
* **Definição:** Um agente que utiliza uma função de utilidade para quantificar o quão "desejável" ou satisfatório é um determinado estado, permitindo escolher a ação de melhor custo-benefício quando há múltiplos caminhos ou objetivos conflitantes.
* **Exemplo:** Um sistema de recomendação de voos que escolhe uma rota combinando o menor preço, menor tempo de viagem e menor número de escalas para o passageiro.

### Agente com aprendizagem
* **Definição:** Um agente estruturado para aprender a partir de suas experiências passadas, utilizando um elemento de crítica para avaliar o desempenho e um elemento de aprendizado para aprimorar suas regras de decisão ao longo do tempo.
* **Exemplo:** Um algoritmo de recomendações de filmes que ajusta suas sugestões com base no histórico de avaliações e no comportamento de reprodução do usuário.

---

### Síntese com autômatos

* **Caso escolhido:** Caso 1 — Jogar futebol.
* **Três estados internos:**
  1. $S_1$: Com a posse da bola no campo de ataque.
  2. $S_2$: Sem a posse da bola e em fase defensiva.
  3. $S_3$: Posicionado para chute ao gol livre de marcação.
* **Três percepções:**
  1. $P_1$: Bola visível ao alcance dos pés e caminho de passe desimpedido.
  2. $P_2$: Adversário se aproximando rapidamente pela frente.
  3. $P_3$: Goleiro adversário adiantado e meta desprotegida.
* **Três ações:**
  1. $A_1$: Tocar a bola para o companheiro melhor posicionado.
  2. $A_2$: Desarmar o adversário/bloquear a passagem.
  3. $A_3$: Chutar a bola com precisão em direção ao gol.
* **Duas regras (Estado Atual + Percepção → Próximo Estado e Ação):**
  1. **Regra 1:** $S_1 + P_3 \rightarrow S_3, A_3$  
     *(Estando com a bola no ataque ($S_1$) ao perceber o goleiro adiantado ($P_3$), o agente transita para o estado de chute ao gol ($S_3$) e executa a ação de chutar ($A_3$)).*
  2. **Regra 2:** $S_2 + P_1 \rightarrow S_1, A_1$  
     *(Estando sem a posse na defesa ($S_2$) ao recuperar a bola com linha de passe livre ($P_1$), o agente transita para o estado de posse no ataque ($S_1$) e executa o passe ($A_1$)).*

* **Como os estados internos representam informação passada:**  
  Os estados internos atuam como uma memória compacta do histórico de percepções. Como o agente não enxerga todo o campo em $360^\circ$ o tempo todo, o estado interno $S_1$ ("Com a posse da bola no campo de ataque") guarda a informação de que o robô dominou a bola no passo anterior, permitindo que ele tome decisões no presente sem precisar reconfirmar se a bola ainda está sob seu controle a cada milissegundo.

* **Limitação da simplificação:**  
  Modelar um agente por autômatos de estados finitos assume um ambiente discreto e simplificado. No futebol real, variáveis como velocidade, força física, trajetória parabólica da bola, vento e desgaste mecânico são contínuas e altamente estocásticas, tornando impossível prever todas as transições de estado com regras discretas rígidas sem perder precisão operacional.
