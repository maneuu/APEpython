user01 = input('01 - Informe seu nome: ')
idade01 = int(input('01 - Informe sua idade: '))
user02 = input('02 - Informe seu nome: ')
idade02 = int(input('02 - Informe sua idade: '))

if idade01 > idade02:
    print(f'O {user01} é mais velho do que o {user02}')
    
elif idade02 > idade01:
    print(f'O {user02} é mais velho do que o {user01}')
    
else:
    print(f'{user01} e {user02} tem a mesma idade')
