# 第九周 学习笔记

## 9.1 高级动态规划
    复杂度来源：1. 状态拥有更多维度；2. 状态方程更加复杂
    本质：内功，逻辑抽象思维，数学能力

## 9.2 字符串算法

```python
class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0 : return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
```
## 实战例题

### 高级动态规划
1. [爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）](https://leetcode-cn.com/problems/climbing-stairs/)
2. [使用最小花费爬楼梯（亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)
3. [编辑距离（字节跳动、亚马逊、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/edit-distance/)
4. [最长上升子序列（字节跳动、亚马逊、微软在半年内面试中考过）](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
5. [解码方法（Facebook、亚马逊、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/decode-ways/)
6. [最长有效括号（华为、亚马逊、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/longest-valid-parentheses/)
7. [最大矩形（谷歌、微软、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/maximal-rectangle/)
8. [不同的子序列（MathWorks 在半年内面试中考过）](https://leetcode-cn.com/problems/distinct-subsequences/)
9. [赛车（谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/race-car/)

### 字符串基础问题
1. [转换成小写字母（谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/to-lower-case/)
2. [最后一个单词的长度（苹果、谷歌、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/length-of-last-word/)
3. [宝石与石头（亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/jewels-and-stones/)
4. [字符串中的第一个唯一字符（亚马逊、微软、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)
5. [字符串转换整数 (atoi) （亚马逊、微软、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/string-to-integer-atoi/) 

### 字符串操作问题
1. [最长公共前缀（亚马逊、谷歌、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/longest-common-prefix/description/)
2. [反转字符串（亚马逊、谷歌、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-string/)
3. [反转字符串 II （亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-string-ii/)
4. [翻转字符串里的单词（微软、字节跳动、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-words-in-a-string/)
5. [反转字符串中的单词 III （微软、字节跳动、华为在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)
6. [仅仅反转字母（字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-only-letters/)  

###异位词问题
1. [有效的字母异位词（Facebook、亚马逊、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/valid-anagram/)
2. [字母异位词分组（亚马逊在半年内面试中常考）](https://leetcode-cn.com/problems/group-anagrams/)
3. [找到字符串中所有字母异位词（Facebook 在半年内面试中常考）](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

###回文串问题
1. [验证回文串（Facebook 在半年内面试中常考）](https://leetcode-cn.com/problems/valid-palindrome/)
2. [验证回文字符串 Ⅱ（Facebook 在半年内面试中常考）](https://leetcode-cn.com/problems/valid-palindrome-ii/)
3. [最长回文子串（亚马逊、字节跳动、华为在半年内面试中常考）](https://leetcode-cn.com/problems/longest-palindromic-substring/)

###最长子串、子序列问题
1. [最长公共子序列（亚马逊、字节跳动、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/longest-common-subsequence/)
2. [编辑距离（亚马逊、字节跳动、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/edit-distance/)
3. [最长回文子串（亚马逊、华为、字节跳动在半年内面试常考）](https://leetcode-cn.com/problems/longest-palindromic-substring/)

###字符串+DP问题
1. [正则表达式匹配（Facebook、微软、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/regular-expression-matching/),[题解](https://leetcode-cn.com/problems/regular-expression-matching/solution/ji-yu-guan-fang-ti-jie-gen-xiang-xi-de-jiang-jie-b/)
2. [通配符匹配（Facebook、微软、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/wildcard-matching/)
3. [不同的子序列（MathWorks 在半年内面试中考过）](https://leetcode-cn.com/problems/distinct-subsequences/)

## 参考链接
1. [Boyer-Moore 算法](https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html)
2. [Sunday 算法](https://blog.csdn.net/u012505432/article/details/52210975)
3. [字符串匹配暴力法代码示例](https://shimo.im/docs/8G0aJqNL86wWrPUE/read)
4. [Rabin-Karp 代码示例](https://shimo.im/docs/1wnsM7eaZ6Ab9j9M/read)
5. [KMP 字符串匹配算法视频](https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171)
6. [字符串匹配的 KMP 算法](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)
7. [不可变字符串](https://lemire.me/blog/2017/07/07/are-your-strings-immutable/)
8. [Atoi 代码示例](https://shimo.im/docs/5kykuLmt7a4DdjSP/read)
9. []()
10. []()
11. []()
12. []()
13. []()
14. []()
15. []()