# As notas no Suap são representadas por valores inteiros entre 0 e 100 ([0,100]).
# Escreva um programa para ler as notas de 8 (oito) estudantes. Ao final, exibir quantas notas válidas para o Suap foram informadas.

valido = 0

for i in range(8):
  nota = int(input('Nota do suap: '))
  if nota >= 0 and nota <= 100: 
    valido += 1
print(f'Foram informadas {valido} notas válidas para o Suap.')
