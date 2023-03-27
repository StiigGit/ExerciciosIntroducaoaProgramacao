#Criado por Ticiano

''' Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma
mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior a 6 o aluno é
aprovado). Escrever também o resultado da média calculada'''

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

média = (nota1 + nota2) / 2

if média >= 6.0 and média <= 10.0:
    print ("Aluno aprovado!")
    print (f"Média: {média}")

elif média < 6.0 and média >= 0.0:
    print ("Aluno reprovado!")
    print (f"Média: {média}")
else:
    print("Valor incorreto!")
    