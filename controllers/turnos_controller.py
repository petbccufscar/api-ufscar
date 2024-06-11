from config.db import connect_db

class turnos:
    def get_turnos():
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM TURNOS"
        cursor.execute(sql)
        colunas = [desc[0] for desc in cursor.description]
    
        # Convertendo o resultado em um dicionário
        turnos = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        return turnos
    
    def get_turno_by_id(id):    
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM TURNOS WHERE co_turno = ?"
        cursor.execute(sql, [id])
        colunas = [desc[0] for desc in cursor.description]
        # Convertendo o resultado em um dicionário
        turno = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        return turno

    def create_turno(nome):
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO TURNOS(no_turno) VALUES (?)"
        cursor.execute(sql, [nome])
        db.commit()
        return "Novo turno adicionado com sucesso"
    
    
    def update_turno(id, nome):
        db = connect_db()
        cursor = db.cursor()
        sql = "UPDATE TURNOS SET no_turno = ? WHERE co_turno = ?"
        cursor.execute(sql, [nome, id])
        db.commit()
        return "O turno " + nome + " foi atualizado com sucesso"

    def delete_turno(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "DELETE FROM TURNOS WHERE co_turno = ?"
        cursor.execute(sql, [id])
        db.commit()
        return "Turno de id: " + id + " deletado com sucesso"