# Instituto Conhecimento Liberta
# Professor: Geneflides Laureno
# Aluno: Romulo Craveiro
# Exercício:
# 1) Solicite ao usuário escrever um texto:
# 1.1 - que deve possuir, no mínimo, 10 cadeias de caracteres.
# 2) Caso o texto possua menos de 10 cadeias de caracteres:
# 2.1 - informe ao usuário a quantidade de cadeias de caracteres que existem no texto;
# 2.2 - finalize o programa.
# 3) Caso o texto possua mais de 10 cadeias de caracteres:
# 3.1 - informe ao usuário a quantidade de cadeias de caracteres existentes
# 3.2 - informe ao usuário as 3 últimas cadeias de caracteres

print('\nDigite um texto com um mínimo de 10 palavras e tecle "Enter": \n')
cadeias_de_caracteres = input()
armazena = cadeias_de_caracteres.split(" ")
quantidade = len(armazena)

if quantidade < 10:
    print("\nOh! Seu texto tem ", quantidade, "palavras, e as instruções pedem 10. Sorry, pal, Game Over!")
else:
    print("\nSeu texto tem ", quantidade, "palavras. Parabéns! Você seguiu corretamente as instruções. \nEstas são as três últimas palavras do seu texto: ", armazena[-3:], "\n")
