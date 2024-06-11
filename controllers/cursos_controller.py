from config.db import connect_db

class cursos:
    def get_cursos():
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM CURSOS"
        cursor.execute(sql)
        colunas = [desc[0] for desc in cursor.description]
    
        # Convertendo o resultado em um dicionário
        cursos = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        return cursos
    
    def get_curso_by_id(id):    
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM CURSOS WHERE co_curso = ?"
        cursor.execute(sql, [id])
        cursos = [desc[0] for desc in cursor.description]
    
        # Convertendo o resultado em um dicionário
        curso = [dict(zip(cursos, row)) for row in cursor.fetchall()]

        return curso

    def create_curso(nome, descricao, duracao, grauId, campusId, turnoId):
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO CURSOS(no_curso, ds_curso, nu_duracao, co_grau, co_campus, co_turno) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, [nome, descricao, duracao, grauId, campusId, turnoId])
        db.commit()
        return "Novo curso adicionado com sucesso"
    
    
    def update_curso(id, nome, descricao, duracao, grauId, campusId, turnoId):
        db = connect_db()
        cursor = db.cursor()
        sql = "UPDATE CURSOS SET no_curso = ?, ds_curso = ?, nu_duracao = ?, co_grau = ?, co_campus = ?, co_turno = ? WHERE co_curso = ?"
        cursor.execute(sql, [nome, descricao, duracao, grauId, campusId, turnoId, id])
        db.commit()
        return "O curso " + nome + " foi atualizado com sucesso"

    def delete_curso(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "DELETE FROM CURSOS WHERE co_curso = ?"
        cursor.execute(sql, [id])
        db.commit()
        return "Curso de id: " + id + " deletado com sucesso"