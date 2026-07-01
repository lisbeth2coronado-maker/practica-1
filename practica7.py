ingreso = "si"
lista_productos = []

while ingreso == "si":
    entrada = input(" Ingrese un producto o la palabra'fin' para finalizar el programa:")
    if entrada !="fin":
        lista_productos.append(entrada)
    else:
        print ("Fin del ingreso de productos",len(lista_productos))
        print("---LISTA DE PRODUCTOS---")
        for producto in lista_productos:
            print(lista_productos)

        ingreso = "no"
    