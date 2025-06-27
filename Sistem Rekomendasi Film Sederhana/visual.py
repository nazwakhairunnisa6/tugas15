import matplotlib.pyplot as plt
import pandas as pd

def plot_genre_distribution(movies_df):
    genre_counts = movies_df['genre'].value_counts()
    
    # Pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribusi Genre Film')
    plt.savefig('img/genre_pie.png')
    
    # Bar chart
    plt.figure(figsize=(8, 6))
    genre_counts.plot(kind='bar')
    plt.title('Jumlah Film per Genre')
    plt.xlabel('Genre')
    plt.ylabel('Jumlah Film')
    plt.savefig('img/genre_rating_bar.png')
