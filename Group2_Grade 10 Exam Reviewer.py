import random # necessary for shuffling questions
exam_attempts = {}  # Global dictionary to store attempts for all subjects

class Student:
    def __init__(self, name):
        """
        Initializes the attributes of the student object and creates a list to
        store the answers given by the student.
        """
        self.name = name
        # List of dictionaries to store the answers given by the student for each subject
        self.english_answers_given = [] # type: ignore
        self.filipino_answers_given = [] # type: ignore
        self.math_answers_given = [] # type: ignore
        self.art_answers_given = [] # type: ignore
        self.science_answers_given = [] # type: ignore

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
    
class Question:
    """
    A class to represent an exam question and handle its display, answer checking,
    and storage for a student's exam session.
    """
    def __init__(self):
        self.question_text = None  # the text of the current question
        self.options = None  # The list of options for the current question.
        self.correct_answer = None  # The correct answer for the current question.
        self.exam_questions = []  # A list to store the questions displayed during the exam session.
        self.exam_answers = []  # A list to store the student's answers during the exam session.

    def display_questions(self, exam_items, selected_type, num_questions, shuffle, subject, user_name):
        """
        Displays a list of exam questions and options to the student. After recording 
        the student's answers, it generates and saves the exam report.

        Parameters:
        ----------
        exam_items : list
            A list of all exam questions and options.
        selected_type : str
            The type of questions to be selected (e.g., multiple choice).
        num_questions : int
            The number of questions to display.
        shuffle : bool
            Whether or not to shuffle the questions.
        subject : str
            The subject name (e.g., 'Math', 'English').
        user_name : str
            The student's name.

        Returns:
        -------
        None
        """
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
        """
        Compares the student's answer with the correct answer and stores the result 
        in both the Question and Student classes.

        Parameters:
        ----------
        answer : str
            The student's provided answer.
        correct_answer : str
            The correct answer for the question.
        subject : str
            The subject name.
        question : str
            The text of the current question.
        options : list
            The list of options for the current question.
        student : Student
            The instance of the Student class representing the current user.

        Returns:
        -------
        None
        """

        if answer.lower() == correct_answer.lower():
            print("You’re correct!")
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")

        # Store the question and answer for the report
        self.exam_questions.append({'question': question, 'correct_answer': correct_answer})
        self.exam_answers.append(answer)

        # Save the answer in the Student instance
        student.save_answer(subject, question, options, answer, correct_answer)

class EnglishReviewer (Question):    
    def __init__(self):
        super().__init__()
        multiple_choice_questions =        ("Which of the following is an example of a metaphor?",
                                            "Which of the following is a theme commonly explored in literature?",
                                            "The main idea of a passage is:",
                                            "Which point of view uses the pronoun 'I'?",
                                            "Which word is an antonym of 'joyful'?",
                                            "Which of the following sentences is written in passive voice?",
                                            "The genre of a book that tells a story about future technology is likely:",
                                            "Which literary device involves exaggeration for effect?",
                                            "What is the purpose of an expository essay?",
                                            "Which of these sentences is an example of direct speech?")
        multiple_choice_options =          (("  [A] The wind howled like a wolf.   ", "  [B] The flowers danced in the breeze. ", "  [C] The stars were diamonds in the sky.", "  [D] She sang as sweetly as a bird."),
                                            ("  [A] Time travel                    ", "  [B] The struggle between good and evil", "  [C] Cooking techniques                 ", "  [D] Sportsmanship"),
                                            ("  [A] A minor detail in the text     ", "  [B] The central point or message      ", "  [C] The author's opinion               ", "  [D] The first sentence"),
                                            ("  [A] First-person                   ", "  [B] Second-person                     ", "  [C] Third-person                       ", "  [D] Omniscient"),
                                            ("  [A] Happy                          ", "  [B] Cheerful                          ", "  [C] Gloomy                             ", "  [D] Bright"),
                                            ("  [A] The dog chased the cat.        ", "  [B] The cat was chased by the dog.    ", "  [C] The cat is chasing the dog.        ", "  [D] The dog is chasing the cat."),
                                            ("  [A] Historical fiction             ", "  [B] Science fiction                   ", "  [C] Mystery                            ", "  [D] Biography"),
                                            ("  [A] Hyperbole                      ", "  [B] Irony                             ", "  [C] Alliteration                       ", "  [D] Onomatopoeia"),
                                            ("  [A] To entertain                   ", "  [B] To inform                         ", "  [C] To persuade                        ", "  [D] To describe"),
                                            ("  [A] She asked me where I was going.", "  [B] 'Where are you going?' she asked. ", "  [C] I was asked where I was going.     ", "  [D] She wondered where I was going."))
        multiple_choice_correct_answers =  ("C", "B", "B", "A", "C", "B", "B", "A", "B", "B")
        true_or_false_questions =          ("A simile compares two things using the words 'like' or 'as.'",
                                            "An autobiography is a story written about someone else's life.",
                                            "A thesis statement is typically found at the end of the introduction paragraph.",
                                            "The climax of a story is the point of highest tension.",
                                            "In a narrative, the setting refers to the time and place where the story occurs.",
                                            "Personification gives human characteristics to nonhuman objects.",
                                            "The tone of a text reflects the author's attitude toward the subject.",
                                            "A biography is a story about someone's life written by someone else.",
                                            "A synonym is a word with the same or nearly the same meaning as another word.",
                                            "The protagonist is always the 'good guy' in a story.")
        true_or_false_options =            (("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"))
        true_or_false_correct_answers =    ("A", "B", "A", "A", "A", "A", "A", "A", "A", "B")

        self.exam_items =  {"Multiple Choice": {"Questions": multiple_choice_questions,
                                                "Options": multiple_choice_options,
                                                "Answers": multiple_choice_correct_answers},
                            "True or False":   {"Questions": true_or_false_questions,
                                                "Options": true_or_false_options,
                                                "Answers": true_or_false_correct_answers}}
        
