import math
a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = (b*b) - (4 * (a) * (c))

if (delta <= 0):
  print('Impossivel calcular')
else:
  x1 = -b + math.sqrt(delta)
  x2 = -b - math.sqrt(delta)

  if ((x1 == 0) or (x2 == 0)):
    print('Impossivel calcular')
  else: 
    x1 = x1 / (2*a)
    print(f'R1 = {x1:.5f}')

    x2 = x2 / (2*a)
    print(f'R2 = {x2:.5f}')