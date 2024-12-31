class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()

    def calculate_overall_average(self):
        total_grades = 0
        total_students = len(self.students)
        for student in self.students:
            total_grades += sum(student.grades)
        return total_grades / total_students if total_students > 0 else 0