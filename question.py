class Question:
    def __init__(self):
        self.question_text = None
        self.options = None
        self.correct_answer = None

    def display_questions(self, exam_items, selected_type, num_questions, shuffle):
        if selected_type == "True or False":
            questions = exam_items["True or False"]["Questions"]
            options = exam_items["True or False"]["Options"]
            answers = exam_items["True or False"]["Answers"]
        elif selected_type == "Multiple Choice":
            questions = exam_items["Multiple Choice"]["Questions"]
            options = exam_items["Multiple Choice"]["Options"]
            answers = exam_items["Multiple Choice"]["Answers"]
        elif selected_type == "Both":
            questions = exam_items["True or False"]["Questions"] + exam_items["Multiple Choice"]["Questions"]
            options = exam_items["True or False"]["Options"] + exam_items["Multiple Choice"]["Options"]
            answers = exam_items["True or False"]["Answers"] + exam_items["Multiple Choice"]["Answers"]

        if shuffle:
            combined = list(zip(questions, options, answers))
            random.shuffle(combined)
            questions, options, answers = zip(*combined)

        questions = questions[:num_questions]
        options = options[:num_questions]
        answers = answers[:num_questions]

        for i, question in enumerate(questions):
            print(f"\nQuestion {i + 1}: {question}")
            if selected_type != "True or False" or selected_type == "Both":
                for option in options[i]:
                    print(option)
            answer = input("Your answer: ")
            self.check_answer(answer, answers[i])

        choice = input("Do you wish to review your exam performance report? (Yes/No): ").lower()
        if choice == "yes":
            Exam_Reviewer.generate_report()
        elif choice == "no":
            Continue_Menu(user_name)
        else:
            print("Invalid input. Please try again.")
            Continue_Menu(user_name)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You’re correct!")
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
            
        Student.save_answer(answer)
