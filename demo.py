###This is for the demo

####LIBRARIES NEEDED#############
import pandas as pd
import time
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns
##################################




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
            time.sleep(.1)

    ratingDifferential = averageDifferentialSum / len(songSet)
    print("Average Percent Differential: ", ratingDifferential.__round__(2))


#################################################################################################################

def correverything_spotify1(file):
    df = pd.read_csv(file)
    attributes = ['duration_ms', 'mode', 'valence', 'tempo', 'popularity']  # Corrected list

    # Correlation Matrix
    correlation_matrix = df[attributes].corr()
    print(correlation_matrix)
    sns.heatmap(correlation_matrix, annot=True)
    plt.show()

def understanding_attributescor(file):
    df = pd.read_csv(file)
    attributes = ['danceability_x', 'energy_x','popularity' ] #all the _xs are spotify's

    # Correlation Matrix
    correlation_matrix = df[['danceability', 'energy', 'popularity']].corr()
    print(correlation_matrix)
    sns.heatmap(correlation_matrix, annot=True)
    plt.show()


#Clustering
def genre_cluster_comp():
    # Load the data from the CSV file
    data = pd.read_csv('FINAL_CLEAN_FILE.csv')

    # Scale the Fantana ratings
    data['Fantana Scaled Rating'] = data['rating'] * 10

    # Define the genres of interest
    selected_genres = ['rock', 'hard-rock', 'metal', 'death-metal', 'country', 'pop', 'edm', 'hip-hop', 'jazz', 'latin',
                       'club', 'chill']

    # Filter the dataset to include only the selected genres
    filtered_data = data[data['track_genre'].isin(selected_genres)]

    # Group by 'track_genre' and calculate the mean for Spotify and Fantana ratings along with any other musical attributes available
    genre_averages = filtered_data.groupby('track_genre').agg({
        'Album Rating': 'mean',
        'Fantana Scaled Rating': 'mean',
        'tempo_x': 'mean',  # Assuming tempo is available
        'valence_x': 'mean'  # Assuming valence is available
    }).reset_index()

    # Normalize the data for clustering
    scaler = StandardScaler()
    genre_features = genre_averages[['Album Rating', 'Fantana Scaled Rating', 'tempo_x', 'valence_x']]
    scaled_features = scaler.fit_transform(genre_features)

    # Clustering
    kmeans = KMeans(n_clusters=len(selected_genres), random_state=42)
    clusters = kmeans.fit_predict(scaled_features)
    genre_averages['Cluster'] = clusters

    # Reduce dimensions for visualization
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(scaled_features)
    genre_averages['PC1'] = principal_components[:, 0]
    genre_averages['PC2'] = principal_components[:, 1]

    # Plotting
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=genre_averages, palette='viridis', s=100, legend=None)
    for i, txt in enumerate(genre_averages['track_genre']):
        plt.annotate(txt, (genre_averages['PC1'][i], genre_averages['PC2'][i]))

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Genre Clusters based on Ratings and Musical Attributes')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    while True:  # Start an infinite loop
        # Present a menu to the user for the demo
        print("\nSelect the function to run for the demo:")
        print("1. Rating Differences (tuplediff)")
        print("2. Correlation of attributes")
        print("3. Correlation of everything")
        print("4. Genre Clustering (genre_cluster_comp)")
        print("9. Exit")

        choice = input("Enter the number of the function to run or 9 to exit: ")

        if choice == '1':
            tuplediff()
        elif choice == '2':
            understanding_attributescor("Spotify/spotify_dataset.csv")  # Ensure this function is defined in your script
        elif choice == '3':
            correverything_spotify1("Spotify/spotify_dataset.csv")  # Ensure this function is defined in your script
        elif choice == '4':
            genre_cluster_comp()
        elif choice == '9':
            print("Exiting the demo.")
            break  # Break the loop to exit
        else:
            print("Invalid selection. Please enter a valid number.")

