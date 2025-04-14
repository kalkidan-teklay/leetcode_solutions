class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        freq2 = defaultdict(int)
        for ch in s1:
            freq[ch] +=1
        for i in range(len(s2)- len(s1) +1):
            window = s2[i: len(s1)+i]
            for j in window:
                freq2[j] += 1
                if freq == freq2:
                    return True
            freq2.clear()
        return False
        