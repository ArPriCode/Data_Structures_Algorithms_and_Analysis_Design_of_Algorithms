class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        pq = []
        n, m = len(nums1), len(nums2)
        for i in range(min(k, n)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
        ans = []
        while pq and k > 0:
            k -= 1
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < m:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans