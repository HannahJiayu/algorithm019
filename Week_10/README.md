
### 期末总结
 + 培养好的刷题习惯
    * 判断逻辑不是一气呵成的，而是一个螺旋迭代的过程，随着编写的深入会发现更加优雅且正确的判断顺序
    * 做完题目去国际站看其他高票回答
    * 刻意练习写简洁的代码
    * 使用自顶向下的编程思想
    * 抵制人肉递归，多用机器思维
    * 寻找最近最简方法，拆分重复子问题
    * 多使用数学归纳法思维
    * 利用数、形结合的思想，把图形给大家画出来
    * 优化思维：空间换时间
    * 拆分知识点、刻意练习、 寻求（主动、被动）反馈
    * 利用无毒神掌进行刷题
        - 第一遍：直接看解法：attention! 多解法比较优劣（时、空复杂度），看大牛、背诵、默写好的解法
        - 第二遍：马上脱稿自己写
        - 第三遍：24h 以后、重新做题，看解法熟练度决定是否需要反复练习
        - 第四遍：一周后，重新做题
        - 第五遍：面试前一周进行恢复性训练
+ 典型的数据结构及算法：
    * 数组
    * 链表、*跳表*
        - 跳表中的元素必须是有序的，跳表对标平衡二叉树，二叉搜索树，可以替代平衡树二分查找
    * 栈、单调栈
        - 单调栈要注意入栈和出栈的条件
    * 哈希表、映射、集合，双指针遍历
        - 有时可以帮助减少一层循环
        - 如果hash过程碰撞太多，哈希表会退化成一个链表，查询复杂度会从O(1)退化到O(n)
        - 
    * 队列
    * 优先队列、*双端队列*
    * *树、二叉树、图*
        - 升维可以提升速度，树和图是链表的升维
        - 链表是特殊的树，树是特殊的图
        - 树型很自然，符合人解决问题的常规思路，比如**递归树**，棋盘状态树（棋的决策空间）
        - 对于树型结构，写循环比较麻烦，因为树不是一个线性结构，而写递归会相对比较简单，因为树的定义本身就是按照递归方式定义的。
        - 二叉搜索树：中序遍历是升序遍历
    * 堆：可以迅速找到一堆数中的最大或最小值的数据结构
        - 常用的实现方法有：二叉堆和Fabonacci堆
        - 二叉堆：是一棵完全二叉树；性质1:是一棵完全树；性质2:树中任意节点的值总是>= 其子节点的值
        - 二叉堆一般都通过‘数组’来实现；索引为i的左孩子的索引是2i+1,右孩子2i+2,索引为i的父节点的索引是floor((i-1)/2)
        - 
    * 滑动窗口
    * 分治,回溯（默记模版）
        - problem split, merge
        - 叶子结点到达的标志就是子问题没有了problem is None
        - 回溯利用试错的思想
    * *二分查找*
        - while left <= right:
    * 泛型递归、树型递归
        - 对于树型结构，写循环比较麻烦，因为树不是一个线性结构，而写递归会相对比较简单，因为树的定义本身就是按照递归方式定义的。
    * 深度优先搜索、广度优先搜索
        - 在树、图中寻找特定结点
        - 遍历：每个节点访问一遍且仅访问一遍
        - visited集合很重要
    * 高级搜索
        - 优化：不重复、剪枝（利用一些判断条件来判断）
        - 双向BFS：双向一层一层扩散
        - 启发式搜索（A*, 优先级搜索）
            + 优化搜索方向，思考型搜索，一边搜索，一边思考（在某一个步骤，可不可以加入一些智能？）
            + 估计函数h(n)，返回一个非负实数，评价哪些节点最有希望是我们要找的一个节点
            + 启发式函数是一种告知搜索方向的方法，它提供了一种明智的方法来猜测哪个邻居节点会导向一个目标
            + A*的关键：估价函数如何定义，可以参考一些相似度测量方法
    * 贪心算法
        - 贪心算法是一种在每一步选择中都采取在当前状态下最好或最优的选择，从而希望导致结果是全局最好或最优的算法。
        - 贪心与动态规划的不同在于：贪心不可回退，而动态规划会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。
        - 贪心法可以解决一些最优化问题，如图中的最小生成树，求哈夫曼编码等，但是对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。
        - 一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法
        - 由于贪心法的高效以及其所求得的答案比较接近最优结果，贪心法可以用作辅助算法或者直接解决一些要求结果不特别准确的问题。
        - 问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解，这种子问题最优解称为最优子结构。
    * 动态规划算法（dynamic programming)
        - 不要人肉递归，实在要递归就画递归树
        - 找到最近最简方法，将其拆解成可重复解决的问题
        - 分治+最优子结构
        - 动态规划和递归或分治没有根本上的区别（关键看有无最优的子结构）
        - 共性：找到重复子问题
        - 差异性：最优子结构，中途可以淘汰次优解，也必须淘汰次优解，分治并没有最优解
    * 排序算法
        - 比较类排序：时间复杂度不能够突破O(nlogn)，也被称为非线性时间比较类排序
            + 交换排序（冒泡排序，快速排序），插入排序（简单插入排序，希尔排序），选择排序（简单选择排序，堆排序），归并排序（二路归并排序，多路归并排序）
        - 非比较类排序：不通过比较来决定元素间的相对次序，因此可以突破基于比较类的时间下接，以线性时间运行
            + 计数排序
            + 桶排序
            + 基数排序
        - 初级排序：O(n^2)   
        - 高级排序：O(nlogn) 
    * 位运算
        - 左移、右移
        - 按位或｜， 按位与&， 按位取反～， 按位异或^
        - 异或：相同为0，不同为1
        - x^0=x, x^1s=~x(1s=~0), x^~x=1s, x^x=0
        - 不利用额外变量交换两个整数：c = a^b, a = a^c, b = b^c (c可以表明a和b各个位之间的关系)
        - 指定位置的位运算s
            + 将x右边的n位清零： x & (~0<<n)
            + 获取x的第n位值：(x >>n) & 1
            + 获取x的第n位的幂值：x & (1<<n)
            + 将第n位设置为1: x | (1<<n)
            + 将第n位设置为0: x & ~(1<<n)
            + 将x最高位至第n位清零： x & ((1<<n)-1)
        - 位运算实战要点：
            + 判断奇偶：x & 1 == 1(奇数)， x & 1 == 0(偶数)
            + x>>1 -> x/2
            + 清零最低位的1: x = x & (x-1)
            + 得到最低位的1: x & -x

    * 字典树(Trie)和并查集
        - 字典树的数据结构:存储的很巧妙，节点不存单词又叫单词查找树
        - 字典树的核心思想：空间换时间，利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的
        - 字典树的基本性质
 