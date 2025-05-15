def advise_plan():
    n, m = map(int, input().split())
    path = []
    for i in range(n + 1):
        path.append([])
    waiting = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        path[a].append(b)
        waiting[b] += 1
    q = []
    for i in range(1, n + 1):
        if waiting[i] == 0:
            q.append(i)
    res = []
    x = 0
    while x < len(q):
        at = q[x]
        x += 1
        res.append(at)
        for to in path[at]:
            waiting[to] -= 1
            if waiting[to] == 0:
                q.append(to)

    if len(res) == n:
        print(*res)
    else:
        print(-1)

advise_plan()
