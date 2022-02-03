l1 = ('aileron', 'flap', 'leme', 'profundor')
i = 0
surperficies_comando = list(l1)
while i < 2:
    sc = input('digite mais uma superficie de comando:')
    surperficies_comando.append(sc)
    i+=1
print(surperficies_comando)

