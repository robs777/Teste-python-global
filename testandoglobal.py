


def main():
    while True:
        print("-="*20)
        print("Seja bem vindo")
        print("-="*20)
        print("Gostaria de fazer a avaliação? ")
        print("1-sim // 2-não")
        paciente = input("Digite 1 ou 2: " )

        if paciente == "1":
            sexo()

        elif paciente == "2":
            print ("Ok, encerrando.")
            break

        else:
            print(f'opção {paciente} inválida. Digite apenas sim ou não.')

def sexo():
    print("informe seu sexo biológico")
    print ("M = masculino // F = feminino")
    paciente = input("Digite M ou F: ")
    if paciente == "M":
        tipo_exameM()
    elif paciente == "F":
        tipo_exameF()

    else:
        print(f"opção {paciente} inválida. Digite apenas a letra M ou F")



###################################


#HOMEM


###################################



def tipo_exameM():
    print("Você gostaria de cadastrar quais tipos de exame?")S
    print("1- Hemograma Completo")
    print("2- Glicemia")
    print("3- Creatina")
    print("4- Ácido úrico")
    print("5- Transaminase Glutamico Oxalacética - TGO")
    print("6- Trasaminase Glutamico Pirúvica - TGP")
    print("7- Lipidograma Completo")
    print("8- 25-Hidroxivitamina D")
    print("9- TSH Ultra Sensível")
    print("10- T4 Livre")
    print("11 - Opção para cadastrar todos os exames")

    paciente = input("Digite sua escolha: ")

    if paciente == "1": 
        hemograma()

    elif paciente =="2":
        glicemia()

    elif paciente =="3":
        creatina()
        
    elif paciente =="4":
        acido_urico()
    elif paciente =="5":
        tgo()
    elif paciente =="6":
        tgp()
    elif paciente =="7":
        lipidograma()
    elif paciente =="8":
        hidroxivitamina()
    elif paciente =="9":
        tsh()
    elif paciente =="10":
        t4_livre()
    elif paciente =="11":
        todos()
    else:
        print(f"Opção {paciente} inválida. Digite Novamente.")


def hemograma():
    print("Coloque os valores de cada requisito")
    print ("ERITROGRAMA")
    hemacias = float(input("Hemácias: "))
    hemoglobina = float(input("hemoglobina"))
    hematocrito = float(input("hematocrito"))
    hb_corp_média = float(input("hb_corp_média"))
    volume_corp_médio = float(input("volume_corp_médio"))
    conc_hb_corp_media = float(input("Conc. Hb. Corp. Média: "))
    RDW = float(input("RDW"))


    print("LEUCOGRAMA")
    leucocitos = float(input("leucocitos "))
    metamielócitos = float(input("metamielócitos "))
    bastonetes = float(input("bastoneres "))
    segmentados = float(input("segmentados: "))
    eosinófilos = float(input("eosinófilos: "))
    basofilos = float(input("basofilos: "))
    linfocitos = float(input("linfocitos: "))
    monocitos = float(input("monocitos: "))
    plaquetas = float(input("plaquetas: "))

    if 4.5 >= hemacias >= 6:
        return "está na média"
    elif hemacias < 4.5:
        return "abaixo da média"
    
    elif hemacias > 6:
        return "acima da média"
    
    #########################
    
    if 13 >= hemoglobina >= 17.8:
        return "está na média"
    elif hemoglobina <13:
        return "abaixo da média"
    elif hemoglobina > 17.8:
        return "acima da média"
    
    ########################
    if 40>= hematocrito >= 54:
        return "está na média"
    elif hematocrito < 40:
        return "abaixo da média"
    elif hematocrito > 54:
        return "acima da média"
    
    ##########################
    if 4.5 >= hb_corp_média >= 6:
        return "está na média"
    elif hb_corp_média < 4.5:
        return "abaixo da média"
    
    elif hb_corp_média > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= volume_corp_médio >= 6:
        return "está na média"
    elif volume_corp_médio < 4.5:
        return "abaixo da média"
    
    elif volume_corp_médio > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= conc_hb_corp_media >= 6:
        return "está na média"
    elif conc_hb_corp_media < 4.5:
        return "abaixo da média"
    
    elif conc_hb_corp_media > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= RDW >= 6:
        return "está na média"
    elif RDW < 4.5:
        return "abaixo da média"
    
    elif RDW > 6:
        return "acima da média"
    
    #########################
    #leucograma
    if 4.5 >= leucocitos >= 6:
        return "está na média"
    elif leucocitos < 4.5:
        return "abaixo da média"
    
    elif leucocitos > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= metamielócitos >= 6:
        return "está na média"
    elif metamielócitos < 4.5:
        return "abaixo da média"
    
    elif metamielócitos > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= bastonetes >= 6:
        return "está na média"
    elif bastonetes < 4.5:
        return "abaixo da média"
    
    elif bastonetes > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= segmentados >= 6:
        return "está na média"
    elif segmentados < 4.5:
        return "abaixo da média"
    
    elif segmentados > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= eosinófilos >= 6:
        return "está na média"
    elif eosinófilos < 4.5:
        return "abaixo da média"
    
    elif eosinófilos > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= basofilos >= 6:
        return "está na média"
    elif basofilos < 4.5:
        return "abaixo da média"
    
    elif basofilos > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= linfocitos >= 6:
        return "está na média"
    elif linfocitos < 4.5:
        return "abaixo da média"
    
    elif linfocitos> 6:
        return "acima da média"
    
    #########################
    if 4.5 >= monocitos >= 6:
        return "está na média"
    elif monocitos < 4.5:
        return "abaixo da média"
    
    elif monocitos > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= plaquetas >= 6:
        return "está na média"
    elif plaquetas < 4.5:
        return "abaixo da média"
    
    elif plaquetas > 6:
        return "acima da média"
    
    #########################


    
    


