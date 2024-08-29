#Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto 
#quiser.

print("Calculadora - Adição\n")
num1 = float(input("Digite o primeiro número que deseja somar:"))
num2 = float(input("Digite o segundo número que deseja somar:"))
soma = num1 + num2
print(soma)

while True:
    print("Tem mais alguma outra dúvida?\n")
    resposta = input(" (S/N): ").upper()
    if resposta == "S" :
        num1 = float(input("Digite o primeiro número que deseja somar:"))
        num2 = float(input("Digite o segundo número que deseja somar:"))
        soma = num1 + num2
        print(soma)
    elif resposta == "N" :
        print("Certo")
        break
    

    
    

