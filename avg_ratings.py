import pandas as pd
import time
#import matplotlib.pyplot as plt
import numpy as np

def tuplediff():
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
        currenArtist = row['artists']
        # Fantano's rating is out of ten whereas Spotify's is out of 100 -- we have to normalize
        # the value by multiplying by 10
        fantanaRating = row['rating'] * 10

        if currentSpotifyAlbumID not in songSet:
            avgValue = (spotifyRating + fantanaRating) / 2

            # Calculating the percent difference between the Spotify Popularity rating and Fantano's Rating
            percentDifference = (abs(spotifyRating - fantanaRating) / avgValue) * 100
            averageDifferentialSum += percentDifference

            ratingTuple = (currentSpotifyAlbumID, currentAlbum, percentDifference)
            print("--------------------------------------------------------------------")
            print("Album Name: ",currentAlbum," By ", currenArtist," Spotify ID: ",currentSpotifyAlbumID)
            print("Spotify Album Rating: ", spotifyRating, " Fantano's Rating: ", fantanaRating," % Difference: ", percentDifference)
            print("--------------------------------------------------------------------")
            print("")
            songSet.add(currentSpotifyAlbumID)
            time.sleep(.5)

    ratingDifferential = averageDifferentialSum / len(songSet)
    print("Average Percent Differential: ", ratingDifferential.__round__(2))
    #print("Total Albums: ", len(songSet))

    # Initializing a tuple that stores the spotify Album ID and how and a ratio describing how similar
    # Anthony Fantana and Spotify rated the album -- the closer the ratio is to 1.0 the more the ratings
    # 'agreed' with each other

# Below is code to generate different graphs/plots of the rating percent differential between albums


# def graphdiffs():
#     import pandas as pd
#     import matplotlib.pyplot as plt
#
#     # Load the data from the CSV file
#     data = pd.read_csv('FINAL_CLEAN_FILE.csv')
#
#     # Extract the relevant columns for the plot
#     spotify_ratings = data['Album Rating']
#     fantana_ratings = data['rating'] * 10  # Scaling Fantana ratings to be comparable to Spotify ratings
#
#     # Create the scatter plot with Fantana ratings in red
#     plt.figure(figsize=(10, 6))
#     plt.scatter(spotify_ratings, fantana_ratings, color='red', alpha=0.5)  # Setting color to red
#     plt.title('Comparison of Spotify and Fantana Album Ratings')
#     plt.xlabel('Spotify Album Rating')
#     plt.ylabel('Fantana Album Rating (scaled)')
#     plt.grid(True)  # Adding grid for better readability
#     plt.show()

# def graphdiffs1():
#     import pandas as pd
#     import matplotlib.pyplot as plt
#
#     # Load the data from the CSV file
#     data = pd.read_csv('FINAL_CLEAN_FILE.csv')
#
#     # Extract the relevant columns for the plot
#     spotify_ratings = data['Album Rating']
#     fantana_ratings = data['rating'] * 10  # Scaling Fantana ratings to be comparable to Spotify ratings
#
#     # Create the scatter plot
#     plt.figure(figsize=(10, 6))
#     plt.scatter(spotify_ratings, fantana_ratings, color='blue', alpha=0.5)  # Spotify ratings in blue
#     plt.scatter(spotify_ratings, fantana_ratings, color='red', alpha=0.5)  # Fantana ratings in red
#     plt.title('Comparison of Spotify and Fantana Album Ratings')
#     plt.xlabel('Spotify Album Rating')
#     plt.ylabel('Fantana Album Rating (scaled)')
#     plt.grid(True)  # Adding grid for better readability
#     plt.show()
#
# def genrecomp():
#     import pandas as pd
#     import matplotlib.pyplot as plt
#     # Load the data from the CSV file
#     data = pd.read_csv('FINAL_CLEAN_FILE.csv')
#
#     # Scale the Fantana ratings
#     data['Fantana Scaled Rating'] = data['rating'] * 10
#
#     # Define the genres of interest
#     selected_genres = ['rock', 'hard rock', 'metal', 'death metal', 'country', 'pop', 'edm', 'hip hop', 'jazz', 'latin',
#                        'club', 'chill']
#
#     # Filter the dataset to include only the selected genres
#     filtered_data = data[data['track_genre'].isin(selected_genres)]
#
#     # Group by 'track_genre' and calculate the mean for Spotify and Fantana ratings
#     genre_averages = filtered_data.groupby('track_genre').agg({
#         'Album Rating': 'mean',
#         'Fantana Scaled Rating': 'mean'
#     }).reset_index()
#
#     # Plotting
#     fig, ax = plt.subplots(figsize=(14, 8))
#
#     # Location of labels on the x-axis
#     x = np.arange(len(genre_averages['track_genre']))
#
#     # Width of the bars
#     bar_width = 0.35
#
#     # Plotting each set of bars for Spotify and Fantana
#     rects1 = ax.bar(x - bar_width / 2, genre_averages['Album Rating'], bar_width, label='Spotify', color='#EBC483')
#     rects2 = ax.bar(x + bar_width / 2, genre_averages['Fantana Scaled Rating'], bar_width, label='Fantana', color='#8ED3C2')
#
#     # Adding some text for labels, title, and custom x-axis tick labels, etc.
#     ax.set_xlabel('Genre')
#     ax.set_ylabel('Average Ratings')
#     ax.set_title('Average Ratings by Genre from Spotify and Fantana')
#     ax.set_xticks(x)
#     ax.set_xticklabels(genre_averages['track_genre'], rotation=45)
#     ax.legend()
#
#     # Adding a bit of layout optimization
#     fig.tight_layout()
#
#     plt.show()


if __name__ == '__main__':
    tuplediff()



