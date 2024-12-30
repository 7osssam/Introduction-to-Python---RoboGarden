import os

def read_grades(file_path):
    grades = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                subject, grade = line.strip().split(',')
                grades[subject] = float(grade)
    except FileNotFoundError:
        print(f"No existing grades file found at {file_path}. Starting fresh.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return grades

def write_grades(file_path, grades):
    try:
        with open(file_path, 'w') as file:
            for subject, grade in grades.items():
                file.write(f"{subject},{grade}\n")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def main():
    # file_path = '/Users/hossam.taha/Documents/Introduction-to-Python---RoboGarden/06 - Files IO and Exceptions/02 - Student Grade Tracker/grades.txt'
    file_path = os.path.join(os.path.dirname(__file__), 'grades.txt')
    grades = read_grades(file_path)
    
    while True:
        print("=========== Student Grade Tracker ===========")
        print("\n1. Add/Update Grade")
        print("2. Calculate Average Grade")
        print("3. Exit")
        print("=============================================")
        choice = input("Enter your choice: ")
        
        print("===========")
        if choice == '1':
            subject = input("Enter the subject: ")
            try:
                grade = float(input("Enter the grade: "))
                grades[subject] = grade
                write_grades(file_path, grades)
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")
        elif choice == '2':
            average = calculate_average(grades)
            print(f"Average grade: {average:.2f}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
        print("===========")

if __name__ == "__main__":
    main()