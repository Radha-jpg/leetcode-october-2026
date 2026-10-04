class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '([{':
                st.append(c)
            elif not st or st.pop() != pairs[c]:
                return False

        return not st