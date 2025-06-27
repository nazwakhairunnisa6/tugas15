import pandas as pd
import os

def load_film_data(csv_file_path='data/film.csv'):
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"File data tidak ditemukan: {csv_file_path}. Pastikan folder 'data' dan file 'film.csv' ada.")
    df = pd.read_csv(csv_file_path)
    required_columns = ['Judul', 'genre', 'rating', 'tahun']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("File CSV harus memiliki kolom: Judul, genre, rating, tahun")
    return df
def get_all_movies_display(movies_df):
    return movies_df[['Judul', 'genre', 'rating', 'tahun']]

if __name__ == '__main__':
    data_dir = 'data'
    csv_path = os.path.join(data_dir, 'film.csv')

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
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

    try:
        film_data = load_film_data(csv_path)
        display_data = get_all_movies_display(film_data)
        print(display_data.to_string(index=False))
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
