# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até 
#que o valor seja maior que 500.

a, b = 0,1 

contador = 0 

while contador < 16:

    print(a)

    a, b = b, a + b

    contador += 1