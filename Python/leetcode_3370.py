class Solution1:
    '''
        3370. Smallest Number With All Set Bits
    '''

    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x


# Example
print(Solution1().smallestNumber(5))
print(Solution1().smallestNumber(10))
print(Solution1().smallestNumber(3))


class Solution2:
    '''
        3370. Smallest Number With All Set Bits
    '''

    def smallestNumber(self, n: int) -> int:
        x = 1
        while (1 << x) - 1 < n:
            x += 1
        return (1 << x) - 1


# Example
print(Solution2().smallestNumber(5))
print(Solution2().smallestNumber(10))
print(Solution2().smallestNumber(3))
