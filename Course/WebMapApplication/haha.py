import folium
from folium.map import Popup

# map = folium.Map(location=[-37.60124346129654, 143.82094414151317])
# map.save("MyHouse.html")

# for coordinates in [[-36.894135, 147.138140], [-36.913904, 147.132841], [-36.898469, 147.130751], [-36.900562, 147.127135], [-36.957449, 147.126593]]:
#     featherFeatureGroup.add_child(folium.Marker(location=coordinates, popup="x"))
# featherFeatureGroup.add_child(folium.Marker(location=[-36.894135, 147.138140], popup="Mt. Feathertop 1922m"))
# featherFeatureGroup.add_child(folium.Marker(location=[-36.913904, 147.132841], popup="High Knob 1802m"))
# featherFeatureGroup.add_child(folium.Marker(location=[-36.898469, 147.130751], popup="Start of climb to Summit"))
# featherFeatureGroup.add_child(folium.Marker(location=[-36.900562, 147.127135], popup="T-Junction of Mt. Feathertop Summit, Federation Hut and Razorback Track"))

# featherFeatureGroup.add_child(folium.Marker(location=[-36.957449, 147.126593], popup="Big Dipper"))

def elevColor (elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'


import pandas

dataframe = pandas.read_csv("Volcanoes.txt")
volcfgroup = folium.FeatureGroup(name="Volcanos")
map = folium.Map(location=[38.58, -99.09])

volcanoLAT = list(dataframe["LAT"])
volcanoLON = list(dataframe["LON"])
vocanoElev = list(dataframe["ELEV"])

for lt, ln, elev in zip(volcanoLAT, volcanoLON, vocanoElev):
    volcfgroup.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, fill_color=elevColor(elev), color = 'grey', fill_opacity = 0.7, stroke=False, popup=elev, icon=folium.Icon(color=elevColor(elev))))

# dfGeoJson = pandas.read_json('world.json', lines=True, encoding='utf-8-sig')
# print(dfGeoJson)
map.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(volcfgroup)

featherFeatureGroup = folium.FeatureGroup(name="Victorian High Country")
feathertopDframe = pandas.read_csv("Feathertop.txt")

feathertopLAT = list(feathertopDframe["LAT"])
feathertopLON = list(feathertopDframe["LON"])
feathertopTitles = list(feathertopDframe["TITLE"])
feathertopElev = list(feathertopDframe["ELEV"])

for lt, ln, title, elev in zip(feathertopLAT, feathertopLON, feathertopTitles, feathertopElev):
    featherFeatureGroup.add_child(folium.Marker(location=[lt, ln], popup=title + ' ' + str(elev) + 'm'))


map.add_child(featherFeatureGroup)
map.add_child(folium.LayerControl())




map.save("MyHouse.html")

feathertop = folium.Map(location=[-36.936180, 147.126490], zoom_start=14)

