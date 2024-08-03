PALAVRA_CHAVE = "WARZONE"

tentativas = 6
letras_erradas = ""
palavra_oculta = "_" * len(PALAVRA_CHAVE)

print("Bem-vindo ao Jogo da Forca!")
print("Você tem 6 tentativas.")
print("Palavra : ", palavra_oculta)

while tentativas > 0 and "_" in palavra_oculta:
    letra = input("Digite uma letra : ").upper()

    if letra in letras_erradas or letra in palavra_oculta:
        print("Você já tentou essa letra.")
        continue

    if letra in PALAVRA_CHAVE:
        nova_palavra_oculta = ""
        for i in range(len(PALAVRA_CHAVE)):
            if PALAVRA_CHAVE[i] == letra:
                nova_palavra_oculta += letra
            else:
                nova_palavra_oculta += palavra_oculta[i]
        palavra_oculta = nova_palavra_oculta
        print("Acertou! Palavra : ", palavra_oculta)
    else:
        letras_erradas += letra
        tentativas -= 1
        print("Errou! Tentativas restantes : ", tentativas)
    
    print("Letras erradas:", letras_erradas)

if "_" not in palavra_oculta:
    print("Parabéns, você venceu!")
else:
    print("Você foi enforcado! A palavra era : ", PALAVRA_CHAVE)
