mensagem = input("Informe a mensagem : ")
palavra_chave = input("Informe a chave : ")

mensagem_filtrada = ""
for caractere in mensagem:
    if caractere.isalpha():
        mensagem_filtrada += caractere.upper()

palavra_chave_filtrada = ""
for caractere in palavra_chave:
    if caractere.isalpha():
        palavra_chave_filtrada += caractere.upper()

palavra_chave_repetida = ""
for i in range(len(mensagem_filtrada)):
    palavra_chave_repetida += palavra_chave_filtrada[i % len(palavra_chave_filtrada)]

mensagem_cifrada = ""
for i in range(len(mensagem_filtrada)):
    letra_mensagem = mensagem_filtrada[i]
    letra_chave = palavra_chave_repetida[i]
    
    valor_mensagem = ord(letra_mensagem) - ord('A')
    valor_chave = ord(letra_chave) - ord('A')
    
    valor_cifrado = (valor_mensagem + valor_chave) % 26
    
    letra_cifrada = chr(valor_cifrado + ord('A'))
    
    mensagem_cifrada += letra_cifrada

mensagem_descriptografada = ""
for i in range(len(mensagem_cifrada)):
    letra_cifrada = mensagem_cifrada[i]
    letra_chave = palavra_chave_repetida[i]
    
    valor_cifrada = ord(letra_cifrada) - ord('A')
    valor_chave = ord(letra_chave) - ord('A')
    
    valor_mensagem = (valor_cifrada - valor_chave + 26) % 26
    
    letra_mensagem = chr(valor_mensagem + ord('A'))
    
    mensagem_descriptografada += letra_mensagem

print("Mensagem criptografada:", mensagem_cifrada)
print("Mensagem descriptografada:", mensagem_descriptografada)
