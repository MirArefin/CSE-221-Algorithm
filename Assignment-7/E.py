import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def min_cost_parity_path(n, m, u_list, v_list, w_list):
    graph = defaultdict(list)
    for u, v, w in zip(u_list, v_list, w_list):
        graph[u].append((v, w))
    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    dist[1][0] = dist[1][1] = 0
    heap = [(0, 1, -1)]  # (cost, node, prev_parity)
    while heap:
        cost, node, prev_p = heapq.heappop(heap)
        for nei, w in graph[node]:
            p = w % 2
            if p == prev_p: continue
            if cost + w < dist[nei][p]:
                dist[nei][p] = cost + w
                heapq.heappush(heap, (cost + w, nei, p))
    res = min(dist[n])
    print(res if res != float('inf') else -1)

n, m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))
min_cost_parity_path(n, m, u_list, v_list, w_list)
