cod1, num1, val1 = input().split()
cod2, num2, val2 = input().split()

cod1 = int(cod1)
cod2 = int(cod2)

num1 = int(num1)
num2 = int(num2)

val1 = float(val1)
val2 = float(val2)

val = (int(num1) * float(val1)) + (int(num2) * float(val2))

print('VALOR A PAGAR: R$ %0.2f'%val)