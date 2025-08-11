nome_produto = input("Digite o nome do produto:")
preco_produto = float(input("Digite o preço do produto:"))

# (float) é utilizado para converte em numeros decimais

print(f"O produto {nome_produto} custa R$ {preco_produto:.2f}.")
#para aparecer o "0" em conjunto com "float" usa-se o codigo ":.2f"