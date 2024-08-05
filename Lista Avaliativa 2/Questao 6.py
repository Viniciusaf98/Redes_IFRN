valor_inicial = int(input("Informe o valor inteiro inicial da P.G : "))
quociente = float(input("Informe a razão da P.G : "))
elementos = int(input("Informe a quantidade de elementos da P.G : "))

print('='*200)
if quociente == 1:
    print("A P.G é constante.")
elif quociente == -1:
    print("A P.G é oscilante.")
elif quociente > 1:
    print("A P.G é crescente.")
elif quociente < 1 and quociente > 0:
    print("A P.G é decrescente.")
else:
    print("A P.G tem um comportamento indefinido.")

soma = 0
print("Os elementos da P.G são:")
for i in range(elementos):
    termo = valor_inicial * (quociente ** i)
    print(termo)
    soma += termo

print("A soma dos elementos da P.G é:", soma)
print('='*200)

enesima = int(input("Informe um valor inteiro correspondente à enésima posição: "))
termo_enesima = valor_inicial * (quociente ** (enesima - 1))
print(f"O valor correspondente à enésima posição {enesima} é: {termo_enesima}")
