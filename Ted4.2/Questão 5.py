#Criado por Ticiano


'''Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e
escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior
ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.'''

saldo = 1000
débito = 999
crédito = 150

saldo_atual = (saldo - débito) + crédito

if saldo_atual > 0:
    print(f"O saldo R${saldo_atual} atual é positivo.")
else:
    print(f"O saldo R${saldo_atual} atual é negativo.")