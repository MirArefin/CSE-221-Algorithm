def longestsubarray(N,K,arr):
    i = 0
    sum = 0 
    max = 0
    for j in range(N):
        sum+= arr[j]
        while sum>K:
            sum -= arr[i]
            i+=1
        if j-i+1>max:
            max = j -i+1
N,K = map(int,input().split())
arr = list((map(int,input().split())))

