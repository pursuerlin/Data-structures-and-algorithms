#######------shell_sort------#######

# 对于原始数组进行[预处理]，使得数组的大部分元素变得有序，再用插入排序
# 希尔排序也称为缩小增量排序，把序列看作一个矩阵，分成m列，逐列进行排序
# m从某个整数逐渐减为1，当m为1时，整个序列完全有序
# 逐步折半为希尔增量，但因为每轮增量并不互质，所以最坏的时间复杂度会退化为O(n^2)
# Hibbard增量，通式：2^k - 1，最坏时间复杂度为O(n^(3/2))
# Sedgewick增量，通式：分为奇偶情况 ，最坏时间复杂度为O(n^(4/3))
def shell_sort(nums):
	size = len(nums)
	gap = size >> 1
	while gap > 0:
		for i in range(gap, size):
			j = i
			while j >= gap and nums[j - gap] > nums[j]:
				nums[j - gap], nums[j] = nums[j], nums[j - gap]
				j -= gap
		gap >>= 1

#######------shell_sort------#######