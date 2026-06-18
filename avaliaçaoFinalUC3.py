from funçoes import *


estoque = {
    1 : {"nome" : "Teclado mecânico magnético", "quantidade": 100,"valor" : 300},
    2 : {"nome" : "Mouse Gamer Redragon", "quantidade": 150, "valor" : 450 },
    3 : {"nome" : "Monitor Curvo Samsung Odyssey G5 32","quantidade" : 70, "valor": 2000}
}
carrinho = {}


while True:
    menu()

    opcao = int(input("Escolha a opção que deseja: "))

    match opcao:
        case 1:
           listar(estoque)

        case 2:
            adicionar_ao_carrinho(estoque, carrinho)

        case 3:
            carrinho_atual(carrinho)

        case 4:
            finalizar_compra(carrinho,estoque)

        case 0:
            print("Obrigado por utilizar nosso sistema volte sempre ao WIFI EXPRESS STORE 🛜")
            break
        case _:
            print("Opção invalida😥!Por Favor digite uma da opções validas abaixo")










