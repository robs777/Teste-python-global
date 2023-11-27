


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
    if paciente == "M" or "m":
        tipo_exameM()
    elif paciente == "F" or "f":
        tipo_exameF()

    else:
        print(f"opção {paciente} inválida. Digite apenas a letra M ou F")



###################################


#HOMEM


###################################



def tipo_exameM():
    print("Você gostaria de receber resultados de quais tipos de exame?")
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
    print("11 - Opção para receber resultados de todos os exames")

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
    hemacias = input("Hemácias: ")
    hemoglobina = input("hemoglobina")
    hematocrito = input("hematocrito")
    hb_corp_média = input("hb_corp_média")
    volume_corp_médio = input("volume_corp_médio")
    conc_hb_corp_media = input("Conc. Hb. Corp. Média: ")
    RDW = input("RDW")


    print("LEUCOGRAMA")
    leucocitos = input("leucocitos ")
    metamielócitos = input("metamielócitos ")
    bastonetes = input("bastoneres ")
    segmentados = input("segmentados: ")
    eosinófilos = input("eosinófilos: ")
    basofilos = input("basofilos: ")
    linfocitos = input("linfocitos: ")
    monocitos = input("monocitos: ")
    plaquetas = input("plaquetas: ")

    if hemacias >=4.5 and hemacias <=6:
        print( "está na média")
    elif hemacias < 4.5:
        print( "abaixo da média")
    
    elif hemacias > 6:
        print( "acima da média")
    
    #########################
    
    if hemoglobina >=13 and hemoglobina <=17.8:
        print( "está na média")
    elif hemoglobina <13:
        print( "abaixo da média")
    elif hemoglobina > 17.8:
        print( "acima da média")
    
    ########################
    if hematocrito >=40 and hematocrito <=54:
        print( "está na média")
    elif hematocrito < 40:
        print( "abaixo da média")
    elif hematocrito > 54:
        print( "acima da média")
    
    ##########################
    if hb_corp_média >=27 and hb_corp_média <=33:
        print( "está na média")
    elif hb_corp_média < 27:
        print( "abaixo da média")
    
    elif hb_corp_média > 33:
        print( "acima da média")
    
    #########################
    if volume_corp_médio >=80 and volume_corp_médio <=100:
        print( "está na média")
    elif volume_corp_médio < 80:
        print( "abaixo da média")
    
    elif volume_corp_médio > 100:
        print( "acima da média")
    
    #########################
    if conc_hb_corp_media >=30 and conc_hb_corp_media <=36:
        print( "está na média")
    elif conc_hb_corp_media < 30:
        print( "abaixo da média")
    
    elif conc_hb_corp_media > 36:
        print( "acima da média")
    
    #########################
    if RDW >=11 and RDW <=14.5:
        print( "está na média")
    elif RDW < 11:
        print( "abaixo da média")
    
    elif RDW > 14.5:
        print( "acima da média")
    
    #########################
    #leucograma
    if leucocitos >=3900 and leucocitos <=12100:
        print( "está na média")
    elif leucocitos < 3900:
        print( "abaixo da média")
    
    elif leucocitos > 12100:
        print( "acima da média")
    
    #########################
    if metamielócitos ==0:
        print( "está na média")
    elif metamielócitos < 0:
        print( "abaixo da média")
    
    elif metamielócitos > 0:
       print("acima da média")
    
    #########################
    if bastonetes >=1 and bastonetes <=6:
        print( "está na média")
    elif bastonetes < 1:
        print( "abaixo da média")
    
    elif bastonetes > 6:
        print( "acima da média")
    
    #########################
    if segmentados >=50 and segmentados <=68:
        print( "está na média")
    elif segmentados < 50:
        print( "abaixo da média")
    
    elif segmentados > 68:
        print( "acima da média")
    
    #########################
    if eosinófilos >=1 and eosinófilos <=8:
        print( "está na média")
    elif eosinófilos < 1:
        print("abaixo da média")
    
    elif eosinófilos > 8:
        print( "acima da média")
    
    #########################
    if basofilos >=0 and basofilos <=2:
        print( "está na média")
    elif basofilos < 0:
        print( "abaixo da média")
    
    elif basofilos > 2:
        print( "acima da média")
    
    #########################
    if linfocitos >=18 and linfocitos <=44:
        print( "está na média")
    elif linfocitos < 18:
        print( "abaixo da média")
    
    elif linfocitos> 44:
        print( "acima da média")
    
    #########################
    if monocitos>=2 and monocitos <=12:
        print( "está na média")
    elif monocitos < 2:
        print( "abaixo da média")
    
    elif monocitos > 12:
        print( "acima da média")
    #########################
    if plaquetas >=150000 and plaquetas <=450000:
        print( "está na média")
    elif plaquetas < 150000:
        print( "abaixo da média")
    
    elif plaquetas > 450000:
        print( "acima da média")
    
    #########################


    
    


