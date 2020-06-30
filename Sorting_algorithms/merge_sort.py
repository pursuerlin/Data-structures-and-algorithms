#######------merge_sort------#######

def merge(left, right):
	l, r = 0, 0
	temp = []
	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			temp.append(left[l])
			l += 1
		else:
			temp.append(right[r])
			r += 1
	temp += left[l:]
	temp += right[r:]
	return temp 

def merge_sort(nums):
	if len(nums) <= 1: return nums
	mid = len(nums) // 2
	left = merge_sort(nums[:mid])
	right = merge_sort(nums[mid:])
	return merge(left, right)

# 归并排序在数组长度比较小的时候可以直接用插入排序进行排序
#######------merge_sort------#######