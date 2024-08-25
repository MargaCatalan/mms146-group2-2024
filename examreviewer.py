# Task Code: Exam_Reviewer_1
class ExamReviewer:
    def __init__(self, subject, questions, student_answers):
        self.subject = subject
        self.questions = questions
        self.student_answers = student_answers

    @staticmethod
    def generate_random_questions(exam_items, selected_type, num_questions, shuffle):
        questions = []
        options = []
        answers = []

        # Collect questions, options, and answers based on selected_type
        if selected_type == "True or False":
            questions = exam_items["True or False"]["Questions"]
            options = exam_items["True or False"]["Options"]
            answers = exam_items["True or False"]["Answers"]
        elif selected_type == "Multiple Choice":
            questions = exam_items["Multiple Choice"]["Questions"]
            options = exam_items["Multiple Choice"]["Options"]
            answers = exam_items["Multiple Choice"]["Answers"]
        elif selected_type == "Both":
            questions.extend(exam_items["True or False"]["Questions"])
            questions.extend(exam_items["Multiple Choice"]["Questions"])
            
            options.extend(exam_items["True or False"]["Options"])
            options.extend(exam_items["Multiple Choice"]["Options"])
            
            answers.extend(exam_items["True or False"]["Answers"])
            answers.extend(exam_items["Multiple Choice"]["Answers"])

        # Shuffle questions, options, and answers together
        if shuffle == "Enabled":
            combined = list(zip(questions, options, answers))
            random.shuffle(combined)
            questions, options, answers = zip(*combined)
            questions = list(questions)
            options = list(options)
            answers = list(answers)

        # Limit to the number of questions requested
        questions = questions[:num_questions]
        options = options[:num_questions]
        answers = answers[:num_questions]

        return questions, options, answers

# Task Code: Exam_Reviewer_2
    def customize_session(subject, user_name):
        print("\n\n----------------------  Exam Customization  ---------------------\n\n")
        print(
            f"You have decided to take the {subject} exam. Let’s customize your exam reviewer!\n")
    
        #Ask for question type
        while True:
            print("What type of exam questions do you wish to take?")
            print("[1] True or False")
            print("[2] Multiple Choice")
            print("[3] Both")
            print("[0] Back")
            answer = input("\nPlease choose an option: ")
            if answer == "0":
                return Review_Menu()  #Go back to review menu
            elif answer in ["1", "2", "3"]:
                question_type = ["True or False",
                                 "Multiple Choice", "Both"][int(answer) - 1]
                break
            else:
                print("Invalid input. Please try again.\n")


        if subject == "Random":
            # If Random, total number of questions in "True or False" or "Multiple Choice": 50 questions
            if question_type == "True or False" or question_type == "Multiple Choice":
                min_question = 1
                max_questions = 50
            # While Both is 100 questions
            else:
                min_question = 1
                max_questions = 100

        else:
    
            #Total number of questions in "True or False" or "Multiple Choice": 10 questions
            #While Both is 20 questions
            if question_type == "True or False" or question_type == "Multiple Choice":
                min_question = 1
                max_questions = 10
            else:
                min_question = 1
                max_questions = 20

        while True:
            try:
                answer = input(
                f"\nHow many questions do you wish to review? (Input range: {min_question} - {max_questions}): ")
                if min_question <= int(answer) <= max_questions:
                    num_questions = int(answer)
                    break
                else:
                    print("Invalid input. Please enter a valid number of questions within the allowed range.\n")

            except ValueError:
                print("Invalid input. Please enter a number.")
    
        #Ask for shuffling
        while True:
            answer = input("Do you want to shuffle the questions? (Yes/No): ")
            if answer.lower() in ["yes"]:
                shuffle = "Enabled"  #Changes
                break
            elif answer.lower() in ["no"]:
                shuffle = "Disabled"
                break
            else:
                print("Invalid input. Please try again.\n")
    
        #Print exam items based on customization
        print(f"\n\n---------------------  {subject} Exam Attempt  ---------------------\n\n")
        print(f"Subject: {subject}")
        print(f"Question Type: {question_type}")
        print(f"Number of Questions: {num_questions}")
        print(f"Shuffle: {shuffle}")

        if subject == "Random":
            # Initialize combined questions
            combined_questions = {"True or False": {"Questions": [], "Options": [], "Answers": []},
                                "Multiple Choice": {"Questions": [], "Options": [], "Answers": []}}

            # Make a dictionary combining all reviewers
            all_reviewers = {
                "English": EnglishReviewer(),
                "Math": MathReviewer(),
                "Filipino": FilipinoReviewer(),
                "Science": ScienceReviewer(),
                "Art": ArtReviewer()
            }

            # Combine questions from all reviewers
            for reviewer in all_reviewers.values():
                exam_items = reviewer.exam_items
                if question_type in ["True or False", "Both"]:
                    combined_questions["True or False"]["Questions"].extend(exam_items["True or False"]["Questions"])
                    combined_questions["True or False"]["Options"].extend(exam_items["True or False"]["Options"])
                    combined_questions["True or False"]["Answers"].extend(exam_items["True or False"]["Answers"])
                if question_type in ["Multiple Choice", "Both"]:
                    combined_questions["Multiple Choice"]["Questions"].extend(exam_items["Multiple Choice"]["Questions"])
                    combined_questions["Multiple Choice"]["Options"].extend(exam_items["Multiple Choice"]["Options"])
                    combined_questions["Multiple Choice"]["Answers"].extend(exam_items["Multiple Choice"]["Answers"])

            # Call display_questions with combined questions
            reviewer.display_questions(combined_questions, question_type, num_questions, shuffle, subject, user_name)

        else:
            # Handle specific subject case
            if subject == "English":
                reviewer = EnglishReviewer()
            elif subject == "Math":
                reviewer = MathReviewer()
            elif subject == "Filipino":
                reviewer = FilipinoReviewer()
            elif subject == "Science":
                reviewer = ScienceReviewer()
            elif subject == "Art":
                reviewer = ArtReviewer()
            else:
                print("Invalid subject. Please try again.")
                return
            
            # Call display_questions
            reviewer.display_questions(reviewer.exam_items, question_type, num_questions, shuffle, subject, user_name)

