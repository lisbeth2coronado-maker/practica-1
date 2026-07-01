salida = "si"

while salida == "si":
    print("\n---MENÚ---\n1. Sumar\n2.Restar\n3. Salir")
    entrada1 = int(input("seleccioná una opcion(1\2\3): "))
    if entrada1 == "1":
        entrada_suma1 = input("Ingrese el primer numero a sumar: ")
        entrada_suma1 = input("Ingrese el segundo numero a sumar: ")
        resultado = entrada_suma1 + entrada_suma2
        print("El resultado de la suma es: ", resultado)
    elif entrada1 == "2":  
       entrada_resta1 = int(input("Ingrese el primer numero a restar: "))
       entrada_resta2 = int(input("Ingrese el primer numero a restar:"))
       resultado = entrada_resta1 - entrada_resta2
       print("El resultado de la resta es: ", resultado)
    elif entrada1 =="3":
        print("Programa finalizado")
        salida ="no"
    else:
        print("Debes ingresar una opcion valida(1\2\3)")    

  

    