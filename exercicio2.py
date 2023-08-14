'''
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia.
'''

hora = int(input("Informe o valor da horas atuais: "))
min = int(input("Informe o valor dos minutos atuais: "))

val = (hora * 60) + min

print(f"Já se passaram: {val}"," minutos desde as 00:00h deste dia")