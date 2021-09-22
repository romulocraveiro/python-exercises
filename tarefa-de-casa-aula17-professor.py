# Solução do professor Flides

print("Digite sua idade:")
idade = int(input())
if idade < 75:
    print("Favor aguardar novas fases")
else:
    print("Digite o seu nome")
    nome = input()
    print("\nOlá,", nome, ". Sua idade é: ", idade, ".")
    if idade >= 95:
        print("Ok, aguarde sua vacina em casa.")
    else:
        print("Escolha Vacina em Casa(C) ou Shopping(S)")
        local = input()
        opcao = local.lower()
        if opcao == "c":
            print(nome, ", logo nossa equipe irá até sua casa!")
        else:
            print(nome, ", compareça ao Shopping!!")