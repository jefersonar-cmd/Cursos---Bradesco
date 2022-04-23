arquivo = open('arqText.txt', 'w')

arquivo.write('Cursos Python \n')
arquivo.write('Aula Prática')
arquivo.close()

print("Leitura do Arquivo Texto\n")
leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()