########################################

def glicemia():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=60 and resultado<= 99:
        print ("está na média")
    elif resultado < 60:
        print ("abaixo da média")
    
    elif resultado > 99:
        print("acima da média")
   
    
    



########################################



def creatina():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=0.76 and resultado<= 1.24:
        print ("está na média")
    elif resultado < 0.76:
        print("abaixo da média")
    
    elif resultado > 1.24:
        print("acima da média")


########################################
def acido_urico():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=3.7 and resultado<= 7.8:
        print("está na média")
    elif resultado < 3.7:
        print("abaixo da média")
    
    elif resultado > 7.8:
        print("acima da média")



########################################
def tgo():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")
    
    if resultado <= 40:
        print("na média")
    
    elif resultado > 40:
        print("acima da média")


########################################
    
def tgp():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado <= 58:
        print("na média")
    
    elif resultado > 58:
        print("acima da média")



########################################
def lipidograma():
    colesterol = input("colesterol total: ")
    hdl = input("colesterol HDL: ")
    ldl = input("colesterol LDL: ")
    nhdl = input("colesterol Não-HDL: ")
    triglicerides = input("triglicerides: ")

    if colesterol <= 190:
        print("na média")
    
    elif colesterol > 190:
        print("acima da média")
    
    #########################
    if hdl >= 40:
        print("na média")
    
    elif hdl < 40:
        print("abaixo da média")
    
    #########################
    if ldl <= 130:
        print("risco baixo")

    elif ldl <=100:
        print("risco intermediario")

    elif ldl <=70:
        print("risco alto")

    elif ldl <=50:
        print("risco muito alto")
    
    elif ldl > 130:
        print( "acima da média")

    
    
    #########################
    
    if nhdl <= 160:
        print("risco baixo")

    elif nhdl <=130:
        print("risco intermediario")

    elif nhdl <=100:
        print("risco alto")

    elif nhdl <=80:
        print("risco muito alto")
    
    elif nhdl > 160:
        print( "acima da média")
    
    #########################
    if triglicerides < 150:
        print( "está na média")
    
    elif triglicerides > 150:
        print( "acima da média")
    
    #########################





########################################

def hidroxivitamina():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    
    if resultado > 20:
        print( "saudável")
    
    elif resultado < 20:
        print( "não saudável")

########################################

def tsh():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=0.38 and resultado<= 5.33:
        print( "está na média")
    elif resultado < 0.38:
        print( "abaixo da média")
    
    elif resultado > 5.33:
        print( "acima da média")

########################################

def t4_livre():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=0.54 and resultado<= 1.24:
        print( "está na média")
    elif resultado < 0.54:
        print( "abaixo da média")
    
    elif resultado > 1.24:
        print("acima da média")

