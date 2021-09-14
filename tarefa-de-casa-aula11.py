
#Instituto Conhecimento Liberta 
#Professor Geneflides Lareno
#Aluno: Romulo Craveiro

# 1) Solicite ao usuário escrever um pequeno texto contendo a palavra "conhecimento". 2) Calcule quantas vezes a palavra "conhecimento apareceu no texto e informe na tela o resultado"

# Olá, Flides! Para rodar o código, por gentileza, copie e cole o seguinte texto:

# O conhecimento liberta porque só ele é capaz de causar transformações profundas e duradouras. Há quem diga que o conhecimento gera melancolia. "Quanto mais conhecimento temos, mais dura a vida nos parece, e mais difícil de lidar", dizem. Entretanto, o que talvez não percebam, é que o conhecimento traz a verdade, sim, e ela é muitas vezes dura, mas não é o conhecimento em si que deprime ou alegra. É o que fazemos dele em nossas vidas, é como o colocamos em prática, não apenas para nos realizarmos, mas também para beneficiar o coletivo e contribuir minimamente para uma transformação da realidade. Em outras palavras, o conhecimento nos faz tomar decisões mais informadas para lidar criativamente com os desafios que percebemos. Conhecimento liberta!

print ('Se você digitar um texto, o computador lhe informará quantas vezes uma determinada palavra aparece! Quer ver? Escreva um pequeno parágrafo usando a palavra "conhecimento" quantas vezes puder e veja o resultado: \n')
paragrafo = input ()
conteConhecimento = paragrafo.count("conhecimento")
print('\n A palavra "conhecimento" aparece ', conteConhecimento, 'vezes.\n')


# Para poder contar também as palavras que aparecem com inicial maiúscula, usamos a função nomedavariavel.lower():

#print ('Se você digitar um texto, o computador lhe informará quantas vezes uma determinada palavra aparece! Quer ver? Escreva um pequeno parágrafo usando a palavra "conhecimento" quantas vezes puder e veja o resultado: \n')
# paragrafo = input ()
# paragrafomin = paragrafo.lower()
# conteConhecimento = paragrafomin.count("conhecimento")
# print('\n A palavra "conhecimento" aparece ', conteConhecimento, 'vezes.\n')

# Dessa vez, vai contar 7 vezes.