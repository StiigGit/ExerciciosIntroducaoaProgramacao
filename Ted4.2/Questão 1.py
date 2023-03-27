#Criado por Ticiano

'''Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10. O
programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado
pelo usuário.'''


numero = float(input("Digite um número: "))


if numero > 10:
    print(f"Maior que 10 - {numero}")
elif numero < 10:
    print(f"Menor que 10 - {numero}")
else:
    print(f" O número é igual a 10 - {numero}")