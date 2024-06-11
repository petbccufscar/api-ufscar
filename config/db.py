import sqlite3
from config.tables.campi import campi
from config.tables.cursos import cursos
from config.tables.graus import graus
from config.tables.modalidades import modalidades
from config.tables.ofertas_modalidades import ofertas_modalidades
from config.tables.ofertas import ofertas
from config.tables.turnos import turnos

DATABASE = "ufscar.db"

def connect_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def generate_tables():
    all_tables = [graus, turnos, campi, cursos, modalidades, ofertas, ofertas_modalidades]
    db = connect_db()
    cursor = db.cursor()

    for table in all_tables:
        for row in table:
            cursor.execute(row)