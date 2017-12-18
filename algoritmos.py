import math

def mse(listTest, listPred):
    somatorio = 0
    for i in range(0, listPred.__len__()):
        x = math.pow(int(listTest[i][2]) - int(listPred[i][2]), 2)
        somatorio += x

    return math.sqrt(somatorio/listPred.__len__())