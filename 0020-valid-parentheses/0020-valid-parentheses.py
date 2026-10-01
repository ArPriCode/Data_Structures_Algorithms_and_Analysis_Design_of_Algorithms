class Solution(object):
    def isValid(self, s):
        close_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []
        for i in s:
            if i in close_to_open:
                if not stack:
                    return False
                top = stack.pop()
                if close_to_open[i] != top:
                    return False
            else:
                stack.append(i)

        if stack:
            return False
        else:
            return True