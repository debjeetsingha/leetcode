"""
Link: https://leetcode.com/problems/baseball-game/
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for x in (operations):
            if x =="C":
                record.pop()
            elif x =="+":
                record.append(record[-2] + record[-1])
            elif x =="D":
                record.append(2*int(record[-1]))
            else:
                record.append(int(x))
        return sum(record)