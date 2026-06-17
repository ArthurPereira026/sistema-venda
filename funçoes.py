
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
