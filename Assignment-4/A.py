N,M=map(int,input().split())
a = []
for i in range(N):
    row=[]
    for j in range(N):
        row.append(0)
    a.append(row)
for k in range(M):
    A,B,C = map(int,input().split())
    a[A-1][B-1] = C
for i in range(N):
    for j in range(N):
        print(a[i][j],end=' ')
    print()