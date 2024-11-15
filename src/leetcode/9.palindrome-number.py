# @leet start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        range_ = int(len(x_str)/2)
        for i in range(range_):
            print(x_str[i], x_str[range_-i])
            if x_str[i] != x_str[range_-i]:
                return False
        return True


# @leet end
x = Solution().isPalindrome(121)
print(x)
