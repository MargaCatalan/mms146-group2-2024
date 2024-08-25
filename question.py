# Task Code: Question_1
class Question:
    def __init__(self):
        self.question_text = None
        self.options = None
        self.correct_answer = None
        self.exam_questions = []
        self.exam_answers = []


# Task Code: Question_2
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
        









