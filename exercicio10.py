"""
Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos
e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.
"""
nummunicipio = float(input("Qual o numero total de eleitores de um municipio?"))
votobranc = float(input("Qual a quantidade de votos brancas?"))
votovul = float(input("Qual a quantidade de votos nulos?"))

h = nummunicipio-(votovul+votobranc)
print("O valor de votos invalidos é", h)

votoval = int(input("Qual a quantidade de votos validados"))

totalvtbrc = (nummunicipio/votobranc)*100
totalvtvul = (nummunicipio/votovul)*100
totalvtval = (nummunicipio/votoval)*100

print("O resultado dos votos são:")

print("A quantidade de votos brancos são", totalvtbrc)
print("A quantidade de votos nulos são", totalvtvul)
print("A quantidade de votos validados são", totalvtval)