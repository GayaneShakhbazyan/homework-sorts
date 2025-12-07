def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)] 
    
    while pq:
        min_dist = float('inf')
        current_node = None
        min_index = -1
        
        for i, (dist, node) in enumerate(pq):
            if dist < min_dist:
                min_dist = dist
                current_node = node
                min_index = i
        
        if current_node is None:
            break
        current_distance, current_node = pq.pop(min_index)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.append((distance, neighbor))
                
    return distances

weighted_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'E': 3},
    'E': {}
}

print(f"\n Դեկստրայի հեռավորություններ (սկիզբը 'A'): {dijkstra(weighted_graph, 'A')}")