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
if operacao != "1" and operacao != "2" and operacao != "3" and  operacao != "4":
    print("Opção inválida! Digite apenas um número de 1 a 4. Recarregue a página e tente novamente.\n")
else: # O código rodaria mesmo sem esta linha de comando, contanto que de desfizessem as indentações dos ifs abaixo.
    if operacao == "1":
        print("Você digitou 1 para soma.")
        soma = numero1 + numero2 # Seria possível também não criar as variáveis de operações e apenas escrever os cálculos como um dos argumentos da função print. Assim: print("Resultado", numero1 + numero2). Veja isso em tarefa-de-casa-aula21.py
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

print("\n\n******Programa finalizado.******\n\n")

# Se, em vez de usar o primeiro if do código acima (com "and") eu simplesmente usasse o bloco de "else" abaixo, o programa faria os cálculos mas imprimiria a mensagem abaixo exceto se a escolha do usuário fosse "4". Provavelmente porque o "else" estaria ligado ao último if.

# else:
#     print("Opção inválida! Digite apenas o número. Recarregue a página e tente novamente.\n")


    

