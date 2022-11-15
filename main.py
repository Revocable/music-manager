from musica import *
from cantor import *
from gravacao import *
from relatorio import *
from archive import *

opc = 0
subopc = 0

#bancos de dados

BDCantores = {"vgod":("mateus","21/07/2000","vgod@gmail.com","16991045382"),}
BDMusicas = {"te ver":("20/11/2020","plug","1:20","virgingod"),}
BDGravacoes = {('te ver', 'vgod', '19/12/2020'): ('muito amor', ['fl studio', 'drom']),}

if existearq("bdm.txt","bdc.txt","bdc.txt"):
    leitura(BDMusicas,BDCantores,BDGravacoes)


#menu de opções

while (opc < 5):
    print("==================================================") 
    print(("MENU DE OPÇÕES").center(50))
    print("==================================================")
    print("1 - Menu principal de músicas")
    print("2 - Menu principal de cantores")
    print("3 - Menu principal de gravações")
    print("4 - Menu principal de relátorios")
    print("5 - Sair")
    print("==================================================")

    opc = int(input("Digite a opção: "))

    if (0 < opc < 6):

        #menu de músicas

        if (opc == 1):
            while (subopc < 5):
                print("==================================================")
                print(("Submenu de músicas").center(50))
                print("1 - Listar todas as musicas")
                print("2 - Listar uma música específica")
                print("3 - Incluir uma música")
                print("4 - Alterar ou excluir uma música")
                print("5 - Voltar para o menu principal")
                print("==================================================")
                print()
                subopc = int(input("Digite a opção: "))
                print()
                print("==================================================")


                if (0 < subopc < 5):
                    if (subopc == 1): 
                        listartodasmusicas(BDMusicas)
                    elif (subopc == 2):
                        listarmusicaespecifica(BDMusicas)
                    elif (subopc == 3):
                        BDMusicas = criarmusica(BDMusicas,BDGravacoes)
                    elif (subopc == 4):
                        BDMusicas = alterarouexcluirmusica(BDMusicas)

                else:
                    print("Digite uma opção válida")

            subopc = 0

        #menu de cantores

        elif (opc == 2):
            while (subopc < 5):
                print("==================================================")
                print(("Submenu de cantores").center(50))
                print("1 - Listar todas os cantores")
                print("2 - Listar um cantor específico")
                print("3 - Incluir um cantor")
                print("4 - Alterar ou excluir um cantor")
                print("5 - Voltar para o menu principal")
                print("==================================================")
                subopc = int(input("Digite a opção: "))
                print("==================================================")

                if (0 < subopc < 5):
                    if (subopc == 1):
                        listarcantores(BDCantores)
                    elif (subopc == 2):
                        listarcantorespecífico(BDCantores)
                    elif (subopc == 3):
                        BDCantores = criarcantor(BDCantores,BDGravacoes)
                    elif (subopc == 4):
                        BDCantores = alterarouexcluircantor(BDCantores)
                
                else:
                    print("Digite uma opção válida")

            subopc = 0

        #menu de gravações

        elif (opc == 3):
            while (subopc < 5):
                print("==================================================")
                print(("Submenu de cantores").center(50))
                print("1 - Listar todas as gravações")
                print("2 - Listar uma gravação específica")
                print("3 - Incluir uma gravação")
                print("4 - Alterar ou excluir uma gravação")
                print("5 - Voltar para o menu principal")
                print("==================================================")
                subopc = int(input("Digite a opção: "))
                print("==================================================")

                if (0 < subopc < 5):
                    if (subopc == 1):
                        listargravacoes(BDGravacoes)
                    if (subopc == 2):
                        listargravacaoespecifica(BDGravacoes)
                    elif (subopc == 3):
                        BDGravacoes = criargravacao(BDGravacoes, BDMusicas, BDCantores)
                    elif (subopc == 4):
                        BDGravacoes = alterarouexcluirgravacao(BDGravacoes)

            subopc = 0

        #relatório
        
        elif (opc == 4):
            relatorio(BDMusicas, BDCantores, BDGravacoes)
                    
    else:
        print("Digite uma opção válida")

escrita(BDMusicas,BDCantores,BDGravacoes)

print("==================================================")
print('|   Fim do Programa ツ   |'.center(48))  
print("==================================================")