al = 0
gas = 0
di = 0

while (True):
  n = int(input())
  if (n == 1): al+=1 
  if (n == 2): gas+=1
  if (n == 3): di+=1
  if (n == 4): break

print('MUITO OBRIGADO')
print(f'Alcool: {al}\nGasolina: {gas}\nDiesel: {di}')