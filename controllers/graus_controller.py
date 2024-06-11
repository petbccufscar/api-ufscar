from config.db import connect_db

class graus:
    def get_graus():
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM GRAUS"
        cursor.execute(sql)
        colunas = [desc[0] for desc in cursor.description]
    
        # Convertendo o resultado em um dicionário
        graus = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        return graus
    
    def get_grau_by_id(id):    
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM GRAUS WHERE co_grau = ?"
        cursor.execute(sql, [id])
        colunas = [desc[0] for desc in cursor.description]
    
        # Convertendo o resultado em um dicionário
        grau = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        return grau
    
    def create_grau(nome):
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO GRAUS(no_grau) VALUES (?)"
        cursor.execute(sql, [nome])
        db.commit()
        return "Novo grau adicionado com sucesso"
    
    def update_grau(id, nome):
        db = connect_db()
        cursor = db.cursor()
        sql = "UPDATE GRAUS SET no_grau = ? WHERE co_grau = ?"
        cursor.execute(sql, [nome, id])
        db.commit()
        return "O grau " + nome + " foi atualizado com sucesso"

    def delete_grau(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "DELETE FROM GRAUS WHERE co_grau = ?"
        cursor.execute(sql, [id])
        db.commit()
        return "Grau de id: " + id + " deletado com sucesso"
    