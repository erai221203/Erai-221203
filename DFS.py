# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = v=[]
        
    print(start, end="  ")
    v.append(start)
    for neighbor in graph[start]:
        if neighbor not in v:
            dfs(graph, neighbor, v)
graph = {
    '1': ['2', '5'],
    '2': ['1', '3', '4','5'],
    '3': ['2', '4', '6'],
    '4': ['2','3','5','6'],
    '5': ['1','2','4','6'],
    '6': ['3','4','5'],
}
start_node = '1'
print("DFS starting from node", start_node)
dfs(graph, start_node)