import sys
sys.setrecursionlimit(2**25)
def cycle(N, adj):
    visited = [0] * (N + 1)
    def dfs(node):
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                if dfs(neighbor):
                    return True
            elif visited[neighbor] == 1:
                return True
        visited[node] = 2 
        return False
    for v in range(1, N + 1):
        if visited[v] == 0:
            if dfs(v):
                return True
    return False
N, M = map(int, input().split())
adj = [[] for i in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
print("YES" if cycle(N, adj) else "NO")