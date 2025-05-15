def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return 
nodes, queries = map(int, input().split())
adj_list = [[] for i in range(nodes + 1)]
for a in range(1, nodes + 1):
    for b in range(1, nodes + 1):
        if a != b and compute_gcd(a, b) == 1:
            adj_list[a].append(b)
    adj_list[a].sort()
for i in range(queries):
    node, position = map(int, input().split())
    if position <= len(adj_list[node]):
        print(adj_list[node][position - 1])
    else:
        print(-1)

