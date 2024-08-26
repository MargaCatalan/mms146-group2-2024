class Student:
    def __init__(self, name):
        """
        Initializes the attributes of the student object and creates a list to
        store the answers given by the student.
        """
        self.name = name
        # List of dictionaries to store the answers given by the student for each subject
        self.english_answers_given = [correct_answer] # type: ignore
        self.filipino_answers_given = [correct_answer] # type: ignore
        self.math_answers_given = [correct_answer] # type: ignore
        self.art_answers_given = [correct_answer] # type: ignore
        self.science_answers_given = [correct_answer] # type: ignore

    def save_answer(self, subject, question, options, answer, correct_answer):
        """
        Method to save the answer of the student by subject.
        """
        if subject == "english":
            self.english_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : answer,
                                               'correct_answer' : correct_answer})
        elif subject == "filipino":
            self.filipino_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : answer,
                                               'correct_answer' : correct_answer})
        elif subject == "math":
            self.math_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : answer,
                                               'correct_answer' : correct_answer})
        elif subject == "art":
            self.art_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : answer,
                                               'correct_answer' : correct_answer})
        elif subject == "science":
            self.science_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : answer,
                                               'correct_answer' : correct_answer})
            
    @staticmethod
    def get_performance_report(subject, questions, student_answers, print_report=True):
        """
        A method to generate the performance report by getting the correct
        answers, mistakes, total items, and percentage of score of the student.
        """
        correct_answers = 0
        mistakes = []
        total_items = len(questions)

        for i, question in enumerate(questions):
            user_answer = student_answers[i]
            correct_answer = question['correct_answer']
            
            if user_answer.lower() == correct_answer.lower():
                correct_answers += 1
            else:
                mistakes.append({
                    'question_number': i + 1,
                    'question': question['question'],
                    'user_answer': user_answer,
                    'correct_answer': correct_answer
                })

        score = correct_answers
        score_percentage = (correct_answers / total_items) * 100 if total_items > 0 else 0
        num_mistakes = total_items - correct_answers

        if print_report:
            print(f"\n\n----------------------  End of {subject} Exam  ---------------------\n\n")
            print("Here's your exam performance report:\n")
            print(f"Correct Answers: {correct_answers}")
            print(f"Mistakes: {num_mistakes}")
            print(f"Your total score is {score}/{total_items}, which is {score_percentage:.2f}%. \n")

            if mistakes:
                print(f"\n[Suggested Items to Review]")
                for mistake in mistakes:
                    print(f"\nQuestion {mistake['question_number']}: {mistake['question']}")
                    print(f"Your answer: {mistake['user_answer']}")
                    print(f"Correct answer: {mistake['correct_answer']}")
            else:
                print("\nCongratulations! You have 0 mistakes!\n")

        return {
            'score': score,
            'total_items': total_items,
            'score_percentage': score_percentage
        }
