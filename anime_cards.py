import streamlit as st

def display_anime_cards(df):
    st.markdown("### Top Anime This Season")

    for _, row in df.iterrows():
        st.markdown(f"""
        <div style="display: flex; gap: 1.2rem; margin-bottom: 2rem; background-color: #f9f9f9; color: #000000; padding: 1rem; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <img src="{row['image_url']}" width="110" height="160" style="border-radius: 8px; object-fit: cover;" />
            <div style="flex: 1">
                <h4 style="margin-bottom: 0.3rem;">{row['title']}</h4>
                <p style="margin: 0.2rem 0;"><b>Type:</b> {row['type']} | <b>Episodes:</b> {row['episodes']}</p>
                <p style="margin: 0.2rem 0;"><b>Score:</b> {row['score']} | <b>Members:</b> {row['members']}</p>
                <p style="margin: 0.2rem 0;"><b>Genres:</b> {row['genres']}</p>
                <p style="margin: 0.2rem 0;"><b>Aired:</b> {row['aired_from']} ({row['aired_day']})</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


def display_poster_gallery(df):
    st.markdown("### 🖼️ Poster Gallery View")
    cols = st.columns(5)

    for i, (_, row) in enumerate(df.iterrows()):
        with cols[i % 5]:
            st.image(row['image_url'], caption=row['title'], use_column_width=True)
