def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
    if len(str1) <= k:
        return len(str1)
    unique = []
    maxsub = 0
    count = 0
    for s in str1:
        if s not in unique and len(unique) >= k:
            unique = []
            count = 0
        elif s not in unique and len(unique) <= k:
            unique.append(s)
            count += 1
            if count > maxsub:
                maxsub = count
        elif s in unique and len(unique) <= k:
            count += 1
            if count > maxsub:
                maxsub = count
    return maxsub
    


print(longest_substring_with_k_distinct("araaci", 2))
print(longest_substring_with_k_distinct("cbbebi", 10))
print(longest_substring_with_k_distinct("a", 2))
print(longest_substring_with_k_distinct("", 2))