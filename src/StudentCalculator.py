class StudentCalculator:
    def __init__(self, studentsList: list):
        self.studentsList = studentsList

    def getBestStudentsCount(self) -> int:
        bestStudentsCount = int(0)
        for student in self.studentsList:
            if self.isBestStudent(student=student):
                bestStudentsCount += 1
        return bestStudentsCount

    def isBestStudent(self, student: dict) -> bool:
        (_, subjects), = student.items()

        for i in subjects:
            if subjects[i] < 90:
                return False
        return True
