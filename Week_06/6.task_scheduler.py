import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_exec = max(freq.values())
        max_count = sum(1 for i in freq.values() if i == max_exec)
        return max(len(tasks), (max_exec - 1)*(n+1) + max_count)