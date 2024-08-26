# Task Code: Menu_1
"Menus"
def Main_Menu():
    """
    Displays the main menu for Group 2's Grade 10 Exam Reviewer.
    Allows the user to choose between reviewing a subject, viewing
    previous exam performance reports, or exiting the program
    """                      
    while True:
        # Display the title of the application
        print("\n\n----------------------  Group 2’s Grade 10 Exam Reviewer  ---------------------\n\n")

        # Greet the user and display the menu options
        print("Hi, {}!".format(user_name.title()))
        print("What do you wish to do?")
        print("  [1] Review a Subject")
        print("  [2] View My Previous Exam Performance Reports")
        print("  [0] None")

        try:
            # Prompt the user to choose an option
            choice = int(input('\n'"Please choose an option: "))
            
            if choice == 1:
                # Navigate to the Review Menu
                Review_Menu()
                  
            elif choice == 2:
                # Navigate to the View Report Menu
                View_Report_Menu()
                  
            elif choice == 0:
                # Navigate to the Exit Menu
                Exit_Menu()

            else:
                # Handle invalid input that is not 1, 2, or 0
                print("Invalid input. Please try again.\n")  
        
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")

def Review_Menu():
    """
    Displays the review menu where the user can select a subject to review.
    The user can choose to review English, Math, Filipino, Science, Art, or
    Random, which is a combination of the aforementioned subjects, or return
    to the main menu.
    """

    # Greet the user with the their name
    print('\n''\n'"-------------------------------  Hello, {}!  -------------------------------"'\n''\n'.format(user_name.title()))

    while True:
        # Display the list of subjects available for review
        print("Which subject do you wish to review?")
        print("  [1] English")
        print("  [2] Math")
        print("  [3] Filipino")
        print("  [4] Science")
        print("  [5] Art")
        print("  [6] Any (Random)")
        print("  [0] Back")

        try:
            # Prompt the user to choose a subject
            choice = int(input('\n'"Please choose an option: "))
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.\n")
            continue # Restart the loop to ask for input again







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
        subjects = ["English", "Math", "Filipino", "Science", "Art"]

        if 1 <= choice <= 5:
            subject = subjects[choice - 1]
            ExamReviewer.generate_report(subject)
        elif choice == 6:
            ExamReviewer.get_all_performance_report()
        elif choice == 0:
            Main_Menu()
        else:
            print("Invalid input. Please try again.")
            continue

        Continue_Menu()


# Task Code: Menu_5
def Continue_Menu():
    """
    Asks the user if they wish to continue using the program or exit.
    The user can choose to return to the main menu for another session
    or exit the program entirely.
    """

    while True:
        # Prompt the user to decide whether to continue using the program
        choice = input('\n'"Do you wish to have another session in the program? (Yes/No): ").lower()
        
        # If yes, return to the main menu for another session
        if choice == "yes":
            Main_Menu()

        # If no, navigate to the exit menu
        elif choice == "no":
            Exit_Menu()

        # Handle invalid input that is not 'yes' or 'no'
        else:
            print("Invalid input. Please try again.")

def Exit_Menu():
    """
    Displays the exit menu, allowing the user to confirm if they want to exit the program.
    If the user chooses to exit, the program will terminate. Otherwise, the user can return to the previous menu
    """
    while True:
        # Prompt the user to confirm if they want to exit the program
        choice_2 = input('\n'"Do you wish to exit the program? (Yes/No): ").lower()

        # If yes, display a farewell message and exit the program
        if choice_2 == "yes":
            print("Thank you for using Group 2’s Grade 10 Exam Reviewer, {}.".format(user_name.capitalize()))
            print("The program will close now.\n")
            exit()

        # If no, return to the previous menu without exiting
        elif choice_2 == "no":
            break
        
        else:
            # Handle invalid input that is not 'yes' or 'no'
            print("Invalid input. Please try again.")

"This is the main loop to run the program" 
while True:
    # Display a welcome message and prompt the user to enter their name.
    print('\n''\n'"----------------------  Welcome to Group 2’s Grade 10 Exam Reviewer  ---------------------"'\n''\n')
    user_name = input('\n'"Please enter your name: ")
    
    # Start the main menu
    Main_Menu()