# Task Code: Exam_Reviewer_3
# Insert your work/contributions below
# To save the attempts made by users in a certain subject    
    def save_exam_attempt(self):
        global exam_attempts
        if self.subject not in exam_attempts:
            exam_attempts[self.subject] = []
    
        # Instead of calling get_performance_report from ExamReviewer, use Student's static method
        score = Student.get_performance_report(self.subject, self.questions, self.student_answers, print_report=False)
        attempt = {
            'questions': self.questions,
            'student_answers': self.student_answers,
            'score': score
        }
        exam_attempts[self.subject].append(attempt)
        
    @staticmethod
    def generate_report(subject):
        global exam_attempts
        if subject not in exam_attempts or not exam_attempts[subject]:
            print(f"No exam attempts found for {subject}.")
            return

        print(f"\n\n----------------------  {user_name.title()}'s {subject} Exam Reports  ---------------------")
        for i, attempt in enumerate(exam_attempts[subject], 1):
            print(f"\n\n----------------------  Attempt {i}  ----------------------\n")
            questions = attempt['questions']
            student_answers = attempt['student_answers']
            score = attempt['score']

            for j, (question, answer) in enumerate(zip(questions, student_answers), 1):
                print(f"\nQuestion {j}: {question['question']}")
                print(f"Your answer: {answer}")
                print(f"Correct answer: {question['correct_answer']}")
                is_correct = answer.lower() == question['correct_answer'].lower()
                print("You got this correct!" if is_correct else "You got this wrong.")


            print("\n\n[Attempt Summary]")
            print(f"Total score: {score['score']}/{score['total_items']}")
            print(f"Percentage: {score['score_percentage']:.2f}%")
        
        print(f"\n\n----------------------  End of {subject} Exam Reports  ---------------------\n\n")

        while True:
            choice = input("Do you wish to view another report? (Yes/No): ").lower()

            if choice == "yes":
                View_Report_Menu()

            elif choice == "no":
                Continue_Menu()

            else:
                print("Invalid input. Please try again.")


# Task Code: Exam_Reviewer_4
@staticmethod
    def get_all_performance_report():
        global exam_attempts
        if not exam_attempts:
            print("No exam attempts found for any subject.")
            return
        
        for subject, attempts in exam_attempts.items():
            print(f"\n\n--------------------------------  {user_name.title()}'s {subject} Exam Reports  --------------------------------")
            for i, attempt in enumerate(attempts, 1):
                print(f"\n\n----------------------  Attempt {i}  ----------------------\n")
                questions = attempt ['questions']
                student_answers = attempt ['student_answers']
                score = attempt ['score']

                for j, (question, answer) in enumerate(zip(questions, student_answers), 1):
                    print(f"\nQuestion {j}: {question['question']}")
                    print(f"Your answer: {answer}")
                    print(f"Correct answer: {question['correct_answer']}")
                    is_correct = answer.lower() == question['correct_answer'].lower()
                    print("You got this correct!" if is_correct else "You got this wrong.")

                print("\n\n[Attempt Summary]")
                print(f"Total score: {score['score']}/{score['total_items']}")
                print(f"Percentage: {score['score_percentage']:.2f}%")

        print(f"\n\n----------------------  End of {user_name.title()}'s Exam Reports  ---------------------")






