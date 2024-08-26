class ExamReviewer:
    """
    Class for handling exam reviews, including generating random questions,
    customizing review sessions, saving attempts, and generating reports.
    """
    def __init__(self, subject, questions, student_answers):
        self.subject = subject  # The subject of the exam
        self.questions = questions  # List of questions that was used in the exam
        self.student_answers = student_answers  # Answers that the student provided

    @staticmethod
    def generate_random_questions(exam_items, selected_type, num_questions, shuffle):
        """
        Creates random set of questions based on the type of exam, the number of questions, and whether they should be shuffled.

        Parameters
        ----------
        exam_items (dict) : Contains the questions, options, and answers for each type of exam.
        selected_type (str) : Type of questions to include (like "True or False", "Multiple Choice", or "Both").
        num_questions (int) : The number of questions to generate.
        shuffle (str) : Whether to shuffle the questions ("Enabled" or "Disabled").
        """
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

        # Limit the number of questions to the requested amount
        questions = questions[:num_questions]
        options = options[:num_questions]
        answers = answers[:num_questions]

        return questions, options, answers

    def customize_session(subject, user_name):
        """
        Sets up the exam session based on what subject and options the user chooses.

        Parameters
        ----------
        subject (str) : Subject for the session.
        user_name (str) : Name of the user taking the exam.
        """
        print("\n\n----------------------  Exam Customization  ---------------------\n\n")
        print(
            f"You have decided to take the {subject} exam. Let’s customize your exam reviewer!\n")
    
        # Ask for question type
        while True:
            print("What type of exam questions do you wish to take?")
            print("[1] True or False")
            print("[2] Multiple Choice")
            print("[3] Both")
            print("[0] Back")
            answer = input("\nPlease choose an option: ")
            if answer == "0":
                return Review_Menu()  # Go back to review menu
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
    
            # Total number of questions in "True or False" or "Multiple Choice": 10 questions
            # While Both is 20 questions
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
    
        # Ask for shuffling
        while True:
            answer = input("Do you want to shuffle the questions? (Yes/No): ")
            if answer.lower() in ["yes"]:
                shuffle = "Enabled"  # Changes
                break
            elif answer.lower() in ["no"]:
                shuffle = "Disabled"
                break
            else:
                print("Invalid input. Please try again.\n")
    
        # Print exam items based on customization
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

    def save_exam_attempt(self):
        """ 
        Saves the student's current exam attempt, including their answers and
        score.

        This method makes sure the student's performance is stored so it can be
        reviewed later.
        """
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
        """
        Generates a detailed report for all student attempts in a specific
        subject.

        Parameters
        ----------
        subject (str) : The subject for which the report will be created.
        """
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

    @staticmethod
    def get_all_performance_report():
        """
        Generates a detailed report covering all the student's exam attempts
        across every subject.

        This gives an overall view of how the student is doing in all subjects.
        """
        global exam_attempts
        # Check if there are any recorded exam attempts
        if not exam_attempts:
            print("No exam attempts found for any subject.")
            return
        
        # Iterate through each subject and its corresponding attempts
        for subject, attempts in exam_attempts.items():
            print(f"\n\n--------------------------------  {user_name.title()}'s {subject} Exam Reports  --------------------------------")

            # Iterate through each attempt for the current subject
            for i, attempt in enumerate(attempts, 1):
                print(f"\n\n----------------------  Attempt {i}  ----------------------\n")
                questions = attempt ['questions']
                student_answers = attempt ['student_answers']
                score = attempt ['score']

                # Display each question, the student's answer, and the correct answer
                for j, (question, answer) in enumerate(zip(questions, student_answers), 1):
                    print(f"\nQuestion {j}: {question['question']}")
                    print(f"Your answer: {answer}")
                    print(f"Correct answer: {question['correct_answer']}")
                    # Check if the student's answer is correct
                    is_correct = answer.lower() == question['correct_answer'].lower()
                    print("You got this correct!" if is_correct else "You got this wrong.")

                # Display the summary of the current attempt
                print("\n\n[Attempt Summary]")
                print(f"Total score: {score['score']}/{score['total_items']}")
                print(f"Percentage: {score['score_percentage']:.2f}%")

        # Print the end of the list of exam reports
        print(f"\n\n----------------------  End of {user_name.title()}'s Exam Reports  ---------------------")
