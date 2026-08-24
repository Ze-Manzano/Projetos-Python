nome = str(input("Qual o seu nome? "))
idade = int(input("Qual a sua idade? "))
cpf = str(input("Qual o seu CPF? "))
salario = float(input("Digite seu salario: "))
emprestimo = float(input("Qual o valor do emprestimo? "))
validacao_garantia = str(input("Você possui algum bem de garantia de emprestimo? (S/N) "))

if validacao_garantia == "S" or validacao_garantia == "s":
    garantia = str(input("Qual o item da sua garantia? "))
    valor_do_bem = int(input("Qual o valor do bem? "))
else:
    valor_do_bem =0
    garantia ="Ø"

if emprestimo <= 100000:
    parcela = 2000
    if emprestimo > salario * 10 + valor_do_bem:
        resultado = "Seu emprestimo foi NEGADO!"
    else:
        resultado = "Seu emprestimo foi APROVADO!"
elif emprestimo >= 100000:
    parcela = 4000
    if emprestimo > salario * 10 + valor_do_bem:
        resultado = "Seu emprestimo foi NEGADO!"
    else:
        resultado ="Seu emprestimo foi APROVADO!"

print("-------EMPRESTIMO GERADO-------")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"CPF: {cpf}")
print(f"Salario: {salario}")
print(f"Emprestimo de: {emprestimo}")
print(f"Parcela: {parcela}")
print(f"Garantia: {garantia}")
print(f"Valor do bem: {valor_do_bem}")
print(f"Resultado: {resultado}")
print("-------------------------------")
