import bisect
def count_in_range(arr, low, high):
    left_index = bisect.bisect_left(arr, low)
    right_index = bisect.bisect_right(arr, high)
    return right_index - left_index
N, K = map(int, input().split())
arr = list(map(int, input().split()))

output = []
for i in range(K):
    low, high = map(int, input().split())
    output.append(str(count_in_range(arr, low, high)))
print("\n".join(output))

