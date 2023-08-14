"""
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
"""
num1 = float(input("Informe o número total de eleitores do município:"))
num2 = float(input("Informe o número total de votos brancos:"))
num3 = float(input("Informe o número de votos nulos:"))
num4 = float(input("Informe o número de votos válidos:"))

total1 = (num2/num1) * 100
total2 = (num3/num1) * 100
total3 = (num4/num1) * 100

print("O resultado dos votos são:")

print(f"A quantidade de votos brancos em percentual é: {total1:.0f}%")

print(f"A quantidade de votos nulos em percentual é: {total2:.0f}%")
print(f"A quantidade de votos validados em percentual é: {total3:.0f}%")
