

def existearq(nome1,nome2,nome3):
    import os
    if os.path.exists(nome1 and nome2 and nome3):
        return(True)
    else:
        return(False)


def escrita(bdm,bdc,bdg):
    arqm = open("bdm.txt", "w")


    for i in bdm:
        nome = i
        data = bdm[i][0]
        estilo = bdm[i][1]
        tempo = bdm[i][2]
        compostitor = bdm[i][3]
        escrita = nome+";"+data+";"+estilo+";"+tempo+";"+compostitor+"\n"
        arqm.write(escrita)
    arqm.close()
    arqc = open("bdc.txt","w")
    for i in bdc:
        nome = i
        nomeartistico = bdc[i][0]
        datanasc = bdc[i][1]
        email = bdc[i][2]
        telefone = bdc[i][3]
        escrita = nome+";"+nomeartistico+";"+datanasc+";"+email+";"+telefone+"\n"
        arqc.write(escrita)
    arqc.close()
    arqg = open("bdg.txt","w")
    for i in bdg:
        nomem = i[0]
        nomea = i[1]
        data = i[2]
        album = bdg[i][0]
        instwrite = ""
        for inst in bdg[i][1]:
            instwrite = instwrite + inst + "#"
        escrita = nomem + ";" + nomea + ";" + data + ";" + album + ";" + instwrite + "\n"
        arqg.write(escrita)
    arqg.close()

def leitura(bdm, bdc, bdg):

    arqm = open("bdm.txt", "r")

    for l in arqm:
        L = l.split(";")

        musica = L[0]
        data = L[1]
        estilo = L[2]
        tempo = L[3]
        cantor = L[4]

        cantor = cantor[:-1]      

        print(L)

    arqm.close()

    arqc = open("bdc.txt", "r")

    for l in arqc:
        L = l.split(";")

        print(L)

    arqc.close()

    arqg = open("bdg.txt", "r")
    
    for l in arqg:
        L = l.split(";")

        print(L)

    arqg.close()
    

# ['te ver', '20/11/2020', 'plug', '1:20', 'virgingod\n']
# ['vgod', 'mateus', '21/07/2000', 'vgod@gmail.com', '16991045382\n']
# ['te ver', 'vgod', '19/12/2020', 'muito amor', 'fl studio#drom#\n']