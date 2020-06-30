#######-------quick_sort------#######

# # 一行代码实现快速排序：
# quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

# # 网上常见的快速排序
# def quick_sort(nums, l, r):
#     left, right = l, r
#     if left >= right: return 
#     pivot = nums[left]
#     while left < right:
#     	while left < right and nums[right] >= pivot:
#     		right -= 1
#     	nums[left] = nums[right]

#     	while left < right and nums[left] < pivot:
#     		left += 1
#     	nums[right] = nums[left]
#     nums[left] = pivot
#     quick_sort(nums, l, left - 1)
#     quick_sort(nums, left + 1, r)

# # 《算法导论》中的快速排序
# def quick_sort(array, l, r):
#     if l < r:
#         q = partition(array, l, r)
#         quick_sort(array, l, q - 1)
#         quick_sort(array, q + 1, r)
 
# def partition(array, l, r):
#     x = array[r]
#     i = l - 1
#     for j in range(l, r):
#         if array[j] <= x:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     array[i + 1], array[r] = array[r], array[i + 1]
#     return i + 1

# # 这个版本跟上个版本的不同在于分片过程不同，只用了一层循环，并且一趟就完成分片，相比之下代码要简洁的多了。

# 用栈实现非递归的快速排序
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])

 #######-------quick_sort------#######