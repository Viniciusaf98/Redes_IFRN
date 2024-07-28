n=int(input('Digite um número que contenha até quatro dígitos : '))
a= n % 10
n= n // 10
b= n % 10
n= n //10
c= n % 10
n= n//10
d= n 
soma = a + b + c + d

print('A soma dos algarismos desse número corresponde a :',soma)