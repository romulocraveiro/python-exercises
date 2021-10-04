# 1. Solicite ao usuário digitar dois números

# 2. Solicite ao usuário escolher a operação desejada: 

# 2.1 Operações:soma, subtração, multiplicação, divisão.

# 2.2 Caso a operação seja <Divisão>:
# 2.2.1 Realize uma chamada de função, passando os dois números
# 2.2.2 A função deverá receber os dois números, realisar a divisão e devolver o resultado

# 2.3 Imprima na tela o resultado da operação.

# 3. Criar um menu de entrada:   "1" [Calcular] - "2" [Sair]
# 3.1 - Programa só deve fechar se Usuário escolher "Sair" 

def divisao(numero1, numero2):
        resultado = numero1 / numero2
        return resultado
        
print("\nDigite 1 para CALCULAR ou qualquer outro número para SAIR:" )
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
        print("Opção inválida! Digite apenas um número de 1 a 4.\n")
        print("Vamos recomeçar:\n")
    else:
        if operacao == "1":            
            print("Resultado da soma:", numero1 + numero2)
        if operacao == "2":         
            print("Resultado da subtração:", numero1 - numero2)
        if operacao == "3":            
            print("Resultado da multiplicação:", numero1 * numero2)
        if operacao == "4":
            div = divisao(numero1, numero2) # Aqui fazemos a função receber os dois números. 
            print("Resultado da divisão:", div)
    print("\nDigite 1 para CALCULAR ou qualquer outro número para SAIR:") 
    num = (int(input()))

print("\n\n******Programa finalizado.******\n\n")    