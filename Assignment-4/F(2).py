n = int(input())
a, b = map(int, input().split())
dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)]
result = []
for k in dirs:
    i = a + k[0]
    j = b + k[1]
    if 1 <= i <= n and 1 <= j <= n:
        result.append((i, j))
result.sort()
print(len(result))
for pos in result:
    print(pos[0], pos[1])
