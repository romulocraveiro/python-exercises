
# 1) Solicite ao usuário digitar o ano de nascimento:
# 2) A partir do ano digitado:
#     2.1 - calcule a idade
#     2.2 - informe a idade
#     2.3 - informe sua faixa etária:
#           Adolescente (13-17), Adulto(18-64), ou Idoso(65 ou acima)
# 3) Caso o usuário tenha menos de 16 anos:
#     3.1 - informe ao usuário quantos anos faltam para ele se tornar idoso

# Tratamento de exceções (aula 20): 
# E se o usuário digitar A de 2 Dígitos?
# E se o usuário digitar Ano Igual a Zero?
# E se o usuário digitar Ano Igual a 2021?
# E se o usuário digitar Ano Maior que 2021?
# E se o usuário digitar Ano Negativo?

print("Digite o ano do seu nascimento com 4 dígitos (ex.: 1964):")
ano = input()
# E se o usuário digitar A de 2 Dígitos?
tamanho = len(ano)
if tamanho != 4:
    print("Opção inválida!! Recarregue a página e tente novamente.")
# E se o usuário digitar Ano Igual a Zero?
# E se o usuário digitar Ano Igual a 2021?
# E se o usuário digitar Ano Maior que 2021?
# E se o usuário digitar Ano Negativo?
# Teremos que, primeiro, converter o input para um número inteiro, para poder
# utilizar operadores relacionais: 
ano = int(ano)
if ano <=0 or ano >= 2021:
    print("Opção inválida!! Recarregue a página e tente novamente.")       
else:
    ano = int(ano)
    idade = 2021 - ano
    print("\nVocê tem", idade, "anos de idade.")
    if idade < 16:
        print("Faltam", (65-idade), "anos para você se tornar idoso.\n")
    if idade >= 13 and idade <= 17:
        print("Adolescente.\n")
    else:
        if idade >= 18 and idade <= 64:
            print("Adulto.\n")
        if idade >= 65:
            print("Idoso.\n")
        