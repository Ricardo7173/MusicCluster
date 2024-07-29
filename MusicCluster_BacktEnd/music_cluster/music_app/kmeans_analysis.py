import os
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from .models import SurveyResponse
import pickle

def run_kmeans():
    data = pd.DataFrame(list(SurveyResponse.objects.all().values()))

    # Seleccionar las columnas relevantes para el análisis
    features = pd.get_dummies(data[['instrument', 'rhythm', 'lyrics', 'language', 
                                    'listening_scenario', 'musical_personality', 
                                    'favorite_genre', 'favorite_artist', 
                                    'listening_platform', 'production_quality']])

    if len(features) < 3:
        print("No hay suficientes datos para realizar el análisis K-Means.")
        return

    # Determinar el número óptimo de clusters
    max_clusters = len(features)
    if max_clusters > 10:
        max_clusters = 10  # Limitar el máximo número de clusters para el análisis

    inertia = []
    K = range(1, max_clusters + 1)
    for k in K:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(features)
        inertia.append(kmeans.inertia_)

    optimal_clusters = 2  # Valor predeterminado
    if len(inertia) > 1:
        optimal_clusters = inertia.index(min(inertia[1:])) + 1

    # Aplicar K-Means con el número óptimo de clusters
    kmeans = KMeans(n_clusters=optimal_clusters)
    data['cluster'] = kmeans.fit_predict(features)

    # Guardar el modelo K-Means ajustado
    model_path = os.path.join(os.path.dirname(__file__), 'kmeans_model.pkl')
    with open(model_path, 'wb') as f:
        pickle.dump(kmeans, f)

    # Gráfico de Dispersión en 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(data['instrument'].astype('category').cat.codes, 
                         data['rhythm'].astype('category').cat.codes,
                         data['lyrics'].astype('category').cat.codes, c=data['cluster'])
    ax.set_xlabel('Instrumentos')
    ax.set_ylabel('Ritmo')
    ax.set_zlabel('Letra')
    plt.title('K-Means Clustering (3D)')
    plt.legend(*scatter.legend_elements(), title='Clusters')
    plt.savefig('music_app/static/music_app/kmeans_3d.png')
    plt.close()

    # Gráfico de Silueta
    silhouette_avg = silhouette_score(features, data['cluster'])
    sample_silhouette_values = silhouette_samples(features, data['cluster'])
    plt.figure(figsize=(8, 6))
    y_lower = 10
    for i in range(optimal_clusters):
        ith_cluster_silhouette_values = sample_silhouette_values[data['cluster'] == i]
        ith_cluster_silhouette_values.sort()
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i
        plt.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values)
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10
    plt.axvline(x=silhouette_avg, color="red", linestyle="--")
    plt.xlabel('Coeficiente de Silueta')
    plt.ylabel('Clusters')
    plt.title('Gráfico de Silueta')
    plt.savefig('music_app/static/music_app/silhouette_plot.png')
    plt.close()

    # Gráfico de Inercia vs Número de Clusters (Elbow Method)
    plt.figure(figsize=(8, 6))
    plt.plot(K, inertia, 'bx-')
    plt.xlabel('Número de Clusters')
    plt.ylabel('Inercia')
    plt.title('Método del Codo para encontrar el Número Óptimo de Clusters')
    plt.savefig('music_app/static/music_app/elbow_method.png')
    plt.close()

    # Mapa de Calor de Correlaciones
    plt.figure(figsize=(10, 8))
    sns.heatmap(features.corr(), annot=True, cmap='coolwarm', linewidths=.5)
    plt.title('Mapa de Calor de Correlaciones')
    plt.savefig('music_app/static/music_app/correlation_heatmap.png')
    plt.close()

    # Gráficos de barras para cada pregunta
    def save_bar_plot(df, column, title, filename):
        plt.figure(figsize=(8, 6))
        counts = df.groupby('cluster')[column].value_counts().unstack().fillna(0)
        counts.plot(kind='bar', stacked=True)
        plt.xlabel('Cluster')
        plt.ylabel('Cantidad')
        plt.title(title)
        plt.savefig(f'music_app/static/music_app/{filename}.png')
        plt.close()

    save_bar_plot(data, 'instrument', 'Instrumentos Favoritos por Cluster', 'instrument_by_cluster')
    save_bar_plot(data, 'rhythm', 'Ritmos Preferidos por Cluster', 'rhythm_by_cluster')
    save_bar_plot(data, 'lyrics', 'Tipos de Letras Preferidos por Cluster', 'lyrics_by_cluster')
    save_bar_plot(data, 'language', 'Idiomas Preferidos por Cluster', 'language_by_cluster')
    save_bar_plot(data, 'listening_scenario', 'Escenarios de Escucha por Cluster', 'scenario_by_cluster')
    save_bar_plot(data, 'musical_personality', 'Personalidades Musicales por Cluster', 'personality_by_cluster')
    save_bar_plot(data, 'favorite_genre', 'Géneros Favoritos por Cluster', 'genre_by_cluster')
    save_bar_plot(data, 'favorite_artist', 'Artistas Favoritos por Cluster', 'artist_by_cluster')
    save_bar_plot(data, 'listening_platform', 'Plataformas de Escucha por Cluster', 'platform_by_cluster')
    save_bar_plot(data, 'production_quality', 'Importancia de la Calidad de Producción por Cluster', 'quality_by_cluster')