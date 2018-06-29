import os
import folium
import pandas as pd

# Adjust the path of the file
path = "\\Users\\pc\\Desktop\\projects\\Python-Projects\\Webmap"
os.chdir(path)
# a function made to add colors to the circles representing the heights of volcanoes

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
# Reading of the data , so we can process these certain data.
data = pd.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data['LON'])
elev = list(data['ELEV'])

#Add Base Map
map1 = folium.Map(location=[38.58,-99.09], zoom_start=6 , tiles = "Mapbox Bright")

#Add the feature group of two additional  maps
fgv = folium.FeatureGroup("Volcavoes")
fgp = folium.FeatureGroup("Population")

#Drawing of the circles , here we process the function color_producer so we classify the heights of the volcanoes
for lt , ln , el in zip(lat , lon , elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln] ,radius = 6 ,popup = str(el) + 'm' , fill_color = color_producer(el), fill = True ,color = 'grey', fill_opacity = 0.7)) 


#Design of  the population layer
    
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# Add the other layers to the base map as children
map1.add_child(fgp)
map1.add_child(fgv)

map1.add_child(folium.LayerControl())
map1.save('Map1.html')



