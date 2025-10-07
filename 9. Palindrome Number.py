class Solution:
    def isPalindrome(self, x: int) -> bool:
        # I numeri negativi non possono essere palindromi
        if x < 0:
            return False
        
        # Converto in stringa e confronto con la stringa invertita
        s = str(x)
        return s == s[::-1]
