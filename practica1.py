pin_correcto = 4321
intentos_max = 3
intentos = 0

while intentos < intentos_max:
    entrada = int(input("ingrese su pin: "))
    if entrada ==pin_correcto:
        print("Acceso concedido")
        break
     else
        print("pin incorrecto")
        intentos += 1
 if intentos == intentos_max:
    print(" tarjeta bloqueada")       
