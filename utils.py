def apply_filters(df, filters):
    f = filters
    df_filtered = df.copy()

    if f['search_title']:
        df_filtered = df_filtered[df_filtered['title'].str.contains(f['search_title'], case=False)]

    df_filtered = df_filtered[df_filtered['score'] >= f['score_filter']]
    df_filtered = df_filtered[df_filtered['episodes'].fillna(0) <= f['ep_filter']]

    if f['anime_type'] != 'All':
        df_filtered = df_filtered[df_filtered['type'] == f['anime_type']]

    if f['genre_filter']:
        df_filtered = df_filtered[df_filtered['genres'].apply(
            lambda x: any(g in x for g in f['genre_filter']))]

    df_filtered = df_filtered.sort_values(by=f['sort_by'], ascending=f['sort_asc'])

    return df_filtered
