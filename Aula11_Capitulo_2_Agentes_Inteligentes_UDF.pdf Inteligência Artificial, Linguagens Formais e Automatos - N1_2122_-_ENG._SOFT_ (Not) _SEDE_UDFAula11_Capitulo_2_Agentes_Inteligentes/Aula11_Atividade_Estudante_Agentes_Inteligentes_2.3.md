Atividade sobre agentes inteligentes
Aula 19/10/2026 | Professora Kadidja Valéria | Inteligência artificial
Disciplina: Inteligência Artificial, Linguagens Formais e Autômatos
Estudante: Paulo Henrique Santos Lopes | Turma: N1
Realize os exercícios 2.3, 2.4 e 2.5 do Capítulo 2 sobre agentes inteligentes. Analise a racionalidade, descreva ambientes de tarefa por meio do modelo PEAS e explique os conceitos com suas próprias palavras. Utilize o capítulo disponibilizado e justifique suas respostas.
Modalidade sugerida: individual com consulta. Tempo estimado: 2h30. Prazo: conforme orientação da professora.

Exercício 2.3
a. Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional.
Julgamento: F

Justificativa: Ser racional não é saber de tudo (onisciência), mas sim tomar a melhor decisão com o que você consegue enxergar e com o que você já sabe.

Exemplo ou contraexemplo: No Pôquer, você não vê a mão do adversário, mas pode jogar de forma perfeitamente racional calculando as chances.

Hipóteses: Racionalidade depende do desempenho esperado com base nas percepções disponíveis, não de ter informação perfeita.

b. Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente.
Julgamento: V

Justificativa: Agentes reativos só olham o momento atual e não têm memória. Se o ambiente exige lembrar do passado para tomar a decisão certa, ele vai falhar ou ficar preso em loop.

Exemplo ou contraexemplo: Um aspirador que não sabe em qual sala está porque só olha o chão de agora e não tem memória de onde veio.

Hipóteses: O ambiente é parcialmente observável e exige memória para decidir a melhor ação.

c. Existe um ambiente de tarefa em que todo agente é racional.
Julgamento: V

Justificativa: Se a nota/pontuação dada pelo ambiente for a mesma para qualquer coisa que o agente fizer, qualquer ação dele vai ser considerada "a melhor possível".

Exemplo ou contraexemplo: Um ambiente em que qualquer ação sempre dá 100 pontos de nota.

Hipóteses: A medida de desempenho é constante e não muda independente da ação escolhida.

d. A entrada para o programa de agente é a mesma que a entrada para a função de agente.
Julgamento: F

Justificativa: A função de agente recebe todo o histórico de percepções desde o começo. O programa de agente roda passo a passo e recebe só a percepção atual do instante.

Exemplo ou contraexemplo: Função recebe [sala limpa no t1, sala suja no t2], enquanto o programa recebe apenas [sala suja no t2].

Hipóteses: A definição padrão do livro (Russell & Norvig) onde o programa roda em ciclos no hardware.

e. Toda função de agente é implementável por uma combinação de programa/máquina.
Julgamento: F

Justificativa: Existem funções que exigem memória ou tempo de processamento infinitos, o que é impossível em computadores reais.

Exemplo ou contraexemplo: Uma função que precisasse resolver o Problema da Parada de Turing ou analisar infinitos estados de um jogo.

Hipóteses: Computadores reais têm limitações físicas e de computabilidade.

f. Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional.
Julgamento: V

Justificativa: Se todas as ações disponíveis levarem ao mesmo resultado e à nota máxima, escolher qualquer uma no chute/carrocel vai dar certo.

Exemplo ou contraexemplo: O ambiente já está perfeito (ex: tudo limpo) e qualquer movimento ganha a pontuação máxima.

Hipóteses: A pontuação obtida é idêntica para todas as opções de ação.

g. É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos.
Julgamento: V

Justificativa: Se dois ambientes exigirem as mesmas regras de decisão para atingir o objetivo, a mesma lógica de agente funciona perfeitamente nos dois.

Exemplo ou contraexemplo: O código de um aspirador que limpa se tiver sujeira e anda se estiver limpo funciona em uma casa de 2 cômodos e em uma de 5 cômodos.

Hipóteses: A regra de ação necessária para pontuar bem é a mesma em ambos os ambientes.

h. Todo agente é racional em um ambiente não observável.
Julgamento: F

Justificativa: Mesmo sem enxergar nada (sem sensores), um agente racional precisa tentar a estratégia com maior chance de dar certo. Se ele agir de forma burra, ele continua sendo irracional.

Exemplo ou contraexemplo: Um aspirador no escuro que fica parado para sempre em vez de andar tentando limpar às cegas.

Hipóteses: O agente possui um conhecimento prévio sobre as ações que pode usar a seu favor.

i. Um agente jogador de pôquer perfeitamente racional nunca perde.
Julgamento: F

Justificativa: O pôquer depende da sorte das cartas jogadas. O agente racional faz a jogada com maior chance de vitória, mas ainda assim pode dar azar e perder.

Exemplo ou contraexemplo: O agente joga com 95% de chance de ganhar na última carta, mas sai justamente os 5% do adversário.

Hipóteses: O ambiente envolve azar/probabilidade (estocástico).


