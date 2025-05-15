import heapq
from collections import defaultdict
def shortest_path(N, M, S, D, u_list, v_list, w_list):
    graph=defaultdict(list)
    for u, v, w in zip(u_list, v_list, w_list):
        graph[u].append((v, w))
    dist=[float('inf')] * (N + 1)
    prev=[-1]*(N + 1)
    dist[S] = 0
    heap=[(0,S)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                prev[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))
    if dist[D] == float('inf'):
        print(-1)
        return
    print(dist[D])
    path = []
    cur = D
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    print(' '.join(map(str, path)))

N,M,S,D=list(map(int, input().split()))
u_list=list(map(int, input().split()))
v_list=list(map(int, input().split())) 
w_list=list(map(int, input().split()))
shortest_path(N,M,S,D,u_list,v_list,w_list)
