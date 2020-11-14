import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.Counter(nums)
        heap = []
        res = []
        i = 0
        for item in hashmap:
            heapq.heappush(heap, (-hashmap[item], item))
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
        

