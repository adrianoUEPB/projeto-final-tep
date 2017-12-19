import algoritmos as alg

aleatorio = alg.aleatorio()
colaborativo = alg.colaborativo()

arquivo = open("rmse.txt", "w")

for i in aleatorio:
    arquivo.write(i)

for i in colaborativo:
    arquivo.write(i)