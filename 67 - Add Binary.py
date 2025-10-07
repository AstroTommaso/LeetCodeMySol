class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Converto da stringa base 2 → intero in base 10
        a = int(a, 2)
        b = int(b, 2)

        # Somma in decimale
        s = a + b

        # Riconverto il risultato in base 2
        return self.to_base2(s)

    def to_base2(self, n: int) -> str:
        if n == 0:
            return "0"
        cifre = []
        while n > 0:
            cifre.append(str(n % 2))
            n //= 2
        return "".join(reversed(cifre))


# esempio d’uso
sol = Solution()
print(sol.addBinary("101", "111"))  # ➝ "1100"
