def mdc(n1, n2):
  if (n2 == 0):
    return n1
  else:
    return mdc(n2, n1 % n2)

trocas = int(input())
for i in range(trocas):
  numeros = [int(num) for num in input().strip().split(' ')]
  print(mdc(numeros[0], numeros[1]))