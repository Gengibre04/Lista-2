#Faça um programa que leia e valide as seguintes informações:
 #1.Nome: maior que 3 caracteres;
 #2.Idade: entre 0 e 150;
 #3.Salário: maior que zero;
 #4.Sexo: 'f' ou 'm';
 #5.Estado Civil: 's', 'c', 'v', 'd';
 #Use a função len(string) para saber o tamanho de um texto (número de caracteres)

def validar_nome(nome):
    return len(nome) > 3  # Verifica se o nome tem mais de 3 caracteres

def validar_idade(idade):
    return len(idade) > 0 and idade.isdigit() and 0 <= int(idade) <= 150  

def validar_salario(salario):
    return len(salario) > 0 and float(salario) > 0  

def validar_sexo(sexo):
    return len(sexo) == 1 and sexo in ['f', 'm']  

def validar_estado_civil(estado_civil):
    return len(estado_civil) == 1 and estado_civil in ['s', 'c', 'v', 'd']  

# Leitura e validação do nome
while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    if validar_nome(nome):
        break
    else:
        print("Nome inválido. Deve ter mais de 3 caracteres.")

# Leitura e validação da idade
while True:
    idade = input("Digite sua idade (entre 0 e 150): ")
    if validar_idade(idade):
        idade = int(idade)  # Converte a idade para inteiro após validação
        break
    else:
        print("Idade inválida. Deve estar entre 0 e 150 e ser um número válido.")

# Leitura e validação do salário
while True:
    salario = input("Digite seu salário (maior que zero): ")
    if validar_salario(salario):
        salario = float(salario)  # Converte o salário para float após validação
        break
    else:
        print("Salário inválido. Deve ser maior que zero e um número válido.")

# Leitura e validação do sexo
while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
    if validar_sexo(sexo):
        break
    else:
        print("Sexo inválido. Digite 'f' para feminino ou 'm' para masculino.")

# Leitura e validação do estado civil
while True:
    estado_civil = input("Digite seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").lower()
    if validar_estado_civil(estado_civil):
        break
    else:
        print("Estado civil inválido. Digite 's', 'c', 'v' ou 'd'.")

# Exibindo as informações válidas
print("\nInformações válidas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {'Solteiro(a)' if estado_civil == 's' else 'Casado(a)' if estado_civil == 'c' else 'Viúvo(a)' if estado_civil == 'v' else 'Divorciado(a)'}")