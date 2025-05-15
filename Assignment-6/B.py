def soccer():
    n, m = map(int, input().split())
    path = []
    for i in range(n + 1):
        path.append([])

    for i in range(m):
        u, v = map(int, input().split())
        path[u].append(v)
        path[v].append(u)
    t = [0] * (n + 1)
    score = 0
    for i in range(1, n + 1):
        if t[i] == 0:
            stk = [i]
            t[i] = 1
            count = [0, 0]
            count[0] += 1
            valid = True
            
            while stk:
                u = stk.pop()
                for v in path[u]:
                    if t[v] == 0:
                        t[v] = 3 - t[u]
                        count[t[v] - 1] += 1
                        stk.append(v)
                    elif t[v] == t[u]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                score += max(count)
    print(score)
soccer()
