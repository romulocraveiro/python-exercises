# 1) Ask the user to type a word. E.g.: Knowledge
# 2) Based on such word, print another one. E.g: Know

print('\nType the word "listen" (without the quotation marks) and the computer will show you an anagram:\n')
word=input()
lowerCase= word.lower()
print(lowerCase[2], lowerCase[1],  lowerCase[0], lowerCase[4], lowerCase[5],  lowerCase[3], "\n")
print("Cool, right? Food for thought...")
