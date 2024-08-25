# Task Code: Menu_1
# Insert your work/contributions below







# Task Code: Menu_2
# Insert your work/contributions below
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

# coded by Michelle Magpayo MMS146: Group2







# Task Code: Menu_3
# Insert your work/contributions below








# Task Code: Menu_4
# Insert your work/contributions below









# Task Code: Menu_5
# Insert your work/contributions below
