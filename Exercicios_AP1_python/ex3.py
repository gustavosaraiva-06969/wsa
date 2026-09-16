print("CALCULANDO A SUA COMPRA")

caderno = 10.0
lapis = 2.0
bolsa = 50.0
lancheira = 30.0
marca_texto = 5.0
caneta = 3.0

#atribuição dos preços dos produtos em um dicionário
preço = {
    "caderno": caderno,
    "lapis": lapis,
    "bolsa": bolsa,
    "lancheira": lancheira,
    "marca_texto": marca_texto,
    "caneta": caneta
}

#input para que o usuário escolha um produto
produto = input("escolha um produto: ")

#uso de operadores lògicos para verificar se o produto escolhido está no dicionário de preços
if produto not in preço:
    print("Produto não encontrado.")
else:
    quantidade = int(input("Quantos produtos você deseja: "))
    preco_unitario = preço[produto]
    subtotal = preco_unitario * quantidade
    imposto = subtotal * 0.1
    total = subtotal + imposto

print(f"Você comprou {quantidade} {produto}(s) e o preço total foi de R${total:.2f} com imposto incluído.")