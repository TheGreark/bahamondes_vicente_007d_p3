import numpy

def ver_menu():
    print("""MENÚ
    1. Grabar
    2. Buscar
    3. Retirarse
    4. Salir""")


def validar_opcion():
    while True:
        try:
            opc=int(input("Elija una opcion: "))
            if opc in (1,2,3,4):
                return opc
            else:
                print("ERROR! OPCION NO DISPONIBLE")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")

#listas
lista_ruts=[]
lista_nombres=[]
lista_dias=[]
lista_nom_mascota=[]
lista_habitaciones=[10,9,8,7,6,5,4,3,2,1]
lista_mascota=[]


#validaciones
def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su RUT (sin puntos ni digito verificador):"))
            if rut >=10000000 and rut<=99999999:
                lista_ruts.append(rut)
                return rut
            else:
                print("ERROR! SU RUT DEBE TENER UN MAXIMO DE 8 CARACTERES")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")

def validar_nombre():
    while True:
        try:
            nombre=input("Ingrese su nombre: ")
            if nombre.isalpha:
                lista_nombres.append(nombre)
                return nombre
            else:
                print("ERROR! SU NOMBRE DEBE TENER MAS DE 3 CARACTERES")
        except:
            print("ERROR! SOLO DEBE INGRESAR LETRAS")

def validar_identificador():
    acum=1
    lista_mascota.append(acum+1)



def validar_nom_mascota():
    while True:
        try:
            nombre_mascota=input("Ingrese el nombre de su mascota: ")
            if nombre_mascota.isalpha:
                lista_nom_mascota.append(nombre_mascota)
                return nombre_mascota
            else:
                print("ERROR! SU NOMBRE DEBE TENER MAS DE 3 CARACTERES")
        except:
            print("ERROR! SOLO DEBE INGRESAR LETRAS")


def validar_habitacion():
    for x in range(2):
        print("HABITACIONES ",lista_habitaciones[x],end="\t")
        for y in range (2,2):
            print([x][y],end="")
        hab=int(input("Elija una habitacion para su macota: "))
        if hab in (1,2,3,4,5,6,7,8,9,10):
            print("MASCOTA EN LA HABITACION ",hab)

def validar_dias():
    while True:
        try:
            dias=int(input("Ingrese los días que estara su mascota: "))
            lista_dias.append(dias)
            return dias
        except:
            print("ERROR! SOLO DEBE INGRSAR NÚMEROS ENTEROS")

def validar_grabar():
    validar_rut()
    validar_nombre()
    validar_nom_mascota()
    validar_dias()
    return validar_opcion()


def validar_buscar():
    while True:
        try:
            rut=int(input("Ingrese su RUT (sin puntos ni digito verificador): "))
            if rut >=10000000 and rut<=99999999:
                if rut in lista_ruts:
                    print("Su mascota se encuentra en la habitacion", lista_habitaciones)
                else:
                    print("ERROR! SU RUT NO SE ENCUENTRA REGISTRADO")
                    return rut
            else:
                print("ERROR! SU RUT DEBE TENER UN MAXIMO DE 8 CARACTERES")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERP ENTERO")

def validar_retirada():
    while True: 
            rut = int(input("Ingrese su rut: "))
            if rut in lista_ruts:
                lista_ruts.remove(rut)
                pagar= lista_dias*15000
                print("Su monto a pagar es de ",pagar)
            elif rut not in lista_ruts:
                print("ERROR! NO SE ENCUENTRA REGISTRADO")
                return rut
def validar_salir():  
    while True:    
        try:
            salir=int(input("¿Seguro que quieres SALIR?  Si (1) / No (2): "))
            if salir == 1:
                print("ADIOS")
                break
            elif salir == 2:
                print("")
            else:
                print("ERROR! OPCION NO DISPONIBLE")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO")