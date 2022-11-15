from datetime import *

def relatorio(bdm, bdc, bdg):

    #input para a data inicial

    diai = int(input("Digite o dia inicial para a busca: "))
    if (0 < diai < 32):
        diacerto = True
    else:
        diacerto = False
        while (diacerto == False):
            diai = int(input("Digite o dia inicial corretamente: "))
            if (0 < diai < 32):
                diacerto = True
    mesi = int(input("Digite o mês inicial para a busca: "))
    if (0 < mesi < 13):
        mescerto = True
    else:
        mescerto = False
        while (mescerto == False):
            mesi = int(input("Digite o mês inicial corretamente: "))
            if (0 < mesi < 13):
                mescerto = True
    anoi = input("Digite o ano inicial para a busca: ")
    if (len(anoi)==0):
        anocerto = False
        while (anocerto == False):
            anoi = input("Digite o ano corretamente: ")
            anocerto = True
    else:
        anocerto = True
    datai = str(diai) + "/" + str(mesi) + "/" + anoi
    datai = datetime.strptime(datai, '%d/%m/%Y')

    #input para a data final

    diaf = int(input("Digite o dia final para a busca: "))
    if (0 < diaf < 32):
        diacerto = True
    else:
        diacerto = False
        while (diacerto == False):
            diaf = int(input("Digite o dia final corretamente: "))
            if (0 < diaf < 32):
                diacerto = True
    mesf = int(input("Digite o mês final para a busca: "))
    if (0 < mesf < 13):
        mescerto = True
    else:
        mescerto = False
        while (mescerto == False):
            mesi = int(input("Digite o mês final corretamente: "))
            if (0 < mesf < 13):
                mescerto = True
    anof = input("Digite o ano final para a busca: ")
    if (len(anof)==0):
        anocerto = False
        while (anocerto == False):
            anoi = input("Digite o ano corretamente: ")
            anocerto = True
    else:
        anocerto = True
    dataf = str(diaf) + "/" + str(mesf) + "/" + anof
    dataf = datetime.strptime(dataf, '%d/%m/%Y')

    for grav in bdg:

        datadic = grav[2]
        datadic = str(datadic)
        datadic = datetime.strptime(datadic, '%d/%m/%Y')
        
        if (datadic >= datai and datadic <= dataf):
            music = grav[0]
            cantor = grav[1]
            

            for m in bdm:
                if (m == music):
                    print(f"Dados da música - Nome: {m.title()} - Data: {bdm[m][0]} - Estilo: {bdm[m][1].title()} - Tempo: {bdm[m][2]} - Compositor: {bdm[m][3].title()} ")
            for c in bdc:
                if (c == cantor):
                    print(f"Dados do cantor - Nome artistico: {c.title()} - Nome real: {bdc[c][0].title()} - Data de nascimento: {bdc[c][1]} - Email: {bdc[c][2]} - Telefone: {bdc[c][3]}", end="")     

            print(f"Albúm: {bdg[grav][0]}", end="")
            print("Instrumentos: ", end="")
            for inst in bdg[grav][1]:
                print(f" {inst.title()} ",end="")
        
        else:
            print(f"Nenhuma gravação registrada entre {datai} e {dataf}")

        print()