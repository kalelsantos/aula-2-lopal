# Escreva um programa em Python que pergunte três informações ao usuário:
# É estudante? (uma string: "sim" ou "nao")
# Dia da semana? (uma string "terça" ou "outros")
# Tipo de sala? (uma string "vip" ou "comum")
#
# O programa deve exibir "Desconto Aplicado!"
# ou "Valor integral"
#
#REGRAS
# O Cliente ganha o desconto
# Se for estudante OU for terça
# E a sala for comum.

cor_rebecca = '\033[38;2;102;51;153m'
reset = '\033[0m'
cor_vermelho = '\033[31m'
cor_verde = '\033[38;2;0;250;154m'


estudante = input(f"{cor_rebecca}É um estudante?{reset}\n").strip().lower()
estudante_validos = ["sim", "nao", "não"]

if estudante in estudante_validos:
    dia = input(f"{cor_rebecca}Qual o dia de hoje?{reset}\n").strip().lower()
    dias_validos = ["segunda", "terca", "terça", "quarta", "quinta", "sexta", "sabado", "sábado", "domingo"]

    if dia in dias_validos:
        sala = input(f"{cor_rebecca}Qual a sala?{reset}\n").strip().lower()
        sala_validos = ["vip", "comum"]

        if sala in sala_validos:
            estudante_comum = (estudante == 'sim' and sala == 'comum')
            terca_comum = (dia in ["terca", "terça"] and sala == 'comum')

            if estudante_comum or terca_comum:
                print(f"{cor_verde}Desconto Aplicado! {reset}")
            elif estudante == 'nao' or sala == 'vip':
                print(f"{cor_vermelho}Valor Integral. {reset}")

        else:
            print(f"{cor_vermelho}Sala Inválida. {reset}")

    else:
        print(f"{cor_vermelho}Dia inexistente. {reset}")
        
else:
    print(f"{cor_vermelho}Resposta Inválida. {reset}")



# if estudante == 'sim' and sala == 'comum' or dia == 'terca' in ["terca", "terça"] and sala == 'comum':
#     print("Desconto Aplicado!")
# elif estudante == 'nao' or sala == 'vip':
#     print("Valor Integral.")


# if dia == "segunda" or "terca" or "terça" or "quarta" or "quinta" or "sexta" or "sabado" or "sábado" or "domingo":
#     sala = input("Qual a sala?\n").strip().lower()
#     if estudante == 'sim' and sala == 'comum' or dia == 'terca' in ["terca", "terça"] and sala == 'comum':
#         print("Desconto Aplicado!")
#     elif estudante == 'nao' or sala == 'vip':
#         print("Valor Integral.")

# else:
#     print("ERRO")