########################################
def todos(): 
    hemograma()
    glicemia()
    creatina()
    acido_urico()
    tgo()
    tgp()
    lipidograma()
    hidroxivitamina()
    tsh()
    t4_livre()

    


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
    hemacias = input("Hemácias: ")
    hemoglobina = input("hemoglobina")
    hematocrito = input("hematocrito")
    hb_corp_média = input("hb_corp_média")
    volume_corp_médio = input("volume_corp_médio")
    conc_hb_corp_media = input("Conc. Hb. Corp. Média: ")
    RDW = input("RDW")


    print("LEUCOGRAMA")
    leucocitos = input("leucocitos ")
    metamielócitos = input("metamielócitos ")
    bastonetes = input("bastoneres ")
    segmentados = input("segmentados: ")
    eosinófilos = input("eosinófilos: ")
    basofilos = input("basofilos: ")
    linfocitos = input("linfocitos: ")
    monocitos = input("monocitos: ")
    plaquetas = input("plaquetas: ")

    if hemacias >=4.5 and hemacias <=6:
        print( "está na média")
    elif hemacias < 4.5:
        print( "abaixo da média")
    
    elif hemacias > 6:
        print( "acima da média")
    
    #########################
    
    if hemoglobina >=13 and hemoglobina <=17.8:
        print( "está na média")
    elif hemoglobina <13:
        print( "abaixo da média")
    elif hemoglobina > 17.8:
        print( "acima da média")
    
    ########################
    if hematocrito >=40 and hematocrito <=54:
        print( "está na média")
    elif hematocrito < 40:
        print( "abaixo da média")
    elif hematocrito > 54:
        print( "acima da média")
    
    ##########################
    if hb_corp_média >=27 and hb_corp_média <=33:
        print( "está na média")
    elif hb_corp_média < 27:
        print( "abaixo da média")
    
    elif hb_corp_média > 33:
        print( "acima da média")
    
    #########################
    if volume_corp_médio >=80 and volume_corp_médio <=100:
        print( "está na média")
    elif volume_corp_médio < 80:
        print( "abaixo da média")
    
    elif volume_corp_médio > 100:
        print( "acima da média")
    
    #########################
    if conc_hb_corp_media >=30 and conc_hb_corp_media <=36:
        print( "está na média")
    elif conc_hb_corp_media < 30:
        print( "abaixo da média")
    
    elif conc_hb_corp_media > 36:
        print( "acima da média")
    
    #########################
    if RDW >=11 and RDW <=14.5:
        print( "está na média")
    elif RDW < 11:
        print( "abaixo da média")
    
    elif RDW > 14.5:
        print( "acima da média")
    
    #########################
    #leucograma
    if leucocitos >=3900 and leucocitos <=12100:
        print( "está na média")
    elif leucocitos < 3900:
        print( "abaixo da média")
    
    elif leucocitos > 12100:
        print( "acima da média")
    
    #########################
    if metamielócitos ==0:
        print( "está na média")
    elif metamielócitos < 0:
        print( "abaixo da média")
    
    elif metamielócitos > 0:
       print("acima da média")
    
    #########################
    if bastonetes >=1 and bastonetes <=6:
        print( "está na média")
    elif bastonetes < 1:
        print( "abaixo da média")
    
    elif bastonetes > 6:
        print( "acima da média")
    
    #########################
    if segmentados >=50 and segmentados <=68:
        print( "está na média")
    elif segmentados < 50:
        print( "abaixo da média")
    
    elif segmentados > 68:
        print( "acima da média")
    
    #########################
    if eosinófilos >=1 and eosinófilos <=8:
        print( "está na média")
    elif eosinófilos < 1:
        print("abaixo da média")
    
    elif eosinófilos > 8:
        print( "acima da média")
    
    #########################
    if basofilos >=0 and basofilos <=2:
        print( "está na média")
    elif basofilos < 0:
        print( "abaixo da média")
    
    elif basofilos > 2:
        print( "acima da média")
    
    #########################
    if linfocitos >=18 and linfocitos <=44:
        print( "está na média")
    elif linfocitos < 18:
        print( "abaixo da média")
    
    elif linfocitos> 44:
        print( "acima da média")
    
    #########################
    if monocitos >=2 and monocitos <=12:
        print( "está na média")
    elif monocitos < 2:
        print( "abaixo da média")
    
    elif monocitos > 12:
        print( "acima da média")
    #########################
    if plaquetas >=150000 and plaquetas <=450000:
        print( "está na média")
    elif plaquetas < 150000:
        print( "abaixo da média")
    
    elif plaquetas > 450000:
        print( "acima da média")
    
    #########################


    
    


