import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n, m, s, d = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
  u, v, w = map(int, input().split())
  g[u].append((v, w))
  g[v].append((u, w))

INF = 1 << 60
dist = [[INF, INF] for _ in range(n + 1)]
dist[s][0] = 0
hq = [(0, s)]

while hq:
  cost, u = heapq.heappop(hq)
  for v, w in g[u]:
    new_cost = cost + w
    if new_cost < dist[v][0]:
      dist[v][1] = dist[v][0]
      dist[v][0] = new_cost
      heapq.heappush(hq, (new_cost, v))
    elif dist[v][0] < new_cost < dist[v][1]:
      dist[v][1] = new_cost
      heapq.heappush(hq, (new_cost, v))

print(dist[d][1] if dist[d][1] < INF else -1)
