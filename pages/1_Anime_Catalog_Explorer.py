import streamlit as st
from anime_catalog import load_anime_data
from filters_kaggle import sidebar_filters_kaggle

# Load dataset
df = load_anime_data()

st.title("Anime Catalog Explorer")
st.markdown("Filter and explore thousands of anime titles from MyAnimeList.")

# Apply filters
filters = sidebar_filters_kaggle(df)

filtered_df = df.copy()

if filters['search_title']:
    filtered_df = filtered_df[filtered_df['title'].str.contains(filters['search_title'], case=False)]

if filters['genre_filter']:
    filtered_df = filtered_df[filtered_df['genres'].apply(lambda x: any(g in x for g in filters['genre_filter']))]

if filters['type_filter']:
    filtered_df = filtered_df[filtered_df['type'].isin(filters['type_filter'])]

filtered_df = filtered_df[
    (filtered_df['aired_from_year'] >= filters['year_range'][0]) &
    (filtered_df['aired_from_year'] <= filters['year_range'][1])
]

filtered_df = filtered_df.sort_values(by=filters['sort_by'], ascending=filters['sort_asc'])

# Display results
st.markdown(f"### Showing {len(filtered_df)} anime")
st.dataframe(filtered_df[[
    'title', 'score', 'rank', 'popularity', 'type',
    'episodes', 'aired_from_year', 'genres'
]])
