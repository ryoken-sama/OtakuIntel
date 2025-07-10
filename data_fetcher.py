import requests
import pandas as pd

def fetch_seasonal_anime():
    url = "https://api.jikan.moe/v4/seasons/now"
    res = requests.get(url)
    if res.status_code != 200:
        return []
    return res.json()["data"]

def preprocess_data(anime_data):
    df = pd.DataFrame(anime_data)

    df = df[[
        'title', 'images', 'score', 'type', 'episodes', 'genres', 'members', 'aired'
    ]]

    df['image_url'] = df['images'].apply(lambda x: x['jpg']['image_url'])
    df['aired_from'] = df['aired'].apply(lambda x: x['from'][:10] if x['from'] else 'N/A')
    df['aired_day'] = pd.to_datetime(df['aired_from'], errors='coerce').dt.day_name()
    df['genres'] = df['genres'].apply(lambda x: ", ".join([g['name'] for g in x]) if x else 'N/A')

    return df
