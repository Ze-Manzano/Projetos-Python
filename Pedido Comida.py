print("------ SEJA BEM VINDO(A) À HAMBURGUERIA MANZANO -----")
cadastro =str(input("Você já possui cadastro na nossa loja? (S/N): "))
if (cadastro == "S" or cadastro == "s"):
    usuario = str(input("Digite seu usuario: "))
    senha = str(input("Digite sua senha: "))
    verificacao = str(input("Digite sua senha novamente: "))

if cadastro == "N" or cadastro == "n":
    print("Vamos criar sua conta!")
    loginc = str(input("Digite seu login: "))
    senhac = str(input("Digite sua senha: "))
    vsenhac = str(input("Digite sua senha novamente: "))
    usuario = loginc

elif senha == verificacao:
    print("\nSeu seu login foi efetuado com sucesso!")

else:
    print("Não foi possível efetuar seu login, tente novamente!")


menu =str(input("Deseja acessar o menu de comidas ou bebidas? Caso deseje comidas, digite (1), caso deseje bebidas, digite (2): "))
print("----- MENU -----")
if menu == "1":
    print("X-Calabresa = R$25,00 (1)")
    print("X-Salada = R$15,00 (2)")
    print("X-Bacon = R$23,00 (3)")
    print("X-Ovo = R$18,00 (4)")
    print("X-Frango = R$27,00 (5)")

else:
    print("Refrigerante Lata = R$8,00 (6)")
    print("Suco de Laranja = R$12,00 (7)")
    print("Cerveja Long Neck = R$15,00 (8)")
    print("Cerveja 600 ml = R$20,00 (9)")

pedido = str(input("Digite o número associado do item que deseja: "))
if pedido == "1":
    pedido = "X-Calabresa"
    valor = 25
elif pedido == "2":
    pedido = "X-Salada"
    valor = 15
elif pedido == "3":
    pedido = "X-Bacon"
    valor = 23
elif pedido == "4":
    pedido = "X-Ovo"
    valor = 18
elif pedido == "5":
    pedido = "X-Frango"
    valor = 27
elif pedido == "6":
    pedido = "Refrigerante Lata"
    valor = 8
elif pedido == "7":
    pedido = "Suco de Laranja"
    valor = 12
elif pedido == "8":
    pedido = "Cerveja Long Neck"
    valor = 15
elif pedido == "9":
    pedido = "Cerveja 600 ml"
    valor = 20

quantidade =int(input("Digite a quantidade que deseja de cada item: "))
valor_finalp = valor * quantidade

print(f"O valor do seu pedido é de R$ {valor_finalp}")
pagamento=int(input("Digite sua forma de pagamento: Se for a vista, digite 1; Se for parcelado, digite 2: "))
if pagamento == 1:
    pagamento = "À vista"
    valor_finalp *= 0.9
else:
    pagamento = "Parcelado"

print(f"Seu preço final é de R$ {valor_finalp}")
print("\nMUITO OBRIGADO POR PEDIR NA HAMBURGURIA MANZANO")
fiscal =str(input("Deseja imprimir sua nota fiscal? (S/N): "))

if fiscal =="S" or fiscal =="s":
    print("--------- NOTA FISCAL ---------")
    print(f"--- Cliente: {usuario} ---")
    print(f"--- Pedido: {pedido} ---")
    print(f"--- Quantidade: {quantidade} ---")
    print(f"--- Forma de pagamento: {pagamento} ---")
    print(f"--- Valor do produto: R$ {valor_finalp} ---")
    print("-----------------------------------")
