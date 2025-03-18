class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        digits = [int(digit) for digit in str(num)]  
        count = 0
   
        for i in range(len(digits) - k + 1):
            included = digits[i : i+k] 
            number = int(''.join(map(str, included)))  
            if number == 0:
              continue
            if num % number == 0:
              count += 1
        return count

        