import sys

numero_1 = int(input("Informe um número inteiro positivo : "))
numero_2 = int(input("Informe outro número inteiro positivo : "))

if numero_1 <= 0 or numero_2 <= 0:
    print("Ambos os número devem ser inteiros positivos")
    sys.exit()

while numero_2 != 0:
    numero_1, numero_2 = numero_2, numero_1 % numero_2

print(f"O MDC é {numero_1}")