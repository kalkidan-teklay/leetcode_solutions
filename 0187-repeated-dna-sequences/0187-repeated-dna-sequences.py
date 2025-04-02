class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        repeated = []
        ten = set()
        for i in range(len(s)-k+1):
            new = s[i: i+k]
            if new in ten:
                if new not in repeated:
                    repeated.append(new)
               
            else:
                ten.add(new)
        return repeated
        