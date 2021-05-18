import random
vamp1 = 0

def battle(ev1, ev2, at, d):
  if (ev1 <= 0 or ev2 <= 0):
    if (ev1 > ev2):
      return 'ev1'
    else:
      return 'ev2'
  else: 
    dado = random.randint(1, 6)
    if(dado <= at):
      ev1 += d
      ev2 -= d
    else:
      ev1 -= d
      ev2 += d
    return battle(ev1, ev2, at, d)

while(True):
  rodada = [int(num) for num in input().strip().split(' ')]
  if (rodada[0] == 0 and rodada[1] == 0 and rodada[2] == 0 and rodada[3] == 0):
    break

  for i in range(0, 1000):
    result = battle(rodada[0], rodada[1], rodada[2], rodada[3])
    if (result == 'ev1'):
      vamp1+=1
  print(round(vamp1/10, 1))
  vamp1 = 0