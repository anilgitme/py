def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
    if not arr:
        return -1
    curSum = 0
    i = 0
    j = len(arr) -1
    while i < j:
        subarr = arr[i:k]
        print(subarr)
        total = 0
        for num in subarr:
            total += num
        if total > curSum:
            curSum = total
            total = 0
        else:
            total = 0
        i += 1
        k += 1
    return curSum


print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
print(max_sub_array_of_size_k(5, [10, 3, 4, 1, 5, 9, 2, 1, 8]))