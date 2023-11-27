


def main():
    while True:
        print("-="*20)
        print("Seja bem vindo")
        print("-="*20)
        print("Gostaria de fazer a avaliação? ")
        print("1-sim // 2-não")
        paciente = input("Digite 1 ou 2: " )

        if paciente == "1":
            tipo_exame()

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

def glicemia():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))



########################################



def creatina():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))


########################################
def acido_urico():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))


########################################
def tgo():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

########################################
    
def tgp():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))


########################################
def lipidograma():
    colesterol = float(input("colesterol total: "))
    hdl = float(input("colesterol HDL: "))
    ldl = float(input("colesterol LDL: "))
    vldl = float(input("colesterol VLDL: "))
    nhdl = float(input("colesterol Não-HDL: "))
    triglicerides = float(input("triglicerides: "))

########################################

def hidroxivitamina():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

########################################

def tsh():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))

########################################

def t4_livre():
    print("Coloque os valores de cada requisito")
    resultado = float(input("resultado: "))
    material = float(input("material: "))
    metodo = float(input("metodo: "))
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

