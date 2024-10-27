from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Base de datos simulada
base_datos = {
    "usuarios": [
        {"id": 1, "nombre": "Juan"},
        {"id": 2, "nombre": "María"}
    ]
}

# Diccionario de usuarios (puedes cambiar las credenciales)
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

@auth.verify_password
def verificar_usuario(username, password):
    if username in usuarios and usuarios[username] == password:
        return username
    return None

# Ruta para obtener los usuarios
@app.route('/usuarios', methods=['GET'])
@auth.login_required
def obtener_usuarios():
    return jsonify(base_datos["usuarios"])

# Ruta para crear el nuevo usuario
@app.route('/usuarios', methods=['POST'])
@auth.login_required
def crear_usuario():
    datos = request.get_json()
    if "nombre" not in datos or not datos["nombre"] or len(datos["nombre"]) < 2:
        return jsonify({"error": "El campo 'nombre' debe contener al menos un carácter."}), 400
    
    nuevo_usuario = {
        "id": len(base_datos["usuarios"]) + 1,
        "nombre": datos["nombre"]
    }
    
    base_datos["usuarios"].append(nuevo_usuario)
    return jsonify(nuevo_usuario), 200
