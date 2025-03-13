class Solution:
    # O(N) Time | O(1) Space
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join([ch for ch in s if ch.isalnum()])
        return new_string.lower() == new_string[::-1].lower()

class Solution2:
    # Two Pointer approach
    # O(N) Time | O(1) Space
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

s = "A man, a plan, a canal: Panama"
sol = Solution2()
print(sol.isPalindrome(s))