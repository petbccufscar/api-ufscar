ofertas = [
        """CREATE TABLE IF NOT EXISTS OFERTAS(
            nu_ano INTEGER NOT NULL,
            co_curso INTEGER NOT NULL,
            nu_peso_cn INTEGER NOT NULL,
            nu_peso_ch INTEGER NOT NULL,
            nu_peso_l INTEGER NOT NULL,
            nu_peso_m INTEGER NOT NULL,
            nu_peso_r INTEGER NOT NULL,
            nu_nmin_cn INTEGER NOT NULL,
            nu_nmin_ch INTEGER NOT NULL,
            nu_nmin_l INTEGER NOT NULL,
            nu_nmin_m INTEGER NOT NULL,
            nu_nmin_r INTEGER NOT NULL,
            qt_vagas_totais INTEGER NOT NULL,
            
            FOREIGN KEY (co_curso) REFERENCES CURSOS(co_curso),
            PRIMARY KEY (nu_ano, co_curso)
        )"""
]