def longestsubarray(N, K, arr):
    left = sum = maxlength = 0

    for right in range(N):
        sum += arr[right]

        if sum > K:
            sum -= arr[left]
            left += 1

        maxlength = max(maxlength, right - left + 1)

    return maxlength

N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(longestsubarray(N, K, arr))
