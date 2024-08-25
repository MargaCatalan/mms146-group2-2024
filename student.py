class Student:
    def __init__(self, name):
        self.name = name
        # List of dictionaries to store the answers given by the student for each subject
        self.english_answers_given = [correct_answer] # type: ignore
        self.filipino_answers_given = [correct_answer] # type: ignore
        self.math_answers_given = [correct_answer] # type: ignore
        self.art_answers_given = [correct_answer] # type: ignore
        self.science_answers_given = [correct_answer] # type: ignore

# Task Code: Student_2
    def save_answer(self, subject, question, options, answer, correct_answer):
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








# Task Code: Student_1
# Insert your work/contributions below
