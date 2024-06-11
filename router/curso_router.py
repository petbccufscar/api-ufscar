from flask import request, jsonify, Blueprint
from controllers.cursos_controller import cursos

curso_bp = Blueprint("curso", __name__)

@curso_bp.route("/cursos", methods = ["GET"])
def get_cursos():
    result = cursos.get_cursos()
    return jsonify(result)


@curso_bp.route("/cursos/<id>", methods = ["GET"])
def get_curso_by_id(id):
    result = cursos.get_curso_by_id(id)
    return jsonify(result)

@curso_bp.route("/curso", methods = ["POST"])
def create_curso():
    data = request.get_json()
    nome = data["no_curso"]
    descricao = data["ds_curso"]
    duracao = data["nu_duracao"]
    grauId = data["co_grau"]
    campusId = data["co_campus"]
    turnoId = data["co_turno"]
    result = cursos.create_curso(nome, descricao, duracao, grauId, campusId, turnoId)
    return jsonify(result)

@curso_bp.route("/curso/<id>", methods = ["PUT"])
def update_curso(id):
    data = request.get_json()
    nome = data["no_curso"]
    descricao = data["ds_curso"]
    duracao = data["nu_duracao"]
    grauId = data["co_grau"]
    campusId = data["co_campus"]
    turnoId = data["co_turno"]
    result = cursos.update_curso(id, nome, descricao, duracao, grauId, campusId, turnoId)
    return jsonify(result)

@curso_bp.route("/curso/<id>", methods = ["DELETE"])
def delete_curso(id):
    result = cursos.delete_curso(id)
    return jsonify(result)