import pandas as pd

df1 = pd.read_csv('Spotify/spotify_dataset.csv')
df2 = pd.read_csv('Fanta/Music review/tracks.csv')

df1 = df1.drop_duplicates(subset=['track_name', 'track_id'])
df2.rename(columns={'name': 'track_name', 'spotify_id': 'track_id'}, inplace=True)
df2 = df2.drop_duplicates(subset=['track_name', 'track_id'])
common_songs = pd.merge(df1, df2, on=["track_name", "track_id"])
print(common_songs[['track_name', 'track_id']])

common_songs.to_csv('common_songs.csv', index=False)
