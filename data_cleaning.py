import pandas as pd 

# The purpose of this file is to cross reference the Spotify song dataset and the dataset containing all of the songs
# Fantana reviewed and combining them into one document. Once we have all of the songs cross referenced and combined into one CSV file,
# we can iterate through the CSV file comparing the popularity rating of the song from Spotify to the rating Fantana gave the corresponding song.

# Reading the data from Fantana Rating Dataset and the Spotify Song dataset (both CSV files)
df1 = pd.read_csv('Spotify/spotify_dataset.csv')
df2 = pd.read_csv('Fanta/Music review/tracks.csv')

# We realized that both datasets from Kaggle contained duplicate songs: we remove them below:
df1 = df1.drop_duplicates(subset=['track_name', 'track_id'])

# Using Spotify IDs to find which songs are in both the Fantana and the Spotify data set.
# Making sure the names of the columns are the same in both datasets so that we can compare them with ease:
df2.rename(columns={'name': 'track_name', 'spotify_id': 'track_id'}, inplace=True)
df2 = df2.drop_duplicates(subset=['track_name', 'track_id'])

# Creating a common song CSV containing all the songs from the Spotify Dataset that Fantana rated so that we can easily find the 
# IDs of the songs that are in both
common_songs = pd.merge(df1, df2, on=["track_name", "track_id"])
print(common_songs[['track_name', 'track_id']])


common_songs.to_csv('common_songs.csv', index=False)

dfGrouping = pd.read_csv('common_songs.csv')
grouped = dfGrouping.groupby('album_name')

# Calculate the average rating for each album
# The Fantana dataset only provides ratings of albums whereas Spotify only gave ratings for each song
# In order to get around this issue we calculated the ratings of Spotify albums ourselves, by averaging the
# ratings of every song in the album -- this way we could accurately compare the fantana and spotify datasets
album_ratings = grouped['popularity'].mean().round(1)

# Create a new DataFrame to store the average ratings for each album
album_ratings_df = pd.DataFrame(album_ratings).reset_index()

# Rename the column to indicate it contains average ratings
album_ratings_df = album_ratings_df.rename(columns={'popularity': 'Album Rating'})

# Merge the average ratings DataFrame with the original DataFrame based on album names
df_merged = pd.merge(dfGrouping, album_ratings_df, on='album_name', how='left')
df_merged.to_csv('final_cleaned_data.csv')
