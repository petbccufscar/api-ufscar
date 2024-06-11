from flask import request, jsonify, Blueprint
from controllers.turnos_controller import turnos

turno_bp = Blueprint("turno", __name__)

@turno_bp.route("/turnos", methods = ["GET"])
def get_turnos():
    result = turnos.get_turnos()
    return jsonify(result)

@turno_bp.route("/turnos/<id>", methods = ["GET"])
def get_turno_by_id(id):
    result = turnos.get_turno_by_id(id)
    return jsonify(result)

@turno_bp.route("/turno", methods = ["POST"])
def create_turno():
    data = request.get_json()
    nome = data["no_turno"]
    result = turnos.create_turno(nome)
    return jsonify(result)

@turno_bp.route("/turno/<id>", methods = ["PUT"])
def update_turno(id):
    data = request.get_json()
    nome = data["no_turno"]
    result = turnos.update_turno(id, nome)
    return jsonify(result)

@turno_bp.route("/turno/<id>", methods = ["DELETE"])
def delete_turno(id):
    result = turnos.delete_turno(id)
    return jsonify(result)