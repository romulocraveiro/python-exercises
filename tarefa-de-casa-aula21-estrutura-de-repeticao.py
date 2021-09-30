# 1. Solicite ao usuário digitar dois números

# 2. Solicite ao usuário escolher a operação desejada: soma, subtração, multiplicação, divisão.

# 2.1 Informe os números digitados
# 2.2 Informe a operação esolhida
# 2.3 Realize a operação
# 2.4 Informe o resultado da operação
# 2.5. Realize, no mínimo, o tratamento de uma exceção.

# 3. Criar um menu de entrada:   "1" [Calcular] - "2" [Sair]
# 3.1 - Programa só deve fechar se Usuário escolher "Sair" 

print("Digite 1 para CALCULAR e 2 para SAIR:" )
num = (int(input()))
while num == 1:
    print("\nDigite um número:")
    numero1 = (int(input()))
    print("Digite outro número:")
    numero2 = (int(input()))
    print("Você digitou", numero1, "e", numero2)
    print("\nAgora, escolha uma operação: digite 1 para soma, 2 para subtração, 3 para multiplicação, ou 4 para divisão. Digite apenas o número:")
    operacao = input()
# Exceções: 1) E se o usuário digitar algo diferente do que foi pedido (seja o que for)?
    if operacao != "1" and operacao != "2" and operacao != "3" and  operacao != "4":
        print("Opção inválida! Digite apenas um número de 1 a 4. Recarregue a página e tente novamente.\n")
    else:
        if operacao == "1":
            print("Você digitou 1 para soma.")
            print("Resultado:", numero1 + numero2)
        if operacao == "2":
            print("Você digitou 2 para subtração.")
            print("Resultado:", numero1 - numero2)
        if operacao == "3":
            print("Você digitou 3 para multiplicação.")
            print("Resultado:", numero1 * numero2 )
        if operacao == "4":
            print("Você digitou 4 para divisão.")
            print("Resultado:",numero1 / numero2)

        
    print("Digite 1 para CALCULAR e 2 para SAIR:" ) # Para estar dentro do "while", tem que ter essa indentação para esta linha e a próxima, que por sua vez é responsável por dar ao usuário a escolha de sair do loop.
    num = (int(input()))

print("\n\n******Programa finalizado.******\n\n")    

    
        
        