class Solution:
    def twoSum(self, nums, target):
        seen = {}  # dizionario: numero -> indice già visto
        for i, num in enumerate(nums):  # scorriamo con indice e valore
            need = target - num         # calcolo quanto mi serve
            if need in seen:            # se l'ho già visto prima
                return [seen[need], i]  # restituisco i due indici
            seen[num] = i               # salvo il numero con il suo indice
# --- prove manuali ---
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(s.twoSum([3, 2, 4], 6))       # [1, 2]
print(s.twoSum([3, 3], 6))          # [0, 1]