import requests

class QualidadeAr:
    def __init__(self, nome, situacao_rede, tipo_rede, data, qualidade):
        self.nome = nome
        self.situacao_rede = situacao_rede
        self.tipo_rede = tipo_rede
        self.data = data
        self.qualidade = qualidade

def listar_todos():
    lista_qualidade_ar2 = _get_cetesb_()
    return lista_qualidade_ar2

def _get_cetesb_():
    url = "https://arcgis.cetesb.sp.gov.br/server/rest/services/QUALAR/CETESB_QUALAR/MapServer/6/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22:-5244191.63658331,%22ymin%22:-2739503.0937498696,%22xmax%22:-5165920.11961926,%22ymax%22:-2661231.5767858177,%22spatialReference%22:{%22wkid%22:102100}}&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100"

    response = requests.get(url)
    url = "https://arcgis.cetesb.sp.gov.br/server/rest/services/QUALAR/CETESB_QUALAR/MapServer/6/query?f=json&returnGeometry=true&spatialRel=esriSpatialRelIntersects&geometry={%22xmin%22:-5244191.63658331,%22ymin%22:-2739503.0937498696,%22xmax%22:-5165920.11961926,%22ymax%22:-2661231.5767858177,%22spatialReference%22:{%22wkid%22:102100}}&geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100"

    response = requests.get(url)
    data = response.json()
    lista_qualidade_ar = []
    for feature in data['features']:
        nome = feature['attributes']['Nome']
        data = feature['attributes']['DATA'][:16]
        situacao_rede = feature['attributes']['Situacao_Rede']
        qualidade = feature['attributes']['Qualidade'] or 'Não coletado'
        tipo_rede = feature['attributes']['Tipo_Rede']
        lista_qualidade_ar.append(QualidadeAr(nome=nome, situacao_rede=situacao_rede, tipo_rede=tipo_rede, data=data, qualidade=qualidade))


    return lista_qualidade_ar