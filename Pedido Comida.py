print("------ SEJA BEM VINDO(A) À HAMBURGUERIA MANZANO -----")

cadastro = str(input("Você já possui cadastro na nossa loja? (S/N): "))



if cadastro == "S" or cadastro == "s":
    usuario = str(input("Digite seu usuário: "))
    senha = str(input("Digite sua senha: "))
    verificacao = str(input("Digite sua senha novamente: "))


    if senha == verificacao:
        print("\nSeu login foi efetuado com sucesso!")
    else:
        print("\nAs senhas não são iguais. Não foi possível efetuar seu login.")
        exit()

elif cadastro == "N" or cadastro == "n":
    print("\nVamos criar sua conta!")

    loginc = str(input("Digite seu login: "))
    senhac = str(input("Digite sua senha: "))
    vsenhac = str(input("Digite sua senha novamente: "))

   
    if senhac == vsenhac:
        usuario = loginc
        print("\nCadastro realizado com sucesso!")
    else:
        print("\nAs senhas não são iguais. Não foi possível criar sua conta.")
        exit()

else:
    print("\nOpção inválida!")
    exit()




pedidos = []
valor_total = 0

while True:

    print("\n----- MENU -----")
    menu = str(input(
        "Deseja acessar o menu de comidas ou bebidas?\n"
        "Comidas (1)\n"
        "Bebidas (2)\n"
        "Digite sua opção: "
    ))

  

    if menu == "1":
        print("\n----- COMIDAS -----")
        print("X-Calabresa = R$25,00 (1)")
        print("X-Salada = R$15,00 (2)")
        print("X-Bacon = R$23,00 (3)")
        print("X-Ovo = R$18,00 (4)")
        print("X-Frango = R$27,00 (5)")

  

    elif menu == "2":
        print("\n----- BEBIDAS -----")
        print("Refrigerante Lata = R$8,00 (6)")
        print("Suco de Laranja = R$12,00 (7)")
        print("Cerveja Long Neck = R$15,00 (8)")
        print("Cerveja 600 ml = R$20,00 (9)")

    else:
        print("\nOpção de menu inválida!")
        continue


    

    pedido = str(input("\nDigite o número associado ao item que deseja: "))

    if pedido == "1":
        nome_pedido = "X-Calabresa"
        valor = 25

    elif pedido == "2":
        nome_pedido = "X-Salada"
        valor = 15

    elif pedido == "3":
        nome_pedido = "X-Bacon"
        valor = 23

    elif pedido == "4":
        nome_pedido = "X-Ovo"
        valor = 18

    elif pedido == "5":
        nome_pedido = "X-Frango"
        valor = 27

    elif pedido == "6":
        nome_pedido = "Refrigerante Lata"
        valor = 8

    elif pedido == "7":
        nome_pedido = "Suco de Laranja"
        valor = 12

    elif pedido == "8":
        nome_pedido = "Cerveja Long Neck"
        valor = 15

    elif pedido == "9":
        nome_pedido = "Cerveja 600 ml"
        valor = 20

    else:
        print("\nProduto inválido!")
        continue


  

    quantidade = int(input("Digite a quantidade que deseja: "))

    subtotal = valor * quantidade
    valor_total += subtotal

    
    pedidos.append({
        "produto": nome_pedido,
        "quantidade": quantidade,
        "subtotal": subtotal
    })

    print(f"\n{quantidade}x {nome_pedido} adicionado ao pedido!")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Valor acumulado: R$ {valor_total:.2f}")


   

    continuar = str(input(
        "\nDeseja pedir outro item? (S/N): "
    ))

    if continuar == "N" or continuar == "n":
        break




print("\n----- RESUMO DO PEDIDO -----")

for item in pedidos:
    print(
        f"{item['quantidade']}x {item['produto']} "
        f"= R$ {item['subtotal']:.2f}"
    )

print(f"\nValor total do pedido: R$ {valor_total:.2f}")

pagamento = int(input(
    "\nDigite sua forma de pagamento:\n"
    "À vista (1)\n"
    "Parcelado (2)\n"
    "Digite sua opção: "
))

if pagamento == 1:
    forma_pagamento = "À vista"
    valor_total *= 0.9
    print("\nVocê recebeu 10% de desconto!")

elif pagamento == 2:
    forma_pagamento = "Parcelado"

else:
    print("\nForma de pagamento inválida.")
    forma_pagamento = "Não informado"




print(f"\nSeu preço final é de R$ {valor_total:.2f}")

print("\nMUITO OBRIGADO POR PEDIR NA HAMBURGUERIA MANZANO!")

fiscal = str(input("Deseja imprimir sua nota fiscal? (S/N): "))

if fiscal == "S" or fiscal == "s":

    print("\n--------- NOTA FISCAL ---------")
    print(f"--- Cliente: {usuario} ---")

    print("--- Pedidos ---")

    for item in pedidos:
        print(
            f"--- {item['produto']} | "
            f"Quantidade: {item['quantidade']} | "
            f"Subtotal: R$ {item['subtotal']:.2f} ---"
        )

    print(f"--- Forma de pagamento: {forma_pagamento} ---")
    print(f"--- Valor final: R$ {valor_total:.2f} ---")
    print("-----------------------------------")