class MathReviewer (Question):
    def __init__(self):
        super().__init__()
        multiple_choice_questions =        ("What is the value of 2³ + 5 x 2 ?",
                                            "Which of the following is a prime number?",
                                            "Simplify: 12/18",
                                            "What is the area of a rectangle with a length of 8cm and a width of 5cm?",
                                            "What is the slope of the line given by the equation y = 3x + 4 ?",
                                            "The Pythagorean theorem is used to find:",
                                            "What is the value of 5! (5 factorial)?",
                                            "Solve for x in the equation 2x - 7 = 9.",
                                            "If the probability of an event happening is 0.25, what is the probability of it not happening?",
                                            "What is the equation of a line with a slope of 2 and a y-intercept of -3?")
        multiple_choice_options =          (("  [A] 16                     ", "  [B] 18                              ", "  [C] 20                         ", "  [D] 22"),
                                            ("  [A] 12                     ", "  [B] 15                              ", "  [C] 17                         ", "  [D] 21"),
                                            ("  [A] 2/3                    ", "  [B] 3/4                             ", "  [C] 4/5                        ", "  [D] 5/6"),
                                            ("  [A] 13cm²                  ", "  [B] 20cm²                           ", "  [C] 40cm²                      ", "  [D] 50cm²"),
                                            ("  [A] 3                      ", "  [B] 4                               ", "  [C] -3                         ", "  [D] -4"),
                                            ("  [A] The area of a circle   ", "  [B] The sides of a right triangle   ", "  [C] The volume of a cylinder   ", "  [D] The angles of a polygon"),
                                            ("  [A] 20                     ", "  [B] 60                              ", "  [C] 120                        ", "  [D] 240"),
                                            ("  [A] 2                      ", "  [B] 4                               ", "  [C] 5                          ", "  [D] 8"),
                                            ("  [A] 0.25                   ", "  [B] 0.50                            ", "  [C] 0.75                       ", "  [D] 1"),
                                            ("  [A] y = 2x - 3             ", "  [B] y = -2x + 3                     ", "  [C] y = 3x + 2                 ", "  [D] y = -3x + 2"))
        multiple_choice_correct_answers =  ("B", "C", "A", "C", "A", "B", "C", "D", "C", "A")
        true_or_false_questions =          ("The product of any two even numbers is always even.",
                                            "The sum of the angles in a triangle is always 180 degrees.",
                                            "The square root of 49 is 7.",
                                            "2x + 3 = 11 solves to x = 4. ",
                                            "A parallelogram has four sides of equal length. ",
                                            "An isosceles triangle has two sides of equal length.",
                                            "The circumference of a circle is given by C = πr². ",
                                            "A histogram is used to display the distribution of numerical data.",
                                            "The number 0 is neither positive nor negative.",
                                            "A rhombus is a type of parallelogram. ")
        true_or_false_options =            (("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"))
        true_or_false_correct_answers =    ("A", "A", "A", "A", "B", "A", "B", "A", "A", "A")

        self.exam_items =  {"Multiple Choice": {"Questions": multiple_choice_questions,
                                                "Options": multiple_choice_options,
                                                "Answers": multiple_choice_correct_answers},
                            "True or False":   {"Questions": true_or_false_questions,
                                                "Options": true_or_false_options,
                                                "Answers": true_or_false_correct_answers}}
        
