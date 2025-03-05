print("===cardapio===")
print("NOME|| CODIGO || PRECO")
print("Cachorro Quente  101  1,20")
print("Bauru Simples  102  1,30")
print("Bauru com ovo  103  1,50")
print("Hamburguer  104  1,20")
print("cheeseburguer  105  1,30")
print("refrigerante  106  1,00")

repeticao = 0
total_geral = 0
itens = []

while(repeticao <= 99):
    codigo = int(input("Digite o codigo do produto\n"))
    
    if (codigo not in [101, 102, 103, 104, 105, 106]):
        print("codigo invalido")
        break
    else:
        quantidade = int(input("Digite a quantidade\n"))
    
    if(codigo == 101):
        produto = 1.20
        nome = "cachorro quente"
    elif(codigo == 102):
        produto = 1.30
        nome = "bauru simples"
    elif(codigo == 103):
        produto = 1.50
        nome = "bauru com ovo"
    elif(codigo == 104):
        produto = 1.20
        nome = "hamburguer"
    elif(codigo == 105):
        produto = 1.30
        nome = "cheeseburguer"
    elif(codigo == 106):
        produto = 1.00
        nome = "refrigerante"
    
    total = produto * quantidade
    total_geral += total
    itens.append(f"{quantidade} x {nome} = {total:.2f}")
    
    print(f"{quantidade} x {nome} = {total:.2f}")
    
    escolha = input("Deseja continuar? (Digite 1 para continuar, 2 para sair)\n")
    
    if escolha == '2':
        break
    
    repeticao += 1

print("\n=== Resumo do Pedido ===")
for item in itens:
    print(item)

print(f"\nTotal geral: R$ {total_geral:.2f}")
