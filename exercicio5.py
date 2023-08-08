'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

soma = num1 + num2
sub1 = num1 - num2
sub2 = num2 - num1
mul = num1 * num2
div = num1 / num2
res = num1 % num2

print("A soma dos dois números é:", soma,"A subtração do primeiro pelo segundo é:", sub1,"A subtração do segundo pelo primeiro é:", sub2,"A multiplicação entre os dois números é:", mul,"A divisão do primeiro pelo segundo é:", div,"O resto da divisão é:", res)

