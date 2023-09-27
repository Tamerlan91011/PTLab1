


class StudentCalculator:
    def __init__(self, studentsList: list):
        self.studentsList = studentsList
        
    def getBestStudentsCount(self) -> int:
        bestStudentsCount: int = 0
        for student in self.studentsList:
            bestStudentsCount = bestStudentsCount+1 if self.isBestStudent(student=student) else bestStudentsCount
        return bestStudentsCount
                
    def isBestStudent(self, student: dict) -> bool:
        (_, subjects), = student.items()
        
        for i in subjects:
            if subjects[i] < 90:
                return False
        return True
        