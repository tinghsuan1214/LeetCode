'''Module providing a function printing python version.'''
from typing import List

class Solution:
    '''
        2125. Number of Laser Beams in a Bank
    '''
    def numberOfBeams(self, bank: List[str]) -> int:
        '''Count laser beams between devices in different rows with no devices in between.'''
        prev_count = 0
        total_beams = 0

        for row in bank:
            current_count = row.count('1')
            # print(f"Row: {row}, Security Devices: {current_count}")
            if current_count > 0:
                total_beams += prev_count * current_count
                # print(f"Total Beams: {total_beams}")
                prev_count = current_count
                # print(f"Previous Count: {prev_count}")

        return total_beams

# Example
# print(Solution().numberOfBeams(["011001", "000000", "010100", "001000"]))
# print(Solution().numberOfBeams(["000", "111", "000"]))
