# 1) Solicite ao usuário digitar um texto bíblico.
# 2) Separe as palavras (cadeias de caracteres) do texto. 
# 2.1 - Armazene-as em um objeto iterável (lista). 
# 2.2 - Calcule o tamanho dessa lista e informe o tamanho pro usuário. 
# 2.3 - Verifique a lista, e para cada vez que a palavra "Jesus" for encontrada, imprima na tela: Jesus é amor!!!
# 3) Criar um menu de entrada: "1" [Escrever texto] - "2" [Sair]
# 3.1 - Programa só deve fechar se usuário escolher "Sair". 

# Obs.: O professor nos deixou livres para adaptar o assunto do exercício, que foi elaborado para a Semana Santa.

print('Digite um texto sobre o rock. Mas atenção: use a palavra "rock" quantas vezes puder e o sistema imprimirá um verso de uma música o mesmo número de vezes. Quer ver?')
texto = input()
minusculo = texto.lower()
armazena = minusculo.split(" ")
tamanho = len(armazena)
print("Seu texto tem", tamanho, "palavras")
for item in armazena:
    if item == "rock":
        print("It's a long way to the top if you wanna rock'n'roll")

# Aqui vai uma sugestão de texto para você rodar o programa:

# Rock é vida, rock é para a alma, let's rock and roll, my friend!
