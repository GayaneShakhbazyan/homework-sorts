graph = {
    'A': ['B', 'C'],
    'B': ['C', 'F'],
    'C': ['D'],
    'D': [],
    'E': [],
    'F': ['D', 'E'],
    'G': ['B', 'F']
}

def topo_bfs(graph):
    # Հաշվում ենք in-degree (մուտքային քանակ)
    indeg = {}
    for v in graph:
        indeg[v] = 0

    for v in graph:
        for u in graph[v]:
            indeg[u] += 1

    # Ավելացնում ենք հանգույցները, որոնց indegree = 0 է
    queue = []
    for v in indeg:
        if indeg[v] == 0:
            queue.append(v)

    order = []

    while queue:
        x = queue.pop(0)
        order.append(x)

        for u in graph[x]:
            indeg[u] -= 1
            if indeg[u] == 0:
                queue.append(u)

    return order


print(topo_bfs(graph))
