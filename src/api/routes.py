"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from api.models import db, User
from flask_jwt_extended import create_access_token

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# REGISTRO

@api.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    
    # Validar que vengan los datos
    if "email" not in body or "password" not in body:
        return jsonify({"msg": "Faltan datos"}), 400
        
    # Crear nuevo usuario
    new_user = User(email=body['email'], password=body['password'], is_active=True)
    
    # Guardar en base de datos
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"msg": "Usuario creado exitosamente"}), 201


# LOGIN

@api.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    email = body.get('email', None)
    password = body.get('password', None)

    # Buscar usuario en la base de datos
    user = User.query.filter_by(email=email).first()

    # Validar si el usuario existe y la contraseña es correcta
    if user is None or user.password != password:
        return jsonify({"msg": "Email o contraseña incorrectos"}), 401

    # Crear el token
    access_token = create_access_token(identity=email)
    return jsonify({"access_token": access_token}), 200