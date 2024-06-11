ofertas_modalidades = [
    """CREATE TABLE IF NOT EXISTS OFERTAS_MODALIDADES(
            co_curso INTEGER,
            co_modalidade INTEGER,
            nu_ano INTEGER,
            qt_vagas INTEGER,
            nu_nota_sisu INTEGER,
            nu_nota_min INTEGER,
            nu_nota_max INTEGER,

            FOREIGN KEY (co_modalidade) REFERENCES MODALIDADES(co_modalidade),
            FOREIGN KEY (co_curso) REFERENCES OFERTAS(co_curso),
            FOREIGN KEY (nu_ano) REFERENCES OFERTAS(nu_ano),
            PRIMARY KEY (nu_ano, co_modalidade, co_curso)
        )"""
]