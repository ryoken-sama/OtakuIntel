import pandas as pd
import streamlit as st

@st.cache_data
def load_anime_data():
    df = pd.read_csv("archive/anime_filtered.csv", encoding="utf-8-sig")

    # Basic cleaning
    df = df[df['title'].notna()]
    df = df[df['score'].notna()]
    df.rename(columns={'genre': 'genres'}, inplace=True)
    df['genres'] = df['genres'].fillna('Unknown')
    df['genres'] = df['genres'].apply(lambda x: x.replace(", ", ",").split(",") if isinstance(x, str) else [])


    # Year from aired string
    df['aired_from_year'] = pd.to_numeric(df['aired_from_year'], errors='coerce')

    return df
