#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é 
#aquele que é divisível somente por ele mesmo e por 1.
def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if eh_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")