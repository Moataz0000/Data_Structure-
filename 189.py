from typing import List



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) -1, -1, -1):

            if digits[i] + 1 != 10: # if the last num is not 10 just adding one and return the list
                digits[i] += 1
                return digits
            
            digits[i] = 0

            if i == 0:
                return [1] + digits

obj = Solution()
print(obj.plusOne(digits=[9]))