########################################

def glicemiaF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=60 and resultado<= 99:
        print ("está na média")
    elif resultado < 60:
        print ("abaixo da média")
    
    elif resultado > 99:
        print("acima da média")
   
    
    



########################################



def creatinaF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=0.76 and resultado<= 1.24:
        print ("está na média")
    elif resultado < 0.76:
        print("abaixo da média")
    
    elif resultado > 1.24:
        print("acima da média")


########################################
def acido_uricoF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=3.7 and resultado<= 7.8:
        print("está na média")
    elif resultado < 3.7:
        print("abaixo da média")
    
    elif resultado > 7.8:
        print("acima da média")



########################################
def tgoF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")
    
    if resultado <= 40:
        print("na média")
    
    elif resultado > 40:
        print("acima da média")


########################################
    
def tgpF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado <= 58:
        print("na média")
    
    elif resultado > 58:
        print("acima da média")



########################################
def lipidogramaF():
    colesterol = input("colesterol total: ")
    hdl = input("colesterol HDL: ")
    ldl = input("colesterol LDL: ")
    nhdl = input("colesterol Não-HDL: ")
    triglicerides = input("triglicerides: ")

    if colesterol <= 190:
        print("na média")
    
    elif colesterol > 190:
        print("acima da média")
    
    #########################
    if hdl >= 40:
        print("na média")
    
    elif hdl < 40:
        print("abaixo da média")
    
    #########################
    if ldl <= 130:
        print("risco baixo")

    elif ldl <=100:
        print("risco intermediario")

    elif ldl <=70:
        print("risco alto")

    elif ldl <=50:
        print("risco muito alto")
    
    elif ldl > 130:
        print( "acima da média")

    
    
    #########################
    
    if nhdl <= 160:
        print("risco baixo")

    elif nhdl <=130:
        print("risco intermediario")

    elif nhdl <=100:
        print("risco alto")

    elif nhdl <=80:
        print("risco muito alto")
    
    elif nhdl > 160:
        print( "acima da média")
    
    #########################
    if triglicerides < 150:
        print( "está na média")
    
    elif triglicerides > 150:
        print( "acima da média")
    
    #########################





########################################

def hidroxivitaminaF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    
    if resultado > 20:
        print( "saudável")
    
    elif resultado > 20:
        print( "não saudável")

########################################

def tshF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=0.38 and resultado<= 5.33:
        print( "está na média")
    elif resultado < 0.38:
        print( "abaixo da média")
    
    elif resultado > 5.33:
        print( "acima da média")

########################################

def t4_livreF():
    print("Coloque os valores de cada requisito")
    resultado = input("resultado: ")
    material = input("material: ")
    metodo = input("metodo: ")

    if resultado >=0.54 and resultado<= 1.24:
        print( "está na média")
    elif resultado < 0.54:
        print( "abaixo da média")
    
    elif resultado > 1.24:
        print("acima da média")

########################################
def todosF(): 
    hemogramaF()
    glicemiaF()
    creatinaF()
    acido_uricoF()
    tgoF()
    tgpF()
    lipidogramaF()
    hidroxivitaminaF()
    tshF()
    t4_livreF()













if __name__ == "__main__":
    main()

