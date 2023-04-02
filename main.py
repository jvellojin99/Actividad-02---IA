# lista de adyacencia
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 3, 'D': 1},
    'C': {'D': 2},
    'D': {}
}

# puntos A y B
start = 'B'
end = 'C'


# función para encontrar la ruta más corta entre dos puntos
def shortest_path(graph, start, end):
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

