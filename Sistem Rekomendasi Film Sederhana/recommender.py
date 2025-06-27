import pandas as pd

def recommend_movies(movies_df, genre, rating):
    
    if genre not in movies_df['genre'].unique():
        raise ValueError(f"Genre {genre} tidak tersedia")
    
    if not isinstance(rating, (int, float)) or rating < 0 or rating > 10:
        raise ValueError("Rating harus berupa angka antara 0-10")
    
    filtered = movies_df[(movies_df['genre'] == genre) & 
                        (movies_df['rating'] >= rating)]
    
    if rating == 5:
        bonus_recommendations = movies_df[(movies_df['genre'] == genre) & 
                            (movies_df['rating'] > rating)].head(3)
        filtered = pd.concat([filtered, bonus_recommendations]).drop_duplicates()
    
    return filtered.sort_values(by='rating', ascending=False)

if __name__ == '__main__':

    test_data = pd.DataFrame({
        'Judul': ['Film A', 'Film B', 'Film C'],
        'genre': ['Aksi', 'Aksi', 'Romantis'],
        'rating': [8.5, 7.5, 6.0],
        'tahun': [2010, 2015, 2018]
    })
    
    print("Test rekomendasi dengan rating 5:")
    print(recommend_movies(test_data, 'Aksi', 5))
    print("\nTest rekomendasi dengan rating 8:")
    print(recommend_movies(test_data, 'Aksi', 8))
