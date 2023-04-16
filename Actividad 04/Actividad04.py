# importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# cargar datos
data = pd.read_csv('E:/Work/Disco D/Kevin/Universidad/Inteligencia artificial/Actividades/datos2.csv')

# preprocesamiento de datos
X = data.iloc[:, 1:].values # seleccionar columnas relevantes
X = np.nan_to_num(X) # manejar valores faltantes
X = (X - X.mean()) / X.std() # normalización de datos

# selección de número óptimo de clusters utilizando el método del codo
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Método del codo')
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')
plt.show()

# entrenamiento del modelo utilizando el número óptimo de clusters
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(X)

# evaluación del modelo utilizando la métrica de silueta
silhouette_avg = silhouette_score(X, kmeans.labels_)
print('El coeficiente de silueta promedio es:', silhouette_avg)

# interpretación de resultados
cluster_labels = kmeans.labels_
