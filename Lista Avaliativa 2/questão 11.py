print('='*200)

x_inicial = int(input("Informe a coordenada de X inicial : "))
y_inicial = int(input("Informe a coordenada de Y inicial : "))
comandos = input("Informe os comandos de movimento do robô (U, D, R, L, O, N, E, W) : ").upper()

x_atual = x_inicial
y_atual = y_inicial
movimentos_validos = 0
movimentos_executados = ""

for comando in comandos:
    if comando == "U":
        y_atual += 1
        movimentos_validos += 1
        movimentos_executados += "U"
    elif comando == "D":
        y_atual -= 1
        movimentos_validos += 1
        movimentos_executados += "D"
    elif comando == "R":
        x_atual += 1
        movimentos_validos += 1
        movimentos_executados += "R"
    elif comando == "L":
        x_atual -= 1
        movimentos_validos += 1
        movimentos_executados += "L"
    elif comando == "O":
        x_atual -= 1
        y_atual += 1
        movimentos_validos += 1
        movimentos_executados += "O"
    elif comando == "N":
        x_atual += 1
        y_atual += 1
        movimentos_validos += 1
        movimentos_executados += "N"
    elif comando == "E":
        x_atual += 1
        y_atual -+ 1
        movimentos_validos += 1
        movimentos_executados += "E"
    elif comando == "W":
        x_atual -= 1
        y_atual -= 1
        movimentos_validos += 1
        movimentos_executados += "W"

print('='*200)
print(f"Posição inicial de X foi {x_inicial} e de Y foi {y_inicial}")
print(f"Posição final de X foi {x_atual} e de Y foi {y_inicial}")
print(f"Quantidade de movimentos válidos executados : {movimentos_validos}")
print(f"Os movimentos executados foram : {movimentos_executados}")

if x_inicial > 0 and y_inicial > 0:
    quadrante_inicial = "No Quadrante 1"
elif x_inicial < 0 and y_inicial > 0:
    quadrante_inicial = "No Quadrante 2"
elif x_inicial < 0 and y_inicial < 0:
    quadrante_inicial = "No Quadrante 3"
elif x_inicial > 0 and y_inicial < 0:
    quadrante_inicial = "No Quadrante 4"
elif x_inicial == 0 and y_inicial != 0:
    quadrante_inicial = "No eixo Y"
elif x_inicial != 0 and y_inicial == 0:
    quadrante_inicial = "No eixo X"
else:
    quadrante_inicial = "Na Origem"

if x_atual > 0 and y_atual > 0:
    quadrante_final = "No Quadrante 1"
elif x_atual < 0 and y_atual > 0:
    quadrante_final = "No Quadrante 2"
elif x_atual < 0 and y_atual < 0:
    quadrante_final = "No Quadrante 3"
elif x_atual > 0 and y_atual < 0:
    quadrante_final = "No Quadrante 4"
elif x_atual == 0 and y_atual != 0:
    quadrante_final = "No eixo Y"
elif x_atual != 0 and y_atual == 0:
    quadrante_final = "No eixo X"
else:
    quadrante_final = "Na Origem"

print(f"O quadrante inicial foi : {quadrante_inicial}")
print(f"O quadrante final foi : {quadrante_final}")