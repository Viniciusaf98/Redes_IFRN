import sys

dia_inicial = int(input('Qual foi o dia inicial ? '))
mes_inicial = int(input('Qual foi o mês inicial ? '))
dia_final = int(input('Qual foi o dia final ? '))
mes_final = int(input('Qual foi o mês final ? '))

if mes_inicial > mes_final or (mes_inicial) == mes_final and dia_inicial > dia_final:
    print('A data inicial precisar ser menor que a data final.')
    sys.exit()

dias_inicial = 0
if mes_inicial > 1:
    dias_inicial += 31
if mes_inicial > 2:
    dias_inicial += 28
if mes_inicial > 3:
    dias_inicial += 31
if mes_inicial > 4:
    dias_inicial += 30
if mes_inicial > 5:
    dias_inicial += 31
if mes_inicial > 6:
    dias_inicial += 30
if mes_inicial > 7:
    dias_inicial += 31
if mes_inicial > 8:
    dias_inicial += 31
if mes_inicial > 9:
    dias_inicial += 30
if mes_inicial > 10:
    dias_inicial += 31
if mes_inicial > 11:
    dias_inicial += 30
if mes_inicial > 12:
    dias_inicial += 31

    dias_inicial += dias_inicial

dias_final = 0
if mes_final > 1:
    dias_final += 31
if mes_final > 2:
    dias_final += 28
if mes_final > 3:
    dias_final += 31
if mes_final > 4:
    dias_final += 30
if mes_final > 5:
    dias_final += 31
if mes_final > 6:
    dias_final += 30
if mes_final > 7:
    dias_final += 31
if mes_final > 8:
    dias_final += 31
if mes_final > 9:
    dias_final += 30
if mes_final > 10:
    dias_final += 31 
if mes_final > 11:
    dias_final += 30
if mes_final > 12:
    dias_final += 31

    dias_final += dia_final

diferença_dias = dias_final - dias_inicial

print('='*200)
print(f"{dia_inicial:02} de {mes_inicial} até {dia_final} de {mes_final} - {diferença_dias} dias.")