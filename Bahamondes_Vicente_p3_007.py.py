import funciones as vb

vb.ver_menu()
vb.validar_opcion

opcion=int(input("Ingrese una opcion: "))

if opcion==1:
    vb.validar_grabar()
elif opcion==2:
    vb.validar_buscar()
elif opcion==3:
    vb.validar_retirada()
elif opcion==4:
    vb.validar_salir()