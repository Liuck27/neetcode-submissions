class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in bracket_map:
                if stack:
                    popped = stack.pop()
                else:
                    popped = 'd'
                if bracket_map[char] != popped:
                    return False
            else:
                stack.append(char)
                
        return not stack
