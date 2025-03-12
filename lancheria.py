
batata = 15.30
hamburguer = 27.90
soda_italiana = 13.50
#Solicite ao usuário que insira a quantidade de cada item que deseja pedir.
 
quantidade_batata = int(input("Entre com a quantidade desejada de batata: "))
quantidade_hamburguer = int(input("Entre com a quantidade desejada hamburguer: "))
quantidade_soda_italiana = int(input("Entre com a quantidade desejada de soda italiana: "))

#Calcule o preço total do pedido, multiplicando o preço de cada item pela quantidade escolhida pelo usuário. Veja!

pedido = (batata*quantidade_batata) + (hamburguer* quantidade_hamburguer) + (soda_italiana*quantidade_soda_italiana)

print(f'O pedido total foi de {pedido}')