v = input().split(' ')
maior = 0

for i in range(0, len(v)):
  curr = int(v[i])
  if ((curr > maior)): maior = curr

print(f'{maior} eh o maior')
