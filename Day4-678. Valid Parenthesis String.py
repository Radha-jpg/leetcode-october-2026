class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for char in s:
            if char == "(":
                low += 1
                high += 1

            elif char == ")":
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # Minimum number of open brackets cannot be negative.
            if low < 0:
                low = 0

            # Too many closing brackets are unavoidable.
            if high < 0:
                return False

        return low == 0