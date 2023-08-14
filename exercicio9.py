'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

anos = int(input("Quantos anos você tem?"))
meses = int(input("Quantos meses você tem?"))
dias = int(input("Quantos dias você tem?"))


resultado = (anos*365)+(meses*30)+dias

print(f"A idade que você tem em dias é: {resultado}" )

