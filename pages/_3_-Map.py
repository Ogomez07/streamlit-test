import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

data = pd.read_csv("data/pisos.csv")
centro = [data["lat"].mean(), data["lon"].mean()] #asumimos plano cartesiano
lat = 40.402924
lon = -3.69730
#1 mapa
m = folium.Map(location=(lat,lon), zoom_start=15)

#pin
# 2 icono
icon = folium.Icon(icon="home", prefix="fa", color="blue")

#3 el pin
def create_marker (row):
    dict_color = {

    "Norte":"blue",
    "Centro":"black",
    "Este":"red",
    "Sur": "purple",
    "Oeste":"white"
    }
    icon = folium.Icon(icon="umbrella-beach", prefix="fa", color=dict_color[row["barrio"]])
    marker = folium.Marker(location=(row["lat"],row["lon"]),
                        icon=icon)
    #4 añado el pin en particular
    marker.add_to(m)

for _, row in data.iterrows():
    create_marker(row)

st_folium(m, width=800, height=600)