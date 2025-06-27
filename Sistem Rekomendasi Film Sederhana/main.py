import os
import pandas as pd
from data_loader import load_data
from recommender import recommend_movies
from visual import plot_genre_distribution

def ensure_data_file():
    if not os.path.exists('data'):
        os.makedirs('data')

    csv_path = os.path.join('data', 'film.csv')
    if not os.path.isfile(csv_path):
        sample_data = """Judul,genre,rating,tahun
John Wick,Aksi,8.0,2014
Mad Max: Fury Road,Aksi,7.9,2015
The Raid,Aksi,7.6,2011
Gladiator,Aksi,8.0,2000
Avengers,Aksi,8.5,2019
Coco,Animasi,8.0,2017
Spider-Man: Menuju Spider-Verse,Animasi,7.0,2018
Nemo,Animasi,7.8,2003
buku catatan,Romantis,8.0,2004
Rain,Romantis,7.8,2010
Love london,Romantis,8.5,2015
Film Terburuk,Drama,1.0,2020
Kisah Sedih,Drama,2.0,2019
Bencana Alam,Aksi,3.0,2018
Cinta yang Hilang,Romantis,4.0,2017
Petualangan Biasa,Aksi,5.0,2016
Kisah Inspiratif,Drama,6.0,2015
Pahlawan Sejati,Aksi,7.0,2014
Cinta Abadi,Romantis,8.0,2013
Karya Agung,Drama,9.0,2012
Film Terbaik Sepanjang Masa,Aksi,10.0,2011"""
        
        with open(csv_path, 'w') as f:
            f.write(sample_data)

def create_image_folder():
    if not os.path.exists('img'):
        os.makedirs('img')

def get_user_input():
    print("\n=== Sistem Rekomendasi Film ===")
    genre = input("Masukkan genre favorit (Aksi/Animasi/Romantis/Drama): ").strip().capitalize()
    while True:
        try:
            rating = float(input("Masukkan rating minimal (0-10): "))
            if 0 <= rating <= 10:
                break
            print("Rating harus antara 0-10. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
    return genre, rating

def filter_and_recommend(movies_df, genre, rating):
    # Rekomendasi film di atas rating
    above_rating = movies_df[(movies_df['genre'] == genre) & (movies_df['rating'] > rating)]
    
    # Rekomendasi film di bawah rating 
    below_rating = movies_df[(movies_df['genre'] == genre) & (movies_df['rating'] < rating)]
    
    return above_rating.sort_values(by='rating', ascending=False), below_rating.sort_values(by='rating', ascending=False)

def main():
    ensure_data_file()
    create_image_folder()
    
    movies_df = load_data()
    
    genre, rating = get_user_input()
    
    recommended_above, recommended_below = filter_and_recommend(movies_df, genre, rating)
    
    print("\n=== Rekomendasi Film di Atas Rating ===")
    if recommended_above.empty:
        print("Tidak ada film di atas rating yang memenuhi kriteria")
    else:
        print(recommended_above[['Judul', 'rating', 'tahun']].to_string(index=False))
    
    print("\n=== Rekomendasi Film di Bawah Rating ===")
    if recommended_below.empty:
        print("Tidak ada film di bawah rating yang memenuhi kriteria")
    else:
        print(recommended_below[['Judul', 'rating', 'tahun']].to_string(index=False))
    
    plot_genre_distribution(movies_df)
    print("\nGrafik genre disimpan di img/genre_pie.png")
    print("Grafik rating per genre disimpan di img/genre_rating_bar.png")

if __name__ == '__main__':
    main()
