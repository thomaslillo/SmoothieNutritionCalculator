import streamlit

streamlit.title('Hi this is my first app')

from streamlit_folium import st_folium
import folium

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], 
    popup="Liberty Bell", 
    tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)
