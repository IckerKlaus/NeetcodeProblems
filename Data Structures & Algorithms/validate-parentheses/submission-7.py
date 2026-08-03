class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Time: O(n)
        Space: O(n)
        '''
        stack = []
        isValid = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in isValid:
                if stack and stack[-1] == isValid[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False