n = int(input("Digite a quantidade de fatores primos: "))

contador = 0  
num = 2  
inicio_sequencia = 0

while contador < n:
    fatores_primos = 0
    num2 = num  
    divisor = 2  
    while divisor * divisor <= num2:
        if num2 % divisor == 0:
            fatores_primos += 1
            while num2 % divisor == 0:
                num2 //= divisor
        divisor += 1
    
    if num2 > 1:
        fatores_primos += 1
    
    if fatores_primos == n:
        if contador == 0:
            inicio_sequencia = num
        contador += 1
    else:
        contador = 0
    
    if contador == n:
        numeros = ''
        for i in range(n):
            if i != 0:
                numeros += ', '
            numeros += str(inicio_sequencia + i)
        print(f"Os primeiros {n} números consecutivos são: {numeros}.")
        break
    
    num += 1