# Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
# Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool
# 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser
# solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o
# número 4.
# Entrada
# A entrada contém apenas valores inteiros e positivos.
# Saída
# Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de
# combustível, conforme exemplo.

alcool = 0 # 1
gasolina = 0 # 2
diesel = 0 # 3
# FIM 4

while True:
    combustivel = int(input("Codigo do combustivel:\n\t>>>"))
    if combustivel == 1:
        alcool += 1
    elif combustivel == 2:
        gasolina += 1
    elif combustivel == 3:
        diesel += 1
    elif combustivel == 4:
        print(f"MUITO OBRIGADO \nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")
        break