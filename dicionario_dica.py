dic1 = {'fisrt': 'Big Data', 'second': 10, 'tird': 5.6}
chaves = [] #lista para receber as chaves do dicionário

for keys in dic1.keys():
    chaves.append(keys) #recebendo cada chave do dicionário
    
print(chaves)#printando todas as chaves
print(chaves[1]) #printando apenas uma chave

c = (*dic1,) #outro modo de pegar as chaves do dicionário
print(c)

a = type(chaves)
b = type (c)
print(a, b)

# "c" é uma tupla e "chaves" é uma lista, a diferença entre elas é que a lista pode ser mudada