class FilipinoReviewer (Question):
    def __init__(self):
        super().__init__()
        multiple_choice_questions =        ("Alin sa mga sumusunod ang tamang kahulugan ng salitang 'kasaysayan'?",
                                            "Sino ang may-akda ng 'Noli Me Tangere'?",
                                            "Ano ang ibig sabihin ng ‘balagtasan’?",
                                            "Alin sa mga sumusunod ang hindi kabilang sa panitikan?",
                                            "Ano ang pangunahing layunin ng ‘Karunungang-Bayan’?",
                                            "Ano ang tamang baybay ng salitang ‘pagtutulungan’?",
                                            "Ano ang ibig sabihin ng idyomang ‘bukambibig’?",
                                            "Sino ang tinaguriang ‘Ama ng Balarila’?",
                                            "Ano ang tawag sa mga kasabihan na naglalayong magbigay aral?",
                                            "Ano ang tawag sa pagkakasunod-sunod ng mga pangyayari sa isang kwento?")
        multiple_choice_options =          (("  [A] Pangarap                          ", "  [B] Kaalaman                     ", "  [C] Nakaraan                     ", "  [D] Hinaharap"),
                                            ("  [A] Emilio Aguinaldo                  ", "  [B] Apolinario Mabini            ", "  [C] Andres Bonifacio             ", "  [D] Jose Rizal"),
                                            ("  [A] Pagtatalo sa pamamagitan ng tula  ", "  [B] Pagtitipon ng mga kabataan   ", "  [C] Pag-awit ng mga awit-bayan   ", "  [D] Pagbigkas ng mga talumpati"),
                                            ("  [A] Maikling kwento                   ", "  [B] Dula                         ", "  [C] Sanaysay                     ", "  [D] Sayaw"),
                                            ("  [A] Magturo ng aral                   ", "  [B] Magpasaya                    ", "  [C] Magtaguyod ng katarungan     ", "  [D] Magbigay ng aliw"),
                                            ("  [A] Pagttulungan                      ", "  [B] Pagtutolungan                ", "  [C] Pagtutulungan                ", "  [D] Pagtotulungan"),
                                            ("  [A] Madaldal                          ", "  [B] Palaging sinasabi            ", "  [C] Palakaibigan                 ", "  [D] Sikat na tao"),
                                            ("  [A] Lope K. Santos                    ", "  [B] Jose Corazon de Jesus        ", "  [C] Francisco Balagtas           ", "  [D] Jose P. Laurel"),
                                            ("  [A] Alamat                            ", "  [B] Bugtong                      ", "  [C] Salawikain                   ", "  [D] Dula"),
                                            ("  [A] Tauhan                            ", "  [B] Tagpuan                      ", "  [C] Banghay                      ", "  [D] Wakas"))
        multiple_choice_correct_answers =  ("C", "D", "A", "D", "A", "C", "B", "A", "C", "C")
        true_or_false_questions =          ("Ang ‘bayanihan’ ay tumutukoy sa pagtutulungan ng mga Pilipino.",
                                            "Ang awit na ‘Lupang Hinirang’ ay orihinal na isinulat sa wikang Ingles.",
                                            "Ang 'Pasyon' ay isang uri ng panitikan na may kaugnayan sa Semana Santa.",
                                            "Ang alamat ay isang kwento tungkol sa pinagmulan ng isang bagay, lugar, o pangyayari.",
                                            "Ang salitang 'balana' ay nangangahulugang lahat ng tao.",
                                            "Ang 'kundiman' ay isang uri ng awit na nagpapahayag ng pag-ibig.",
                                            "Ang epiko ay isang mahabang tula na karaniwang nagsasalaysay ng mga kabayanihan.",
                                            "Ang sawikain ay mga pahayag na di-tuwirang nagbibigay kahulugan.",
                                            "Ang sanaysay ay isang uri ng sulating nagpapahayag ng pananaw o kuro-kuro.",
                                            "Ang talumpati ay isang uri ng pagsasalita sa harap ng maraming tao.")
        true_or_false_options =            (("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"),
                                            ("  [A] Tama    ", "  [B] Mali"))
        true_or_false_correct_answers =    ("A", "B", "A", "A", "A", "A", "A", "A", "A", "A")

        self.exam_items =  {"Multiple Choice": {"Questions": multiple_choice_questions,
                                                "Options": multiple_choice_options,
                                                "Answers": multiple_choice_correct_answers},
                            "True or False":   {"Questions": true_or_false_questions,
                                                "Options": true_or_false_options,
                                                "Answers": true_or_false_correct_answers}}       

