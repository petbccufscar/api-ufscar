cursos = [
        """CREATE TABLE IF NOT EXISTS CURSOS(
            co_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            no_curso TEXT NOT NULL,
            ds_curso TEXT NOT NULL,
            nu_duracao INTEGER NOT NULL,
            co_turno INTEGER NOT NULL,
            co_grau INTEGER NOT NULL,
            co_campus INTEGER NOT NULL,

            FOREIGN KEY (co_turno) REFERENCES TURNOS(co_turno) ON DELETE RESTRICT,
            FOREIGN KEY (co_grau) REFERENCES GRAUS(co_grau) ON DELETE RESTRICT,
            FOREIGN KEY (co_campus) REFERENCES CAMPI(co_campus) ON DELETE RESTRICT
        )"""
]