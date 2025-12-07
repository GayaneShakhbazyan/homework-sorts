def conn_comp(graph):
    visited = set()
    components = []
    def dfs(node, current_comp):
        visited.add(node)
        current_comp.append(node)
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                dfs(neighbor, current_comp)
    for node in graph:
        if node not in visited:
            new_comp = []
            dfs(node, new_comp)
            components.append(new_comp)
    return components

example = {1: [2],
           2: [1, 3],
           3: [2],
           4: [5],
           5: [4],
           6: [],
           7: []}
result = conn_comp(example)
print(result)