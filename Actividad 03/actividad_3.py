from itertools import combinations
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Definimos la lista de adyacencia
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'C': 3, 'D': 1},
    'C': {'D': 2},
    'D': {}
}

# Generamos todas las posibles combinaciones de nodos
nodes = list(graph.keys())
node_pairs = list(combinations(nodes, 2))

# Definimos una función para encontrar todas las rutas posibles entre dos nodos utilizando el algoritmo de búsqueda en profundidad
def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Generamos un conjunto de datos etiquetados utilizando el algoritmo de búsqueda en profundidad
X = []
y = []

for pair in node_pairs:
    paths = dfs(graph, pair[0], pair[1])
    if paths:
        X.append(pair)
        y.append(1)
    else:
        X.append(pair)
        y.append(0)

# Creamos un modelo de clasificación utilizando la regresión logística
clf = LogisticRegression()
clf.fit(X, y)

# Predecimos si existe una ruta entre los nodos A y D utilizando el modelo entrenado
prediction = clf.predict([(start, end)])
if prediction[0] == 1:
    print("Existe una ruta entre los nodos", start, "y", end)
else:
    print("No existe una ruta entre los nodos", start, "y", end)
