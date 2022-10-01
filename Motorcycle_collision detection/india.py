import streamlit as st 
import pandas as pd 
import numpy as np 
import pydeck as pdk

DATA_URL = (
    "in.csv"
)

data = pd.read_csv(DATA_URL)
st.map(data)



midpoint = (np.average(data["latitude"]), np.average(data["longitude"]))
st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/dark-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 30,
    },
    layers=[
        pdk.Layer(
        "HexagonLayer",
        data=data[['latitude', 'longitude']],
        get_position=["longitude", "latitude"],
        auto_highlight=True,
        radius=100,
        extruded=True,
        pickable=True,
        elevation_scale=4,
        elevation_range=[0, 1000],
        ),
    ],
))
