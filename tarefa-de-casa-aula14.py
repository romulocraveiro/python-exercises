# Instituto Conhecimento Liberta
# Professor: Geneflides Laureno
# Aluno: Romulo Craveiro
# Exercício:
# 1) Solicite ao usuário escrever um texto com mais de 10 palavras
# 2) Imprima a 3ª e a 7ª palavras
# 3) Imprima as 3 primeiras palavras
# 4) Imprima apenas as 5 últimas palavras

print("\nDigite um texto com mais de 10 palavras\n")
texto = input()
armazena_palavras = texto.split(" ")

print("\nA TERCEIRA PALAVRA DO TEXTO É: " + armazena_palavras[2], "\nA SÉTIMA PALAVRA DO TEXTO É: " + armazena_palavras[6] + "\nAS TRÊS PRIMEIRAS PALAVRAS SÃO: " , armazena_palavras[:3], "\nAS 5 ÚLTIMAS PALAVRAS SÃO: " , armazena_palavras[-5:]) 

#Inicialmente eu usei o sinal de + para concatenar. Deu certo até tentar usar com o slicing. Conclusão: o sinal de mais (+) não concatena slicing e sim somente strings. Nesse caso, usa-se a vírgula. Aliás, a diferença entre vírgula e sinal de adição é que aquela cria um espaço entre caracteres ou cadeias de caracteres, enquanto este só admite concatenar strings, e sem espaço entre elas. De qualquer forma, funcionaria usar vírgula para tudo.
# Também, notei que se usar -1, não imprime a última palavra. Daí deduzi que seria [-5:] para imprimir as 5 últimas.


