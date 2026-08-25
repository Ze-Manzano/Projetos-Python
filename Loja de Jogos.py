print("--- SEJA BEM-VINDO(A) A MAIOR LOJA DE JOGOS DA CESUMAR ---")
nome =str(input("Digite seu nome: "))
cpf = str(input("Digite seu CPF: "))
jogo = str(input("Digite o jogo desejado: "))
preco =int(input("Digite o valor do jogo: "))
print("Formas de pagamento:\n Dinheiro/Pix: 10% de desconto.\n Cartão à vista: 5% de desconto.\n Cartão Parcelado: sem desconto.\n Boleto: 15% de desconto.\n")
pagamento = int(input("Digite sua forma de pagamento desejada: (1) Dinheiro/Pix, (2) Cartão à vista, (3) Cartão parcelado, (4) Boleto: "))

if pagamento == 1:
    preco *= 0.90
elif pagamento == 2:
    preco *= 0.95
elif pagamento == 3:
    preco == preco
elif pagamento == 4:
    preco *= 0.85


print("--- LOJA DE JOGOS CESUMAR ---")
print(f"{nome}")
print(f"{cpf}")
print(f"{jogo}")
print(f"{preco}")
