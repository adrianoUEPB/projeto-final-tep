import algoritmos as alg

arquivo = open("rmse.txt", "w")
arquivo.write("particao\t\talgoritmo\t\trmse\n")
print("Gerando aleatorio...")
aleatorio = alg.aleatorio()
for i in aleatorio:
    arquivo.write(i + "\n")

print("Aleatorio gerado")
print("Gerando colaborativo...")
colaborativo = alg.colaborativo()
for i in colaborativo:
    arquivo.write(i + "\n")

print("Colaborativo gerado")
