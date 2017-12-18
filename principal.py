import algoritmos as alg
import random

for i in range(1, 6):
    baseTest = 'dadosParaTEP/u{0}.test'.format(i)
    baseAleatoria = 'aleatorio/u{0}.aleatorio'.format(i)
    arquivo = open(baseTest, 'r')
    arquivoAleatorio = open(baseAleatoria, 'w')

    entrada = []
    saida = []

    for linha in arquivo:
        entrada.append(linha.split("\t"))

    for linha in range(0, entrada.__len__()):
        escrita = entrada[linha][0] +"\t"+ entrada[linha][1] +"\t"+ str(random.randint(1,5)) + "\n"
        arquivoAleatorio.write(escrita)

    arquivoAleatorio = open(baseAleatoria, 'r')
    for linha in arquivoAleatorio:
        saida.append(linha.split("\t"))

    print('u{0}.test = {1}'.format(i, alg.mse(entrada, saida)))

print('finish')



