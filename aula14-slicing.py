print("Digite uma palavra:")
palavra = input()
# print("\nÍndice 2:", palavra[2])
print("\nÍndice 5:", palavra[5])
print("\nSlicing 2:", palavra[:2])
print("\nSlicing 5:", palavra[:5])
print("\nSlicing 3-5:", palavra[3:5]) # Não conta o último (não imprime)
print("\nSlicing 1-3:", palavra[1:3])


# Mais informações sobre slicing
# x = "my string"

# x[start:end] 	# items start through end-1
# x[start:]    	# items start through the rest of the list
# x[:end]      	# items from the beginning through end-1
# x[:]         	# a copy of the whole list

# Fonte: https://www.pythonforbeginners.com/dictionary/python-slicing