def write_to_diary():
    with open("diary.txt", "a") as file:
        entry = input("Write your entry: ")
        file.write(entry + "\n")
        print("Entry saved successfully!")
        
def read_from_diary():
    try:
        with open("diary.txt", "r") as file:
            print("Your entries:")
            print(file.read())
            print("===========")
    except FileNotFoundError:
        print("No entries found.")

while True:
    print("=========== Personal Diary ===========")
    print("1. Write to diary")
    print("2. Read from diary")
    print("3. Exit")
    print("======================================")
    
    choice = input("Enter your choice: ")
    print("===========")
        
    if choice == "1":
        write_to_diary()
    elif choice == "2":
        read_from_diary()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
    
