import sys

x = input("Informe a quantidade de elementos que a lista terá : ")

    # Verifica se a entrada é um número inteiro e positivo
if x.isdigit():
    x = int(x)
else:
    print("Erro! Você deve informar números inteiros e positivos.")
    sys.exit()


valores = []

while True:
    # Solicita ao usuário um valor inteiro
    n = input("Informe outro valor inteiro : ")

    # Verifica se a entrada é um número inteiro
    if n.isdigit() or (n[1:].isdigit() and n[0] == '-'):
        n = int(n)
    else:
        print("Erro! Você deve informar um número inteiro.")
        continue

    # Se o valor for zero, encerra o loop
    if n == 0:
        break

    # Adiciona o valor à lista e ordena a lista
    valores.append(n)
    valores.sort()

    # Remove o maior valor se a lista ultrapassar o número de elementos permitido
    if len(valores) > x:
        valores.pop()

    # Exibe a lista atualizada
    print(valores)

    # Exibe os menores valores informados
print(f"Os menores valores informados foram : {valores}")
