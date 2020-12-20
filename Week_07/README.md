[TOC]
# 第7周 学习笔记

## 7.1 字典树（Trie）
    1. 字典树的数据结构
    2. 字典树的核心思想
        减少无谓的字符串比较
    3. 字典树的基本性质
        1. 结点本身不存完整单词，可以存频次之类的信息；
        2. 从根到某一结点，将路径上的字符连接起来，作为该结点对应的字符串；
        3. 每个结点的所有子结点路径代表的字符都不相同。

## 7.2 并查集
    并查集是一种数据结构，针对组团和配对的问题，通俗理解：‘你和他是不是朋友’！ 
1. 基本操作  
    makeset：建立一个新的并查集，其中包含s个单元素集合  
    unionset：把元素x和元素y所在的集合合并，要求x和y所在的集合不相交，如果相交则不合并  
    find：找到元素x所在集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只要将它们各自的代表比较一下就可以了  

2. 关键点  
    领头元素

## 7.3 高级搜索
+ 回顾初级搜索：
    1. 朴素搜索
    2. 优化方式：不重复（fibonacci），剪枝（生成括号问题）
    3. 搜索方向：DFS，BFS，双向搜索、启发式搜索（优先级搜索）
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

def DFS(self, tree): #非递归

    if tree.root is None: 
        return [] 

    visited, stack = [], [tree.root]

    while stack: 
        node = stack.pop() 
        visited.add(node)

        process (node) 
        nodes = generate_related_nodes(node) 
        stack.push(nodes) 

    # other processing work 
    ...

# Python
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
    ...
```
+ 剪枝
    1. 回溯  
        回溯是一种分治试错的过程，当前层不满足条件时可以取消上一步或上几步的选择
    2. 可以将‘剪枝’看作是条件判断，比如N皇后问题，pie,na 被占了之后，停止搜索

+ 高级搜索的优化方向
    * 尽早结束没必要的搜索、剪枝
    * 增加搜索的方向  

## 7.4 启发式搜索（A* 算法）
1. 估价函数（又叫启发式函数）
    1. 利用启发式函数可以告知搜索方向

## 7.5 平衡二叉树
1. 平衡二叉树的种类
2. 近似平衡二叉树
    加入了取舍tradeoff
    + 红黑树：高度差小于两倍

## 7.6 实战例题
### 1. 实现 Trie (前缀树) （亚马逊、微软、谷歌在半年内面试中考过）

### 2. 单词接龙（亚马逊、Facebook、谷歌在半年内面试中考过）

### 3. 二进制矩阵中的最短路径（亚马逊、字节跳动、Facebook 在半年内面试中考过）
+ 技术关键：8连通图，8个方向坐标

### 4. 单词搜索（亚马逊、微软、苹果在半年内面试中考过）
+ 解题思路：4连通图




