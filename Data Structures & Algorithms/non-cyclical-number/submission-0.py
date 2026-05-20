class Solution:
    def isHappy(self, n: int) -> bool:

        def compute_next(num:int) -> int:
            total = 0
            while num:      # keep dividing until reach 0
                num, digit = divmod(num, 10)  # floor division and modulo
                total += digit*digit
            return total
            
        seen = set([n])
        while n!=1:
            n = compute_next(n)
            if n in seen:
                return False
            seen.add(n)
            
        return True