from dados import data
from encadeamentoFrente import encadeamentoFrente
from encadeamentoMisto import encadeamentoMisto
from encadeamentoTras import encadeamentoTras

new_data = data

user = input("Deseja digitar novos valores? (y/n): ")

if user == "y":
    print("Digite True ou False")
    for x in new_data:
        new_data[x] = input(x + ": ")

encadeamentoMisto(new_data)



