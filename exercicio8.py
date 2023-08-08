'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda.Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

num1 = float(input("Informe o preço de custo de um produto:"))
num2 = float(input("Informe o percentual de custo:"))

resultado = num1 * num2/100

print("O valor da venda é:", resultado)

