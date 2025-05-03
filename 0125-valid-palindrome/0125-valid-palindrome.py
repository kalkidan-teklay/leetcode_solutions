class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        if len(s) == 1:
            return True
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        clean = cleaned_string.lower()
        if len(clean) == 0:
            return True
        left, right = 0, len(clean) -1
        for i in range(len(clean)):
            while left < right:
                if clean[left] == clean[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        