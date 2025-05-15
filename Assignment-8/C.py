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
def compute_mst(n, edges, exclude_idx=-1):
    parent = list(range(n+1))
    rank = [0] * (n+1)
    total_weight = 0
    edges_used = 0
    edges_in_mst = []
    for i, (u, v, w) in enumerate(edges):
        if i == exclude_idx:
            continue
        if union(parent, rank, u, v):
            total_weight += w
            edges_used += 1
            edges_in_mst.append(i)
            if edges_used == n-1:
                break
    return total_weight if edges_used == n-1 else float('inf'), edges_in_mst
def compute_second_best(n, edges):
    edges.sort(key=lambda x: x[2])
    best_weight, best_mst_edges = compute_mst(n, edges)
    second_best = float('inf')
    for edge_idx in best_mst_edges:
        alt_weight, _ = compute_mst(n, edges, edge_idx)
        if best_weight < alt_weight < second_best:
            second_best = alt_weight
    return second_best if second_best != float('inf') else -1
N, M = map(int, input().split())
edges = []
for i in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
print(compute_second_best(N, edges))