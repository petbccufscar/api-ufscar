from flask import Flask, Blueprint
from config.db import generate_tables
from router.curso_router import curso_bp
from router.turno_router import turno_bp
from router.grau_router import grau_bp
from router.campus_router import campus_bp

app = Flask(__name__)

app.register_blueprint(curso_bp)
app.register_blueprint(turno_bp)
app.register_blueprint(grau_bp)
app.register_blueprint(campus_bp)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    generate_tables()
    app.run(debug=True)