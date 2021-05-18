cod, q = input().split(' ')
tupla = {
  1: 4,
  2: 4.50,
  3: 5,
  4: 2,
  5: 1.5,
}

q = int(q)
cod = int(cod)

print(f'Total: R$ {tupla[cod] * q:.2f}')
