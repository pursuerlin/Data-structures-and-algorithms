#######------selection_sort------#######

# 选择排序相较于冒泡排序可以较少元素之间的交换次数，但是一个不稳定排序
def selection_sort(nums):
	for i in range(len(nums) - 1):
		cur_min = i
		for j in range(i + 1, len(nums)):
			if nums[j] < nums[cur_min]:
				cur_min = j
		nums[i], nums[cur_min] = nums[cur_min], nums[i]

#######------selection_sort------#######