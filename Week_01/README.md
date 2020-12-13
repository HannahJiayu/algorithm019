[TOC]
# 学习笔记
+ 本周知识点：数组、链表、跳表（没有遇到具体题目）、栈、队列、优先队列

## 数组
1. 指针是数组的灵魂，指针的类型可以包括单指针、双指针；
同时，利用指针对数组进行遍历时可以利用从前向后、从后向前、夹逼的策略；
2. 栈：与最近相关性有关的内容，优先考虑栈；
其中，单调栈可以解决‘最大’‘最小’的问题；
3. 队列：	和滑动窗口相关的题目利用双端队列来解决；

## 链表

```java

class LinkedList { 
    Node head; // head of list 
  
    /* Linked list Node*/
    class Node { 
        int data; 
        Node next; 
  
        // Constructor to create a new node 
        // Next is by default initialized 
        // as null 
        Node(int d) { data = d; } 
    } 
}
```

## 跳表
时间复杂度：h = log（n) - 1

## 优先队列

##总结
+ 做题思维：有些判断逻辑不是一气呵成的，
而是随着编写会发现更为优雅正确的判断顺序；
+ array 和 list相互补充（如果有完美的数据结构，就不需要array和list了））
+ 掌握较好的知识点：数组、链表、栈
+ 掌握一般的知识点：双端队列
+ 最难理解的知识点：优先队列，滑动窗口

