arquivo = open('notas.txt')

allmedia = []
for linha in arquivo:
    nome = linha[:3]
    notas = linha[4:]
    soma = 0
    for nota in notas.split():
        soma = soma + int(nota)
    media = soma / 4
    allmedia.append(media)

maior = max(allmedia)
menor = min(allmedia)
arquivo.close()
print (maior)
print (menor)