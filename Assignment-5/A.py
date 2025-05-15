N, M = map(int, input().split())
front = 0
rear = 0
result = []
graph = {}
for i in range(1, N + 1):
    graph[i] = []
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    graph[i].sort()
visited = [False] * (N + 1)
queue = [0] * (N + 5)
queue[rear] = 1
rear += 1
visited[1] = True
while front < rear:
    node = queue[front]
    front += 1
    result.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue[rear] = neighbor
            rear += 1
print(*result)