N,M=map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
a = []
for i in range(N):
    a.append([])
for i in range(M):
    first_node = A[i]-1
    last_node = B[i]
    weight = C[i]
    a[first_node].append((last_node,weight))
for i in range(N):
    print(i+1, end=': ')
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()