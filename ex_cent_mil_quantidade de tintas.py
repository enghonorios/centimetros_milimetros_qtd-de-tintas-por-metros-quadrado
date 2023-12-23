p1 = float(input('Largura x Comprimento da parede 1: '))
p2 = float(input('Largura x Comprimento da parede 2: '))
p3 = float(input('Largura x Comprimento da parede 3: '))
p4 = float(input('Largura x Comprimento da parede 4: '))
ps = float(input('Largura x Comprimento do teto: '))

Mtt= p1+p2+p3+p4+ps
Centimetros= Mtt/100
Milimetros= Mtt/1000
Tinta= Mtt *3.6 #litros de tinta para pintura
Latas= Tinta/18
Massa= Mtt *1.82 #kg de massa corrida para paredes

print(f'Largura total das paredes: {Mtt}')
print(f'Transformada para centimetro: {Centimetros}')
print(f'Já para milimetros: {Milimetros}')
print(f'Quantidade de tinta para pintura: {Tinta} litros.')
print(f'Considerando a metragem acima precida de {Latas:.1f} de tinta com 18 litros para pintura.')
print(f'Irá utilizar {Massa} kg de massa corrida.')
