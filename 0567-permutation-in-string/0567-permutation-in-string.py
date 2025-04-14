class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        freq = defaultdict(int)
        freq2 = defaultdict(int)
        check = False
        for ch in s1:
            freq[ch] +=1
        for i in range(len(s2)- length +1):
            window = s2[i: length+i]
            for j in window:
                freq2[j] += 1
                if freq == freq2:
                    check = True
            freq2.clear()
        return check
        