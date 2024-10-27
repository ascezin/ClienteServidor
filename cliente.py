import requests
from requests.auth import HTTPBasicAuth

def obtener_usuarios():
    response = requests.get('http://localhost:5000/usuarios', auth=HTTPBasicAuth('usuario2', 'contraseña2'))  
    if response.status_code == 200:
        usuarios = response.json()
        print("Usuarios encontrados:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}")
    else:
        print("Error al obtener usuarios")

def crear_usuario(nombre):
    response = requests.post('http://localhost:5000/usuarios', json={"nombre": nombre}, auth=HTTPBasicAuth('usuario1', 'contraseña1'))
    
    if response.status_code == 200:
        print("Usuario agregado correctamente:", response.json())
    else:
        print("Error al crear el usuario:", response.status_code)
        try:
            print("Respuesta JSON:", response.json())
        except requests.exceptions.JSONDecodeError:
            print("Contenido de la respuesta no JSON:", response.text)

def buscar_usuario(idBuscar):
    encotro_usuario = False
    response = requests.get('http://localhost:5000/usuarios', auth=HTTPBasicAuth('usuario2', 'contraseña2'))  
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            if usuario['id'] == idBuscar:
                print("Usuario encontrado acorde al id:", idBuscar)
                print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}")
                encotro_usuario = True
                break
        if not encotro_usuario:
            print("No se encontró el usuario a buscar")
    else:
        print("Error al obtener la lista de usuarios.")



if __name__ == '__main__':
    obtener_usuarios()
    crear_usuario("David Jesus")  # Agrega un nuevo usuario
    obtener_usuarios()  # Verifica que el usuario fue agregado
    buscar_usuario(2)
    # Usa un ID válido aquí después de agregar
