n = int(input("Digite a quantidade de fatores primos que um número pode ter : "))

numero = 2
consecutivos = []

while len(consecutivos) < n:
    fatores = set()
    tempo = numero
    divisor = 2
    
    while tempo > 1:
        if tempo % divisor == 0:
            fatores.add(divisor)
            while tempo % divisor == 0:
                tempo //= divisor
        divisor += 1
   
    if len(fatores) == n:
        consecutivos.append(numero)
    else:
        consecutivos = []

    numero += 1

print(f"Os primeiros {n} números consecutivos são {consecutivos}.")