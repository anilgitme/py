import math
def smallest_subarray_sum(s, arr):
    if not arr:
        return -1
    minLen = math.inf
    for i in range(len(arr)):
        total = 0
        for j in range(i + 1, len(arr)):     
            if arr[i] >= s or arr[j] >= s:
                minLen = 1
            subarr = arr[i:j+1]
            for num in subarr:
                total += num
                if total >= s:
                    if len(subarr) < minLen:
                        minLen = len(subarr)
                        
    if minLen == math.inf:
        return 0
    return minLen

print(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]))
print(smallest_subarray_sum(7, [2, 1, 5, 2, 8]))
print(smallest_subarray_sum(8, [3, 4, 1, 1, 6]))
print(smallest_subarray_sum(1, []))