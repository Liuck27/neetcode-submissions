class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        result = []
        for digit in reversed(digits):

            res = (digit + carry) % 10 
            carry = (digit + carry) // 10 

            result.append(res)
        
        if carry:
            result.append(carry) 

        return result[::-1]