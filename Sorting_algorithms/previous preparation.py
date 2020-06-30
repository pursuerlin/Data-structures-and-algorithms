# 生成随机数列
from random import randint

def generateRandomArray(n, min, max):
	arr = []
	arr = [randint(min, max) for x in range(n)]
	return arr

# 对于一些极端情况，考虑算法的效率，需要生成基本有序的数列
def generateNearOrderArray(n, swapTimes):
	arr = []
	for i in range(n): 
		arr.append(i)
	for j in range(swapTimes):
		posx = randint(0, n - 1)
		posy = randint(0, n - 1)
		arr[posx], arr[posy] = arr[posy], arr[posx]
	return arr

# 判断数列是否有序
def isSorted(alist):
	for i in range(len(alist) - 1):
		if alist[i] > alist[i + 1]:
			return False
	return True