#Criado por Ticiano#



maçã = int(input('Digite a quantidade de maçãs que deseja comprar:  '))

valor_normal = float(maçã* 1.30)
valor_promoção = float(maçã* 1.00)

if maçã <= 12:
    print(f'Valor da compra: R${valor_normal}')
elif maçã > 12:
    print(f'Valor da compra: R${valor_promoção}')
