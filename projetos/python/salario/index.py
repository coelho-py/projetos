nome = str(input("qual seu nome?"))
idade = int(input("qual sua idade?"))
sexo = str(input("qual seu sexo? (F) feminino e (M) Masculino" ))
salario = float(input("qual seu salario?"))

if idade >= 30 and sexo == "m":
    porcento = 1
elif idade < 30 and sexo == "m":
    porcento = 0.5
elif idade >= 30 and sexo == "f":
    porcento = 2
elif idade < 30 and sexo == "f":
    porcento = 0.8

salariototal = float(salario * porcento)

print(f'nome: ', nome)
print(f'idade: ', idade)
print(f'sexo: ', sexo)
print(f'salario liquido: ', salariototal)

