kilometragem = float(input('Informe a kilometragem ate o destino final: '))
if kilometragem > 200:
    gasolina = kilometragem * 0.50
    print('A viagem sera mais cara! O gasto sera de {}'.format(gasolina))
else:
    gasolinaMaisb = kilometragem * 0.40
    print('Viagem mais economica! O gasto sera de {}'.format(gasolinaMaisb))
