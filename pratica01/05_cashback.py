valor_compra = float(input('Informe o valor da compra: '))

if valor_compra <= 100:
    cash_back = valor_compra * 0.04
    print(f'Parabéns você recebeu R${cash_back:.2f} de Cashback!!')
elif valor_compra <= 200:
    cash_back = valor_compra * 0.06
    print(f'Parabéns você recebeu R${cash_back:.2f} de Cashback!!')
elif valor_compra <= 400:
    cash_back = valor_compra * 0.08
    print(f'Parabéns você recebeu R${cash_back:.2f} de Cashback!!')
else:
    cash_back = valor_compra * 0.1
    print(f'Parabéns você recebeu R${cash_back:.2f} de Cashback!!')
