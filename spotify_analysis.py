import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def dpclust(csv_file_path, n_clusters=2, random_state=42):
    data = pd.read_csv(csv_file_path)
    attributes = data[['popularity', 'danceability', 'energy']]
    scaler = StandardScaler()
    attributes_scaled = scaler.fit_transform(attributes)

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(attributes_scaled)
    data['cluster'] = clusters

    plt.figure(figsize=(10, 8))
    plt.scatter(data['popularity'], data['danceability'], c=data['cluster'], cmap='viridis')
    plt.colorbar()
    plt.xlabel('Popularity')
    plt.ylabel('Danceability')
    plt.title('2D Cluster Plot of Popularity vs Danceability')
    plt.show()

def pe_clust(csv_file_path, n_clusters=2, random_state=42):
    data = pd.read_csv(csv_file_path)
    attributes = data[['popularity', 'energy']]
    scaler = StandardScaler()
    attributes_scaled = scaler.fit_transform(attributes)

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(attributes_scaled)
    data['cluster'] = clusters

    plt.figure(figsize=(10, 8))
    plt.scatter(data['popularity'], data['energy'], c=data['cluster'], cmap='viridis')
    plt.colorbar()
    plt.xlabel('Popularity')
    plt.ylabel('Energy')
    plt.title('2D Cluster Plot of Popularity vs Energy')
    plt.show()

def analyze_danceability_popularity(csv_file_path):
    data = pd.read_csv(csv_file_path)

    corr, _ = pearsonr(data['danceability'], data['popularity'])
    print(f"The Pearson correlation coefficient between danceability and popularity is: {corr:.3f}")

    X = data['danceability'].values.reshape(-1, 1)  # Features (independent variables)
    y = data['popularity'].values  # Target (dependent variable)
    model = LinearRegression()
    model.fit(X, y)
    trendline = model.predict(X)

    plt.figure(figsize=(10, 6))
    plt.hexbin(data['danceability'], data['popularity'], gridsize=50, cmap='Reds', mincnt=1)
    cb = plt.colorbar()
    cb.set_label('Density')

    plt.plot(X, trendline, color='blue')

    plt.xlabel('Danceability')
    plt.ylabel('Popularity')
    plt.title('Density Heatmap of Danceability vs Popularity with Regression Line')

    plt.show()

def analyze_energy_popularity(csv_file_path):
    data = pd.read_csv(csv_file_path)

    corr, _ = pearsonr(data['energy'], data['popularity'])
    print(f"The Pearson correlation coefficient between energy and popularity is: {corr:.3f}")

    X = data['energy'].values.reshape(-1, 1)
    y = data['popularity'].values
    model = LinearRegression()
    model.fit(X, y)
    trendline = model.predict(X)

    plt.figure(figsize=(10, 6))
    plt.hexbin(data['energy'], data['popularity'], gridsize=50, cmap='Reds', mincnt=1)
    cb = plt.colorbar()
    cb.set_label('Density')

    plt.plot(X, trendline, color='blue')

    plt.xlabel('Energy')
    plt.ylabel('Popularity')
    plt.title('Density Heatmap of Energy vs Popularity with Regression Line')

    plt.show()

def analyze_danceability_energy(csv_file_path):
    data = pd.read_csv(csv_file_path)

    corr, _ = pearsonr(data['danceability'], data['energy'])
    print(f"The Pearson correlation coefficient between danceability and energy is: {corr:.3f}")

    X = data['danceability'].values.reshape(-1, 1)
    y = data['energy'].values
    model = LinearRegression()
    model.fit(X, y)
    trendline = model.predict(X)

    plt.figure(figsize=(10, 6))
    plt.hexbin(data['danceability'], data['energy'], gridsize=50, cmap='Reds', mincnt=1)
    cb = plt.colorbar()
    cb.set_label('Density')

    plt.plot(X, trendline, color='blue')
    plt.xlabel('Danceability')
    plt.ylabel('Energy')
    plt.title('Density Heatmap of Danceability vs Energy with Regression Line')
    plt.show()

# Example usage:
if __name__ == '__main__':
    analyze_danceability_popularity("Spotify/spotify_dataset.csv")
    analyze_energy_popularity("Spotify/spotify_dataset.csv")
    analyze_danceability_energy("Spotify/spotify_dataset.csv")
