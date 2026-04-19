class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        pairs = {"]":"[", "}":"{", ")":"("}

        stack = []
        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            if char == "]" or char == ")" or char == "}":
                if not stack:
                    return False
                value = stack.pop()
                if value == pairs[char]:
                    continue
                else:
                    return False
        if stack:
            return False
        return True

        