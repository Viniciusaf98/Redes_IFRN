import sys

num = int(input("Informe um número inteiro positivo : "))

if num <= 0:
    print("O número informado não é um inteiro positivo")
    sys.exit()

num_original = num
num_digitos = 0
temp = num

while temp > 0:
    num_digitos += 1
    temp //=10

soma_potencias = 0
temp = num
while temp > 0:
    digito = temp % 10
    valor_digito = digito

    for _ in range(num_digitos - 1):
        valor_digito *= digito
    soma_potencias += valor_digito
    temp //= 10

if soma_potencias == num_original:
    print(f"{num_original} é um número de Armstrong.")

else:
    print(f"{num_original} não é um número de Armstrong.")