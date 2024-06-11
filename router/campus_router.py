from flask import request, jsonify, Blueprint
from controllers.campi_controller import campi

campus_bp = Blueprint("campus", __name__)

@campus_bp.route("/campi", methods = ["GET"])
def get_campi():
    result = campi.get_campi()
    return jsonify(result)


@campus_bp.route("/campus/<id>", methods = ["GET"])
def get_campus_by_id(id):
    result = campi.get_campus_by_id(id)
    return jsonify(result)


@campus_bp.route("/campus", methods = ["POST"])
def create_campus():
    data = request.get_json()
    nome = data["no_campus"]
    result = campi.create_campus(nome)
    return jsonify(result)


@campus_bp.route("/campus/<id>", methods = ["PUT"])
def update_campus(id):
    data = request.get_json()
    nome = data["no_campus"]
    result = campi.update_campus(id, nome)
    return jsonify(result)


@campus_bp.route("/campus/<id>", methods = ["DELETE"])
def delete_campus(id):
    result = campi.delete_campus(id)
    return jsonify(result)