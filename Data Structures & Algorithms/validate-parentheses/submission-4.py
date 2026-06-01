class Solution:
    def isValid(self, s: str) -> bool:

        openP = {"(":")","[":"]","{":"}"}

        stack = []
        for par in s:
            if par in openP:
                stack.append(par)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if openP[opening] != par:
                    return False

        return len(stack) == 0

            

        