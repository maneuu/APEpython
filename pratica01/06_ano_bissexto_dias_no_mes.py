mes = int(input('Insira o número que corresponde o mês do ano atual(2024): '))
if mes == 2:
    print('Há 29 dias no Mês de Fevereiro')
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print('HÁ 31 DIAS NO MÊS ATUAL')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('HÁ 30 DIAS NO MÊS ATUAL')
else:
    print('Insira um número de 1 a 12 que corresponda o mês atual(2024)')
