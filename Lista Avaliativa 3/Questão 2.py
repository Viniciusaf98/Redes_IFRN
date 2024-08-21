import sys

try:
    x = int(input("Informe a quantidade de elementos que a lista terá : "))
except ValueError:
    print("Erro! Você deve informar números inteiros. ")
    sys.exit()

if x <= 0 :
    print("Erro! A quantidade de elementos deve ser positiva. ")
    sys.exit()

valores = []

while True:
    try:
        n = int(input("Informe outro valor inteiro : "))
    except ValueError:
        print("Erro! Você deve informar um número inteiro. ")
        continue

    if n == 0:
        break

    valores.append(n)
    valores.sort()  

    if len(valores) > x:
        valores.pop()  

    print(valores)  

print(f"Os menores valores informados foram : {valores}")
