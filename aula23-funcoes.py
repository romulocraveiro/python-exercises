def dicionario(palavra):
    if palavra == "coragem":
        significado = "bravura"
        return significado
    else:
        significado = "\nSinônimo não disponível."
        return significado

print("Digite uma palavra:")
palavra = input()
significado = dicionario(palavra) # quando nomeamos uma função, isso se chama "assinatura de função". Infelizmente, porém, não existe a função dicionario em Python; ela fica "undefined". Então teremos que criar a função, dando um "import" uma biblioteca. Pàra isto, temos que definir "dicionario" (veja o topo do código)
print('Sinônimo de', palavra, "=" , significado)

