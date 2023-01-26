# %% 最大子数组
def maxSubArray(nums):
    size = len(nums)
    if size == 0:
        return 0
    dp = [0 for _ in range(size)]

    dp[0] = nums[0]
    for i in range(1, size):
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1] + nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)

a=[2,-3,1,3,-3,2,2,1]
maxSubArray(a)
# %% 杨辉三角 II
def getRow(rowIndex: int):
    lastRow =list()
    for i in range(0, rowIndex):
        Row = list() 
        for j in range(0, i+1): 
            if (j == 0) or (j == i):
                Row.append(1)
            else: 
                Row.append(lastRow[j]+lastRow[j-1])
        lastRow = Row
    return Row
getRow(3)
# %% 股票问题 I
def maxProfit(prices):
    d = [0 for _ in range(len(prices))]
    for i in range(1,len(prices)):
            d[i] = d[i-1] + prices[i] - prices[i-1]
    return max(d)
a = [7,1,5,3,6,4]
maxProfit(a)
a.index(max(a))
a.index(min(a))
# %% 跳跃游戏 II
def jump(nums):
    lastPoint = 0
    nowPoint = nums[0]
    step = 1

    temp = 0
    while nowPoint < len(nums) - 1:
        Max = 0

        for i in range(lastPoint+1, nowPoint+1):
            if nums[i] + i > Max:
                Max = nums[i] + i
                temp = i 
        lastPoint = temp
        nowPoint = temp + nums[temp]
        step = step + 1

    return step

nums = [2,3,1,1,4] 
jump(nums)              
# %% 跳跃游戏 I
def canJump(nums):
    if len(nums) == 1:
        return True
    else:
        end = nums[0]

        while end < len(nums) - 1:

            flag = False
            if not nums[end]: 
                for i in range(1, end):
                    if nums[i] + i > nums[end] + end:
                        flag = True
                        temp = nums[i] + i 
                if not flag:
                    return False
                else:
                    end = temp 
            else:
                end = nums[end] + end 
                
        else:
            return True
nums = [2,5,0,0] 
canJump(nums)    
# %%
a = [1,2,3,4]
b = a[1] + a[1]
a[1] = a[a[1]] + a[1]
a 