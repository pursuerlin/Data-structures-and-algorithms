#######------bubble_sort------#######

# k 用来比较优化后的差别，只是简单的比较循环次数，不够严谨
def bubble_sort(nums):
    k = 0
    for i in range(len(nums) - 1):
    	for j in range(len(nums) - i - 1):
    		if nums[j] > nums[j + 1]: 
    			nums[j], nums[j + 1] = nums[j + 1], nums[j]
    		k += 1

# 优化1：内层每次循环时如果不发生数据交换，即整体已排好序
def bubble_sort1(nums):
    k = 0
    for i in range(len(nums) - 1):
    	exchange = False
    	for j in range(len(nums) - i - 1):
    		if nums[j] > nums[j + 1]: 
    			nums[j], nums[j + 1] = nums[j + 1], nums[j]
    			exchange = True
    		k += 1
    	if exchange == False: break


# 优化2：理论上，冒泡排序有序区的长度等于排序的轮次，
# 实际上可以在每一轮排序后，记录下最后一次元素交换的位置，
# 那个位置就是无序区的边界，往后就是有序区了
def bubble_sort2(nums):
    lastexchange = 0
    k = 0
    sortboard = len(nums) - 1
    for i in range(len(nums) - 1):
    	# exchange = False 
    	for j in range(sortboard):
    		if nums[j] > nums[j + 1]: 
    			nums[j], nums[j + 1] = nums[j + 1], nums[j]
    			# exchange = True
    			lastexchange = j + 1
    		k += 1
    	# if exchange == False: break
    	sortboard = lastexchange

# 两种优化合在一起貌似会更好
# 还有一种鸡尾酒排序，是冒泡排序的改进版，其时间复杂度更优
#######------bubble_sort------#######