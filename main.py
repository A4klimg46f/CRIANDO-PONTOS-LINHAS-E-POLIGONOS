import geopandas as gpd

# Cria um ponto
point = gpd.GeoSeries([Point(0, 0)])
point.crs = "EPSG:4326" # Define o sistema de coordenadas
point.to_file("ponto.shp") # Salva o ponto em um arquivo shapefile

# Cria uma linha
line = gpd.GeoSeries([LineString([(0, 0), (1, 1)])])
line.crs = "EPSG:4326" # Define o sistema de coordenadas
line.to_file("linha.shp") # Salva a linha em um arquivo shapefile

# Cria um polígono
polygon = gpd.GeoSeries([Polygon([(0, 0), (1, 1), (1, 0)])])
polygon.crs = "EPSG:4326" # Define o sistema de coordenadas
polygon.to_file("poligono.shp") # Salva o polígono em um arquivo shapefile

#Nesse exemplo, estamos criando um ponto, uma linha e um polígono utilizando a classe GeoSeries do Geopandas. Para cada um desses elementos, estamos definindo o sistema de coordenadas e salvando em um arquivo shapefile com o método to_file(). Note que, para utilizar a classe Point, LineString e Polygon, é necessário importar a classe geometry da biblioteca shapely.
