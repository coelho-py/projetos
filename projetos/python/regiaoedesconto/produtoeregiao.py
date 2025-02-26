valor = float(input("valor do produto:"))
regiao = int(input("regiao do produto \n 1- região norte 5% \n 2- região sul 15% \n 3- região sudeste 7% \n 4- região nordeste 12% \n 5- região centro-oeste 20% \n"))


if (regiao == 1):
    result = 5
elif (regiao == 2):
    result = 15
elif (regiao == 3):
    result = 720    
elif (regiao == 4):
    result = 12
elif (regiao == 5):
    result = 20
elif (regiao > 5):
    result = 0

if (result == 0):
    print("produto importado.")
else:
    desconto = valor * (result / 100)
    valortotal = valor - desconto
    print(f'valor com desconto: ' + str(desconto) + '\n valor total com desconto: ' + str(valortotal)) 