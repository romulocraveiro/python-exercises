# 1) Solicite ao usuário digitar o ano de nascimento:
# 2) A partir do ano digitado:
#     2.1 - calcule a idade
#     2.2 - informe a idade
#     2.3 - informe sua faixa etária:
#           Adolescente (13-17), Adulto(18-64), ou Idoso(65 ou acima)
# 3) Caso o usuário tenha menos de 16 anos:
#     3.1 - informe ao usuário quantos anos faltam para ele se tornar idoso


print("Digite o ano do seu nascimento:")
ano = (int(input()))
idade = 2021 - ano
print("Você tem", idade, "anos de idade.")
if idade<16:
    print("Faltam", (65-idade), "anos para você se tornar idoso.")
if idade >=13 and idade <=17:
    print("Adolescente.")
else:
    if idade >=18 and idade <=64:
        print("Adulto.")
    if idade >=65:
        print("Idoso.")

