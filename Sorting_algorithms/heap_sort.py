#######------heap_sort------#######

# 选择排序可以进行优化，每轮选最值可以用堆进行优化
# 堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，虽然实质上还是一维数组。
# 堆的存储：
# 一般都用数组来表示堆，i结点的父结点下标就为(i – 1) / 2。它的左右子结点下标分别为2 * i + 1和2 * i + 2。如第0个结点左右子结点下标分别为1和2。

def heap_Sort(nums):
    # 调整堆
    def adjustHeap(nums, i, size):
        # 非叶子结点的左右两个孩子
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        # 在当前结点、左孩子、右孩子中找到最大元素的索引
        largest = i 
        if lchild < size and nums[lchild] > nums[largest]: 
            largest = lchild 
        if rchild < size and nums[rchild] > nums[largest]: 
            largest = rchild 
        # 如果最大元素的索引不是当前结点，把大的结点交换到上面，继续调整堆
        if largest != i: 
            nums[largest], nums[i] = nums[i], nums[largest] 
            # 第 2 个参数传入 largest 的索引是交换前大数字对应的索引
            # 交换后该索引对应的是小数字，应该把该小数字向下调整
            adjustHeap(nums, largest, size)
    # 建立堆
    def builtHeap(nums, size):
        for i in range(len(nums)//2)[::-1]: # 从倒数第一个非叶子结点开始建立大根堆
            adjustHeap(nums, i, size) # 对所有非叶子结点进行堆的调整
        # print(nums)  # 第一次建立好的大根堆
    # 堆排序 
    size = len(nums)
    builtHeap(nums, size) 
    for i in range(len(nums))[::-1]: 
        # 每次根结点都是最大的数，最大数放到后面
        nums[0], nums[i] = nums[i], nums[0] 
        # 交换完后还需要继续调整堆，只需调整根节点，此时数组的 size 不包括已经排序好的数
        adjustHeap(nums, 0, i) 
    return nums  # 由于每次大的都会放到后面，因此最后的 nums 是从小到大排列
#######------heap_sort------#######	 