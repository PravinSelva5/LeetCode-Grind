class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unableToEat = 0

        while unableToEat < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                unableToEat = 0
            else:
                unableToEat += 1
                students.append(students[0])
                students.pop(0)
        
        return unableToEat