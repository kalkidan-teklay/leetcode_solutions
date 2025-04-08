from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        for ch in freq:
            if freq[ch] < k:
                substrings = s.split(ch)
                return max(self.longestSubstring(sub, k) for sub in substrings)

   
        return len(s)
