class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        noCount = 0

        while (noCount != len(students)):
            if(students[0] != sandwiches[0]):
                student = students.pop(0)
                students.append(student)
                noCount += 1
            else:
                #a student ate
                student = students.pop(0)
                sandwiches.pop(0)
                noCount=0
            

        return noCount
        
            