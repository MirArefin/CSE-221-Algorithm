
def advising():
        N, M=map(int, input().split()) 
        g=[[] for i in range (N+1)]
        order=[0]*(N+1)
        for j in range (M):
            q=[]
            A, B=map (int, input().split()) 
            g[A].append(B)
            order [B]+=1
        q=[]
        for i in range (1,N+1):
            if order[i]==0:
                 q.append(i)
        res=[]
        i=0
        while i<len(q):
            course=q[i]
            i+=1
            res.append(course) 
            for j in g[course]: 
                order [j]-=1
                if order[j]==0: 
                    q.append(j)
        if len(res)==N:
            print("".join(map (str, res)))
        else:
            print("-1")
advising()
