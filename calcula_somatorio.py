'''
## Lista 04 - Exercício 31 (parcial)

# Calcula o somatório de 2 até n de i / (i * (i - 1)) e exibe o resultado com 2 casas decimais.
'''

# Entrada de dados
n = int(input())

# Inicializa e calcula o somatório
somatorio = 0

for i in range(2, n + 1):
    somatorio += i / (i * (i - 1))

# Exibe o resultado formatado com 2 casas decimais
print(f"{somatorio:.2f}")