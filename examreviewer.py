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
# Insert your work/contributions below








# Task Code: Exam_Reviewer_3
# Insert your work/contributions below








# Task Code: Exam_Reviewer_4
# Insert your work/contributions below








