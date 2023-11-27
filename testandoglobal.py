


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



def tipo_exame():
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

###################################
def hemograma():
    print("Coloque os valores de cada requisito")
    print ("ERITROGRAMA")
    hemacias = float(input("Hemácias: "))
    hemoglobina = float(input("hemoglobina"))
    hematocrito = float(input("hematocrito"))
    hb_corp_média = float(input("hb_corp_média"))
    volume_corp_médio = float(input("volume_corp_médio"))
    RDW = float(input("RDW"))

    print("LEUCOGRAMA")
    leucocitos = float(input("Hemácias: "))
    metamielócitos = float(input("Hemácias: "))
    bastoneres = float(input("Hemácias: "))
    segmentados = float(input("Hemácias: "))
    eosinófilos = float(input("Hemácias: "))
    basofilos = float(input("Hemácias: "))
    linfocitos = float(input("Hemácias: "))
    monocitos = float(input("Hemácias: "))
    plaquetas = float(input("Hemácias: "))


########################################

def glicemia():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))



########################################



def creatina():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))


########################################
def acido_urico():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))


########################################
def tgo():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))

########################################
    
def tgp():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))


########################################
def lipidograma():
    colesterol = float(input("Hemácias: "))
    hdl = float(input("Hemácias: "))
    ldl = float(input("Hemácias: "))
    vldl = float(input("Hemácias: "))
    nhdl = float(input("Hemácias: "))
    triglicerides = float(input("Hemácias: "))

########################################

def hidroxivitamina():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))

########################################

def tsh():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))

########################################

def t4_livre():
    print("Coloque os valores de cada requisito")
    resultado = float(input("Hemácias: "))
    material = float(input("Hemácias: "))
    metodo = float(input("Hemácias: "))
########################################
def todos(): 
    pass











if __name__ == "__main__":
    main()

