import requests
from cachetools import cached, LRUCache, TTLCache
import json
from datetime import datetime
class QualidadeAr:
    def __init__(self, nome, situacao_rede, tipo_rede, data, qualidade):
        self.nome = nome
        self.situacao_rede = situacao_rede
        self.tipo_rede = tipo_rede
        self.data = data
        self.qualidade = qualidade
class Detalhes:
    def __init__(self, indice, data):
        self.indice = indice
        self.data = data

def listar_todos():
    lista_qualidade_ar2 = _get_cetesb()
    return lista_qualidade_ar2

def listar_detalhes():
    return _listar_detalhes()

@cached(cache=TTLCache(maxsize=1024, ttl=3600))
def _get_cetesb():
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

def _listar_detalhes():
    json_data = '{"M1": 2, "TM1": 1678550400000, "M2": 2, "TM2": 1678546800000, "M3": 2, "TM3": 1678543200000, "M4": 2, "TM4": 1678539600000, "M5": 2, "TM5": 1678536000000}'

    data = json.loads(json_data)
    keys = list(data.keys())
    lista_detalhes = []
    for i in range(0, len(keys), 2):
        valueIndice = data[keys[i]]
        valueData = datetime.fromtimestamp(data[keys[i+1]]/1000).strftime("%Y-%m-%d %Hh")
        lista_detalhes.append(Detalhes(indice=valueIndice,data=valueData))
    nome_detalhes = "São bernardo do Campo"
    return lista_detalhes, nome_detalhes

if __name__ == '__main__':

    lista_detalhes, nome = _listar_detalhes()
    print(lista_detalhes[0].data)
    print(nome)
