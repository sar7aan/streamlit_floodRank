import streamlit as st
import leafmap.foliumap as leafmap
import ee
import geemap


def app():

    st.title("Flood Risk Rank")

    filepath = "https://drive.google.com/uc?export=download&id=1D4doN-_MaDYk6zXc5JJPxqFetLsQDVsw"
    gm = leafmap.Map(center=[24.5, 70.0], zoom=8)#, tiles="Stamen Terrain")
    gm.add_heatmap(
        filepath,
        latitude="Latitude",
        longitude="Longitude",
        value="Rank",
        name="Heat map",
        radius=20,
    )
    gm.to_streamlit(height=500)