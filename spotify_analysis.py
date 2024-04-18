import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns

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

def correverything():
    df = pd.read_csv("Spotify/spotify_dataset.csv")

    # Define the attributes to plot
    attributes = ['danceability', 'energy', 'popularity']

    # Create a figure with subplots
    fig, axes = plt.subplots(nrows=1, ncols=len(attributes), figsize=(15, 5))

    # Plot histograms for each attribute
    for ax, attribute in zip(axes, attributes):
        sns.histplot(df[attribute], bins=30, kde=False, ax=ax)
        ax.set_title(f'Distribution of {attribute.capitalize()}')
        ax.set_xlabel(f'{attribute.capitalize()} Rating')
        ax.set_ylabel('Number of Songs')

    # Display the plots
    plt.tight_layout()
    plt.show()

    # Exploratory Data Analysis using pairplot with histograms
    sns.pairplot(df[['danceability', 'energy', 'popularity']], diag_kind='hist', diag_kws={'bins': 30})
    plt.show()

    # Correlation Matrix
    correlation_matrix = df[['danceability', 'energy', 'popularity']].corr()
    print(correlation_matrix)
    sns.heatmap(correlation_matrix, annot=True)
    plt.show()

    # Clustering to find patterns (Standardization included)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(df[['danceability', 'energy', 'popularity']])

    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(data_scaled)
    df['cluster'] = clusters

    # Visualize clusters using hexbin plots to aggregate data
    grid = sns.JointGrid(data=df, x='energy', y='popularity', space=0)
    grid.plot_joint(plt.hexbin, gridsize=30, cmap='viridis', mincnt=1)
    sns.kdeplot(df['energy'], ax=grid.ax_marg_x, legend=False)
    sns.kdeplot(df['popularity'], ax=grid.ax_marg_y, vertical=True, legend=False)
    plt.suptitle("Clustered Data on Energy vs Popularity with Density Marginals")
    plt.show()

    # Regression Analysis
    X = df[['danceability', 'energy']]
    y = df['popularity']
    model = LinearRegression()
    model.fit(X, y)
    df['predicted_popularity'] = model.predict(X)

    # Plot regression results using a hexbin plot for aggregation
    plt.figure(figsize=(10, 6))
    plt.hexbin(df['popularity'], df['predicted_popularity'], gridsize=50, cmap='Reds', mincnt=1)
    plt.colorbar(label='Count in bin')
    plt.plot([df['popularity'].min(), df['popularity'].max()],
             [df['popularity'].min(), df['popularity'].max()], 'k--')
    plt.xlabel('Actual Popularity')
    plt.ylabel('Predicted Popularity')
    plt.title('Actual vs Predicted Popularity Hexbin Plot')
    plt.show()
# Example usage:
if __name__ == '__main__':
    # analyze_danceability_popularity("Spotify/spotify_dataset.csv")
    # analyze_energy_popularity("Spotify/spotify_dataset.csv")
    # analyze_danceability_energy("Spotify/spotify_dataset.csv")
    correverything()
