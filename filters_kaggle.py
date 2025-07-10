import streamlit as st

def sidebar_filters_kaggle(df):
    st.sidebar.header("🔎 Filters")

    # Title Search
    search_title = st.sidebar.text_input("Search Title")

    # Genre Filter
    all_genres = sorted(set(g for sublist in df['genres'] for g in sublist))
    genre_filter = st.sidebar.multiselect("Genres", all_genres)

    # Type Filter
    all_types = df['type'].dropna().unique()
    type_filter = st.sidebar.multiselect("Type", sorted(all_types))

    # Year Range Filter
    year_min = int(df['aired_from_year'].min())
    year_max = int(df['aired_from_year'].max())
    year_range = st.sidebar.slider("Aired Year", year_min, year_max, (2010, 2023))

    # Sort Options
    sort_by = st.sidebar.selectbox("Sort by", options=['score', 'rank', 'popularity', 'members', 'aired_from_year'])
    sort_asc = st.sidebar.toggle("Ascending", value=False)

    return {
        'search_title': search_title,
        'genre_filter': genre_filter,
        'type_filter': type_filter,
        'year_range': year_range,
        'sort_by': sort_by,
        'sort_asc': sort_asc
    }
