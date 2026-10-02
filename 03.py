# Escreva um programa em python que receba
# As seguintes 4 informações do usuário
# Renda Mensal (Um número que possa ser quebrado "FLOAT")
# Score de crédito (Um número inteiro "INT" de 0 a 1000)
# Possui bens como garantia? (Uma String "STR": "sim" ou "nao")
# Tem histórico de Inadimplência? (Uma String "STR": "sim" ou "não")
#
# O empréstimo será APROVADO se o cliente cumprir uma das duas regras abaixo:
#
# REGRA 1
# Ter renda mensal maior ou igual a R$:3.000,00
# Ter score de crédito maior ou igual a 600
# E NÃO ter histórico de inadimplência.
#
# REGRA 2
# Independente de renda ou score,
# se o cliente NÃO tiver histórico de inadimplência
# E possuir bens como garantia, ele também é aprovado.
#
# Se o cliente não se encaixar em nenhuma das duas regras,
#o empréstimo será REPROVADO

cor_rebecca = '\033[38;2;102;51;153m'
reset = '\033[0m'
cor_vermelho = '\033[31m'
cor_verde = '\033[38;2;0;250;154m'


renda = float(input("Digite a renda mensal do cliente\n"))

score = int(input("Digite a score de crédito do cliente\n"))
if score < 0 or score > 1000:
    print("Score Inválido.")
else:
    bens = input("O cliente possui bens como garantia?\n digite 'sim' ou 'não' \n").strip().lower()
    bens_valido = ["sim", "nao", "não"]


    if bens in bens_valido:
        historico = input("O cliente possui histórico de inadimplência?\n digite 'sim' ou 'não' \n").strip().lower()
        historico_valido = ["sim", "nao", "não"]

        if historico in historico_valido:
            if renda >= 3000.00 and score >= 600 and historico in ["nao", "não"]:
                print("Empréstimo Aprovado!")
                
            elif historico in ["nao", "não"] and bens == "sim":
                print("Empréstimo Aprovado!")



            else:
                print("Empréstimo Reprovado!")

        else:
            print("Resposta Inválida. ")

    else:
        print("Resposta Inválida. ")
