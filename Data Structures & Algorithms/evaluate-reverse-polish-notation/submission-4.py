class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                # Pop the second operand first!
                right = stack.pop()
                left = stack.pop()
                
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    # Truncate toward zero using int()
                    stack.append(int(left / right))
            else:
                # This handles negative numbers correctly
                stack.append(int(token))
                
        return stack[0]