import math

def mse(listTest, listPred):
    somatorio = 0
    for i in range(0, listPred.__len__()):
        x = math.pow(int(listTest[i][2]) - int(listPred[i][2]), 2)
        somatorio += x

    return math.sqrt(somatorio/listPred.__len__())

def vizinhoMaisProximo(usuario1, usuario2):
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


