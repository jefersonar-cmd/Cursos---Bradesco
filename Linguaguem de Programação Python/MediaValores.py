qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    # Entrada de Valores
    valor = float(input("Digite um valor: "))

# Caso digite um valor negativo o laço encerra
media = soma / qtd
print(f'\nTotal da Soma: {soma}')
print(f'\nQuantidade de valores digitados: {qtd}')
print(f'\nMédia dos valores: {media}')