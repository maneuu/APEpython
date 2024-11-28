# Escreva um programa para ler os votos ("SIM" ou "NAO"”) de 80 (oitenta) pessoas. Ao final, calcular e exibir a porcentagem de votos "SIM", votos "NAO" e votos inválidos.

cont_s = 0
cont_n = 0
cont_i = 0

for i in range(10):
  voto = input(f'{i+1} - SIM(s) OU NÃO(n): ') 
  voto = voto.lower()
  if voto == 's':
    cont_s += 1
  elif voto == 'n':
    cont_n += 1
  else:
    cont_i += 1

total = cont_s + cont_n + cont_i
cont_s = cont_s * 100/(total)
cont_n = cont_n * 100/(total)
cont_i = cont_i * 100/(total)

print(f'Votos sim: {cont_s:.1f}%\nVotos não: {cont_n:.1f}%\nVotos inválidos: {cont_i:.1f}%')