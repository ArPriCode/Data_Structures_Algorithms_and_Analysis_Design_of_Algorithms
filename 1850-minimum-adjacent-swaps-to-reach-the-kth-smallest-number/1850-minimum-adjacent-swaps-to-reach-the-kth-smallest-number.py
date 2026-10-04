class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        a = list(num)
        for _ in range(k):
            i = len(a) - 2

            while a[i] >= a[i + 1]:
                i -= 1

            j = len(a) - 1

            while a[j] <= a[i]:
                j -= 1

            a[i], a[j] = a[j], a[i]

            left = i + 1
            right = len(a) - 1

            while left < right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1

        target = a
        original = list(num)
        ans = 0

        for i in range(len(original)):
            j = i

            while original[j] != target[i]:
                j += 1

            while j > i:
                original[j], original[j - 1] = original[j - 1], original[j]
                j -= 1
                ans += 1

        return ans