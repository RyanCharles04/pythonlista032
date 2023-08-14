'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

cont = float(input("Informe o valor da conta: "))

acre = cont * 10/100

val = cont + acre

print(f"O valor da conta mais o acréscimo de 10% do garçom é: R${val:.2f}".replace(".",","))