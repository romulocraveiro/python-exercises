# 1) Solicite ao usuário digitar a sua idade.
# Caso o usuário tenha menos de 75 anos:
# 2.1 - Peça-lhe para aguardar próximas fases
# 2.2 - finalize o programa
# 3 Caso o usuário tenha 75 anos ou mais:
# 3.1 - pergunte o seu nome 
# 3.2 - informe o seu nome e idade
# 3.3 - informe as modalidades de agendamento
# Desafio: propor pelo menos duas formas de resolver a questão

print("\nA PREFEITURA DE SALVADOR LHE DÁ BOAS VINDAS AO SISTEMA DE VACINAÇÃO")
print("Para saber se já chegou a sua vez de se vacinar, digite aqui a sua idade:")
idade = int(input())
if idade < 75:
    print("\nAguarde a divulgação da data de sua vacinação. Obrigada, e parabéns por sua iniciativa de se vacinar!\n")
else: 
    print("Digite o seu nome: ")
    nome = input()
    print("De acordo com os dados informados, o seu nome é", nome, "e você tem", idade, "anos." )
    print("Para fazer o agendamento, ligue para 3333 32333 ou clique aqui.")

