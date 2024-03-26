import math
import sys

a = float(input('Digite o comprimento do lado (a) de um triângulo : '))
b = float(input('Digite o comprimeito do lado (b) de um triângulo : '))
c = float(input('Digite o comprimento do lado (c) de um triângulo : '))

if a + b < c or a + c < b or b + c < a :
    print('Não é um triângulo!')
    sys.exit()

ângulo_1 = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
ângulo_2 = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
ângulo_3 = 180 - ângulo_1 - ângulo_2

print('O triângulo possui os respectivos lados : ')
print(f'{round(ângulo_1, 2)}º')
print(f'{round(ângulo_2, 2)}º')
print(f'{round(ângulo_3, 2)}º')

if a == b and c:
    print('O triângulo é Equilatero ')
elif a == b or b == c or a == c:
    print('O triângulo é Isósceles ')
else:
    print('O triângulo é Escaleno ')

if ângulo_1 > 90 or ângulo_2 > 90 or ângulo_3 > 90:
    print('ângulo obtuso.')
elif ângulo_1 == 90 or ângulo_2 == 90 or ângulo_3 == 90:
    print('Ângulo retângular.')
else:
    print('Ângulo agudo.')