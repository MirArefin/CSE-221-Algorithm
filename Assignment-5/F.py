from collections import deque
import sys
input = sys.stdin.read
def max_diamonds(grid, R, H):
    visited = [[False] * H for _ in range(R)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_diamonds = 0
    def bfs(r, h):
        q = deque()
        q.append((r, h))
        visited[r][h] = True
        count = 1 if grid[r][h] == 'D' else 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < H and not visited[nx][ny] and grid[nx][ny] != '#':
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    if grid[nx][ny] == 'D':
                        count += 1
        return count
    for i in range(R):
        for j in range(H):
            if not visited[i][j] and grid[i][j] != '#':
                max_diamonds = max(max_diamonds, bfs(i, j))
    return max_diamonds
data = input().split()
R, H = int(data[0]), int(data[1])
grid = [list(data[i + 2]) for i in range(R)]
print(max_diamonds(grid, R, H))