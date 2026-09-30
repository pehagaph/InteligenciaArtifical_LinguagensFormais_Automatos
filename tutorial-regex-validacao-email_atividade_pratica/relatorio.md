Explicação dos Resultados maria@gmail.com: VÁLIDO. Possui utilizador, @, domínio e extensão .com válida.
joao.silva@udf.edu.br: VÁLIDO. Aceita pontos no utilizador e domínios compostos (.edu.br).
estudante_01@faculdade.com: VÁLIDO. Aceita sublinha (_) e números no nome de utilizador.
pedro.gmail.com: INVÁLIDO. Não possui o símbolo @ obrigatório para separar o utilizador do domínio.
ana@dominio: INVÁLIDO. Não possui extensão de domínio (como .com ou .br com pelo menos 2 letras).

Como a Regex do Desafio Funciona ^(?!...): Garante que não existem pontos consecutivos (..) em nenhuma parte do texto.
[A-Za-z0-9_+-]+(?:.[A-Za-z0-9_+-]+): Garante que o utilizador começa e termina com um caractere válido, permitindo pontos apenas no meio (impede ponto no início ou logo antes do @).
@: Exige o caractere literal @.
[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*: Garante que os subdomínios não começam nem terminam com hífen (-).
.[A-Za-z]{2,}$: Exige a extensão final precedida de ponto com pelo menos 2 letras.
