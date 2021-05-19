n = int(input())
i = 0
fib = []

while (i < n):
  if (i == 0 or i == 1):
    fib.append(i)
  else: 
    prox = fib[i-1] + fib[i-2]

    fib.append(prox)
  i += 1

for j in range(0, n):
  fib[j] = str(fib[j])

fib = ' '.join(fib)
print(fib)