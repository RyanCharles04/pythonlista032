'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''

nome = str(input("Informe o nome de um vendedor: "))
sal = float(input("Informe o seu salário fixo: "))
venda = float(input("Informe o total de vendas efetuadas por ele no mês em dinheiro: "))

com1 = sal * 15/100
comfin= com1

print(f"O seu nome é: {nome}")
print(f"O seu salário fixo é: R${sal:.2f}".replace(".",","))
print(f"A comissão ganha é: R${com1:.2f}".replace(".",","))
print(f"Seu salário completo é: R${comfin:.2f}".replace(".",","))


