def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    print(start_node, end=' ')
    visited.add(start_node)
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS ճանապարհը (սկիզբը 'A'):")
dfs(graph, 'A')  
print()