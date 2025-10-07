class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n >= target:   # se trovo un numero >= target
                return i      # qui è la posizione giusta
        return len(nums)      # altrimenti va in fondo
# --- prove manuali ---
s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))  # 2
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))      