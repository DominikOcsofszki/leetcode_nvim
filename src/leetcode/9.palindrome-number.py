# @leet start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        len_x = len(x_str)
        print(len_x)
        if len_x in (1, 0):
            return True
        start = 0
        end = len_x - 1
        while start < end:
            if start == end:
                return True
            if x_str[start] != x_str[end]:
                return False
            start += 1
            end -= 1

    return True


def test_is_palindrome():
    s = Solution()
    tests = [[121, True], [-121, False], [10, False]]
    for test in tests:
        assert s.isPalindrome(test[0]) == test[1], test


# test_isPalindrome()

# @leet end