class ScienceReviewer (Question):
    def __init__(self):
        super().__init__()
        multiple_choice_questions =        ("What is the chemical symbol for water?",
                                            "Which organ is primarily responsible for pumping blood throughout the body?",
                                            "What is the main gas found in the Earth's atmosphere?",
                                            "Which of the following is an example of a chemical change?",
                                            "What force keeps objects grounded on Earth?",
                                            "Which planet is known as the 'Red Planet'?",
                                            "What is the most abundant element in the universe?",
                                            "Which part of the cell is responsible for producing energy?",
                                            "Which type of rock is formed by cooling and solidification of lava or magma?",
                                            "What is the powerhouse of the cell?")
        multiple_choice_options =          (("  [A] H2O          ", "  [B] O2            ", "  [C] CO2             ", "  [D] H2"),
                                            ("  [A] Brain        ", "  [B] Lungs         ", "  [C] Liver           ", "  [D] Heart"),
                                            ("  [A] Oxygen       ", "  [B] Nitrogen      ", "  [C] Carbon Dioxide  ", "  [D] Hydrogen"),
                                            ("  [A] Melting ice  ", "  [B] Burning wood  ", "  [C] Cutting paper   ", "  [D] Boiling water"),
                                            ("  [A] Magnetism    ", "  [B] Friction      ", "  [C] Gravity         ", "  [D] Inertia"),
                                            ("  [A] Venus        ", "  [B] Mars          ", "  [C] Jupiter         ", "  [D] Saturn"),
                                            ("  [A] Oxygen       ", "  [B] Carbon        ", "  [C] Helium          ", "  [D] Hydrogen"),
                                            ("  [A] Nucleus      ", "  [B] Ribosome      ", "  [C] Mitochondria    ", "  [D] Chloroplast"),
                                            ("  [A] Sedimentary  ", "  [B] Metamorphic   ", "  [C] Igneous         ", "  [D] Fossil"),
                                            ("  [A] Nucleus      ", "  [B] Mitochondria  ", "  [C] Chloroplast     ", "  [D] Golgi Apparatus"))
        multiple_choice_correct_answers =  ("A", "D", "B", "B", "C", "B", "D", "C", "C", "B")
        true_or_false_questions =          ("The Earth revolves around the Sun once every 24 hours.",
                                            "Photosynthesis is the process by which plants make their own food.",
                                            "The Moon has its own light source.",
                                            "An atom is made up of protons, neutrons, and electrons.",
                                            "The boiling point of water is 100°C (212°F) at sea level.",
                                            "DNA is the molecule that carries genetic information. ",
                                            "Sound travels faster in water than in air.",
                                            "Metals are generally good conductors of electricity.",
                                            "The process of evaporation changes liquid to gas.",
                                            "An ecosystem is a community of living organisms interacting with their environment.")
        true_or_false_options =            (("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"))
        true_or_false_correct_answers =    ("B", "A", "B", "A", "A", "A", "A", "A", "A", "A")

        self.exam_items =  {"Multiple Choice": {"Questions": multiple_choice_questions,
                                                "Options": multiple_choice_options,
                                                "Answers": multiple_choice_correct_answers},
                            "True or False":   {"Questions": true_or_false_questions,
                                                "Options": true_or_false_options,
                                                "Answers": true_or_false_correct_answers}}

