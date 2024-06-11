from config.db import connect_db

class campi:
    def get_campi():
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM CAMPI"
        cursor.execute(sql)
        colunas = [desc[0] for desc in cursor.description]
    
        # Convertendo o resultado em um dicionário
        campi = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        return campi

    def get_campus_by_id(id):    
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM CAMPI WHERE co_campus = ?"
        cursor.execute(sql, [id])
        colunas = [desc[0] for desc in cursor.description]
    
        # Convertendo o resultado em um dicionário
        campus = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        return campus

    def create_campus(nome):
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO CAMPI(no_campus) VALUES (?)"
        cursor.execute(sql, [nome])
        db.commit()
        return "Novo campus adicionado com sucesso"

    def update_campus(id, nome):
        db = connect_db()
        cursor = db.cursor()
        sql = "UPDATE CAMPIS SET no_campus = ? WHERE co_campus = ?"
        cursor.execute(sql, [nome, id])
        db.commit()
        return "O campus " + nome + " foi atualizado com sucesso"

    def delete_campus(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "DELETE FROM CAMPI WHERE co_campus = ?"
        cursor.execute(sql, [id])
        db.commit()
        return "Campus de id: " + id + " deletado com sucesso"