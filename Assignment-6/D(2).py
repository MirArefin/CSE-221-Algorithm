import sys
sys.setrecursionlimit(2*10000+5)
input=sys.stdin.readline
N,R=map(int,input().split())
g=[[] for i in range(N+1)]
for i in range(N-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
size=[0]*(N+1)
visited=[False]*(N+1)
def dfs(x):
    visited[x]=True
    size[x]=1
    for k in g[x]:
        if not visited[k]:
            dfs(k)
            size[x]+=size[k]
dfs(R)
q=int(input())
for i in range(q):
    print(size[int(input())])