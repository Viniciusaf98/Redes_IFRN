valor = float(input('Digite o valor do saque : R$'))

cem_real = cinquenta_real = vinte_real = dez_real = cinco_real = dois_real = 0
um_real = cinquenta_centavo = vinte_cinco_centavo = dez_centavo = cinco_centavo = um_centavo = 0

valor_centavo = int(valor * 100)

if valor_centavo >= 10000:
    cem_real = valor_centavo // 10000
    valor_centavo %= 10000

if valor_centavo >= 5000:
    cinquenta_real = valor_centavo // 5000
    valor_centavo %= 5000

if valor_centavo >= 2000:
    vinte_real = valor_centavo // 2000
    valor_centavo %= 2000

if valor_centavo >= 1000:
    dez_real = valor_centavo // 1000
    valor_centavo %= 1000

if valor_centavo >= 500:
    cinco_real = valor_centavo// 500
    valor_centavo %= 500

if valor_centavo >= 200:
    dois_real = valor_centavo// 200
    valor_centavo %= 200

if valor_centavo >= 100:
    um_real = valor_centavo // 100
    valor_centavo %= 100

if valor_centavo >= 50:
    cinquenta_centavo = valor_centavo // 50
    valor_centavo %= 50

if valor_centavo >= 25:
    vinte_cinco_centavo = valor_centavo // 25
    valor_centavo %= 25

if valor_centavo >= 10:
    dez_centavo = valor_centavo // 10
    valor_centavo %= 10

if valor_centavo >= 5:
    cinco_centavo = valor_centavo // 5
    valor_centavo %= 5

if valor_centavo >= 1:
    um_centavo = valor_centavo

if cem_real > 0:
    print(f'Quantidade de cédulas de R$100,00 : {cem_real}')
if cinquenta_real > 0:
    print(f'Quantidade de cédulas de R$50,00 : {cinquenta_real}')
if vinte_real > 0:
    print(f'Quantidade de cédulas de R$20,00 : {vinte_real}')
if dez_real > 0:
    print(f'Quantidade de cédulas de R$10,00 : {dez_real}')
if cinco_real > 0:
    print(f'Quantidade de cédulas de R$5,00 : {cinco_real}')
if dois_real > 0:
    print(f'Quantidade de cédulas de R$2,00 : {dois_real}')
if um_real > 0:
    print(f'Quantidade de moedas de R$1,00 : {um_real}')
if cinquenta_centavo > 0:
    print(f'Quantidade de moedas de R$0,50 : {cinquenta_centavo}')
if vinte_cinco_centavo > 0:
    print(f'Quantidade de moedas de R$0,25 : {vinte_cinco_centavo}')
if dez_centavo > 0:
    print(f'Quantidade de moedas de R$0,10 : {dez_centavo}')
if cinco_centavo > 0:
    print(f'Quantidade de moedas de R$0,05 : {cinco_centavo}')
if um_centavo > 0:
    print(f'Quantidade de moedas de R$0,01 : {um_centavo}')