class ArtReviewer (Question):
    def __init__(self):
        super().__init__()
        multiple_choice_questions =        ("What are the primary colors?",
                                            "Which of the following is a medium commonly used in drawing?",
                                            "Which of the following refers to the lightness or darkness of a color?",  
                                            "Which of these art forms involves creating three-dimensional objects?",
                                            "Which artist is known for the painting 'Starry Night'?",
                                            "What is the term for the arrangement of elements in a work of art?",
                                            "What is the primary purpose of art criticism?",
                                            "Which of the following is a warm color?",
                                            "Which term describes the technique of using light and shadow to create the illusion of three-dimensionality?",
                                            "Which of these is a famous sculptor?")
        multiple_choice_options =          (("  [A] Red, Green, Blue      ", "  [B] Red, Yellow, Blue              ", "  [C] Red, Blue, White   ", "  [D] Red, Yellow, Green"),
                                            ("  [A] Charcoal              ", "  [B] Clay                           ", "  [C] Metal              ", "  [D] Wood"),
                                            ("  [A] Hue                   ", "  [B] Saturation                     ", "  [C] Value              ", "  [D] Tone"), 
                                            ("  [A] Sculpture             ", "  [B] Painting                       ", "  [C] Photography        ", "  [D] Drawing"),
                                            ("  [A] Claude Monet          ", "  [B] Pablo Picasso                  ", "  [C] Vincent van Gogh   ", "  [D] Leonardo da Vinci"),
                                            ("  [A] Contrast              ", "  [B] Balance                        ", "  [C] Composition        ", "  [D] Rhythm"),
                                            ("  [A] To insult the artist  ", "  [B] To evaluate and interpret art  ", "  [C] To sell artwork    ", "  [D] To teach art techniques"),
                                            ("  [A] Blue                  ", "  [B] Green                          ", "  [C] Red                ", "  [D] Purple"),
                                            ("  [A] Chiaroscuro           ", "  [B] Fresco                         ", "  [C] Impasto            ", "  [D] Sfumato"),
                                            ("  [A] Michelangelo          ", "  [B] Edgar Degas                    ", "  [C] Johannes Vermeer   ", "  [D] Henri Matisse"))
        multiple_choice_correct_answers =  ("B", "A", "C", "A", "C", "C", "B", "C", "A", "A")
        true_or_false_questions =          ("A landscape painting typically features natural scenery.",
                                            "Pablo Picasso is known for co-founding the Cubist movement.",
                                            "The Mona Lisa was painted by Vincent van Gogh.",
                                            "The Impressionist movement was focused on capturing light and movement.",
                                            "Abstract art focuses on realistic depictions of subjects.",
                                            "A still life is a work of art that depicts inanimate objects.",
                                            "The use of perspective in art creates the illusion of depth.",
                                            "Renaissance art is known for its focus on humanism and the natural world.",
                                            "A mural is a large painting that is typically done on a wall or ceiling.",
                                            "The Baroque period is characterized by exaggerated motion and clear detail to produce drama and grandeur in art.")
        true_or_false_options =            (("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"),
                                            ("  [A] True    ", "  [B] False"))
        true_or_false_correct_answers =    ("A", "A", "B", "A", "B", "A", "A", "A", "A", "A")

        self.exam_items =  {"Multiple Choice": {"Questions": multiple_choice_questions,
                                                "Options": multiple_choice_options,
                                                "Answers": multiple_choice_correct_answers},
                            "True or False":   {"Questions": true_or_false_questions,
                                                "Options": true_or_false_options,
                                                "Answers": true_or_false_correct_answers}}
        
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

def Main_Menu():
    """
    Displays the main menu for Group 2's Grade 10 Exam Reviewer.
    Allows the user to choose between reviewing a subject, viewing
    previous exam performance reports, or exiting the program
    """                      
    while True:
        # Display the title of the program
        print("\n\n----------------------  Group 2’s Grade 10 Exam Reviewer  ---------------------\n\n")

        # Greet the user and display the menu options
        print("Hi, {}!".format(user_name.title()))
        print("What do you wish to do?")
        print("  [1] Review a Subject")
        print("  [2] View My Previous Exam Performance Reports")
        print("  [0] None")

        try:
            # Prompt the user to choose an option
            choice = int(input('\n'"Please choose an option: "))
            
            if choice == 1:
                # Navigate to the Review Menu
                Review_Menu()
                  
            elif choice == 2:
                # Navigate to the View Report Menu
                View_Report_Menu()
                  
            elif choice == 0:
                # Navigate to the Exit Menu
                Exit_Menu()

            else:
                # Handle invalid input that is not 1, 2, or 0
                print("Invalid input. Please try again.\n")  
        
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")

