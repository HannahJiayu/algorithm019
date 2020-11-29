#学习笔记
##深度优先搜索、广度优先搜索
本质上是递归、写循环

+ 遍历搜索--深度优先搜索 (递归模版，若不用递归，可以手动维护一个栈)
```python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
        # already visited 
        return 

    visited.add(node) 

    # process current node here. 
    ...
    for next_node in node.children(): 
        if next_node not in visited: 
            dfs(next_node, visited)
```
+ 遍历搜索--广度优先搜索（按层，利用队列）  
```python
def BFS(graph, start, end):
    visited = set()
    queue = [] 
    queue.append([start]) 
    while queue: 
        node = queue.pop() 
        visited.add(node)
        process(node) 
        nodes = generate_related_nodes(node) 
        queue.push(nodes)
    # other processing work 

```
* 优先级优先搜索

###实战题目
#### 1.二叉树的层序遍历
Method1:BFS  
>如何标识每一层的结束？记住每一层结点的数量

Method2:DFS
#### 2.最小基因变化
#### 3.括号生成
利用深度优先搜索的方式，每次有可能生成左括号和右括号，对应到递归的状态树里面，因此是一种深度优先搜索的方式；
#### 4.岛屿数量
由于问题存在，相邻的相邻，子子孙孙无穷尽的情况，因此要用dfs的方式进行处理


#### 5.单词接龙？？
**最短转化序列**-->广度优先搜索  
优化建图

##贪心算法
**贪心vs回溯vs动态规划**
贪心：当下做局部最优判断  
回溯：能够回退  
动态规划：最优判断+回溯
贪心法比较高效，贪心法一般不能得到我们所要求的答案，因此贪心法也可以用作辅助算法或者直接解决一些结果不特别准确的问题。  
###实战题目（柠檬水找零、买卖股票、分发饼干）
####模拟机器人
要点：direction 不是两个数，而是一个状态转换表！！
```python
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
```
####跳跃游戏
思路：**从后往前**进行贪心，从后向前判断每个结点是否可以到达

##二分查找
**前提**
1. 目标函数单调性（有序非常重要）  
2. 存在上下界  
3. 能够通过索引访问  

```python
left, right = 0, len(array) - 1 
while left <= right: 
      mid = (left + right) / 2 
      if array[mid] == target: 
            # find the target!! 
            break or return result 
      elif array[mid] < target: 
            left = mid + 1 
      else: 
            right = mid - 1
```
###习题
####平方根
1.二分查找
2.牛顿迭代法
##本周心得
1.‘搜索’是在可能的子空间中寻找答案，从这个角度就理解了“暴力搜索”为什么叫“暴力搜索”  

