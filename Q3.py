class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        for i in range(len(s)):
            lis.append(s[i])
            if s[i] == ')':
                if i == 0:
                    return False
                elif i > 0 and lis[lis.index(s[i])-1] != '(':
                    return False
                else:
                    lis.pop()
                    lis.pop()
            elif s[i] == ']':
                if i == 0:
                    return False
                elif i > 0 and lis[lis.index(s[i])-1] != '[':
                    return False
                else:
                    lis.pop()
                    lis.pop()
            elif s[i] == '}':
                if i == 0:
                    return False
                elif i > 0 and lis[lis.index(s[i])-1] != '{':
                    return False
                else:
                    lis.pop()
                    lis.pop()
        if lis:
            return False
        else:
            return True

