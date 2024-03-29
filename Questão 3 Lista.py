print('='*200)
hora_partida = int(input('Qual a hora de inicio da viagem? '))
minutos_partida = int(input('{} horas e quantos minutos? '.format(hora_partida)))
hora_chegada = int(input('Qual a hora de termino da viagem? '))
minutos_chegada = int(input('{} horas e quantos minutos? '.format(hora_chegada)))
tempo_parado = int(input('Quantos segundos foram gastos em tempo parado? '))

        #Diferenciar de um dia para o outro
if hora_chegada < hora_partida or (hora_chegada == hora_partida and minutos_chegada < minutos_partida):
    print('A viagem passou para o dia seguinte!')
    horas_total = (24 - hora_partida) + hora_chegada

else:
    horas_total = hora_chegada - hora_partida

        #Variaveis de tempo
minutos_total = minutos_chegada - minutos_partida
segundos_h = horas_total * 3600
segundos_m = minutos_total * 60
tempo_da_viagem = segundos_h + segundos_m
tempo_em_movimento = segundos_h + segundos_m - tempo_parado
tempo_em_movimento_1 = tempo_em_movimento / 3600
tempo_da_viagem_1 = tempo_da_viagem / 3600

litros = int(input('Quantos litros de combustivel foram gastos na viagem? '))
preço =  float(input('Qual o preço do combustível colocado nessa viagem? R$'))
distância = int(input('Quantal a distância percorrida (em KM) nessa viagem? '))

        #Variaveis geral
velocidade_media_global = distância / tempo_da_viagem_1
velocidade_movimento = distância / tempo_em_movimento_1
custo = preço * litros
autonomia = distância / litros
sem_sentindo = litros / tempo_da_viagem_1
gastos_h = distância / custo

print('='*200)
print('O tempo que foi gasto na viagem foi de {} segundos'.format(tempo_da_viagem))
print('A velocidade média global foi {:.2f} Km/h e a velocidade média em movimento foi {:.2f} Km/ '.format(velocidade_media_global, velocidade_movimento))
print('O custo de combustível nessa viagem foi de R${:.2f} '.format(custo))
print('A autonomia do carro foi de {:.2f} Km/L \nLitros gastos por hora {:.2f} L/h \nValor gasto por Km foi de R$ {:.2f}'.format(autonomia, sem_sentindo, gastos_h))
