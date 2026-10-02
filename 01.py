# Escreva um programa em python com as seguintes informações
# Idade (um número inteiro)
# Altura em centímetros (um número inteiro)
# Tem autorização dos pais? (string de sim ou não)
#
# O programa deve exibir "Acesso Liberado" se o visitante
# Puder andar no brinquedo, ou "Acesso Negado". caso contrário.
#
# REGRA
# Tiver idade maior ou igual a 12 E altura maior ou igual a 140 
# OU
# Se tiver autorização igual a "sim"
#n SE TIVER PERMISSÃO, IDADE E ALTURA NÃO IMPORTAM!!!

cor_rebecca = '\033[38;2;102;51;153m'
reset = '\033[0m'
cor_vermelho = '\033[31m'
cor_verde = '\033[38;2;0;250;154m'


idade = int(input(f"{cor_rebecca}Digite a idade: {reset}"))

if idade == 18:
    print(f"{cor_verde}Acesso Liberado!{reset}")
else:
    altura = int(input(f"{cor_rebecca}Digite sua altura em {reset}{cor_verde}centímetros: {reset}"))
    autorizacao = input(f"{cor_rebecca}Tem autorização dos pais?{reset}\n").strip().lower()

    if idade >= 12 and altura >= 140 or autorizacao in ["sim", "s"]:
        print(f"{cor_verde}Acesso liberado!{reset}")
    elif idade < 12 or altura < 140 or autorizacao in ["nao", "n", "ñ", "não"]:
        print(f"{cor_vermelho}Acesso negado!{reset}")
    else:
        print(f"{cor_vermelho}ERRO")