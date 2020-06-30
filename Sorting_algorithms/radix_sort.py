# 基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
# 由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
def radix_sort(input_list):

	def MaxBit(input_list):
		max_data = max(input_list)
		bits_num = 0
		while max_data:
			bits_num += 1
			max_data //= 10
		return bits_num

	def digit(num, d):
		p = 1
		while d > 1:
			d -= 1
			p *= 10
		return num // p % 10

	if len(input_list) == 0:
		return []
	sorted_list = input_list
	length = len(sorted_list)
	bucket = [0] * length

	for d in range(1, MaxBit(sorted_list) + 1):
		count = [0] * 10

		for i in range(0, length):
			count[digit(sorted_list[i], d)] += 1

		for i in range(1, 10):
			count[i] += count[i - 1]

		for i in range(0, length)[::-1]:
			k = digit(sorted_list[i], d)
			bucket[count[k] - 1] = sorted_list[i]
			count[k] -= 1
		for i in range(0, length):
			sorted_list[i] = bucket[i]

	return sorted_list

# LSD Radix Sort
def radixSort(nums):
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))  # 最大数的位数决定了外循环多少次
    buckets = [[] for row in range(mod)] # 构造 mod 个空桶
    while mostBit:
        for num in nums:  # 将数据放入对应的桶中
            buckets[num // div % mod].append(num)
        i = 0  # nums 的索引
        for bucket in buckets:  # 将数据收集起来
            while bucket:
                nums[i] = bucket.pop(0) # 依次取出
                i += 1
        div *= 10
        mostBit -= 1
    return nums

#######------radix_sort------#######