from funçoes import *


estoque = {
    1 : {"nome" : "Teclado mecânico magnético", "quantidade": 100,"valor" : 300},
    2 : {"nome" : "Mouse Gamer Redragon", "quantidade": 150, "valor" : 450 },
    3 : {"nome" : "Monitor Curvo Samsung Odyssey G5 32","quantidade" : 70, "valor": 2000}
}
carrinho = {}

while True:
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

    opcao = int(input("Escolha a opção que deseja: "))

    match opcao:
        case 1:
           listar(estoque)

        case 2:
            adicionar_ao_carrinho(estoque, carrinho)






