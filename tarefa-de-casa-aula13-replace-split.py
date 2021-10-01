# Instituto Conhecimento Liberta
# Professor: Geneflides Laureno
# Aluno: Romulo Craveiro

# Exercício:
# 1) Solicite ao usuário  escrever um texto.
# 2) Solicite ao usuário escrever duas palavras: 
# 2.1) a palavra a ser substituída; 
# 2.2) a palavra que substituirá a antiga. 
# 3) Imprima o texto original e o texto modificado. 
# 4) Informe quantas palavras foram encontradas no texto.

print('\nVAMOS BRINCAR COM AS PALAVRAS! No final, você trocará uma delas e saberá quantas digitou. PRIMEIRO PASSO: digite um pequeno texto:\n')
texto = input()
print('\nPRÓXIMO PASSO:\n') 
print("a) primeiro, você digitará uma palavra do seu texto que quer que seja substituída por outra;")
print("b) depois, você digitará a palavra que substituirá a primeira.\n")
print("Vamos lá?\n")
print('Digite a palavra que você quer substituir:\n')
palavra1 = input()
print('\nAgora, digite a palavra que substituirá a primeira:\n')
palavra2 = input()
troca = texto.replace(palavra1, palavra2)
print("\nTEXTO ORIGINAL:\n", texto)
print("\nTEXTO MODIFICADO:\n", troca)
armazena_palavras = troca.split(" ")
#Uma vez que, após a função split, os elementos ficam separados dentro de um array, usaremos a função len para contá-los:
conta_palavras = len(armazena_palavras) 
print("\nTotal de palavras:\n", conta_palavras)

