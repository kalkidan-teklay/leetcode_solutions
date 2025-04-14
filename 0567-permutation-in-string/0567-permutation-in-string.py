from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for ch in s1:
            freq1[ch] += 1

        for i in range(len(s2)):
            freq2[s2[i]] += 1

            # remove the leftmost char when window size exceeds s1
            if i >= len(s1):
                left_char = s2[i - len(s1)]
                freq2[left_char] -= 1
                if freq2[left_char] == 0:
                    del freq2[left_char]

            if freq1 == freq2:
                return True

        return False

        