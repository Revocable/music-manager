#Inserindo Cantores

def criarcantor(dic,dic2):

    nomeart = input("Digite o nome artístico do cantor:").lower()

    if (nomeart in dic or nomeart in dic2):
        print("Essse cantor já foi cadastrado!")
    else:
        nome = input('Digite o nome real do cantor:').lower() 

        if (nome in dic):
            print("Musica já cadastrada!")
        else:
            dia = int(input("Digite o dia de nascimento: "))

            if (dia < 0 or dia > 31):
                dataincorreta = True

                while dataincorreta:
                    print("Digite a data no formato correto!")

                    dia = int(input("Digite o dia de nascimento: "))
                    if (0 < dia < 32):
                        dataincorreta = False
                    else:
                        dataincorreta = True
            else:
                dataincorreta = False

            mes = int(input("Digite o mês de nascimento: "))

            if (mes < 0 or mes > 12):
                dataincorreta = True
                while dataincorreta:
                    print("Digite a data no formato correto!")

                    mes = int(input("Digite o mês de nascimento: "))

                    if (0 < mes < 13):
                        dataincorreta = False
                    else:
                        dataincorreta = True
            else:
                dataincorreta = False

            ano = input("Digite o ano de nascimento: ")

            if (len(ano) > 4):
                dataincorreta = True
                while dataincorreta:
                    print("Digite a data no formato correto!")

                    ano = input("Digite o ano do nascimento: ")

                    if (len(ano)>4):
                        dataincorreta = True
                    else:
                        dataincorreta = False
            else:
                dataincorreta = False
            data = str(dia)+"/"+str(mes)+"/"+ano

        email = input("Digite o email do cantor:").lower()
        
        if ( len(email)==0 or "@" not in email):
            emailvalido = False
            while (emailvalido == False):
                email = input("Digite um email válido: ")
                if (len(email)>0):
                    emailvalido = True
        else:
            emailvalido = True
        telefone = input("Digite o telefone do cantor:")
        if (len(telefone)==0):
            telefonevalido = False
            while (telefonevalido == False):
                telefone = input("Digite um telefone válido: ")
                if (len(telefone)>0):
                    telefonevalido = True
        else:
            emailvalido = True

        tupla = (nome, data, email, telefone,)

        dic[nomeart] = tupla
        return(dic)

#Listando todos os Cantores

def listarcantores(dic):
    
    if (len(dic) == 0):
        print("Banco de Dados vazio!")
    else:
        print("Cantores Registrados:")
        for i in dic:
            print(f"Cantor: {i.title()} Nome Real: {dic[i][0].title()} Data de Nascimento: {dic[i][1]} Email: {dic[i][2]} Telefone: {dic[i][3]}")

#Listando um Cantor específico

def listarcantorespecífico(dic):

    if (len(dic) == 0):
        print("Banco de Dados vazio!")
    else:
        cons = input("Digite o nome do cantor que deseja buscar:").lower()

        if (cons in dic):
            for i in dic:
                if (i == cons):
                    print(f"Cantor: {i.title()} Nome Real: {dic[i][0].title()} Data de Nascimento: {dic[i][1]} Email: {dic[i][2]} Telefone: {dic[i][3]}")
                    print()
        else:
            print("Cantor não cadastrado em nosso Banco de Dados!")

#Alterando ou excluindo um Cantor

def alterarouexcluircantor(dic):

    if (len(dic) == 0):
        print("Banco de Dados vazio!")
    else:
        print("1 - Alterar um cantor")
        print("2 - Excluir um cantor")

        opc = int(input("Digite a opção: "))

        if (0 < opc < 3):
            if (opc == 1):
                nome = input("Digite o nome do cantor que deseja alterar: ").lower()

                for i in dic:
                    achou = False
                    if (i == nome):
                        achou = True

                        if achou:
                            print(f"Deseja mesmo alterar os dados do cantor: Nome: {i}?")
                            confirma = int(input("1- Sim\n2- Não\n"))

                            if (0 < confirma < 2): 
                                if (confirma == 1):
                                    altnomeart = input("Digite o novo nome artístico <enter> para ignorar:").lower()
                                    if (altnomeart == ""):
                                        altnomeart = nome

                                    altnomereal = input("Digite o novo nome real <enter> para ignorar:").lower()
                                    if (altnomereal == ""):
                                        altnomereal = dic[i][0]

                                    dia = input("Digite o dia de nascimento (<enter> para não alterar):")

                                    if (dia == ""):
                                        dia = dic[i][2][0:2]

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

                                    # dd/mm/aaaa

                                    if (mes == ""):
                                        mes = dic[i][2][2:4]

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

                                    altemail = input("Digite o novo email <enter> para ignorar:").lower()
                                    if (altemail == ""):
                                        altemail= dic[i][2]

                                    alttelefone = input("Digite o novo telefone <enter> para não alterar:")
                                    if (alttelefone == ""):
                                        alttelefone = dic[i][3]
            
                                    tupla = (altnomereal, altdata, altemail, alttelefone)
                                    dic.pop(nome)
                                    dic[altnomeart] = tupla

                                    return(dic)

                                else:
                                    print("Operação cancelada!")
                                    
                            else:
                                print("Digite uma opção válida!")

                        if achou == False:
                            print("Cantor não cadastrado em nosso Banco de Dados!")

            if (opc == 2):
                nome = input("Digite o nome da música que deseja deletar: ").lower()
                for i in dic:
                    if (i == nome):
                        achou = True

                    if achou:
                        print(f"Deseja mesmo alterar os dados do cantor: Nome: {i}?")
                        confirma= int(input("1- Sim\n2- Não\n"))
                        if (0 < confirma < 3):
                            if (confirma == 1):
                                dic.pop(nome)
                                print(dic)
                                return(dic)
                            else:
                                print("Operação cancelada!")

                        else:
                            print("Digite uma opção válida!")
                    else:
                        print("Música não cadastrada em nosso Banco de Dados!")     

        else:
            print("Digite uma opção válida!")