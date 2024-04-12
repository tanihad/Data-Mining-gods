import pandas as pd

# Load the datasets
df1 = pd.read_csv('Spotify/spotify_dataset.csv')
df2 = pd.read_csv('Fanta/Music review/tracks.csv')


# Check if the Spotify ID column needs renaming in either dataframe
# Here we assume both dataframes already use 'spotify_id' as the column name

# Function to check for a Spotify ID in both dataframes
def check_spotify_id(spotify_id):
    # Check if the ID is in both dataframes
    in_df1 = df1['track_id'].isin([spotify_id]).any()
    in_df2 = df2['spotify_id'].isin([spotify_id]).any()

    # Return results
    if in_df1 and in_df2:
        return f"The Spotify ID {spotify_id} is present in both datasets."
    elif in_df1:
        return f"The Spotify ID {spotify_id} is present only in the first dataset."
    elif in_df2:
        return f"The Spotify ID {spotify_id} is present only in the second dataset."
    else:
        return f"The Spotify ID {spotify_id} is not present in either dataset."


# Example usage
spotify_id_input = input("Enter a Spotify ID to check: ")
result = check_spotify_id(spotify_id_input)
print(result)
