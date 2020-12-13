[TOC]
# 学习笔记
## 递归思想 归去来兮
>1.结点的定义，包括数据结构及算法特性的定义；
>
2.重复性（自相似性）;
>
3.递归和循环两者的汇编语言类似;


+ 树递归

+ 泛型递归
+ 递归代码模版

```python
def recursion(level, param1, param2, ...): 
    #1 recursion terminator 
    if level > MAX_LEVEL: 
       process_result 
       return 

    #2 process logic in current level 
    process(level, data...) 

    #3 drill down 
    self.recursion(level + 1, p1, ...) 

    #4 reverse the current level status if needed
```
### 思维要点
>1. 不要人肉递归

>2. **找最近重复子问题**

>3. 数学归纳法的思维
### 习题
#### 1. 生成括号
要点：1.利用参数传递左、右括号的数量；2.if-else的drill down；
#### 2. 翻转二叉树
要点：依次翻转左、右结点，翻转完在返回根
#### 3. 验证二叉搜索树
要点：节点的左子树小于节点，右子树小于节点，所有的左子树和右子树自身也是二叉搜索树；
>递归方法：自顶向下，父节点的值依次是左、右结点的上、下界,利用父节点来约束子节点
#### 4. 二叉树的最小深度
要点：找到最小重复，将3个节点或两个节点的情况想清楚，然后写出递归
#### 5.二叉树的序列化与反序列化
要点：要将一层的逻辑都处理完再做其他的事情；
注意：字符串和int的转化可能会导致判等出现问题；利用，.join(res)来避免；
#### 6.组合
+ 如果解决一个问题有多个步骤，每一个步骤有多种方法，
题目又要我们找出所有的方法，可以使用回溯算法；
+ 注意优化（剪枝）
+ 画搜索二叉树
```python
Method1:
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        if k == 0 or n < k:
            return []
        res = []
        def backtrace(nums, path, start):
            path.append(nums[start])
            if len(path) == k:
                res.append(path)
                return
            else:
                for i in range(start+1, n):
                    backtrace(nums, path[:], i)
        for i in range(0, n-k+1):
            backtrace(nums, [], i)
        return res
Method2:省空间
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k ==0 or n < k:
            return []
        nums = [i for i in range(1, n+1)]
        res = []
        def dfs(cur, path):
            if len(path) == k:
                res.append(path[:])
                return
            if cur == n:
                return
            path.append(nums[cur])
            dfs(cur + 1, path)
            path.pop()
            dfs(cur + 1, path)
        dfs(0, [])
        return res
```

## 分治、回溯的实现和特性
###分治
divide -> conquer -> merge  
**关键点**：如何拆分子问题（依靠经验）；如何合并子问题的结果

1. terminator  
2. process（split your big problem)  
3. subproblem,merge
4. reverse status

###分治习题
####1. 最大子序和
```python
Method1:DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
Method2:分治
```
###回溯
试错：不断在每一层上进行尝试；
归去来兮的感觉

```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
    print_result 
    return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
    
  # revert the current level states
```
![递归状态树](/Users/jiayuhan/Documents/algorithm019/Week_03/recursion_tree.png "图片title")
####1.Pow（x,n)
要点：注意n<0时的处理；分治+递归状态树  
思考🤔：如何利用分治+迭代
####2.二叉树的最近祖先
要点：这是一道树相关的问题，与树相关可以利用递归解决，因此要找到如何定义子问题  
公共祖先的定义：子树包含p，q结点  
首先定义出口条件，然后从上至下判断当前结点是否可能是公共祖先；  
判断逻辑：分别递归左右子树，寻找p，q结点，根据寻找结果设计判断逻辑
>如果左、右子树返回的结果均为非空，那么root为common ancestor
>如果左子树为空，那么访问右子树时，第一个p，q中的结点便是anncestor
#### 3.组合
+ 如果解决一个问题有多个步骤，每一个步骤有多种方法，
题目又要我们找出所有的方法，可以使用回溯算法；
+ 注意优化（剪枝）
+ 画搜索二叉树
+ 练一下后序清理的回溯
ps:调用递归时，可以将父节点作为参数传入

####4.全排列
+ 状态变量
>1.递归到几层depth，选了哪些数path，布尔数组used

```python
Method1:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        visited = [True] * len(nums)
        def dfs(nums, depth, path, visited):
            if depth == len(nums):
                res.append(path[:])
                return
            else:
                for i in range(len(nums)):
                    if visited[i]:
                        path.append(nums[i])
                        visited[i] = False
                        dfs(nums, depth + 1, path, visited)
                        visited[i] = True
                        path.pop()
        dfs(nums, 0, [], visited)
        return res
Method2:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        def backtrace(first = 0):
            if first == len(nums):
                res.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrace(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrace()
        return res

```








