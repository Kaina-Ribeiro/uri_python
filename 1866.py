n = int(input())

a = 0
while (n > 0):
  val = int(input())
  for i in range(0, val):
    if (i%2 == 0):
      a += 1
    else:
      a -= 1
  print(a)  
  a = 0
  n -= 1

