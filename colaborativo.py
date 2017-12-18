import algoritmos as alg
import numpy as np

arquivo = open("teste.base", "r")
# arquivo = open("dadosParaTEP/u1.base", "r")
read = []
for i in arquivo:
    read.append(i.split("\t"))

#criando a matriz de 0
matriz = np.zeros((943, 1682), dtype=np.int)
for i in range(0, read.__len__()):
    matriz[int(read[i][0])-1][int(read[i][1])-1] = int(read[i][2])

listaProximidade = []
proximidade = {}
for linha in range(0, 89):
    for linha2 in range(0, 89):
        # aux = linha
        # while(aux-1 >= 0):
        #     aux -= 1
        #     dicionarioAuux =
        #     if(listaProximidade[aux].__contains__('u{0}'.format(linha2+1))):
        #         proximidade['u{0}'.format(linha2+1)] = listaProximidade[aux]['u{0}'.format(linha2+1)]
        proximidade['u{0}'.format(linha2+1)] = alg.vizinhoMaisProximo(matriz[linha], matriz[linha2])

    listaProximidade.append(proximidade)
    proximidade = {}

for i in listaProximidade:
    print(i)

# print(matriz)
print('finalizado')