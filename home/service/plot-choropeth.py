import pandas as pd
import json
import numpy as np
from urllib.request import urlopen
import plotly.express as px

def plot_map():
    covid_cities = pd.read_csv('../../20230405_dados_covid_municipios_sp_short.csv', sep=',')
    covid_cities.head()
    with urlopen('https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-35-mun.json') as response:
        geo_json_sp = json.load(response)
    geo_json_sp

    # cidades = ["Guarulhos", "Diadema", "São Paulo","São Bernardo do Campo", "Carapicuíba", "Taboão da Serra"]
    #
    # # Filtrando as features pelo nome das cidades
    # filtered_features = []
    # for feature in geo_json_sp["features"]:
    #     if feature["properties"]["name"] in cidades:
    #         filtered_features.append(feature)
    #
    # filtered_data = {
    #     "type": "FeatureCollection",
    #     "features": filtered_features
    # }
    # geo_json_sp = json.dumps(filtered_data)

    covid_cities['log_casos'] = np.log(covid_cities['casos'] + 1)
    covid_cities['log_casos_100k'] = np.log(covid_cities['casos_100k'] + 1)

    fig = get_fig(covid_cities, geo_json_sp)
    fig.update_geos(fitbounds="locations", visible=False)
    # plotly.offline.plot(fig, filename="sp_map_covid_cases.html")
    fig.write_html("../templates/pages/sp.html")
    print("Gerado com sucesso!")

def get_fig(covid_cities, geo_json_sp):
    fig = px.choropleth_mapbox(covid_cities,
                               geojson=geo_json_sp,
                               locations="id",
                               featureidkey="properties.id",
                               color="log_casos",
                               # animation_frame="data",
                               hover_name="cidade",
                               hover_data=["casos"],
                               title="Casos de COVID-19 em São Paulo",
                               color_continuous_scale="Viridis",
                               mapbox_style="carto-positron",  # defining a new map style
                               center={"lat": -23.5489, "lon": -46.6388},
                               zoom=7,
                               opacity=0.9, )
    return fig


if __name__ == '__main__':
    plot_map()
