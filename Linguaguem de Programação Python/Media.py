notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

#calcular media
mediaFinal = (notaA + notaB) / 2

#verificação
if mediaFinal >= 7.0:
    print(f'A média: {mediaFinal} - Aprovado')
else:
    print(f'A média: {mediaFinal} - Reprovado')