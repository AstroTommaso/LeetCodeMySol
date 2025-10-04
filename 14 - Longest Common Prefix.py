from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Prendiamo la prima parola come riferimento
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Confrontiamo questo carattere con tutte le altre stringhe
            for s in strs[1:]:
                # Se la stringa è troppo corta o la lettera è diversa → fermati
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        
        # Se arriviamo alla fine, tutta la prima parola è prefisso comune
        return strs[0]
