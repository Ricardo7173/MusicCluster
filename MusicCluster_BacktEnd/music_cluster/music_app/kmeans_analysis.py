import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from .models import SurveyResponse
import os

def run_kmeans():
    data = pd.DataFrame(list(SurveyResponse.objects.all().values()))

    if len(data) < 3:
        print("No hay suficientes datos para realizar el agrupamiento K-Means.")
        return

    features = data[['age', 'listening_hours_per_week']]
    features = features.dropna()

    kmeans = KMeans(n_clusters=3, random_state=0)
    data['cluster'] = kmeans.fit_predict(features)

    static_dir = os.path.join(os.path.dirname(__file__), 'static', 'music_app')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # Gráfico de dispersión
    plt.figure(figsize=(8, 6))
    plt.scatter(data['age'], data['listening_hours_per_week'], c=data['cluster'])
    plt.xlabel('Age')
    plt.ylabel('Listening Hours per Week')
    plt.title('K-Means Clustering of Music Preferences')
    kmeans_plot_path = os.path.join(static_dir, 'kmeans_plot.png')
    plt.savefig(kmeans_plot_path)
    plt.close()
    print(f"K-Means Plot guardado en: {kmeans_plot_path}")

    # Gráfico de barras de géneros favoritos por clúster
    plt.figure(figsize=(8, 6))
    genre_counts = data.groupby('cluster')['favorite_genre'].value_counts().unstack().fillna(0)
    genre_counts.plot(kind='bar', stacked=True)
    plt.xlabel('Cluster')
    plt.ylabel('Count')
    plt.title('Favorite Genres by Cluster')
    genre_by_cluster_path = os.path.join(static_dir, 'genre_by_cluster.png')
    plt.savefig(genre_by_cluster_path)
    plt.close()
    print(f"Favorite Genres by Cluster guardado en: {genre_by_cluster_path}")

    # Gráfico de barras de dispositivos preferidos por clúster
    plt.figure(figsize=(8, 6))
    device_counts = data.groupby('cluster')['device_preference'].value_counts().unstack().fillna(0)
    device_counts.plot(kind='bar', stacked=True)
    plt.xlabel('Cluster')
    plt.ylabel('Count')
    plt.title('Device Preferences by Cluster')
    device_by_cluster_path = os.path.join(static_dir, 'device_by_cluster.png')
    plt.savefig(device_by_cluster_path)
    plt.close()
    print(f"Device Preferences by Cluster guardado en: {device_by_cluster_path}")
