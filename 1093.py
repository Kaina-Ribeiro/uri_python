from math import ceil
lados_dado = 6

while True:
  ev1, ev2, at, d = [int(num) for num in input().split(' ')]

  if (ev1 == 0 and ev2 == 0 and at == 0 and d == 0):
    break

  v1, v2 = ceil(ev1/d), ceil(ev2/d)
  print(v1, v2)
  if (at == 3):
    print(at, '??')
    res = (v1/(v1 + v2)) * 100
    print(res)
    print('{:.1f}'.format(res))
  else:
    dado = 1 - (lados_dado - at)/lados_dado
    print(dado)
    dado = (1 - dado)/dado
    print(dado)
    res = (1 - pow(dado, v1))/(1 - pow(dado, v1+v2)) * 100
    print('{:.1f}'.format(res))