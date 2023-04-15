# importar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# cargar datos
data = pd.read_csv('C:\\Users\\Joselito\\Documents\\datos2.csv')

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

