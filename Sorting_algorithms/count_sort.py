#######------count_sort------#######

import itertools
def count_sort(nums):
    if len(nums) <= 1: return

    # a中有counts[i]个数不大于i
    counts = [0] * (max(nums) + 1)
    for num in nums:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))

    # 临时数组，储存排序之后的结果
    nums_sorted = [0] * len(nums)
    for num in reversed(nums):
        index = counts[num] - 1
        nums_sorted[index] = num
        counts[num] -= 1
    
    nums[:] = nums_sorted

#######------count_sort------#######