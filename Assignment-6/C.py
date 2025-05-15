from collections import deque
n=int(input())
x1,y1,x2,y2=map(int,input().split())
dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]
visited = [[0]*n for i in range(n)]
queue=deque([(x1-1,y1-1,0)])
visited[x1-1][y1-1]=1
while queue:
    x,y,d=queue.popleft()
    if x==x2-1 and y==y2-1:
        print(d)
        break
    for i in range(8):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n:
          if not visited[nx][ny]:
            visited[nx][ny]=1
            queue.append((nx,ny,d+1))
else:
    print(-1)