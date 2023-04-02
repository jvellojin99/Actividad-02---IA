# Definimos la lista de adyacencia
graph = {
    'A': {'B': 5, 'C': 6},
    'B': {'C': 3, 'D': 1},
    'C': {'D': 2},
    'D': {}
}

# Definimos los puntos A y B
start = 'A'
end = 'D'

# Definimos una función para encontrar la ruta más corta entre dos puntos
def shortest_path(graph, start, end):
    # Inicializamos las variables necesarias
    visited = set()
    distances = {node: float('inf') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0

    # Ejecutamos el algoritmo para encontrar la ruta más corta
    while True:
        current_node = min(
            {node: distances[node] for node in graph if node not in visited},
            key=distances.get
        )
        #aqui
        visited.add(current_node)
        if current_node == end:
            break
        for neighbor, distance in graph[current_node].items():
            if neighbor in visited:
                continue
            tentative_distance = distances[current_node] + distance
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous_nodes[neighbor] = current_node

    # Construimos la ruta encontrada
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    # Devolvemos la ruta encontrada
    return path


# Ejecutamos la función para encontrar la ruta más corta entre los puntos A y D
ruta = shortest_path(graph, start, end)

# Imprimimos la ruta encontrada
print("Ruta encontrada:", ruta)