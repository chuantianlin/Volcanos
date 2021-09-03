import folium
import pandas

data=pandas.read_csv("v.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation<3000:
        return "orange"
    else:
        return "red"

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fgv=folium.FeatureGroup(name="My map")
for lt,lg,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,lg],radius=6,popup=folium.Popup(str(el),parse_html=True),
    color=color_producer(el),fill=True,fill_opacity=0.7))
fgp=folium.FeatureGroup(name="My population")
fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig')).read(),style_function=lambda x: {'fillColor': 'yello'if x['properties']['POP2005']<10000000 else "Blue"
if 10000000<=x ['properties']['POP2005']<100000000 else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")
