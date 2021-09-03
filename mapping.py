import folium
import pandas
data=pandas.read_csv("v.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fg=folium.FeatureGroup(name="My map")
for lt,lg,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,lg],popup=folium.Popup(str(el),parse_html=True),icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map.html")
