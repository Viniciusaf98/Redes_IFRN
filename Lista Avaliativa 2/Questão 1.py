massa_inicial = float(input("Informe a massa inicial (em gramas): "))

massa = massa_inicial
segundos = 0

while massa >= 0.5:
    massa /= 2
    segundos += 50

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_2 = segundos % 3600 % 60

print(f"Massa Inicial: {massa_inicial} gramas.")
print(f"Massa Final: {massa} gramas.")
print(f"Tempo total: {horas} horas, {minutos} minutos e {segundos_2} segundos.")