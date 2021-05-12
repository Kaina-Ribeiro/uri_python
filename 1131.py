g = 0
grenais = 0
inter = 0
gremio = 0
empates = 0

while (True):
  grenais += 1
  n1, n2 = input().split(' ')

  n1 = int(n1)
  n2 = int(n2)

  if (n1 == n2): empates += 1
  if (n1 > n2): inter += 1
  if (n2 > n1): gremio += 1

  while(g != 1 and g != 2):
    print('Novo grenal (1-sim 2-nao)')
    g = int(input())
  if (g==2): break
  if (g==1): g = 0

print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empates}')
if (empates == grenais): print('Nao houve vencedor')
else: print(f'{"Inter" if inter > gremio else "Gremio"} venceu mais')