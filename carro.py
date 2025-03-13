velocidadeatual = float(input("Informe a velocidade do carro: "))
velocidademax = 80.00  
diferencavel = velocidadeatual - velocidademax
valorMulta = diferencavel * 7  

if velocidadeatual > velocidademax:
    print(f"Você está ultrapassando o limite máximo de velocidade! Sua multa é no valor de R${valorMulta:.2f}.")
else:
    print("Parabéns, você está respeitando as regras de trânsito!")
