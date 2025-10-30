'''Module providing a function printing python version.'''
from typing import List


class Solution1:
    '''
        1526. Minimum Number of Increments on Subarrays to Form a Target Array
    '''

    def minNumberOperations(self, target: List[int]) -> int:
        '''
        Calculate the minimum number of operations to form the target array.
        '''
        n = len(target)
        operations = target[0]
        for i in range(1, n):
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        return operations


# Example
print(Solution1().minNumberOperations([1, 2, 3, 2, 1]))
print(Solution1().minNumberOperations([3, 1, 1, 2]))
print(Solution1().minNumberOperations([3, 1, 5, 4, 2]))


class Solution2:
    '''
        1526. Minimum Number of Increments on Subarrays to Form a Target Array
    '''

    def minNumberOperations(self, target: List[int]) -> int:
        '''
        Calculate the minimum number of operations to form the target array.
        '''
        prev = ans = 0
        for i in target:
            if i >= prev:
                ans += i - prev
            prev = i
        return ans


# Example
print(Solution2().minNumberOperations([1, 2, 3, 2, 1]))
print(Solution2().minNumberOperations([3, 1, 1, 2]))
print(Solution2().minNumberOperations([3, 1, 5, 4, 2]))
