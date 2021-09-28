# 1. Solicite ao usuário digitar dois números

# 2. Solicite ao usuário escolher a operação desejada: soma, subtração, multiplicação, divisão.
# 2.1 Informe os números digitados
# 2.2 Informe a operação esolhida
# 2.3 Realize a operação
# 2.4 Informe o resultado da operação

# 3. Realize, no mínimo, o tratamento de uma exceção.

print("\nDigite um número:")
numero1 = (int(input()))
print("Digite outro número:")
numero2 = (int(input()))
print("Você digitou", numero1, "e", numero2)
print("\nAgora, escolha uma operação: digite 1 para soma, 2 para subtração, 3 para multiplicação, ou 4 para divisão. Digite apenas o número:")
operacao = input()
# Exceções: 1) E se o usuário digitar algo diferente do que foi pedido (seja o que for)?
if operacao != "1" or operacao != "2" or operacao != "3" or operacao != "4":
    print("Opção inválida! Digite apenas o número. Recarregue a página e tente novamente.\n")
else:
    if operacao == "1":
        print("Você digitou 1 para soma.")
        soma = numero1 + numero2
        print("Resultado:", soma)
    if operacao == "2":
        print("Você digitou 2 para subtração.")
        subtracao = numero1 - numero2
        print("Resultado:", subtracao)
    if operacao == "3":
        print("Você digitou 3 para multiplicação.")
        multiplicacao = numero1 * numero2
        print("Resultado:", multiplicacao)
    if operacao == "4":
        print("Você digitou 4 para divisão.")
        divisao = numero1 / numero2
        print("Resultado:", divisao)
    
        

        


