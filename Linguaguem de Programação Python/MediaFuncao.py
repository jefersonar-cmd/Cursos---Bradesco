def lernotas():
    n = float(input("Digite uma nota para o aluno(a): "))
    return n

def resultado(n1, n2):
    media = (n1+n2) / 2
    print(f'Nota 1: {n1}')
    print(f'Nota 2: {n2}')
    print(f'Média: {media} Resultado: ', end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
resultado(a, b)