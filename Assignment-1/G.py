def BubbleSortforTrains(trains):
    n=len(trains)
    for i in range(n):
        for j in range(n-1-i):
            if (trains[j][0]>trains [j+1][0]):
                 trains[j], trains [j+1]=trains [j+1], trains[j]
            elif trains[j][0]==trains[j+1][0] :
                  if trains[j][1]<trains[j+1][1]:
                     trains[j], trains [j+1]=trains [j+1], trains[j]
N=int(input())
Temp=[]
for k in range(N):
    x=input().split()
    name=x[0]
    place=x[4]
    time=x[-1].split(':')
    Temp.append((name, time[0]*60+time[1] , x))
    BubbleSortforTrains(Temp)
for k in Temp:
    print(f'{k[2][0]} will departure for {k[2][4]} at {k[2][-1]}')
