from flask import Blueprint, jsonify, request
from app.controllers.user_controller import (
    listar_usuarios,
    criar_usuario,
    atualizar_usuario,
    deletar_usuario
)

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
def get_user():
    return jsonify(listar_usuarios())


@users_bp.route("/", methods=["POST"])
def post_user():
    data = request.get_json()
    response, status = criar_usuario(data)
    return jsonify(response), status


@users_bp.route("/<int:id>", methods=["PATCH"])
def patch_user(id):
    data = request.get_json()
    response, status = atualizar_usuario(id, data)
    return jsonify(response), status


@users_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    response, status = deletar_usuario(id)
    return jsonify(response), status