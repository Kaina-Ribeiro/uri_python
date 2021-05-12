reload = 0
while (True):
  cont = 0
  media = 0
  while (cont < 2):
    a = float(input())
    if (0 <= a <= 10):
      cont += 1
      media += a
    else: 
      print('nota invalida')

  print(f'media = {media/2:.2f}')
  
  while (True):
    print('novo calculo (1-sim 2-nao)')
    reload = float(input())
    if (reload == 1 or reload == 2): break
   
  if (reload == 2): break
  