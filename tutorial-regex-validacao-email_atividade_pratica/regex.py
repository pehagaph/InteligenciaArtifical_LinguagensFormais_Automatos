# Código Completo da Atividade Prática (com o Desafio incluso)
# Este programa em Python cumpre todos os 5 requisitos da atividade e aplica a Regex aprimorada do desafio:

import re

# -------------------------------------------------------------------
# REGEX APRIMORADA (Atende aos requisitos do DESAFIO):
# - Não permite ponto no início nem no final do usuário (antes do @)
# - Não permite pontos consecutivos (..) no usuário ou domínio
# - Hífen não pode estar no início nem no final do domínio
# -------------------------------------------------------------------
padrao_email_desafio = r"^(?!.*\.\.)[A-Za-z0-9_+-]+(?:\.[A-Za-z0-9_+-]+)*@[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)*\.[A-Za-z]{2,}$"

# Lista de casos de teste indicados no tutorial
emails_para_testar = [
    "maria@gmail.com",
    "joao.silva@udf.edu.br",
    "estudante_01@faculdade.com",
    "pedro.gmail.com",
    "ana@dominio"
]

validos = []
invalidos = []

print("--- PROCESSANDO OS E-MAILS DE TESTE ---")

for email in emails_para_testar:
    if re.fullmatch(padrao_email_desafio, email):
        validos.append(email)
    else:
        # Identificação e explicação do motivo de rejeição
        motivo = ""
        if "@" not in email:
            motivo = "Falta o símbolo obrigatório '@'."
        elif email.startswith("@"):
            motivo = "Falta a parte do usuário antes do '@'."
        else:
            partes = email.split("@")
            if len(partes) == 2:
                usuario, dominio = partes
                if not dominio:
                    motivo = "Falta o domínio após o '@'."
                elif "." not in dominio:
                    motivo = "Falta a extensão do domínio (ex: .com, .edu.br) ou o ponto separador."
                elif len(dominio.split(".")[-1]) < 2:
                    motivo = "A extensão do domínio deve ter pelo menos 2 letras."
                elif usuario.startswith(".") or usuario.endswith("."):
                    motivo = "O nome de usuário não pode começar nem terminar com ponto."
                elif ".." in email:
                    motivo = "Não são permitidos pontos consecutivos ('..')."
                else:
                    motivo = "Formato de caracteres inválido para usuário ou domínio."
            else:
                motivo = "O e-mail contém múltiplos símbolos '@'."
        
        invalidos.append((email, motivo))

# -------------------------------------------------------------------
# APRESENTAÇÃO DOS RESULTADOS (Itens 3, 4 e 5 da atividade)
# -------------------------------------------------------------------
print("\n E-MAILS VÁLIDOS:")
for item in validos:
    print(f"  ✓ {item}")

print("\n E-MAILS INVÁLIDOS:")
for item, motivo in invalidos:
    print(f"  ✗ {item}")
    print(f"    └─ Motivo: {motivo}")
