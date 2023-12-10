from collections import deque
def bfs(start,graph):
    v=[]
    q=deque([start])
    v.append(start)
    while q:
        current=q.popleft()
        print(current,end='\t')
        for i in graph[current]:
            if i not in v:
                q.append(i)
                v.append(i)
graph={ '1': ['2','3'],
        '3': ['3','1'],
        '2': ['1'],
    }
start='2'
bfs(start,graph)