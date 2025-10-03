class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # parto dall'ultima cifra e vado verso sinistra
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # non serve altro, ritorno subito
            digits[i] = 0  # se è 9 diventa 0 e passo al prossimo ciclo

        # se sono usciti tutti 9 (es. [9,9,9]) allora aggiungo un 1 davanti
        digits.insert(0, 1)
        return digits
