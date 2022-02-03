word = input("Digte a palavra par ser conferida:")
NL = len(word)
a = 0
b = -1
k = 0
for i in range(1, NL+1): #numeros de vezes que vai conferir 
    if word[a] == word[b]:
        k+=1
    a+=1
    b-=1
    
if k == NL:
    print('É palíndromo') #permance igual se é lida de trás para frente
else:
    print('Não é palíndromo')