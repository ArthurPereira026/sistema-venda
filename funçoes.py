import os
from datetime import time
from xml.sax import parse


def listar(estoque):
    print(f"{'ID':>5} | {'Nome':^50} | {'Quantidade':<10} | {'Valor':<10}")
    print(f"{'-' * 82}")
    for k,v in estoque.items():
        print(f"{k:<5} | {v["nome"]:^50} | {v["quantidade"]:<10} | {v["valor"]:<10}")

def adicionar_ao_carrinho(estoque,carrinho):
    listar(estoque)
    adicionar_id =  int(input("Digite o ID do produto que deseja c adicionar ao seu carrinho: "))
    if adicionar_id in estoque:
        adicionar_qtd = int(input("Digite a quantidade do produto: "))
        if adicionar_qtd <= estoque[adicionar_id]["quantidade"]:
            estoque[adicionar_id]["quantidade"] -= adicionar_qtd
            carrinho[adicionar_id] = {
                "quantidade" : adicionar_qtd,
                "valor" : estoque[adicionar_id]["valor"],
                "total" : adicionar_qtd*estoque[adicionar_id]["valor"],
                "nome" : estoque[adicionar_id]["nome"]
            }
            print("Compra adicionada com sucesso!")
        else:
            print(f"A Quantidade  que você digitou está acima do nosso estoque! O nosso estoque é de {estoque[adicionar_id]["quantidade"]}")
    else:
        print("O ID que você digitou n existe no nosso estoque!Por Favor digite um ID valido")

def carrinho_atual (carrinho):
    print("Carrinho Atual 🛒\n")
    subTotal = 0
    if len(carrinho) == 0:
        print("O seu carrinho esta vazio😥😥")
    else:
       for chave, valor in carrinho.items():
           subTotal += valor["valor"]
           print(f"{valor["quantidade"]} {valor["nome"]} foi adicionado ao seu carrinho no valor de R$ {valor["valor"]:.2f} (und.) -> total {valor["total"]:.2f}")
    print(f"Subtotal = {subTotal:.2f}")

def finalizar_compra (carrinho,estoque):
    subTotal = 0
    desconto = 0

    for chave, valor in carrinho.items():
        subTotal += valor["total"]

    cupom = input("Você possui um cupom de desconto? Enter para pular: ")
    if cupom == "DEV10":
        desconto = subTotal*0.1
    elif cupom == "DEV20":
        desconto = subTotal*0.2
    else:
        print("O cupom digitado é invalido ou expirou!!")
    print(f"Valor total sem desconto: R${subTotal:.2f}")
    print(f"Valor total com desconto: R${desconto:.f2}")
    print(f"Valor total a pagar: R${subTotal-desconto:.2f}")
    pagar = input("Deseja efetuar o pagamento?(s/n): ").lower()

    if pagar == "s":
        for i in range(5):
            print("."*i)
            time.sleep(1)
            os.system("cls")
        print("Compra Realizada com sucesso😊😊!Obrigado por comprar no WIFI EXPRESS STORE 🛜! Volte sempre!")
    else:
        for k, v in carrinho.items():
            estoque[k]["quantidade"] += v["quantidade"]
        print("Compra cancelada😥😥!")

def menu ():
    print("""
    ----------------------------------------------
      SEJA BEM-VINDO AO ➡ WIFI EXPRESS STORE 🛜
    ----------------------------------------------
           -> OPÇÕES DISPONIVEIS PARA VC <-
    ----------------------------------------------        
    [1]  Visualizar Estoque      
    [2]  Adicionar item ao Carrinho
    [3]  Visualizar Carrinho
    [4]  Finalizar Compra
    [0]  Sair do Sistema 
    \n""")


