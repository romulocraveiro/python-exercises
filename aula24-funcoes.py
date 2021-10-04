#FUNÇÃO
def func_reg(est):
    if est == "ceará" or est == "piauí" or est == "maranhão " or est == "rio grande do norte" or est == "pernambuco" or est == "paraíba" or est == "sergipe" or est == "alagoas" or est == "bahia": 
        resultado = "região Nordeste."
        return resultado
    if est == "espírito santo" or est == "minas gerais" or est == "rio de janeiro" or est == "são paulo":
        resultado = "região Sudeste."
        return resultado
    if est == "santa catarina" or est == "paraná" or est == "rio grande do sul":
        resultado = "região Sul."
        return resultado    
    if est == "mato grosso" or est == "goiás" or est == "mato grosso do sul":
        resultado = "região Centro-Oeste."
        return resultado  
    if est == "amazonas" or est == "pará" or est == "roraima" or est == "amapá" or est == "tocantins" or est == "rondônia" or est == "acre":
        resultado = "região Norte."
        return resultado 
    
#PROGRAMA PRINCIPAL
print("Digite o seu estado:")
texto = input()
est = texto.lower()
regiao = func_reg(est)
print("\nVocê mora na", regiao)
