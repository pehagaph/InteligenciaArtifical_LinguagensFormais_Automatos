Exercícios Práticos para Fixação — Resolução

=========================================
Bloco 1 (Derivação)
Dada G₁: S → aS | b
=========================================

A) Gere a palavra aaab:
   - S ⇒ aS
   - aS ⇒ aaS
   - aaS ⇒ aaaS
   - aaaS ⇒ aaab

B) Explique como você sabe que a derivação terminou:
   - A derivação termina quando a forma sentencial resultante contém apenas símbolos terminais (neste caso, os caracteres 'a' e 'b') e nenhum símbolo não-terminal (como 'S'). Como não há mais variáveis para substituir, nenhuma regra de produção pode ser aplicada.


=========================================
Bloco 2 (GLC)
Dada G₂: S → aSb | ε
=========================================

A) Gere a palavra aaabbb:
   - S ⇒ aSb
   - aSb ⇒ a(aSb)b = aaSbb
   - aaSbb ⇒ aa(aSb)bb = aaaSbbb
   - aaaSbbb ⇒ aaa(ε)bbb = aaabbb

B) É possível gerar aabbb? Justifique:
   - Não é possível.
   - Justificativa: A regra de produção S → aSb adiciona exatamente um 'a' à esquerda e um 'b' à direita a cada passo. Por isso, a gramática G₂ gera apenas palavras com número igual de 'a's e 'b's da forma aⁿbⁿ (onde n ≥ 0). A palavra 'aabbb' possui dois 'a's e três 'b's (números desiguais), tornando sua geração impossível por essa gramática.


=========================================
Bloco 3 (Classificação)
=========================================

Dada a gramática com produções:
S → aA | A → b
(isto é: S → aA e A → b)

Classifique como Regular ou Livre de Contexto:
- Classificação: A gramática é Regular (e, por consequência, também é Livre de Contexto, pois toda gramática regular é livre de contexto).
- Justificativa: 
  1. Todas as regras de produção possuem a forma de uma Gramática Regular Linear à Direita: V → tV ou V → t (onde V é um não-terminal e t é um terminal).
     - S → aA segue a forma A → aB
     - A → b segue a forma A → a
  2. Não existem símbolos não-terminais nas posições intermediárias e o lado esquerdo de cada regra possui exatamente um símbolo não-terminal.
