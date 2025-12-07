def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf')] * V for _ in range(V)]
    
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif j in graph[i]:
                dist[i][j] = graph[i][j]
                
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    for i in range(V):
        if dist[i][i] < 0:
            return "Գրաֆը պարունակում է բացասական ցիկլ"
            
    return dist

graph_fw = {
    0: {1: 3, 2: 8},
    1: {2: 4},
    2: {0: 1}
}
distances_fw = floyd_warshall(graph_fw)

print("\n Ֆլոյդ-Վարշալի հեռավորությունների մատրիցը:")

if isinstance(distances_fw, str):
    print(distances_fw)
else:
    for row in distances_fw:
        printable_row = [round(d, 2) if d != float('inf') else 'INF' for d in row]
        print(printable_row)