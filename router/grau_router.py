from flask import request, jsonify, Blueprint
from controllers.graus_controller import graus

grau_bp = Blueprint("grau", __name__)

@grau_bp.route("/graus", methods = ["GET"])
def get_graus():
    result = graus.get_graus()
    return jsonify(result)

@grau_bp.route("/grau/<id>", methods = ["GET"])
def get_grau_by_id(id):
    result = graus.get_grau_by_id(id)
    return jsonify(result)

@grau_bp.route("/grau", methods = ["POST"])
def create_grau():
    data = request.get_json()
    nome = data["no_grau"]
    result = graus.create_grau(nome)
    return jsonify(result)

@grau_bp.route("/grau/<id>", methods = ["PUT"])
def update_grau(id):
    data = request.get_json()
    nome = data["no_grau"]
    result = graus.update_grau(id, nome)
    return jsonify(result)

@grau_bp.route("/grau/<id>", methods = ["DELETE"])
def delete_grau(id):
    result = graus.delete_grau(id)
    return jsonify(result)