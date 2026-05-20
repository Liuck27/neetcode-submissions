class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for s in strs:
            res.append(str(len(s))+"#"+s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        i=0
        while i<len(s):

            length = ""
            start = i

            for char in s[start:]:
                if char.isnumeric():
                    length += char
                    i +=1
                elif char == "#":
                    i +=1
                    res.append(s[i:i+int(length)])
                    i += int(length)
                    break
                else:
                    continue

                
            

        return res



