#Inserindo Cantores

def criargravacao(dic, dicmusic, diccantor):

    LINST = []

    nome = input("Digite o nome da música: ").lower()

    if (nome in dicmusic):
        nomeart = input("Digite o nome artístico do cantor: ")

        if (nomeart in diccantor):
            dia = input("Digite o dia da gravação: ")
            mes = input("Digite o mês da gravação: ")
            ano = input("Digite o ano da gravação: ")
            data = dia+"/"+mes+"/"+ano

            album = input("Digite o nome do álbum: ")

            inst = input("Digite o nome do instrumento (<enter> para finalizar): ")

            while (inst != ""):

                LINST.append(inst)
                
                inst = input("Digite o nome do instrumento (<enter> para finalizar): ")

            tupla = (nome, nomeart, data,)

            dic[tupla] = (album, LINST,)

        else:
            print("Cantor não cadastrado!")

    else:
        print("Música não cadastrada!")
    
    return(dic)

#Listando todos os Cantores

def listargravacoes(dic):

    if (len(dic) == 0):
        print("Banco de Dados vazio!")
    else:
        print("Gravações Registradas:")

        for i in dic:
            print(f"Gravação: {i[0].title()} - Nome Artístico: {i[1].title()} - Data: {i[2]} Álbum: {dic[i][0].title()} -", end = " ")

            print("Instrumentos:", end = " ")

            for inst in dic[i][1]:
                print(inst.title(), end = "; ")

            print()

#Listando uma Gravação específica

def listargravacaoespecifica(dic):

    if (len(dic) == 0):
        print("Banco de Dados vazio.")
    else:
        cons = input("Digite o nome da gravação que deseja buscar: ").lower()

        find = False

        for i in dic:
            if (i[0] == cons):
                find = True
                
            if (find == True):
                print(f"Gravação: {i[0].title()} - Nome Artístico: {i[1].title()} - Data: {i[2]} Álbum: {dic[i][0].title()} -", end = " ")

                print("Instrumentos:", end = " ")

                for inst in dic[i][1]:
                    print(inst.title(), end = "; ")

                print()

            else:
                print("Gravação não registrada no Banco de Dados!")

#Alterando ou excluindo uma Gravação

def alterarouexcluirgravacao(dic):

    LINST = []

    if (len(dic) == 0):
        print("Banco de Dados vazio!")
    else:
        print("1 - Alterar uma gravação")
        print("2 - Excluir uma gravação")

        opc = int(input("Digite a opção: "))

        if (0 < opc < 3):
            if (opc == 1):
                nome = input("Digite o nome da gravação que deseja alterar: ").lower()

                achou = False

                for i in dic:
                    if (i[0] == nome):
                        achou = True

                        if achou:
                            print(f"Deseja mesmo alterar os dados da gravação: {i[0]}?")
                            confirma = int(input("1- Sim\n2- Não\n"))

                            if (0 < confirma < 2): 
                                if (confirma == 1):
                                    altnome = input("Digite o novo título (<enter> para ignorar): ").lower()
                                    if (altnome == ""):
                                        altnome = nome

                                    altnomeart = input("Digite o novo nome artístico (<enter> para ignorar): ").lower()
                                    if (altnomeart == ""):
                                        altnomeart = i[1]

                                    # BDGravacoes = {('te ver', 'vgod', '19/12/2020'): ('muito amor', ['fl studio', 'drom']),}

                                    dia = input("Digite o dia de nascimento (<enter> para não alterar):")

                                    if (dia == ""):
                                        dia = i[2][0:2]

                                    elif (int(dia) < 0 or int(dia) > 31):
                                        dataincorreta = True
                                        while dataincorreta:
                                            print("Digite a data no formato correto!")

                                            dia = int(input("Digite o dia da gravação: "))
                                            if (0 < dia < 32):
                                                dataincorreta = False
                                            else:
                                                dataincorreta = True

                                    else:
                                        dataincorreta = False

                                    mes = input("Digite o mês da gravação. <enter> para não alterar: ")

                                    if (mes == ""):
                                        mes = i[2][3:5]

                                    elif (int(mes) < 0 or int(mes) > 12):
                                        dataincorreta = True
                                        while dataincorreta:
                                            print("Digite a data no formato correto!")

                                            mes = int(input("Digite o mês da gravação: "))
                                            if (0 < mes < 13):
                                                dataincorreta = False
                                            else:
                                                dataincorreta = True

                                    else:
                                        dataincorreta = False

                                    ano = input("Digite o ano da gravação: ")

                                    if (ano == ""):
                                        ano = i[2][6:10]

                                    if (len(ano) > 4):
                                        dataincorreta = True
                                        while dataincorreta:
                                            print("Digite a data no formato correto!")

                                            ano = input("Digite o ano da gravação: ")

                                            if (len(ano) > 4):
                                                dataincorreta = True
                                            else:
                                                dataincorreta = False

                                    else:
                                        dataincorreta = False

                                    altdata = str(dia) + "/"+ str(mes) + "/" + ano

                                    altalbum = input("Digite o novo álbum (<enter> para ignorar): ").lower()
                                    if (altalbum == ""):
                                        altalbum = dic[i][0]

                                    inst = input("Digite o nome do instrumento (<enter> para finalizar): ")

                                    while (inst != ""):

                                        LINST.append(inst)
                
                                        inst = input("Digite o nome do instrumento (<enter> para finalizar): ")

                                    if (inst == ""):
                                        LINST = dic[i][1]
             
                                    dic.pop(i)
                                    i = (altnome, altnomeart, altdata,)
                                    dic[i] = (altalbum, LINST,)
                                    
                                    return(dic)
                                else:
                                    print("Operação cancelada!")
                            else:
                                print("Digite uma opção válida!")

                        if achou == False:
                            print("Cantor não cadastrado no Banco de Dados!")

            if (opc == 2):
                nome = input("Digite o nome da gravação que deseja deletar: ").lower()
                for i in dic:
                    if (i[0] == nome):
                        achou = True
    
                    if achou:
                        print(f"Deseja mesmo deletar a gravação: {i[0]}?")
                        confirma= int(input("1- Sim\n2- Não\n"))

                        if (0 < confirma < 3):
                            if (confirma == 1):
                                dic.pop(i)
                                print(dic)

                                return(dic)
                                
                            else:
                                print("Operação cancelada!")

                        else:
                            print("Digite uma opção válida!")
                    else:
                        print("Música não cadastrada em nosso banco de músicas!")     

        else:
            print("Digite uma opção válida!")