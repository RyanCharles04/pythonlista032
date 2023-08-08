'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
'''
import math

kil = float(input("Informe o seu peso em kilos: "))
metros = float(input("Informe sua altura em metros: "))

resultado =  kil / math.pow(metros,2)

print("O seu índice de massa corporal corresponde à:", resultado)