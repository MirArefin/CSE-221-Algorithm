n,sum = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
right = len(arr)-1
temp = []
while left<right:
    if arr[left]+arr[right] == sum:
        temp.append(left+1)
        temp.append(right+1)
        break
    elif arr[left]+arr[right]<sum:
        left+=1
    else:
        right -= 1
if temp == []:
    print(-1)
else:
    print(f'{temp[0]} {temp[1]}')