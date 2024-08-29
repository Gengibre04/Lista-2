# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
def analisar_numeros(numeros):
    if not numeros:
        return None, None, 0 

    menor_valor = min(numeros)
    maior_valor = max(numeros)
    soma_valores = sum(numeros)
    
    return menor_valor, maior_valor, soma_valores

def validar_entrada(numeros):
    return all(0 <= num <= 1000 for num in numeros)

while True:
    numeros = input("Digite uma lista de números entre 0 e 1000, separados por espaço: ")
    

    try:
        lista_numeros = list(map(int, numeros.split()))
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        continue

    if validar_entrada(lista_numeros):
        break
    else:
        print("Todos os números devem estar entre 0 e 1000. Tente novamente.")

menor, maior, soma = analisar_numeros(lista_numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")