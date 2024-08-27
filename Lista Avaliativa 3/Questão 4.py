import math, random

n = int(input("Informe o número de elementos : "))
if n <= 0:
    print("O número de elementos deve ser um número positivo.")
    exit()

    # Gerar a lista de números aleatórios
lista = [random.randint(0, 99) for _ in range(n)]

    # Cálculo da média
media = sum(lista) / n

    # Cálculo da mediana
ordem = sorted(lista)
if n % 2 == 0:
    mediana = (ordem[n // 2 - 1] + ordem[n // 2]) / 2
else:
    mediana = ordem[n // 2]

    # Cálculo da variância populacional
variancia = sum((x - media) ** 2 for x in lista) / n

    # Cálculo do desvio padrão populacional
desvio_padrao = math.sqrt(variancia)

print(f"Lista : {lista}")
print('='*30)
print(f"Média : {media:.2f}")
print('='*30)
print(f"Mediana : {mediana:.2f}")
print('='*30)
print(f"Variância : {variancia:.2f}")
print('='*30)
print(f"Desvio padrão : {desvio_padrao:.2f}")
