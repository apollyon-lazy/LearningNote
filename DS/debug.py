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
# %% 最小路径和
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j != 0:
                grid[0][j] = grid[0][j-1] + grid[0][j]
            if i != 0 and j == 0:
                grid[i][0] = grid[i-1][0] + grid[i][0]
            if i != 0 and j != 0:
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
    return grid[-1][-1]

a=[[1,3,1],[1,5,1],[4,2,1]]
minPathSum(a)

uniquePathsWithObstacles(a)
# %%
def stoneGame(piles):
    p1 = 0 
    p2 = len(piles) - 1
    n1 = 0 # Alice
    n2 = 0 # Bob

    while p2 - p1 >= 3:
        left = piles[p1] - max(piles[p1+1], piles[p2]) # 拿走左边的收益
        right = piles[p2] - max(piles[p2-1], piles[p1]) # 拿走右边的收益
        if left >= right:
            n1 = n1 + piles[p1]
            p1 = p1 + 1
        else:
            n1 = n1 + piles[p2]
            p2 = p2 - 1

        left = piles[p1] - max(piles[p1+1], piles[p2]) # 拿走左边的收益
        right = piles[p2] - max(piles[p2-1], piles[p1]) # 拿走右边的收益
        if left >= right:
            n2 = n2 + piles[p1]
            p1 = p1 + 1
        else:
            n2 = n2 + piles[p2]
            p2 = p2 - 1
                
    n1 = n1 + max(piles[p1], piles[p2])
    n2 = n2 + min(piles[p1], piles[p2])
    if n1 > n2:
        return True
    else:
        return False
a=[6,9,4,3,9,8]
stoneGame(a)
# %%

def minimumTotal(triangle):
    n = len(triangle)
    for i in range(n):
        for j in range(i+1):
            if i != 0 and j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            if i != 0 and j == i:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            if i != 0 and j != i:
                triangle[i][j] = min(triangle[i-1][j-1],triangle[i-1][j]) + triangle[i][j]
    return min(triangle[-1])

a = [[2],[3,4],[6,5,7],[4,1,8,3]]       
minimumTotal(a)
# %%
class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 1 or len(height) == 2:
            return 0

        i = 0
        j = len(height) - 1
        water = 0
        while height[i] == 0:
            i = i + 1
        while height[j] == 0:
            j = j - 1        
        left = height[i]
        right = height[j]


        while j - i >= 2:
            if left <= right: #左墙低
                i = i + 1
                if height[]
# %%
def maximalSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '0':
                matrix[i][j] = 0
            elif i == 0 or j == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
    return max(max(matrix)) ** 2
a = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
maximalSquare(a)

# %%

a = 1
str(a)