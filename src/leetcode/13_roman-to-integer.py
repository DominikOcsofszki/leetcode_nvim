import pytest
# @leet start


class Solution:
    def romanToInt(self, s: str) -> int:
        return 1


@pytest.mark.parametrize("s,output", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
])
def test_romanToInt(s: str, output) -> int:
    assert s == output
