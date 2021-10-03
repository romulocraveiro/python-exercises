def dicionario(palavra):
    if palavra == "coragem":
        significado = "bravura"
        return significado
    else:
        significado = "\nSinônimo não disponível."
        return significado

print("Digite uma palavra:")
palavra = input()
significado = dicionario(palavra) # Quando nomeamos uma função, isso se chama "assinatura de função". Infelizmente, não existe a função dicionario em Python; ela fica "undefined". Então teremos que definir "dicionario" (veja o topo do código), por enquanto, aqui dentro do código.
print('Sinônimo de', palavra, "=" , significado)

