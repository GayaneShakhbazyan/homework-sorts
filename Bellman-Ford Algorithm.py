def bellman_ford(nodes, edges, start_node):
    distances = {node: float('inf') for node in nodes}
    distances[start_node] = 0
    for _ in range(len(nodes) - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight                
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return "Գրաֆը պարունակում է բացասական ցիկլ"
            
    return distances
nodes = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'C', 6), ('A', 'D', 6), ('B', 'A', 3), ('C', 'D', 1),
    ('D', 'B', -2), ('D', 'E', 2), ('E', 'B', 1), ('C', 'E', 4)
]

print(f"\n Բելման-Ֆորդի հեռավորություններ (սկիզբը 'A'): {bellman_ford(nodes, edges, 'A')}")