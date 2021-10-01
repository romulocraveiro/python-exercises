# 1) Solicite ao usuário digitar a sua idade:
# 2) Caso o usuário tenha entre 75 e 95 anos:
#     2.1 - pergunte o nome do usuário;
#     2.2 - informe o nome e idade do mesmo;
#     2.3 - solicite ao usuário escolher a forma que ele quer se vacinar;
#     2.4 - acima de 95 anos a vacinação é exclusivamente em casa.
#     2.5 - Acima de 120 anos, cumprimente-o por ele ser um "Herói"
# 3) Caso o usuário tenha menos de 75 anos:
#     3.1 - informe ao usuário para aguardar próximas fases;
#     3.2 - finalize o programa

# Codifique usando algum operador lógico.

print("\nDigite a sua idade:")
idade = int(input())

if idade >= 96 and idade <= 120:
    print("Seu atendimento é exclusivamente em casa. Para fazer o agendamento, ligue para 3333 32333 ou clique aqui.\n")

if idade > 120:
    print("Parabéns! Chegar à sua idade é para pessoas heróicas!")
        
else:
    if idade >=75 and idade <=95:
        print("\nDigite o seu nome:")
        nome = input()
        print("\nDe acordo com os dados informados, o seu nome é", nome, "e você tem", idade, "anos.")
        print("Agora, escolha como quer se vacinar: digite C se quiser que seja em casa ou S se quiser que seja no shopping:")
        opcao = input()
        uppercase = opcao.upper()
    
        if uppercase == "C":
            print("\nVocê escolheu se vacinar em casa. Para fazer o agendamento, ligue para 3333 32333 ou clique aqui.\n")
        else:
            if uppercase == "S":
                print("\nVocê escolheu se vacinar no shopping. Use máscara e leve álcool em gel ;-)\n")
    else:
        print("\nAguarde a divulgação da data de sua vacinação. Obrigada, e parabéns por sua iniciativa de se vacinar!\n")