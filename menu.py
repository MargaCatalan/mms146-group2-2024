# Task Code: Menu_1
"Menus"
def Main_Menu():                      
    while True:
        print("\n\n----------------------  Group 2’s Grade 10 Exam Reviewer  ---------------------\n\n")
        print("Hi, {}!".format(user_name.title()))
        print("What do you wish to do?")
        print("  [1] Review a Subject")
        print("  [2] View My Previous Exam Performance Reports")
        print("  [0] None")

        try:
            choice = int(input('\n'"Please choose an option: "))
            
            if choice == 1:
                Review_Menu()
                  
            elif choice == 2:                                                 
                View_Report_Menu()
                  
            elif choice == 0:
                Exit_Menu()

            else:
                print("Invalid input. Please try again.\n")  
        
        except ValueError:
            print("Invalid input. Please enter a number.")

def Review_Menu():
    print('\n''\n'"-------------------------------  Hello, {}!  -------------------------------"'\n''\n'.format(user_name.title()))
    while True:
        print("Which subject do you wish to review?")
        print("  [1] English")
        print("  [2] Math")
        print("  [3] Filipino")
        print("  [4] Science")
        print("  [5] Art")
        print("  [6] Any (Random)")
        print("  [0] Back")

        try:
            choice = int(input('\n'"Please choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue







# Task Code: Menu_2
def Review_Menu(name):
    print(f"---------------------- Hello, {name}! ----------------------")
    while True:
        print("Which subject do you wish to review?")
        print("[1] English")
        print("[2] Math")
        print("[3] Filipino")
        print("[4] Science")
        print("[5] Art")
        print("[6] Any (Random)")
        print("[0] Back")
        answer = input("Please choose an option: ")
        if answer == "0":
            # go back to main menu (not implemented in this code)
            pass
        elif answer in ["1", "2", "3", "4", "5", "6"]:
            subjects = ["English", "Math", "Filipino", "Science", "Art", "Any (Random)"]
            subject = subjects[int(answer) - 1]
            customize_session(subject)
            break
        else:
            print("Invalid input. Please try again.")

# Call the Review_Menu function with a blank name
Review_Menu("")









# Task Code: Menu_3
def View_Report_Menu():
    while True:
        print('\n''\n'"----------------------  Viewing Previous Exam Performance Reports  ---------------------"'\n''\n'.format(user_name.title()))
        print("Which subject’s exam performance report do you wish to view?")
        print("  [1] English")
        print("  [2] Math")
        print("  [3] Filipino")
        print("  [4] Science")
        print("  [5] Art")
        print("  [6] All")
        print("  [0] Back")

        try:
            choice = int(input('\nPlease choose an option: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue








# Task Code: Menu_4
# Insert your work/contributions below









# Task Code: Menu_5
def Continue_Menu():
    while True:
        choice = input('\n'"Do you wish to have another session in the program? (Yes/No): ").lower()
    
        if choice == "yes":
            Main_Menu()

        elif choice == "no":
            Exit_Menu()

        else:
            print("Invalid input. Please try again.")

def Exit_Menu():
    while True:
        choice_2 = input('\n'"Do you wish to exit the program? (Yes/No): ").lower()

        if choice_2 == "yes":
            print("Thank you for using Group 2’s Grade 10 Exam Reviewer, {}.".format(user_name.capitalize()))
            print("The program will close now.\n")
            exit()

        elif choice_2 == "no":
            break
        
        else:
            print("Invalid input. Please try again.")

"Running the program" 
while True:
    print('\n''\n'"----------------------  Welcome to Group 2’s Grade 10 Exam Reviewer  ---------------------"'\n''\n')
    user_name = input('\n'"Please enter your name: ")
    Main_Menu()
