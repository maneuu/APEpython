total_chash_back = 0 
total_compra = 0
for i in range(400):
  compra = float(input('\nINFORME O VALOR DA COMPRA: '))
  if compra <= 100:
    cash_back = compra * 0.04
  elif compra <= 200:
      cash_back = compra * 0.06
  elif compra <= 400:
      cash_back = compra * 0.08
  else:
      cash_back = compra * 0.1
  total_chash_back += cash_back
  total_compra += compra

print(total_chash_back)
print(total_compra)

