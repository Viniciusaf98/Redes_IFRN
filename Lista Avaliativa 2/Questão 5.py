import sys

n = int(input("Informe um valor inteiro positivo : "))

if n <= 0:
    print("O valor não é inteiro positivo.")
    sys.exit()
else:
    contagem = 0

    while n > 0:
        n = n // 10
        contagem += 1

    print(f"O valor informado possui {contagem} dígitos.")