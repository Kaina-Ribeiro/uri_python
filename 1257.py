import string

n = int(input())

while(n > 0 ):
  t = int(input())
  count = 0
  entry = 0
  while(t > 0):
    val = input()
    for i in range(0, len(val)):
      count = count + string.ascii_lowercase.index((val[i]).lower()) + entry + i
    entry += 1
    t -= 1

  print(count)
  n -= 1