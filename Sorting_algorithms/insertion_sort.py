#######------insertion_sort------#######

# 维护一个有序区，将元素一个个插入到有序区的合适位置
# 1.在大多数元素已经有序的情况下，插入排序的工作量较小
# 2.在元素数量较少的情况下，插入排序的工作量较小
# 基于这两个特点，衍生出希尔排序
def insertion_sort(nums):
	for i in range(1, len(nums)):
		for j in range(i - 1, -1, -1):
			if nums[j + 1] < nums[j]:
				nums[j + 1], nums[j] = nums[j], nums[j + 1]
			else:
				break
# 为了避免元素的频繁交换，可以进行优化
def insertion_sort1(nums):
	for i in range(1, len(nums)):
		tem = nums[i]
		for j in range(i - 1, -1, -1):
			if tem < nums[j]:
				nums[j + 1] = nums[j]
			else:
				nums[j + 1] = tem
				break
			if j == 0:
				nums[j] = tem

# 这个方式更好	
def insertion_sort2(nums):
	n = len(nums)
	if n <= 1:
		return 
	for i in range(1, n):
		cur_value = nums[i]
		position = i
		while position > 0 and nums[position - 1] > cur_value:
			nums[position] = nums[position - 1]
			position -= 1
		nums[position] = cur_value

# 插入元素的位置可以用二分查找方法优化
#######------insertion_sort------#######