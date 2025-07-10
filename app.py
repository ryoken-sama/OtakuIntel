import streamlit as st
from datetime import datetime

from data_fetcher import fetch_seasonal_anime, preprocess_data
from filters import sidebar_filters
from anime_cards import display_anime_cards, display_poster_gallery
from charts import show_genre_chart, show_airing_chart
from utils import apply_filters

st.set_page_config(page_title="OtakuIntel", layout="wide")
st.title("OtakuIntel")
st.markdown(f"**Seasonal Anime Dashboard** — {datetime.now().strftime('%B %Y')}")

st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
        }
        h4 {
            font-size: 1.1rem;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)


anime_data = fetch_seasonal_anime()
if not anime_data:
    st.error("Could not fetch data.")
    st.stop()

df = preprocess_data(anime_data)
filters = sidebar_filters(df)
filtered_df = apply_filters(df, filters)

st.markdown(f"### Showing {len(filtered_df)} anime")
st.divider()

display_anime_cards(filtered_df)

if st.checkbox("Show Poster Gallery"):
    display_poster_gallery(filtered_df)

if st.checkbox("Show Genre Chart", value=True):
    show_genre_chart(df)

if st.checkbox("Show Airing Day Chart", value=True):
    show_airing_chart(df)

st.download_button("📥 Download CSV", filtered_df.to_csv(index=False), file_name="otakuintel_seasonal.csv")
