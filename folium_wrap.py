import folium
from folium import plugins
from geopy.geocoders import Nominatim

def find_and_point_location(loc,width='500', height='500',tiles='OpenStreetMap',zoom_start=16,icon_color="orange", icon="info-sign"): 
    """
    loc => string
    住所や名所名を入力。自動検索。

    Tiles
    *:“OpenStreetMap”
    *:“Stamen Terrain”
    *:“Stamen Toner”
    *:“Stamen Watercolor”
    *:“CartoDB positron”
    *:“CartoDB dark_matter”
    #:“Cloudmade” (Must pass API key)
    #:“Mapbox” (Must pass API key)

    icon (この中のものはすべて使えるらしい)
    https://glyphsearch.com/?library=glyphicons

    icon_color
    ['red','blue','green','purple','orange','darkred','lightred',
    'beige','darkblue','darkgreen','cadetblue','darkpurple',
    'white','pink','lightblue','lightgreen','gray','black',
    'lightgray']
    """
    geolocator = Nominatim(user_agent="test-agent") # user_agent はなんでもOKらしい
    location = geolocator.geocode(loc)
    latlon = [
        location.latitude,
        location.longitude
        ]
    f = folium.Figure(width=width, height=height)
    map = folium.Map(
        location=[
            location.latitude, 
            location.longitude
            ],
            zoom_start=zoom_start,
            tiles=tiles
            ).add_to(f)
    folium.Marker(
        location=[
            location.latitude,
            location.longitude
            ],
        popup=str(loc),
        icon=folium.Icon(color=icon_color, icon=icon)
            ).add_to(map)
    return map