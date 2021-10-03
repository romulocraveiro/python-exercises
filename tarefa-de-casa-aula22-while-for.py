# 1) Solicite ao usuário digitar um texto bíblico.
# 2) Separe as palavras (cadeias de caracteres) do texto. 
# 2.1 - Armazene-as em um objeto iterável (lista). 
# 2.2 - Calcule o tamanho dessa lista e informe o tamanho pro usuário. 
# 2.3 - Verifique a lista, e para cada vez que a palavra "Jesus" for encontrada, imprima na tela: Jesus é amor!!!
# 3) Criar um menu de entrada: "1" [Escrever texto] - "2" [Sair]
# 3.1 - Programa só deve fechar se usuário escolher "Sair". 

# Obs.: O professor nos deixou livres para adaptar o assunto do exercício, que foi elaborado para a Semana Santa.

# Aqui vai uma sugestão de texto para você rodar o programa:

# Rock é vida, rock é para a alma, let's rock and roll, my friend!

print("\nDigite 1 para CONTINUAR, ou qualquer outro número para SAIR:\n" )
num = (int(input()))
while num == 1:
    print('\nDigite um texto usando a palavra "rock" quantas vezes puder. O sistema lhe informará quantas palavras ele tem e imprimirá o verso de uma música o mesmo número de vezes em que a palavra aparecer no seu texto. Quer ver?')
    print("\nDigite o seu texto:\n")
    texto = input()
    minusculo = texto.lower()
    armazena = minusculo.split(" ")
    tamanho = len(armazena)
    print("\nSeu texto tem", tamanho, "palavras. Agora, vamos ao verso da música:\n")
    for item in armazena:
        if item == "rock":
            print("It's a long way to the top if you wanna rock'n'roll!")
    print("\nDigite 1 para CONTINUAR ou qualquer outro número para SAIR:" )
    num = (int(input()))
print("\n\n=======THE END=======\n\n")
# Aqui vai uma sugestão de texto para você rodar o programa:
# Rock é vida, rock é para a alma, let's rock and roll, my friend!
