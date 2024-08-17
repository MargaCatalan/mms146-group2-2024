import random    # necessary for shuffling questions
class ExamReviewer:
    pass

    def generateRandomQuestions():
        '''
        Generates questions and options based on customize_session.
        '''
        # the following code will create a list of questions.
        
        # if user selects 'True or False' question type, only include the questions from the 'True or False' dictionary.
        if self.question_type == "True or False":
            questions = self.exam_items["True or False"]["Questions"]
            options = self.exam_items["True or False"]["Options"]
        # if user selects 'Multiple Choice' question type, only include the questions from the 'Multiple Choice' dictionary.
        elif self.question_type == "Multiple Choice":
            questions = self.exam_items["Multiple Choice"]["Questions"]
            options = self.exam_items["Multiple Choice"]["Options"]
        # if user selects both question types, add both to a list.
        else:
            questions = list(self.exam_items["True or False"]["Questions"]) + list(self.exam_items["Multiple Choice"]["Questions"])
            options = self.exam_items["Multiple Choice"]["Options"]

        
    #customize_session method
    def customize_session(subject):
        print("---------------------- Exam Customization ---------------------")
        print(
            f"You have decided to take the {subject} exam. Let’s customize your exam reviewer!")
    
        #Ask for question type
        while True:
            print("What type of exam questions do you wish to take?")
            print("[1] True or False")
            print("[2] Multiple Choice")
            print("[3] Both")
            print("[0] Back")
            answer = input("Please choose an option: ")
            if answer == "0":
                return Review_Menu()  #Go back to review menu
            elif answer in ["1", "2", "3"]:
                question_type = ["True or False",
                                 "Multiple Choice", "Both"][int(answer) - 1]
                break
            else:
                print("Invalid input. Please try again.")
    
        #Total number of questions in True or False" or "Multiple Choice": 10 questions
        #While Both is 20 questions
        if question_type == "True or False" or question_type == "Multiple Choice":
            min_question = 5
            max_questions = 10
        else:
            min_question = 5
            max_questions = 20
        while True:
            answer = input(
                f"How many questions do you wish to review? (max {max_questions}): ")
            if min_question <= int(answer) <= max_questions:
                num_questions = int(answer)
                break
            else:
                print(
                    "Invalid input. Please enter a valid number of questions within the allowed range.")
    
        #Ask for shuffling
        while True:
            answer = input("Do you want to shuffle the questions? (Yes/No): ")
            if answer.lower() in ["yes", "no"]:
                shuffle = self.generate_random_questions()  #Changes
                break
            else:
                print("Invalid input. Please try again.")
    
        #Print exam items based on customization
        print(f"Exam Customization Summary:")
        print(f"Subject: {subject}")
        print(f"Question Type: {question_type}")
        print(f"Number of Questions: {num_questions}")
        print(f"Shuffle: {shuffle}")
    
        #Call display_questions with customized parameters
        Question.display_questions(subject, question_type, num_questions, shuffle)
