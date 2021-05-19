n = int(input())
i = 0

while (i < n):
  val = int(input())
  div = 0
  for j in range(1, val):
    if (val % j == 0):
      div += j
  if (div == val):
    print(f'{val} eh perfeito')
  else:
    print(f'{val} nao eh perfeito')  
  i += 1