########################################

def glicemia():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"


########################################



def creatina():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"



########################################
def acido_urico():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"



########################################
def tgo():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"


########################################
    
def tgp():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"



########################################
def lipidograma():
    colesterol = float(input("colesterol total: "))
    hdl = float(input("colesterol HDL: "))
    ldl = float(input("colesterol LDL: "))
    vldl = float(input("colesterol VLDL: "))
    nhdl = float(input("colesterol Não-HDL: "))
    triglicerides = float(input("triglicerides: "))

    if 4.5 >= colesterol >= 6:
        return "está na média"
    elif colesterol < 4.5:
        return "abaixo da média"
    
    elif colesterol > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= hdl >= 6:
        return "está na média"
    elif hdl < 4.5:
        return "abaixo da média"
    
    elif hdl > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= ldl >= 6:
        return "está na média"
    elif ldl < 4.5:
        return "abaixo da média"
    
    elif ldl > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= vldl >= 6:
        return "está na média"
    elif vldl < 4.5:
        return "abaixo da média"
    
    elif vldl > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= nhdl >= 6:
        return "está na média"
    elif nhdl < 4.5:
        return "abaixo da média"
    
    elif nhdl > 6:
        return "acima da média"
    
    #########################
    if 4.5 >= triglicerides >= 6:
        return "está na média"
    elif triglicerides < 4.5:
        return "abaixo da média"
    
    elif triglicerides > 6:
        return "acima da média"
    
    #########################





########################################

def hidroxivitamina():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"

########################################

def tsh():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"

########################################

def t4_livre():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

    if 4.5 >= resultado >= 6:
        return "está na média"
    elif resultado < 4.5:
        return "abaixo da média"
    
    elif resultado > 6:
        return "acima da média"

########################################
def todos(): 
    pass


###################################


#MULHER


###################################

def tipo_exameF():
    print("Você gostaria de cadastrar quais tipos de exame?")
    print("1- Hemograma Completo")
    print("2- Glicemia")
    print("3- Creatina")
    print("4- Ácido úrico")
    print("5- Transaminase Glutamico Oxalacética - TGO")
    print("6- Trasaminase Glutamico Pirúvica - TGP")
    print("7- Lipidograma Completo")
    print("8- 25-Hidroxivitamina D")
    print("9- TSH Ultra Sensível")
    print("10- T4 Livre")
    print("11 - Opção para cadastrar todos os exames")

    paciente = input("Digite sua escolha: ")

    if paciente == "1": 
        hemogramaF()

    elif paciente =="2":
        glicemiaF()

    elif paciente =="3":
        creatinaF()
        
    elif paciente =="4":
        acido_uricoF()
    elif paciente =="5":
        tgoF()
    elif paciente =="6":
        tgpF()
    elif paciente =="7":
        lipidogramaF()
    elif paciente =="8":
        hidroxivitaminaF()
    elif paciente =="9":
        tshF()
    elif paciente =="10":
        t4_livreF()
    elif paciente =="11":
        todosF()
    else:
        print(f"Opção {paciente} inválida. Digite Novamente.")


def hemogramaF():
    print("Coloque os valores de cada requisito")
    print ("ERITROGRAMA")
    hemacias = float(input("Hemácias: "))
    hemoglobina = float(input("hemoglobina"))
    hematocrito = float(input("hematocrito"))
    hb_corp_média = float(input("hb_corp_média"))
    volume_corp_médio = float(input("volume_corp_médio"))
    RDW = float(input("RDW"))

    if hemacias == 5:
        return "bom"

    print("LEUCOGRAMA")
    leucocitos = float(input("leucocitos "))
    metamielócitos = float(input("metamielócitos "))
    bastoneres = float(input("bastoneres "))
    segmentados = float(input("segmentados: "))
    eosinófilos = float(input("eosinófilos: "))
    basofilos = float(input("basofilos: "))
    linfocitos = float(input("linfocitos: "))
    monocitos = float(input("monocitos: "))
    plaquetas = float(input("plaquetas: "))


########################################

def glicemiaF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))



########################################



def creatinaF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))


########################################
def acido_uricoF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))


########################################
def tgoF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

########################################
    
def tgpF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))


########################################
def lipidogramaF():
    colesterol = float(input("colesterol total: "))
    hdl = float(input("colesterol HDL: "))
    ldl = float(input("colesterol LDL: "))
    vldl = float(input("colesterol VLDL: "))
    nhdl = float(input("colesterol Não-HDL: "))
    triglicerides = float(input("triglicerides: "))

########################################

def hidroxivitaminaF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

########################################

def tshF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

########################################

def t4_livreF():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))
########################################
def todosF(): 
    pass














if __name__ == "__main__":
    main()

