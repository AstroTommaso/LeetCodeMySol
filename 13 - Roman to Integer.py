class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        prev_value = 0
        
        # Scorro da destra verso sinistra
        for char in reversed(s):
            value = values[char]
            if value < prev_value:
                total -= value   # Caso di sottrazione (es. IV)
            else:
                total += value   # Caso normale
            prev_value = value
        
        return total
