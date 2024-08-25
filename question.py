# Task Code: Question_1
# Insert your work/contributions below







# Task Code: Question_2
class Question:
    def __init__(self):
        self.question_text = None
        self.options = None
        self.correct_answer = None
        self.exam_questions = []
        self.exam_answers = []

    def display_questions(self, exam_items, selected_type, num_questions, shuffle, subject, user_name):
        # Generate questions using the static method from ExamReviewer
        questions, options, answers = ExamReviewer.generate_random_questions(
            exam_items, selected_type, num_questions, shuffle
        )

        # Create a Student instance
        student = Student(user_name)

        # Display questions
        for i, question in enumerate(questions):
            print(f"\nQuestion {i + 1}: {question}")
            for option in options[i]:
                print(option)
            answer = input("\nYour Answer: ")

            # Check the answer and save it
            self.check_answer(answer, answers[i], subject, question, options[i], student)

        # After all questions have been answered
        examreviewer = ExamReviewer(subject, self.exam_questions, self.exam_answers)
        examreviewer.save_exam_attempt()
        Student.get_performance_report(subject, self.exam_questions, self.exam_answers, print_report=True)

        # Handle user choice for review or continuation
        while True:
            choice = input('\nDo you wish to have another review session? (Yes/No): ').lower()
            if choice == "yes":
                Review_Menu()  
            elif choice == "no":
                Continue_Menu()  
            else:
                print("Invalid input. Please try again.")

    def check_answer(self, answer, correct_answer, subject, question, options, student):
        if answer.lower() == correct_answer.lower():
            print("You’re correct!")
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")

        # Store the question and answer for the report
        self.exam_questions.append({'question': question, 'correct_answer': correct_answer})
        self.exam_answers.append(answer)

        # Save the answer in the Student instance
        student.save_answer(subject, question, options, answer, correct_answer)








# Task Code: Question_3
# Insert your work/contributions below








