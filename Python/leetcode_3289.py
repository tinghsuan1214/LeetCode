from typing import List


class Solution:
    '''
        3289. The Two Sneaky Numbers of Digitville
    '''

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] == 2:
                res.append(x)

        return res


# Example
print(Solution().getSneakyNumbers([0, 1, 1, 0]))
print(Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2]))
print(Solution().getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
