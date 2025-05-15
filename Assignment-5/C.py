from collections import deque
N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
graph = {}
for i in range(1, N + 1):
    graph[i] = []
for i in range(M):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])  
for node in graph:
    graph[node].sort()
distance = [-1] * (N + 1)
parent = [-1] * (N + 1)
queue = deque()
queue.append(S)
distance[S] = 0
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            parent[neighbor] = current
            queue.append(neighbor)
if distance[D] == -1:
    print(-1)
else:
    path = []
    current = D
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    print(distance[D])
    print(" ".join(map(str, path)))