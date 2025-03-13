from random import randint
comp = randint(0, 5)
num = int(input('Informe um numero: '))
if num == comp:
    print('Acertou!!')
else:
    print('Tente novamente')