class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1
        digits.reverse()

        for i, digit in enumerate(digits):

            if digit == 9:
                digits[i] = 0 
            else:
                digits[i] = digit + carry
                carry = 0
                break
        
        if carry:
            digits.append(carry) 

        digits.reverse()
        return digits