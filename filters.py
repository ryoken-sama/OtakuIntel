import streamlit as st

def sidebar_filters(df):
    st.sidebar.header("🔎 Filters")

    search_title = st.sidebar.text_input("Search Title")

    min_score, max_score = int(df['score'].min()), int(df['score'].max())
    score_filter = st.sidebar.slider("Minimum Score", min_score, max_score, value=min_score)

    ep_max = df['episodes'].dropna().max() if not df['episodes'].isnull().all() else 100
    ep_filter = st.sidebar.slider("Max Episodes", 0, int(ep_max), value=int(ep_max))

    all_genres = sorted(set(g for sublist in df['genres'].str.split(', ') if isinstance(sublist, list) for g in sublist))
    genre_filter = st.sidebar.multiselect("Genres", options=all_genres)

    anime_type = st.sidebar.selectbox("Type", options=['All'] + sorted(df['type'].dropna().unique().tolist()))

    sort_by = st.sidebar.selectbox("Sort by", options=['score', 'members', 'title', 'episodes'])
    sort_asc = st.sidebar.toggle("Ascending", value=False)

    return {
        'search_title': search_title,
        'score_filter': score_filter,
        'ep_filter': ep_filter,
        'genre_filter': genre_filter,
        'anime_type': anime_type,
        'sort_by': sort_by,
        'sort_asc': sort_asc
    }
