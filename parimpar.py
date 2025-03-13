numero = int(input('Informe um numero:  '))
resultado = numero % 2

if resultado == 0:
    print('O numero {} eh par'.format(numero))
else:
    print('O resultado eh {} impar'.format(numero))