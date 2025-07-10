import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def show_genre_chart(df):
    genre_list = sum([g.split(', ') for g in df['genres'] if g != 'N/A'], [])
    genre_counts = pd.Series(genre_list).value_counts().head(10)

    fig, ax = plt.subplots()
    ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

def show_airing_chart(df):
    airing_counts = df['aired_day'].value_counts().sort_index()
    st.bar_chart(airing_counts)
