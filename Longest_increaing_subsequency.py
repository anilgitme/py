def longest_increasing_subsequency(l: List) -> int:
    result = end = 0
    
    for i in range(len(l)):
        if i > 0 and l[i - 1] >= l[i]:
            end = i
        
        result = max(result, i - end+1)
    return result

print(longest_increasing_subsequency([3,5,7,2,1]))
print(longest_increasing_subsequency([2,2,2,2]))
print(longest_increasing_subsequency([]))
print(longest_increasing_subsequency([2,2,3,4,4]))