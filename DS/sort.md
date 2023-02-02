 # 排序算法
## 冒泡算法
1. 比较相邻的元素。如果第一个比第二个大（从小到大排序），就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 除了最后一个元素，针对其他所有的元素重复以上步骤。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
``` Python
def BubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]: # 排序顺序只改这行
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
a = [3, 2, 4, 7, 8, 5, 1, 9, 0, 6]
BubbleSort(a)
```
## 选择排序
1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。
``` Python
def SelectSort(arr):
    for i in range(0, len(arr)-1):
        maxIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[maxIndex]:  # 排序顺序只改这行
                maxIndex = j  # 注释
        if i != maxIndex:  # 注释
            arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    return arr


a = [3, 2, 4, 7, 8, 5, 1, 9, 0, 6]
SelectSort(a)
```
## 插入排序

1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
``` Python
# 错误原因：range无法生成逆序列 
'''
def InsertSort(arr):
    for i in range(1,len(arr)):
        maxIndex = i
        for j in range(i-1, 0):
            if arr[j] > arr[i]:
                maxIndex = j
        if maxIndex != i:
            arr[j], arr[maxIndex] = arr[maxIndex], arr[j]
    return arr
'''
def InsertSort(arr):
    for i in range(1,len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] < current: # 排序顺序只改这行 
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr
a = [3, 2, 4, 7, 8, 5, 1, 9, 0, 6]    
InsertSort(a)  
```

## 希尔排序
1. 选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
2. 按增量序列个数 k，对序列进行 k 趟排序；
3. 每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

``` Python
def ShellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp: # 排序顺序只改这行
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr
a = [3, 2, 4, 7, 8, 5, 1, 9, 0, 6]    
ShellSort(a)  
```

## 归并排序
1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
4. 重复步骤 3 直到某一指针达到序列尾；
5. 将另一序列剩下的所有元素直接复制到合并序列尾。

``` Python
def MergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(MergeSort(left), MergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] > right[0]: # 排序顺序只改这行
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result
a = [3, 2, 4, 7, 8, 5, 1, 9, 0, 6]    
ShellSort(a)  
```

## 快速排序
1. 从数列中挑出一个元素，称为 “基准”（pivot）；
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。


``` Python
def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

a = [3, 2, 4, 7, 8, 5, 1, 9, 0, 6]    
quickSort(a) 
```