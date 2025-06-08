import time

user1 = None
user2 = None
user3 = None
pass1 = None
pass2 = None
pass3 = None
usuarios = 0
print("----Bienvenido!!---\n Que desea hacer?\n[1] - iniciar Sesion\n[2] - Registrar Usuario\n[3] - Salir")

while True:
    try:
        opcion = int(input("Ingrese una opcion(1-3): "))
        if opcion == 1:
            print("---Haz seleccionado Iniciar Sesion---")
            if user1 == None and user2 == None and user3 == None:
                print("No existen registros de usuarios.")
                print("Es necesario crear un usuario antes de iniciar sesion.\nVolviendo al menu principal...")
                time.sleep(1)
            else:
                while True:
                    registro_user = input("Ingrese su nombre de usuario: ")
                    if registro_user == user1:
                        pass_user = input("Ingrese la contraseña: ")
                        if pass_user == pass1 :
                            print(f"Bienvenido {registro_user}\nQue desea hacer?\n[1 - Realizar llamada]\n[2 - Enviar correo electronico]\n[3 - Cerrar sesion]")
                            try:
                                while True:
                                    ask = int(input("Elija una opcion: "))
                                    if ask == 1:
                                        while True:
                                            try:
                                                num_telefono = (input("Ingrese el numero telefonico: "))
                                                if num_telefono[0] != "9":
                                                    print("El numero debe comenzar por 9.")
                                                    continue
                                                if len(num_telefono) != 9:
                                                    print("El numero debe tener 9 digitos!!")
                                                    continue
                                                print(f"Llamando al numero '{num_telefono}'")
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("No contestaron.")
                                                time.sleep(1)
                                                print("Volviendo al menu principal...")
                                                break
                                
                                            except ValueError:                
                                                print("Entrada no valida debe ingresar un numero telefonico. (EJ: 9XXXXXXXX)")
                                    if ask == 2:
                                        while True:
                                            correo = input("Ingrese el correo electronico al cual se le enviara el mensaje: ")
                                            if "@" in correo:
                                                correo_electronico = correo
                                                mensaje = input("Ingrese el mensaje que desea enviar: ")
                                                print(f"El mensaje se enviara en [2] segundos.")
                                                print("Enviando...")
                                                time.sleep(2)
                                                print("Mensaje enviado!")
                                                print("Saliendo...")
                                                time.sleep(1.5)
                                                break
                                            else:
                                                print("Entrada invalida!! (Ingrese un correo valido (Ej: benjamin@gmail.com))")
                                                continue

                            except ValueError:
                                print("Debe ingresar un opcion valida!! (1-3)") 
                        else:
                            print("Contraseña incorrecta, Vuelva a intentarlo.")
                            continue
                    
                    elif registro_user == user2:
                        pass_user = input("Ingrese la contraseña: ")
                        if pass_user == pass2 :
                            print(f"Bienvenido {registro_user}\nQue desea hacer?\n[1 - Realizar llamada]\n[2 - Enviar correo electronico]\n[3 - Cerrar sesion]")
                            try:
                                while True:
                                    ask = int(input("Elija una opcion: "))
                                    if ask == 1:
                                        while True:
                                            try:
                                                num_telefono = (input("Ingrese el numero telefonico: "))
                                                if num_telefono[0] != "9":
                                                    print("El numero debe comenzar por 9.")
                                                    continue
                                                if len(num_telefono) != 9:
                                                    print("El numero debe tener 9 digitos!!")
                                                    continue
                                                print(f"Llamando al numero '{num_telefono}'")
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("No contestaron.")
                                                time.sleep(1)
                                                print("Volviendo al menu principal...")
                                                break
                                
                                            except ValueError:                
                                                print("Entrada no valida debe ingresar un numero telefonico. (EJ: 9XXXXXXXX)")
                                    if ask == 2:
                                        while True:
                                            correo = input("Ingrese el correo electronico al cual se le enviara el mensaje: ")
                                            if "@" in correo:
                                                correo_electronico = correo
                                                mensaje = input("Ingrese el mensaje que desea enviar: ")
                                                print(f"El mensaje se enviara en [2] segundos.")
                                                print("Enviando...")
                                                time.sleep(2)
                                                print("Mensaje enviado!")
                                                print("Saliendo...")
                                                time.sleep(1.5)
                                                break
                                            else:
                                                print("Entrada invalida!! (Ingrese un correo valido (Ej: benjamin@gmail.com))")
                                                continue

                            except ValueError:
                                print("Debe ingresar un opcion valida!! (1-3)") 
                        else:
                            print("Contraseña incorrecta, Vuelva a intentarlo.")
                            continue
            
                    
                    elif registro_user == user3:
                        pass_user = input("Ingrese la contraseña: ")
                        if pass_user == pass3 :
                            print(f"Bienvenido {registro_user}\nQue desea hacer?\n[1 - Realizar llamada]\n[2 - Enviar correo electronico]\n[3 - Cerrar sesion]")
                            try:
                                while True:
                                    ask = int(input("Elija una opcion: "))
                                    if ask == 1:
                                        while True:
                                            try:
                                                num_telefono = (input("Ingrese el numero telefonico: "))
                                                if num_telefono[0] != "9":
                                                    print("El numero debe comenzar por 9.")
                                                    continue
                                                if len(num_telefono) != 9:
                                                    print("El numero debe tener 9 digitos!!")
                                                    continue
                                                print(f"Llamando al numero '{num_telefono}'")
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("Ring~~~")
                                                time.sleep(0.5)
                                                print("No contestaron.")
                                                time.sleep(1)
                                                print("Volviendo al menu principal...")
                                                break
                                
                                            except ValueError:                
                                                print("Entrada no valida debe ingresar un numero telefonico. (EJ: 9XXXXXXXX)")
                                    if ask == 2:
                                        while True:
                                            correo = input("Ingrese el correo electronico al cual se le enviara el mensaje: ")
                                            if "@" in correo:
                                                correo_electronico = correo
                                                mensaje = input("Ingrese el mensaje que desea enviar: ")
                                                print(f"El mensaje se enviara en [2] segundos.")
                                                print("Enviando...")
                                                time.sleep(2)
                                                print("Mensaje enviado!")
                                                print("Saliendo...")
                                                time.sleep(1.5)
                                                break
                                            else:
                                                print("Entrada invalida!! (Ingrese un correo valido (Ej: benjamin@gmail.com))")
                                                continue

                            except ValueError:
                                print("Debe ingresar un opcion valida!! (1-3)") 
                        else:
                            print("Contraseña incorrecta, Vuelva a intentarlo.")
                            continue
                    else:
                        print(f"El usuario '{registro_user}' no se encuentra registrado.")
                        salir = int(input("¿Desea volver al menu principal, o volver a ingresar el nombre de usuario?([1 - salir] [2 - volver a intentar]):  "))
                        if salir == 1:
                            break
                        else:
                            continue

                        

        if opcion == 2:
            print("---Haz seleccionado Registrar Usuario---")
            if usuarios >= 3:
                print("Usuarios maximos alcanzado!.\nVolviendo al menu principal...")
                time.sleep(1.5)
                continue
         
            while True:
                if user1 != None:
                    ask = int(input("Desea Ingresar otro usuario?([1 - Si]-[2 - Volver al menu]): "))
                    if ask == 1:
                        usuario2 = input("Ingrese su nombre de usuario: ")

                        if len(usuario2) > 16:
                            print("El nombre de usuario no puede tener mas de 16 caracteres.")
                            continue                
                        if " " in usuario2:
                            print("El nombre de usuario no puede tener espacios.")
                            continue
                        if usuario2 == user1 or usuario2 == user2 or usuario2 == user3:
                            print("Ese nombre de usuario esta en uso")
                            continue

                        usuario2_pass = input("Ingrese su contraseña: ")
                        if len(usuario2_pass) > 16:
                            print("La contraseña no puede tener mas de 16 caracteres.") 
                            continue
                        if " " in usuario2_pass:
                            print("La contraseña no puede tener espacios.")
                            continue

                        user2 = usuario2
                        pass2 = usuario2_pass
                        usuarios += 1
                        print(f"Usuario {user2} ha sido creado.\nVolviendo al menu principal...")
                        time.sleep(1.25)

                        break
                    
                    if ask == 2:
                        print("Saliendo...")
                        time.sleep(1.25)
                        break

                if user1 != None and user2 != None:
                    ask = int(input("Desea Ingresar 2otro usuario?([1 - Si]-[2 - Volver al menu]): "))
                    if ask == 1:
                        usuario3 = input("Ingrese su nombre de usuario: ")

                        if len(usuario3) > 16:
                            print("El nombre de usuario no puede tener mas de 16 caracteres.")
                            continue                
                        if " " in usuario3:
                            print("El nombre de usuario no puede tener espacios.")
                            continue
                        if usuario3 == user1 or usuario3 == user2 or usuario3 == user3:
                            print("Ese nombre de usuario esta en uso")
                            continue

                        usuario3_pass = input("Ingrese su contraseña: ")
                        if len(usuario3_pass) > 16:
                            print("La contraseña no puede tener mas de 16 caracteres.") 
                            continue
                        if " " in usuario3_pass:
                            print("La contraseña no puede tener espacios.")
                            continue

                        user3 = usuario3
                        pass3 = usuario3_pass
                        usuarios += 1
                        print(f"Usuario {user3} ha sido creado.\nVolviendo al menu principal...")
                        time.sleep(1.25)
                        break
                    
                    if ask == 2:
                        print("Saliendo...")
                        time.sleep(1.25)
                        break
                nuevo_usuario = input("Ingrese su nombre de usuario: ")
                nueva_pass = input("Ingrese su contraseña: ")
                
                if len(nuevo_usuario) > 16:
                    print("El nombre de usuario no puede tener mas de 16 caracteres.")
                    continue                
                if len(nueva_pass) > 16:
                    print("La contraseña no puede tener mas de 16 caracteres.") 
                    continue
                if " " in nuevo_usuario:
                    print("El nombre de usuario no puede tener espacios.")
                    continue
                if " " in nueva_pass:
                    print("La contraseña no puede tener espacios.")
                    continue
                if nuevo_usuario == user1 or nuevo_usuario == user2 or nuevo_usuario == user3:
                    print("Ese nombre de usuario esta en uso")
                    continue
                usuarios += 1
                user1 = nuevo_usuario
                pass1 = nueva_pass
                break

    except ValueError:
        print("Error! Debe ingresar un numero dentro del rango (1-3).")

