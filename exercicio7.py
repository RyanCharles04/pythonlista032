'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

num1 = float(input("Informe um valor de uma compra: "))
num2 = float(input("Informe o número de prestações escolhidas: "))

valor = num1 / num2

print("O valor das prestações é:", valor)