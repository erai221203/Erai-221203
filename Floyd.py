#Floyd Warshall
def floyd(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
graph = [
    [0,5,float('inf'),10],
    [float('inf'),0,3,float('inf')],
    [float('inf'),float('inf'),0,1],
    [float('inf'),float('inf'),float('inf'),0]]
result = floyd(graph)
for row in result:
    print(row)
