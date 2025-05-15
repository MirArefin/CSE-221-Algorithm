import sys
import heapq

def dijkstra(N, graph, start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(heap, (dist[neighbor], neighbor))
    return dist

def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])
    S = int(data[2])
    T = int(data[3])

    graph = [[] for _ in range(N + 1)]
    index = 4
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        graph[u].append((v, w))
        index+=3

    dist_from_S = dijkstra(N, graph, S)
    dist_from_T = dijkstra(N, graph, T)

    best_time = float('inf')
    meeting_node = -1
    for i in range(1,N+1):
        if dist_from_S[i]==dist_from_T[i] and dist_from_S[i] != float('inf'):
            if dist_from_S[i]<best_time or (dist_from_S[i] == best_time and i < meeting_node):
                best_time=dist_from_S[i]
                meeting_node=i

    if meeting_node == -1:
        print(-1)
    else:
        print(f"{best_time} {meeting_node}")

if __name__ == "__main__":
    main()
