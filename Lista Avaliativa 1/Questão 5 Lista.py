minuto = int(input('Quantos minutos o veículo ficou no estacionamento? '))
horas = minuto // 60
if minuto <= 60:
    valor = 8.00                              
    print (f'Você terá que pagar R$ {valor:.2f}') 

elif minuto >= 61 and minuto <= 120:
    valor = 8.00 * 2                          
    print (f'Você terá que pagar R$ {valor:.2f}') 


elif minuto >= 121 and minuto <= 180:
    valor = 16.00 + 5.00                     
    print (f'Você terá que pagar R$ {valor:.2f}') 

elif minuto >= 181 and minuto <= 240:
    valor = 16.00 + (5.00 * 2)              
    print (f'Você terá que pagar R$ {valor:.2f}') 


elif horas >= 5 and horas <= 11:
    if minuto % 60 != 0:
        valor = (16.00 + 10.00) + (3.00 * (1 + horas - 4)) 
        print (f'Você terá que pagar R$ {valor:.2f}')     
    
    if minuto % 60 == 0:
        valor = (16.00 + 10.00) + (3.00 * (horas - 4))  
        print (f'Você terá que pagar R$ {valor:.2f}')     
elif minuto == 720:
    valor = 16.00 + 10 + 24.00
    print (f'Você terá que pagar R$ {valor:.2f}')

else:
    print (f'Você terá que pagar R$ 30.00 ')