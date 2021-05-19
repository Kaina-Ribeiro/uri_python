n = float(input())
cedulas = [100, 50, 20, 10, 5, 2]
coins = [50, 25, 10, 5, 1]

notas = int(n)
moedas = (n - notas) * 100

if (int((moedas*1000) % 10) == 9):
  moedas = round(moedas)

print('NOTAS:')
for i in cedulas: 
  print(f'{notas//i} nota(s) de R$ {i:.2f}')
  notas %= i

print('MOEDAS:')
print(f'{int(notas/1)} moeda(s) de R$ {1:.2f}')
notas %= 1

for i in coins: 
  print(f'{int(moedas/i)} moeda(s) de R$ {i/100:.2f}')
  moedas %= i
