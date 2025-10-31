from typing import List


class Solution1:  # Approach 1: Simulation
    '''
        3354. Make Array Elements Equal to Zero
    '''

    def countValidSelections(self, nums: List[int]) -> int:
        '''Count the number of all valid starting choices.'''
        count = 0
        nonZeros = sum(1 for x in nums if x > 0)
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                if self.isValid(nums, nonZeros, i, -1):
                    count += 1
                if self.isValid(nums, nonZeros, i, 1):
                    count += 1
        return count

    def isValid(self, nums, nonZeros, start, direction):
        '''
        Simulates a process starting from a specific starting point and direction 
        to determine whether the entire array can be returned to zero.
        '''
        temp = nums[:]
        curr = start
        while nonZeros > 0 and 0 <= curr < len(nums):
            if temp[curr] > 0:
                temp[curr] -= 1
                direction *= -1
                if temp[curr] == 0:
                    nonZeros -= 1
            curr += direction
        return nonZeros == 0


# Example
print(Solution1().countValidSelections([1, 0, 2, 0, 3]))
print(Solution1().countValidSelections([2, 3, 4, 0, 4, 1, 0]))


class Solution2:  # Approach 2: Prefix Sum
    '''
        3354. Make Array Elements Equal to Zero
    '''

    def countValidSelections(self, nums: List[int]) -> int:
        '''
        Count valid starting positions and directions using prefix sums.
        For each zero, compare the left and right cumulative sums to check
        if the array can be reduced to all zeros.
        '''
        n = len(nums)
        ans = 0
        s = sum(nums)
        left, right = 0, s
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
        return ans


# Example
print(Solution2().countValidSelections([1, 0, 2, 0, 3]))
print(Solution2().countValidSelections([2, 3, 4, 0, 4, 1, 0]))


class Solution3:  # Approach 3: Optimized Prefix Sum
    '''
        3354. Make Array Elements Equal to Zero
    '''

    def countValidSelections(self, nums: List[int]) -> int:
        '''
        Optimized prefix sum approach:
        - If left and right sums are equal → both directions valid (+2)
        - If they differ by 1 → one direction valid (+1)
        - Otherwise → invalid (+0)
        '''
        n = len(nums)
        t = sum(nums)
        s = 0
        ans = 0
        for i in range(n):
            ts = t - s
            if nums[i] == 0:
                if ts == s:
                    ans += 2
                elif abs(ts-s) == 1:
                    ans += 1
            s += nums[i]
        return ans


# Example
print(Solution3().countValidSelections([1, 0, 2, 0, 3]))
print(Solution3().countValidSelections([2, 3, 4, 0, 4, 1, 0]))
