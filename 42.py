a, b, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

v = [a, b, c]
old = v.copy()

for i in range(0, len(v)):
  for j in range(0, len(v)):
    if (v[i] < v[j]):
      temp = v[i]
      v[i] = v[j]
      v[j] = temp

for i in v:
  print(i)

print()

for i in old:
  print(i)
