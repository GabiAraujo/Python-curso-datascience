#Calculadora
#mensagem inicial ao usuário
while 1:
    print('*********Python Calculator************')
    print('Selecione o número da operação desejada')
    print('1 - Soma \n' '2 - Subtração\n' '3 - Multiplicação\n' '4 - Divisão') 

    #pedindo que o usuário selecione qual operação será realizada
    op = int(input('Digite sua opção(1/2/3/4): '))

    #números a serem operados digitados pelo usuário
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))


    if op == 1:
        r = n1+n2
        print('%d + %d = %d ' %(n1,n2,r))
    elif op == 2:
        r= n1 - n2
        print('%d - %d = %d ' %(n1,n2,r))
    elif op == 3:
        r = n1*n2
        print('%d * %d = %d ' %(n1,n2,r))
    elif op == 4:
        r = n1/n2
        print('%d / %d = %d ' %(n1,n2,r))
    else:
        print('Opção inválida')
