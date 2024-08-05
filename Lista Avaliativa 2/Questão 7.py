valor_inicial = int(input("Informe o valor inteiro inicial da P.A : "))
razao = int(input("Informe a razão da P.A : "))
elementos = int(input("Informe a quantidade de elementos da P.A : "))

print('='*200)
print("Os valores da P.A são : ")
for i in range(elementos):
    elemento = valor_inicial + i * razao
    print(elemento, end=" ")

if razao == 0:
    print("A P.A é constante. ")
elif razao > 0:
    print("A P.A é crescente. ")
else:
    print("A P.A é decrescente. ")

soma = 0
for i in range(elementos):
    soma += valor_inicial + i * razao
print(f"A soma dos elementos da P.A é {soma}")
print('='*200)

enesima = int(input("Informe um valor inteiro correspondente à enésima posição : "))

termo_enesima = valor_inicial + (enesima - 1) * razao
print(f"O valor correspondente à enésima posição {enesima} é: {termo_enesima}")