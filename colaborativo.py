import algoritmos as alg
import numpy as np

arquivoColaborativo = open("colaborativo/teste.colaborativo", "w")
arquivo = open("dadosParaTEP/u1.base", "r")
read = []
for i in arquivo:
    read.append(i.split("\t"))

# criando a matriz de 0
matriz = np.zeros((943, 1682), dtype=np.int)
for i in range(0, read.__len__()):
    matriz[int(read[i][0])-1][int(read[i][1])-1] = int(read[i][2])

listaProximidade = []
proximidade = {}
for linha in range(0, 943):
    for linha2 in range(0, 943):
        if(linha != linha2):
            proximidade['{0}'.format(linha2+1)] = alg.calculoVizinhoMaisProximo(matriz[linha], matriz[linha2])

    listaProximidade.append(proximidade)
    proximidade = {}

for i in listaProximidade:
    print(i)

vizinhos = {}
listaProx2 = []
for i in listaProximidade:
    for j in range(0, 101):
        maior = max(i, key=i.get)
        vizinhos[maior] = i.pop(maior)
    listaProx2.append(vizinhos)
    vizinhos = {}


entrada = []
saida = []

arquivoTest = open("dadosParaTEP/u1.test", "r")

for linha in arquivoTest:
    entrada.append(linha.split("\t"))

# print(listaProx2[0])

for linha in range(0, entrada.__len__()):
    valor = alg.atribuirNota(listaProx2[int(entrada[linha][0])-1], matriz, int(entrada[linha][1])-1)
    escrita = entrada[linha][0] +"\t"+ entrada[linha][1] +"\t"+ str(valor) + "\n"
    arquivoColaborativo.write(escrita)

arquivoColaborativo = open("colaborativo/teste.colaborativo", "r")
for i in arquivoColaborativo:
    saida.append(i.split("\t"))

print('u1.test = {0}'.format(alg.rmse(entrada, saida)))
