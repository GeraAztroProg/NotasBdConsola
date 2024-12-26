#Conexion a la base de datos
import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #Consulta
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        #Guardar datos
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)

        #Correccion de un error al tener el correo duplicado
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self] #objeto
        except:
            result = [0, self]    

        return result 

    def identificar(self):    
        
        #consulta 
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # datos de consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result

