usurio_correcto = "admin"
contraseña_correcta = "1234"

intentos = 0

while intentos < 3:
    usuario = input("ingrese el usuario:")
    contraseña = input("ingrese la contraseña:")

    if usuario== usuario_correcto and  contraseña == contraseña_correcta:
        print("inicio de sesion correcto")
        break
    else:
        print("usuario o contraseña incorrecta")
        intentos += 1
    
    if intentos == 3:
        print("usuario bloqueado")