def bfs_collections(graph, start_node):
    queue = [start_node]
    visited = {start_node}
    
    print(f"\nBFS ճանապարհը (սկիզբը '{start_node}'):")
    
    while queue:
        node = queue.pop(0) 
        print(node, end=' ')
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_collections(graph, 'A') 
print()

