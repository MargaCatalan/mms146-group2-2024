class Student:
    def __init__(self, name):
        self.name = name
        # List of dictionaries to store the answers given by the student for each subject
        self.english_answers_given = []
        self.filipino_answers_given = []
        self.math_answers_given = []
        self.art_answers_given = []
        self.science_answers_given = []
        
 def save_answer(self, subject, question, options, given_answer, correct_answer):
        if subject == "english":
            self.english_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : given_answer,
                                               'correct_answer' : correct_answer})
        elif subject == "filipino":
            self.filipino_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : given_answer,
                                               'correct_answer' : correct_answer})
        elif subject == "math":
            self.math_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : given_answer,
                                               'correct_answer' : correct_answer})
        elif subject == "art":
            self.art_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : given_answer,
                                               'correct_answer' : correct_answer})
        elif subject == "science":
            self.science_answers_given.append({'question' : question,
                                               'options' : options,
                                               'given_answer' : given_answer,
                                               'correct_answer' : correct_answer})

        def get_performance_report(self):
            pass
            
