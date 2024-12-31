from student import Student
from database import StudentDatabase

def get_user_input():
    while True:
        print("=========== Student Database System ===========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Overall Average")
        print("4. Exit")
        print("===============================================")
        choice = input("Choose an option: ")
        print("===========")
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice. Please try again.")
            print("===========")
        
def execute_choice(choice, student_db):
    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grades = [float(grade) for grade in input("Enter student grades (comma-separated): ").split(",")]
        student = Student(name, age, grades)
        student_db.add_student(student)
        print(f"Student '{name}' added.")
    elif choice == "2":
        student_db.display_all_students()
    elif choice == "3":
        overall_average = student_db.calculate_overall_average()
        print(f"Overall Average Grade: {overall_average:.2f}")
        

def main():
    # Initialize the student database
    student_db = StudentDatabase()

    while True:
        choice = get_user_input()
        if choice == "4":
            break
        execute_choice(choice, student_db)
    

if __name__ == "__main__":
    main()