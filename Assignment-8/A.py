def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, size, a, b):
    root1 = find(parent, a)
    root2 = find(parent, b)
    if root1 != root2:
        if size[root1] < size[root2]:
            parent[root1] = root2
            size[root2] += size[root1]
        else:
            parent[root2] = root1
            size[root1] += size[root2]
    return size[find(parent, a)]
def Friendships(n, friendships):
    parent = list(range(n+1))  
    size = [1] * (n+1)
    results = []
    for a, b in friendships:
        results.append(union(parent, size, a, b))
    return results
N, K = map(int, input().split())
edges = []
for i in range(K):
    a, b = map(int, input().split())
    edges.append((a, b))
res = Friendships(N, edges)
for i in res:
    print(i)