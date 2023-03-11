class QualidadeAr:
    def __init__(self, nome, situacao_rede, tipo_rede, data, qualidade):
        self.nome = nome
        self.situacao_rede = situacao_rede
        self.tipo_rede = tipo_rede
        self.data = data
        self.qualidade = qualidade

def listar_todos():
    qualidade_santo_andre = QualidadeAr(nome="Santo André",
                                        situacao_rede="A",
                                        tipo_rede="A",
                                        data="2023-03-11 10:00:00.000",
                                        qualidade="N1 - BOA")
    qualidade_capao = QualidadeAr(nome="Capão Redondo",
                                  situacao_rede="A",
                                  tipo_rede="A",
                                  data="2023-03-11 10:00:00.000",
                                  qualidade="N1 - BOA")
    qualidade_carapicuiba = QualidadeAr(nome="Carapicuíba",
                                        situacao_rede="A",
                                        tipo_rede="A",
                                        data="2023-03-11 10:00:00.000",
                                        qualidade="N1 - BOA")
    qualidade_ibirapuera = QualidadeAr(nome="Ibirapuera",
                                       situacao_rede="A",
                                       tipo_rede="A",
                                       data="2023-03-11 12:00:00.000",
                                       qualidade="Não coletado")
    qualidade_ibirapuera2 = QualidadeAr(nome="Ibirapuera",
                                       situacao_rede="A",
                                       tipo_rede="A",
                                       data="2023-03-11 12:00:00.000",
                                       qualidade="Não coletado")

    lista_qualidade_ar = []
    lista_qualidade_ar.append(qualidade_santo_andre)
    lista_qualidade_ar.append(qualidade_capao)
    lista_qualidade_ar.append(qualidade_carapicuiba)
    lista_qualidade_ar.append(qualidade_ibirapuera)
    lista_qualidade_ar.append(qualidade_ibirapuera2)
    return lista_qualidade_ar
