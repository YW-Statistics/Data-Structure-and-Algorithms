# Title: Sort Algorithm
# Time: 2020/10/23
# Author: Vincent

# 工具箱
from random import randint

# 生成随机序列
def generateRandomSequence(start, end):
    output = [randint(start, end) for _ in range(100)]
    return output

# 检验排序正确性
def testSorted(sorted_list):
    if not sorted_list:
        raise ValueError('数组为空，无法检测！')
    for i in range(1, len(sorted_list)):
        # 默认检测升序
        if sorted_list[i] < sorted_list[i-1]:
            return False
    return True


'------------------------------下面开始正文------------------------------------'
# 冒泡排序
def bubbleSort(nums):
    size = len(nums)
    for i in range(size-1, -1, -1):
        flag = False
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True
        if not flag:
            break
    return nums

# 快速排序
def quickSort(nums):
    size = len(nums) # 计算数组长度
    def helper(left, right):
        if left >= right: # 递归出口：当左指针大于右指针时，表明左右两侧均已调整完成
            return nums
        pivot = left # 设置基准值指针
        i, j = left, right # 设置左右指针
        while i < j:
            # 指针滑动，保证右指针指向小于基准的元素，左指针指向大于基准的元素
            while i < j and nums[j] > nums[pivot]:
                j -= 1
            while i < j and nums[i] <= nums[pivot]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        # 调整基准点
        nums[pivot], nums[j] = nums[j], nums[pivot]
        helper(left, j-1) # 调整基准点左侧
        helper(j+1, right) # 调整基准点右侧
        return nums
    return helper(0, size-1)
                
# 插入排序
def insertionSort(nums):
    size = len(nums)
    for i in range(1, size):
        if nums[i] < nums[i-1]:
            tmp = nums.pop(i)
            for j in range(i):
                if tmp < nums[j]:
                    nums.insert(j, tmp)
                    break
    return nums

def insertionSort1(nums):
    size = len(nums)
    for i in range(1, size):
        while i > 0 and nums[i-1] > nums[i]:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1
    return nums

# 希尔排序
def shellSort(nums):
    size = len(nums)
    gap = size // 2
    while gap:
        for i in range(gap, size):
            while i - gap >= 0 and nums[i-gap] > nums[i]:
                nums[i-gap], nums[i] = nums[i], nums[i-gap]
                i -= gap
        gap //= 2
    return nums

# 选择排序
def selectionSort(nums):
    size = len(nums)
    start = 0
    while start < size:
        min_num = float('inf')
        min_index = 0
        for j in range(start, size):
            if nums[j] < min_num:
                min_num = nums[j]
                min_index = j
        nums[start], nums[min_index] = nums[min_index], nums[start]
        start += 1
    return nums
    
# 归并排序
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) or j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        if i == len(left):
            while j < len(right):
                res.append(right[j])
                j += 1
        elif j == len(right):
            while i < len(left):
                res.append(left[i])
                i += 1
    return res

# 计数排序
def countingSort(nums):
    max_num, min_num = max(nums), min(nums)
    tmp = [0] * (max_num-min_num+1)
    for num in nums:
        tmp[num-min_num] += 1
        
    res = []
    for i in range(len(tmp)):
        while tmp[i] > 0:
            res.append(i+min_num)
            tmp[i] -= 1
    return res
    
# 基数排序
def radixSort(nums):
    if not nums:
        return []
    maxNum = max(nums)
    maxDigit = len(str(maxNum))
    bucketList = [[] for _ in range(10)]
    div, mod = 1, 10
    for i in range(maxDigit):
        for num in nums:
            bucketList[num % mod // div].append(num)
        div *= 10
        mod *= 10
        idx = 0
        for j in range(10):
            for k in bucketList[j]:
                nums[idx] = k
                idx += 1
            bucketList[j] = []
    return nums
        
# 桶排序
def bucketSort(nums, bucketSize):
    if len(nums) < 2:
        return nums
    max_num, min_num = max(nums), min(nums)
    bucketNum = (max_num-min_num) // bucketSize + 1
    buckets = [[] for _ in range(bucketNum)]
    for num in nums:
        buckets[(num-min_num) // bucketSize].append(num)
    res = []
    for bucket in buckets:
        if not bucket:
            continue
        if bucketSize == 1: # 如果桶间隔为1，等价于计数排序，直接扩展
            res.extend(bucket)
        else:
            if bucketNum == 1: # 如果桶数为1，说明间隔过大
                bucketSize -= 1
            res.extend(bucketSort(bucket, bucketSize))
    return res
    

if __name__ == '__main__':
    sample = generateRandomSequence(0, 100)
    
    # bubble_sorted = bubbleSort(sample)
    # testSorted(bubble_sorted)
    
    # quick_sorted = quickSort(sample)
    # testSorted(quick_sorted)
    
    # insertion_sorted = insertionSort(sample)
    # testSorted(insertion_sorted)
    # insertion_sorted1 = insertionSort1(sample)
    # testSorted(insertion_sorted1)
    
    # shell_sorted = shellSort(sample)
    # testSorted(shell_sorted)
    
    # selection_sorted = selectionSort(sample)
    # testSorted(selection_sorted)
    
    # merge_sorted = mergeSort(sample)
    # testSorted(merge_sorted)
    
    # counting_sorted = countingSort(sample)
    # testSorted(counting_sorted)
    
    # radix_sorted = radixSort(sample)
    # testSorted(radix_sorted)
    
    bucket_sorted = bucketSort(sample, 5)
    testSorted(bucket_sorted)
    