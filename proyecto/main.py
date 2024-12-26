from usuarios import acciones

"""
PROYECTO PYTHON-MYSQL
 - Abrir un asistente para
 - Login o registro
 - Si elegimos registro, creara un usuario en bd
 - Si elegimos login, idenficara al usuario y preguntara
 - crear nota, mostrar notas, borrarlas

"""

print("""
Acciones disponibles:
    - Registro 
    - Login
""")

hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == 'Registro':
    hazEl.registro()

elif accion == 'Login':
    hazEl.login()


