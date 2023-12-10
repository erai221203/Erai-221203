#BFS
from collections import deque
def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited.append(start)
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
graph = {
    '1': ['2', '5'],
    '2': ['1', '3', '4','5'],
    '3': ['2', '4', '6'],
    '4': ['2','3','5','6'],
    '5': ['1','2','4','6'],
    '6': ['3','4','5'],
}

start = '1'
print("BFS starting from node", start)
bfs(graph, start)
