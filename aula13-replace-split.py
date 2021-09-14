print('\nDigite um pequeno texto usando a palavra "refrigerante":')
texto = input()
palavrasMinusculas = texto.lower()#Senão o programa não considera a palavra caso o usuário inicie a frase com ela
troca = palavrasMinusculas.replace("refrigerante", "vinho")
inicialMaiuscula = troca.capitalize() #Senão será impressa a primeira palavra da frase com inicial minúscula
print("\nTexto Modificado:\n", inicialMaiuscula)
print('\nDigite um novo texto usando a palavra "refrigerante":')
texto1 = input()
armazena_palavras = texto1.split(" ")
print("\n Texto original: \n", texto)
print("Texto novo: ", texto1)
print("\nCadeias de caracteres separados e armazenados em vetor:\n", armazena_palavras)
print("\nTerceira cadeia de caracteres: ", armazena_palavras[2])



