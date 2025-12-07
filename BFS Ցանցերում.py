def short_bfs(graph, start, end):
    queue = [(start, [start])] 
    visited = {start}
    
    while queue:
        node, path = queue.pop(0) 
        
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor] 
                queue.append((neighbor, new_path))
    
    return "Ճանապարհ չկա"
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

path = short_bfs(graph, 'A', 'F')
print(f"\n Ամենակարճ ճանապարհը A-ից F: {path}") 