
# =============DESAFIO FINAL: DIAS DA SEMANA EM LÍNGUA RUSSA=================

# Inspirado por uma aula em que o professor Flides nos ensinou funções usando um dicionário como exemplo, por eu estar aprendendo russo, resolvi criar um dicionário português-russo dos dias da semana:

# FUNÇÕES
def dicionario(dia):
    if dia == "segunda-feira":
        traducao = "понидельник (pronuncia-se /pa-nidjêlnik/)"
        return traducao
    if dia == "terça-feira":
        traducao = "вторник (pronuncia-se /ftórnik/)"
        return traducao
    if dia == "quarta-feira":
        traducao = "среда (pronuncia-se /sriedá/)" 
        return traducao
    if dia == "quinta-feira":
        traducao = "четверг (pronuncia-se /tchítvierg/)"
        return traducao
    if dia == "sexta-feira":
        traducao = "пятница (pronuncia-se /piát-nitzá/)"
        return traducao
    if dia == "sábado":
        traducao = "суббота (pronuncia-se /subóta/)"
        return traducao
    if dia == "domingo":
        traducao = "воскресенье (pronuncia-se /vascreciénie/)"
        return traducao
def tratamento_de_erro(escrita):
    while escrita != "segunda-feira" and escrita != "terça-feira" and escrita != "quarta-feira"  and escrita != "quinta-feira" and escrita != "sexta-feira" and escrita != "sábado" and escrita != "domingo": 
        print("\nOPÇÃO INVÁLIDA. Verifique a grafia das palavras. Lembre-se de usar acentos ou hífen, quando for o caso.\n")
        print("Digite o dia da semana em português:")
        escrita = input()
    return escrita
# PROGRAMA PRINCIPAL
print("\nQuer saber como dizer os dias da semana em russo?")
print("Digite o dia da semana em português:")
entrada = input()
dia = entrada.lower()
# VALIDAÇÃO DAS PALAVRAS E TRATAMENTO DE ERROS DO USUÁRIO 
dia = tratamento_de_erro(dia)
russo = dicionario(dia)
print(dia, "em russo:", russo, "\n")
