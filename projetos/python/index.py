print("===cardapio===")
print("NOME|| CODIGO || PRECO")
print("Cachorro Quente  101  1,20")
print("Bauru Simples  102  1,30")
print("Bauru com ovo  103  1,50")
print("Hamburguer  104  1,20")
print("cheeseburguer  105  1,30")
print("refrigerante  106  1,00")

quantidadei = 0
produto = 0
i = 0

while i < 10:
    codigo = float(input("Digite o codigo do produto\n"))
    if (not codigo or codigo > 107 or codigo < 101):
        print("codigo invalido")
        break
    else:
        quantidade = float(input("Digita a quantidade\n"))

    if(codigo == 101):
        produto += 1.20
        nome = "cachorro quente"
        quantidadei += quantidade 
    elif(codigo == 102):
        produto += 1.30
        nome = "bauru simples"
        quantidadei += quantidade
    elif(codigo == 103):
        produto += 1.50
        nome = "bauru com ovo"
        quantidadei += quantidade
    elif(codigo == 104):
        produto += 1.20
        nome = "hamburguer"
        quantidadei += quantidade
    elif(codigo == 105):
        produto += 1.30
        nome = "cheeseburguer"
        quantidadei += quantidade
    elif(codigo == 106):
        produto += 1
        nome = "refrigerante"
        quantidadei += quantidade

    escolha = print(input("1 - sim \n 2 - nao \n"))

    if (escolha == 1):
        i = 11
    elif (escolha == 2):
        i += 1
    
    if i > 10:
        break

valor = produto * quantidade
print(f'voce escolheu o produto:' + str(nome) + '\nna quantidade de: ' + str(quantidade) + '\ndo valor de:' + str(produto) + '\nvalor total: ' + str(valor))
