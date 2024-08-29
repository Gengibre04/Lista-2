# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos 
#valores.
def analisar_numeros(numeros):
    if not numeros:
        return None, None, 0  

    menor_valor = min(numeros)
    maior_valor = max(numeros)
    soma_valores = sum(numeros)
    
    return menor_valor, maior_valor, soma_valores

numeros = input("Digite uma lista de números separados por espaço: ")

lista_numeros = list(map(int, numeros.split()))

menor, maior, soma = analisar_numeros(lista_numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")

