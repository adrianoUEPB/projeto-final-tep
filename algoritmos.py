import math
import random
import numpy as np

def aleatorio():
    retorno = []
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

        retorno.append('{0}\t\t{1}\t\t{2}'.format(i, 'aleatorio', rmse(entrada, saida)))
    return retorno

def colaborativo():
    retorno = []
    for i in range(1, 6):
        base = 'dadosParaTEP/u{0}.base'.format(i)
        baseTest = 'dadosParaTEP/u{0}.test'.format(i)
        baseColaborativa = 'colaborativo/u{0}.colaborativo'.format(i)

        arquivoColaborativo = open(baseColaborativa, "w")
        arquivo = open(base, "r")
        read = []
        for i in arquivo:
            read.append(i.split("\t"))

        # criando a matriz de 0
        matriz = np.zeros((943, 1682), dtype=np.int)
        for i in range(0, read.__len__()):
            matriz[int(read[i][0])-1][int(read[i][1])-1] = int(read[i][2])

        #ListaProximidade contem todas as proximidades calculadas
        listaProximidade = []

        #Proximidade como um dicionario ira guardar a chave que eh o id do usuario com
        #com o valor da similaridade para aquele usuario
        #a posicao na listaProximidade eh referente ao id do usuario
        proximidade = {}
        for linha in range(0, 943):
            for linha2 in range(0, 943):
                if(linha != linha2):
                    proximidade['{0}'.format(linha2+1)] = calculoVizinhoMaisProximo(matriz[linha], matriz[linha2])

            listaProximidade.append(proximidade)
            proximidade = {}

        #o dicionario vizinhos serve para guardar os 80 vizinhos mais proximos,
        # guardando chave como id do usuario e valor a similaridade
        # sera adicionado a uma nova lista de proximo
        vizinhos = {}
        listaProx2 = []
        for i in listaProximidade:
            for j in range(0, 81):
                maior = max(i, key=i.get)
                vizinhos[maior] = i.pop(maior)
            listaProx2.append(vizinhos)
            vizinhos = {}

        entrada = []
        saida = []

        arquivoTest = open(baseTest, "r")

        for linha in arquivoTest:
            entrada.append(linha.split("\t"))

        for linha in range(0, entrada.__len__()):
            valor = atribuirNota(listaProx2[int(entrada[linha][0])-1], matriz, int(entrada[linha][1])-1)
            escrita = entrada[linha][0] +"\t\t"+ entrada[linha][1] +"\t\t"+ str(valor) + "\n"
            arquivoColaborativo.write(escrita)

        arquivoColaborativo = open(baseColaborativa, "r")
        for i in arquivoColaborativo:
            saida.append(i.split("\t"))

        retorno.append('{0}\t\t{1}\t\t{2}'.format(i, 'colaborativo', rmse(entrada, saida)))
    return retorno

'''
Calculo do erro.
Recebe a lista da base de teste e a lista das notas que estao sendo preditas
'''
def rmse(listTest, listPred):
    somatorio = 0
    for i in range(0, listPred.__len__()):
        x = math.pow(int(listTest[i][2]) - int(listPred[i][2]), 2)
        somatorio += x

    return math.sqrt(somatorio/listPred.__len__())

'''
Calculando os vizinhos mais proximos
Recebe usuario1 e usuario2, realiza o calculo da similaridade dos cossenos
para os usuarios recebidos, quanto mais proximo de 1, mais proximo os pontos estao
'''
def calculoVizinhoMaisProximo(usuario1, usuario2):
    soma1 = 0
    for i in range(0, usuario1.__len__()):
        soma1 += usuario1[i] * usuario2[i]

    norma1 = 0
    norma2 = 0
    for i in usuario1:
        norma1 += math.pow(i, 2)

    for i in usuario2:
        norma2 += math.pow(i, 2)

    return soma1 / (math.sqrt(norma1) * math.sqrt(norma2))

'''
Metodo responsavel por atribuir as notas para o algoritmo colaborativo
Recebe como parametro:
- o dicionario com os vizinhos mais proximos de um usuario
- a matriz com as pontuaçoes
- o filme que esta sendo atribuido a nota
'''
def atribuirNota(dicionario, matriz, filme):
    chaves = dicionario.keys()
    soma1 = 0.0
    soma2 = 0.0
    for i in chaves:
        nota = matriz[int(i)-1][filme]
        if(nota != 0):
            soma1 += nota * dicionario[i]
            soma2 += dicionario[i]


    try:
        if(soma2 == 0):
            return 0
        retorno = int(soma1/soma2)
    except ValueError:
        return 0

    return retorno
