from collections import deque
def bfs(start, end, graph, n):
    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    queue = deque()
    queue.append(start)
    dist[start] = 0
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + 1
                parent[neighbor] = curr
                queue.append(neighbor)
                if neighbor == end:
                    break
    if dist[end] == -1:
        return -1, []
    path = []
    node = end
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()
    return dist[end], path
N, M, S, D, K = map(int, input().split())
graph = {}
for i in range(1, N + 1):
    graph[i] = []
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
dist1, path1 = bfs(S, K, graph, N)
dist2, path2 = bfs(K, D, graph, N)
if dist1 == -1 or dist2 == -1:
    print(-1)
else:
    res = path1 + path2[1:]
    print(len(res) - 1)
    print(" ".join(map(str, res)))