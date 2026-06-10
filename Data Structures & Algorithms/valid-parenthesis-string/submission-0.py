class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        ast = []

        for i,elem in enumerate(s):
            if elem == "(":
                left.append(i)
            elif elem == "*":
                ast.append(i)
            else:
                if left:
                    left.pop()
                elif ast:
                    ast.pop()
                else:
                    return False

        while left and ast:
            l = left.pop()
            r = ast.pop()
            if r<l:
                return False

        return not left
            

        