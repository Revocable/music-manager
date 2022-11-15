
def criarmusica(dic, dic2):
    nome = input("Digite o nome da musica: ").lower()
    if (nome in dic or nome in dic2):
        print("Musica já cadastrada!")
    else:
        dia = int(input("Digite o dia da gravação: "))
        if (dia < 0 or dia > 31):
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
        mes = int(input("Digite o mês da gravação: "))
        if (mes < 0 or mes > 12):
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
        if (len(ano)>4):
            dataincorreta = True
            while dataincorreta:
                print("Digite a data no formato correto!")
                ano = input("Digite o ano da gravação: ")
                if (len(ano)>4):
                    dataincorreta = True
                else:
                    dataincorreta = False
        else:
            dataincorreta = False
        data = str(dia)+"/"+str(mes)+"/"+ano
        estilo = input("Digite o estilo da música: ").lower()
        tempo = input("Digite o tempo da música: ").lower()
        compositor = input("Digite o nome do compositor: ").lower()
        tupla = (data,estilo,tempo,compositor)
        dic[nome] = tupla
        print(dic)
        return(dic)

####################################

def listartodasmusicas(dic):
    if (len(dic) == 0):
        print("Banco de músicas vazio. Por favor insira alguma música para continuar!")
    else:
        print("Musicas Registradas em nosso banco de dados:")
        print()
        for i in dic:
            print(f"Nome: {i.title()} - Data: {dic[i][0]} - Estilo: {dic[i][1].title()} - Tempo: {dic[i][2]} - Compositor: {dic[i][3].title()} ")
            print()

#####################################

def listarmusicaespecifica(dic):
    if (len(dic) == 0):
        print("Banco de músicas vazio. Por favor insira alguma música para continuar!")
    else:
        consulta = input("Digite o nome da música para consultar: ")
        consulta = consulta.lower()
        if (consulta in dic):
            for i in dic:
                if i == consulta:
                    print(f"Nome: {i.title()} - Data: {dic[i][0]} - Estilo: {dic[i][1].title()} - Tempo: {dic[i][2]} - Compostior: {dic[i][3].title()} ")
                    print()
        else:
            print("Música não registrada em nosso banco de músicas.")

###################################

def alterarouexcluirmusica(dic):

    if ((len(dic) == 0)):
        print("Banco de músicas vazio. Por favor insira alguma música para continuar!")
    else:
        print("1- Alterar uma música")
        print("2- Excluir uma música")
        opc = int(input("Digite a opção: "))
        if (opc == 1 or opc == 2):
            if (opc == 1):
                nome = input("Digite o nome da música que deseja alterar: ")
                nome = nome.lower()
                for itens in dic:
                    find = False
                    if (itens == nome):
                        find = True
                        if find:
                            print(f"Deseja mesmo alterar os dados da musica: Nome: {itens.title()} - Data: {dic[itens][0]} - Estilo: {dic[itens][1].title()} - Tempo: {dic[itens][2]} - Compostior: {dic[itens][3].title()} ? ")
                            confirm = input("1- Sim\n2- Não\n ")
                            if (confirm == "1" or confirm == "2"): 
                                if (confirm == "1"):
                                    altnome = input("Insira o novo nome <enter para não alterar>: ")
                                    if (len(altnome)==0):
                                        altnome = dic[itens][0]
                                    dia = input("Digite o novo dia da gravação. <enter> para não alterar: ")
                                    if (len(dia) == 0):
                                        dia = dic[itens][1][0:1]
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
                                    if (len(mes) == 0):
                                        mes = dic[itens][1][3:4]
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
                                    if (len(ano)>4):
                                        dataincorreta = True
                                        while dataincorreta:
                                            print("Digite a data no formato correto!")
                                            ano = input("Digite o ano da gravação: ")
                                            if (len(ano)>4):
                                                dataincorreta = True
                                            else:
                                                dataincorreta = False
                                    else:
                                        dataincorreta = False
                                    altdata = str(dia)+"/"+str(mes)+"/"+ano
                                    altestilo = input("Digite o novo estilo <enter para não alterar>: ")
                                    if (len(altestilo)==0):
                                        altestilo = dic[itens][1]
                                    alttempo = input("Digite o novo tempo <enter para não alterar>: ")
                                    if (len(alttempo)==0):
                                        alttempo = dic[itens][2]
                                    altcompositor = input("Digite o novo compositor <enter para não alterar>: ")
                                    if (len(altcompositor)==0):
                                        altcompositor= dic[itens][3]

                                    altnome = altnome.lower()
                                    altestilo = altestilo.lower()
                                    altcompositor = altcompositor.lower()
                                    tupla = (altdata,altestilo,alttempo,altcompositor)
                                    dic.pop(nome)
                                    dic[altnome] = tupla
                                    return(dic)
                                else:
                                    print("Operação cancelada!")
                            else:
                                print("Digite uma opção válida!")
                        if find == False:
                            print("Musica não cadastrada em nosso banco de músicas!")


            if (opc == 2):
                nome = input("Digite o nome da música que deseja deletar: ")
                nome = nome.lower()
                for itens in dic:
                    if (itens == nome):
                        find = True
                    else:
                        find = False
                    if find:
                        print(f"Deseja mesmo alterar os dados da musica: Nome: {itens.title()} - Data: {dic[itens][0]} - Estilo: {dic[itens][1].title()} - Tempo: {dic[itens][2]} - Compostior: {dic[itens][3].title()} ? ")
                        confirm = input("1- Sim\n2- Não\n")
                        if (confirm == "1" or confirm == "2"):
                            if (confirm == "1"):
                                dic.pop(nome)
                                print(dic)
                                return(dic)
                            else:
                                print("Operação cancelada!")
                    else:
                        print("Música não cadastrada em nosso banco de músicas!")     

        else:
            print("Digite uma opção válida!")

# a = {"te ver":("20/11/2020","plug","1:20","virgingod"),}

# alterarouexcluirmusica(a)