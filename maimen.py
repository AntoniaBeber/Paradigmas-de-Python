num1 = int(input('Informe um numero: '))
num2 = int(input('Informe um numero: '))
num3 = int(input('Informe um numero: '))

maiornum = max(num1, num2, num3)
menornum = min(num1, num2, num3)
print('O maior numero eh o {}'.format(maiornum) + 'e o menor numero eh o {}'.format(menornum))