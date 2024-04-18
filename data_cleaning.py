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

# The above code is create an almost fully-clean file:
# However since multiple songs can belong to the same album we need to remove the duplicate album occurences
# Since we only care about the Albums.
# We need to create a final file that only contains the following data:
# 1. Album Name, 2. Spotify Album ID, 3. Spotify Album Rating, 4. Fantana Album Rating

#Remove Duplicate Album ID:
mergedCSV = pd.read_csv('final_cleaned_data.csv')
mergedCSV.drop_duplicates(subset=['album_id'], keep='first',inplace=True)

# Remove redundant Columns:
columnsToRemove = ['Unnamed: 0_x','track_id','track_name','duration_ms','explicit_x','danceability_x', 'energy_x','key_x',
                   'loudness_x','mode_x','speechiness_x','acousticness_x','instrumentalness_x','liveness_x',
                   'valence_x','tempo_x','time_signature','Unnamed: 0_y','youtube_id','explicit_y','preview',
                   'danceability_y', 'energy_y', 'key_y','loudness_y', 'mode_y', 'speechiness_y', 'acousticness_y', 'instrumentalness_y',
                   'liveness_y','valence_y', 'tempo_y']
mergedCSV.drop(columns=columnsToRemove, inplace=True)
mergedCSV.to_csv('CLEAN_DATA.csv')

# Adding Anthony Fantanas Ratings to the Final CSV:
fantanaRatings = df1['rating']
#fantanaAlbumNames = df1['project_name']
mergedFinalCSV = pd.merge(mergedCSV, fantanaRatings, on='album_name', how='left')
mergedFinalCSV.to_csv('FINAL_CLEAN_FILE.csv')