def Review_Menu():
    """
    Displays the review menu where the user can select a subject to review.
    The user can choose to review English, Math, Filipino, Science, Art, or
    Random, which is a combination of the aforementioned subjects, or return
    to the main menu.
    """

    # Greet the user with the their name
    print('\n''\n'"-------------------------------  Hello, {}!  -------------------------------"'\n''\n'.format(user_name.title()))

    while True:
        # Display the list of subjects available for review
        print("Which subject do you wish to review?")
        print("  [1] English")
        print("  [2] Math")
        print("  [3] Filipino")
        print("  [4] Science")
        print("  [5] Art")
        print("  [6] Any (Random)")
        print("  [0] Back")

        try:
            # Prompt the user to choose a subject
            choice = int(input('\n'"Please choose an option: "))
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.\n")
            continue # Restart the loop to ask for input again

        # Map the user's choice to the corresponding subject
        if choice == 1: 
            chosen_subject = "English" 
            print("English Subject") 
            ExamReviewer.customize_session(chosen_subject, user_name) 
        
        elif choice == 2: 
            chosen_subject = "Math" 
            print ("Math Subject") 
            ExamReviewer.customize_session(chosen_subject, user_name)  
        
        elif choice == 3: 
            chosen_subject = "Filipino" 
            print("Filipino Subject")
            ExamReviewer.customize_session(chosen_subject, user_name)  
        
        elif choice == 4: 
            chosen_subject = "Science" 
            print("Science Subject") 
            ExamReviewer.customize_session(chosen_subject, user_name) 
        
        elif choice == 5: 
            chosen_subject = "Art" 
            print("Art Subject") 
            ExamReviewer.customize_session(chosen_subject, user_name)  
        
        elif choice == 6: 
            chosen_subject = "Random" 
            print("Random Subject") 
            ExamReviewer.customize_session(chosen_subject, user_name) 

        elif choice == 0:
            # Return to the main menu
            Main_Menu()
            
        else:
            # Handle invalid input that is not 1, 2, 3, 4, 5, 6, or, 0
            print("Invalid input. Please try again.\n")

def View_Report_Menu():
    """
    Displays the menu for viewing previous exam performance reports.
    The user can choose to review a report from a selected subject,
    view reports for all subjects, or return to the main menu.
    """
    while True:
        # Display the header for viewing exam performance reports
        print('\n''\n'"----------------------  Viewing Previous Exam Performance Reports  ---------------------"'\n''\n'.format(user_name.title()))

        # Display the list of subjects for which reports can be viewed
        print("Which subject’s exam performance report do you wish to view?")
        print("  [1] English")
        print("  [2] Math")
        print("  [3] Filipino")
        print("  [4] Science")
        print("  [5] Art")
        print("  [6] All")
        print("  [0] Back")

        try:
            # Prompt the user to select an option
            choice = int(input('\nPlease choose an option: '))
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a number.")
            continue  # Restart the loop to ask for input again

        subjects = ["English", "Math", "Filipino", "Science", "Art"]

        if 1 <= choice <= 5:
            subject = subjects[choice - 1]
            ExamReviewer.generate_report(subject)
        elif choice == 6:
            ExamReviewer.get_all_performance_report()
        elif choice == 0:
            Main_Menu()
        else:
            print("Invalid input. Please try again.")
            continue  # Restart the loop to ask for input again

        # After viewing a report, navigate to the continue menu
        Continue_Menu()

def Continue_Menu():
    """
    Asks the user if they wish to continue using the program or exit.
    The user can choose to return to the main menu for another session
    or exit the program entirely.
    """

    while True:
        # Prompt the user to decide whether to continue using the program
        choice = input('\n'"Do you wish to have another session in the program? (Yes/No): ").lower()
        
        # If yes, return to the main menu for another session
        if choice == "yes":
            Main_Menu()

        # If no, navigate to the exit menu
        elif choice == "no":
            Exit_Menu()

        # Handle invalid input that is not 'yes' or 'no'
        else:
            print("Invalid input. Please try again.")

def Exit_Menu():
    """
    Displays the exit menu, allowing the user to confirm if they want to exit the program.
    If the user chooses to exit, the program will terminate. Otherwise, the user can return to the previous menu
    """
    while True:
        # Prompt the user to confirm if they want to exit the program
        choice_2 = input('\n'"Do you wish to exit the program? (Yes/No): ").lower()

        # If yes, display a farewell message and exit the program
        if choice_2 == "yes":
            print("Thank you for using Group 2’s Grade 10 Exam Reviewer, {}.".format(user_name.capitalize()))
            print("The program will close now.\n")
            exit()

        # If no, return to the previous menu without exiting
        elif choice_2 == "no":
            break
        
        else:
            # Handle invalid input that is not 'yes' or 'no'
            print("Invalid input. Please try again.")

"This is the main loop to run the program" 
while True:
    # Display a welcome message and prompt the user to enter their name.
    print('\n''\n'"----------------------  Welcome to Group 2’s Grade 10 Exam Reviewer  ---------------------"'\n''\n')
    user_name = input('\n'"Please enter your name: ")
    
    # Start the main menu
    Main_Menu()
