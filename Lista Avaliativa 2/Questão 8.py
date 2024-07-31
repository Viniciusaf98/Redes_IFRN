import sys

x = int(input("Informe um número inteiro positivo : "))

if x <= 0:
    print("o número deve ser positivo.")
    sys.exit()

else:
    n = 1
    triangular = False
    while True:
        triangular_n = n * (n+1) // 2

        if triangular_n == x:
            triangular = True
            break

        if triangular_n > x:
            break

        n += 1

    if triangular:
        print(f"O número {x} é triangular.")

    else:
        print(f"O número {x} não é triangular.")
