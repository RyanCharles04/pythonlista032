'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

kil = float(input("Informe o seu peso em kilos: "))
met = float(input("Informe sua altura em metros: "))

resultado = kil * 1000
valor = met * 100

print(f"Seu pelo em gramas corresponte à: {resultado:.0f}g")
print(f" Sua altura em centímetros corresponde à: {valor:.0f}cm")