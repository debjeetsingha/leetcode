"""
Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""

from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)
        counter = 0
        while (students_queue and sandwiches_queue) and counter<len(students_queue):
            if students_queue[0]==sandwiches_queue[0]:
                students_queue.popleft()
                sandwiches_queue.popleft()
                counter=0
            else:
                counter+=1
                students_queue.append(students_queue.popleft())

        return len(students_queue)

