import time
import os
import json  # ou csv, se quiser salvar a lista de produtos

produtos = {
20348400023:{"Nome": "Relogio", "preço": 470.00},
234953003034:{"Nome": "Placamae", "preço": 780.90},
200934: {"Nome": "Gamepad", "preço": 200.00},
1203000: {"Nome": "LuzRGB", "preço": 70.00},
   }

carrinhodecompras = []
def exibir_produtos():
    print("\n produtos estão disponíveis:")
    for codigo, info in produtos.items(): 
      print(f"codigo: {codigo} - produto: {info['Nome']} - Preço: R${info['preço']:.2f}")
      

      def adicionar_produtos(codigo):
         if codigo in produtos :
              carrinhodecompras.append(produtos[codigo])
         print(f"\n_Produto{produtos[codigo]['Nome']} adicionado ao carrinho de compras!")
    else:
         print("\nCodigo de produto invalido :(")
