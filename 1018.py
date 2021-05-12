val = int(input())
values = [100, 50, 20, 10, 5, 2, 1]

print(val)
for i in values: 
  print(f'{val//i} nota(s) de R$ {i},00')
  val %= i
