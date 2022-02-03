def soma_pares(n):
    soma = 0
    for i in range(0, n, 2):
        soma+=i
    print(soma)

inteiro = int(input('digita o numero ai mano: '))

soma_pares(inteiro)
        