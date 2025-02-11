# Criação e Salvamento de Arquivos Shapefile com GeoPandas

Este projeto demonstra como criar elementos geoespaciais básicos (ponto, linha e polígono) utilizando a biblioteca GeoPandas, 
definir seu sistema de coordenadas e salvar esses elementos em arquivos Shapefile

## Pré-requisitos
Antes de executar o código, certifique-se de que o Python está instalado no seu sistema, juntamente com as bibliotecas GeoPandas e Shapely. 
Caso precise instalá-las, utilize o seguinte comando:
pip install geopandas shapely
Além disso, é necessário ter o software GDAL instalado no sistema para que o GeoPandas possa exportar os arquivos Shapefile corretamente.

## Funcionalidades do Código
Este script realiza as seguintes operações:
1. Criação de um Ponto:
  - Um ponto é criado utilizando a classe Point da biblioteca Shapely e armazenado em uma GeoSeries do GeoPandas. Ele é exportado como um arquivo Shapefile chamado ponto.shp.
2. Criação de uma Linha:
  - Uma linha é criada utilizando a classe LineString da biblioteca Shapely e armazenada em uma GeoSeries. A linha é exportada para um arquivo Shapefile chamado linha.shp.
3. Criação de um Polígono:
  - Um polígono é criado utilizando a classe Polygon da biblioteca Shapely e armazenado em uma GeoSeries. Ele é exportado como um arquivo Shapefile chamado poligono.shp.
4. Definição do Sistema de Coordenadas:
  - Para cada elemento criado, o sistema de coordenadas EPSG:4326 (WGS 84, amplamente utilizado em aplicações GIS) é definido.
## Estrutura do Código
O código segue a seguinte estrutura:

import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon

## Criação de um ponto
point = gpd.GeoSeries([Point(0, 0)])
point.crs = "EPSG:4326"  # Define o sistema de coordenadas
point.to_file("ponto.shp")  # Salva o ponto em um arquivo Shapefile

## Criação de uma linha
line = gpd.GeoSeries([LineString([(0, 0), (1, 1)])])
line.crs = "EPSG:4326"  # Define o sistema de coordenadas
line.to_file("linha.shp")  # Salva a linha em um arquivo Shapefile

## Criação de um polígono
polygon = gpd.GeoSeries([Polygon([(0, 0), (1, 1), (1, 0)])])
polygon.crs = "EPSG:4326"  # Define o sistema de coordenadas
polygon.to_file("poligono.shp")  # Salva o polígono em um arquivo Shapefile

## Saída do Script
Após a execução, o script gera três arquivos Shapefile na pasta de trabalho atual:
  1. ponto.shp contendo o ponto (0, 0).
  2. linha.shp contendo a linha formada pelos pontos (0, 0) e (1, 1).
  3. poligono.shp contendo o polígono formado pelos vértices (0, 0), (1, 1) e (1, 0).
Cada arquivo estará no sistema de coordenadas EPSG:4326.

## Observações
  - Certifique-se de que você tem permissão para gravar arquivos na pasta onde o script está sendo executado.
  - Para editar ou visualizar os arquivos Shapefile gerados, você pode usar softwares GIS como QGIS, ArcGIS ou ferramentas de leitura de shapefiles em Python, como o próprio GeoPandas.

