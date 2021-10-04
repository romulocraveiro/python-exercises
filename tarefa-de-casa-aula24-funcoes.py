# 1) Solicite ao usuário digitar [SIM] ou [Não].
# 2) Solicite ao usuário responder a 4 perguntas:
# 2.1) Tem sintomas febris?
# 2.2) Tem sintomas de tosse?
# 2.3) Tem sintomas de falta de paladar?
# 2.4) Tem sintomas de falta de olfato?
# 3) Consolide as respostas e informe ao usuário:
# 3.1 Caso todas as respostas sejam sim: usuário deve ir urgente o médico.
# 3.2 Caso a resposta ao item 2.3 ou item 2.4 seja sim: usuário deve ir urgente o médico.
# 3.3 Caso as respostas ao item 2.3 e item 2.4 sejam não:usuário deve aguardar em casa. 

# FUNÇÃO
def ir_ao_medico(paladar, olfato): # As respostas a febre e tosse são irrelevantes para o funcionamento da lógica desta função
    if paladar == "sim" or olfato == "sim":
        orientacao = "Vá ao médico com urgência!"
        return orientacao
    else:
        if paladar == "não" and olfato == "não":
            orientacao = "Aguarde em casa."
            return orientacao
        if paladar == "nao" and olfato == "nao":
            orientacao = "Aguarde em casa."
            return orientacao
def valida_resposta(respx):
    while respx != "sim" and respx != "não" and respx != "nao":
        print("Por favor, digite sim ou não:")
        respx = input() # Lembrando que esta linha para o loop, pois vai passar a considerar a nova resposta do usuário.
    return respx
# PROGRAMA PRINCIPAL
print("***AVALIAÇÃO DE SINTOMAS DE COVID***")
print("Para responder às perguntas, digite SIM ou NÃO" )
# COLETA DE DADOS
print("Você tem febre?")
fever = input()
febre = fever.lower()
febre = valida_resposta(febre)
print("Você tem tosse?")
cough = input()
tosse = cough.lower()
tosse = valida_resposta(tosse)
print("Você tem falta de paladar?")
taste = input()
paladar = taste.lower()
paladar = valida_resposta(paladar)
print("Você tem falta de olfato?")
smell = input()
olfato = smell.lower()
olfato = valida_resposta(olfato)
# LÓGICA DE TESTE
orientacao = ir_ao_medico(paladar, olfato)
print(orientacao)

