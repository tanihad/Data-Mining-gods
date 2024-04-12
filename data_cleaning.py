import pandas as pd

# Load the datasets
df1 = pd.read_csv('Spotify/spotify_dataset.csv')
df2 = pd.read_csv('Fanta/Music review/tracks.csv')

# Remove duplicates from df1 based on 'track_name' and 'track_id'
df1 = df1.drop_duplicates(subset=['track_name', 'track_id'])

# Rename columns in df2 to match those in df1
df2.rename(columns={'name': 'track_name', 'spotify_id': 'track_id'}, inplace=True)

# Remove duplicates from df2 based on 'track_name' and 'track_id'
df2 = df2.drop_duplicates(subset=['track_name', 'track_id'])

# Merge the dataframes on both 'track_name' and 'track_id'
common_songs = pd.merge(df1, df2, on=["track_name", "track_id"])

# Print the list of common songs with their track IDs
print(common_songs[['track_name', 'track_id']])

# Save the resulting dataframe to a CSV file
common_songs.to_csv('common_songs.csv', index=False)
