import usuarios.usuario as modelo
import notas.acciones  

class Acciones:

    def registro(self):
        print("\nOK!! Vamos a registrar en el sistema ...")
        
        nombre = input("Cual es tu nombre? :")
        apellido = input("Cual son tus apellido?: ")
        email = input("Cual es tu correo electronico?: ")
        password = input("Cual es tu contraseña?: ")
    
        usuario = modelo.Usuario(nombre, apellido, email, password)
        registro = usuario.registrar()    

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente.")    

    def login(self):
        print("\nOk!! Identificate en el sistema..")
        
        try:
            email = input("Cual es tu correo electronico?: ")
            password = input("Cual es tu contraseña?: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto intenta mas tarde")
        

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            - Crear una nota (crear)
            - Mostrar nota (mostrar)
            - Eliminar notas (eliminar)
            - Salir (salir)
        """)

        hazEl = notas.acciones.Acciones()

        accion = input("Que deseas hacer?: ")

        if accion == 'crear':
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'mostrar':
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'eliminar':
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'salir':
            print(f"\nok!! {usuario[1]} hasta pronto")
            exit() # salir de la aplicacion

    