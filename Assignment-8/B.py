
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x == root_y:
        return False  
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1  
    return True  
def compute_mst(n, edges):
    parent = list(range(n+1))
    rank = [0] * (n+1)
    edges.sort(key=lambda x: x[2])
    total_weight = 0
    edges_in_mst = 0
    for u, v, w in edges:
        if union(parent, rank, u, v):
            total_weight += w
            edges_in_mst += 1
            if edges_in_mst == n-1:
                break  
    return total_weight
N, M = map(int, input().split())
edges = []
for i in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
print(compute_mst(N, edges))