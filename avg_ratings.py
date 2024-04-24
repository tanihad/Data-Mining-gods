import pandas as pd

# Moving through both the Spotify and Fantana Dataset and finding the average ratings from each
# 1. Loop through combined file
# 2. For every song ID -- retrieve the corresponding songs popularity rating from the 
#    spotify dataset and its song rating from the Fantana dataset.
# 3. Add each rating to their corresponding rating sum -- while keeping track of the number of ratings
# 4. Calculate average rating
# Fantana - spotify_id
# Final - album_id



def calculateCorrelation():
    combinedDataFrame = pd.read_csv('FINAL_CLEAN_FILE.csv')
    # fantanaDataFrame = pd.read_csv('Fanta/Music review/albums.csv')

    # Total number of IDs
    total_id = len(combinedDataFrame)

    # Starting sums to calculate the average rating for Fantanas and
    averageDifferentialSum = 0
    songSet = set()

    for index, row in combinedDataFrame.iterrows():
        # For each album in the Dataframe, look up its ID in the Fantana
        currentSpotifyAlbumID = row['album_id']
        currentAlbum = row['album_name']

        spotifyRating = row['Album Rating']
        fantanaRating = row['rating'] * 10

        if currentSpotifyAlbumID not in songSet:
            print(spotifyRating, fantanaRating)
            avgValue = (spotifyRating + fantanaRating) / 2

            # Calculating the percent difference between the Spotify Popularity rating and Fantano's Rating
            percentDifference = (abs(spotifyRating - fantanaRating) / avgValue) * 100
            averageDifferentialSum += percentDifference
            ratingTuple = (currentSpotifyAlbumID, currentAlbum, percentDifference)
            songSet.add(currentSpotifyAlbumID)
            print(ratingTuple)

    ratingDifferential = averageDifferentialSum / len(songSet)
    print("Average Percent Differential: ", ratingDifferential)
    print("Total Songs: ", len(songSet))

    # Initializing a tuple that stores the spotify Album ID and how and a ratio describing how similar
    # Anthony Fantana and Spotify rated the album -- the closer the ratio is to 1.0 the more the ratings
    # 'agreed' with each other

if __name__ == '__main__':
    calculateCorrelation()

