# mms146-group2-2024
# PROJECT SPECIFICATIONS: Grade 10 Text-Based Exam Reviewer

### Application Overview

The Grade 10 Text-based Exam Reviewer is a Python-based application designed to help Grade 10 students prepare for exams through interactive text-based quizzes. The project includes a variety of subjects such as English, Math, Filipino, Science and Art. Each subject comes with both multiple-choice and true/false questions which are fully customizable. The goal of this project is to provide students with a comprehensive review tool that allows them to test their knowledge, receive immediate feedback, and review their performance.

#### Key Features

1. **Question Bank**
    - Store a list of exam questions categorized by subject or topic.
    - Implement retrieval of random questions for review.

2. **Answer Storage**
    - Allow students to input their answers to each question.
    - Provide a mechanism to save and retrieve answers for future review.

3. **Performance Analysis**
    - Creates reports that detail the number of questions answered correctly and incorrectly.
    - Calculate overall performance metrics such as scores or percentages.

4. **Customization Options**
    - Provides options to tailor the review experience, such as choosing specific topics only for review, or deciding what types of exams to answer.

#### Class Structure

These are the classes and their specifications that we are expected to implement:

1. **Question Class**
    - Description
      The Question class is responsible for managing individual exam questions. It stores the question text, possible options, the correct answer, and the item number for easy identification. The class also provides methods to display questions and check the user's answers.
      
    - Features
      - Question Storage: Holds the question text, options, and correct answer.
      - Display Functionality: Displays the question and options to the user, and collects their answer.
      - Answer Checking: Compares the user's input to the correct answer and tracks the result.
     
    - Class Structure
      - Attributes
        - question_text: Stores the text of the question.
        - options: A list of possible answers for multiple-choice questions.
        - correct_answer: Stores the correct answer for the question.
        - item_number: Identifies the question number in the exam.
          
      - Methods
        - display_questions(self):
          Displays the current question and its possible options. After the user submits an answer, it calls the check_answer() method to verify if the answer is correct. It also asks the user if they want to view their performance report.
        - check_answer(self):
          Checks whether the answer submitted by the user matches the correct answer. This method also calls the save_answer() method from the Student class to record the user's answer.

2. **Student Class**
    - Description
      The Student Class stores the data designed to represent each user engaging with the application. This class encapsulates the key attributes and methods necessary for managing a student's interaction with the review system, tracking their progress, and generating performance reports.
      
    - Features
      - Recognizes the name of the user and logs it.
      - Allows users to save answers they have given using the save_answer() method.
      - Allows users to generate a performance report using the get_performance_report() method.
   
    - Class Structure
      - Attributes
        - name: stores the name of the student
        - english_answers_given: stores the answers given by the user in the english reveiwer
        - filipino_answers_given: stores the answers given by the user in the filipino reveiwer
        - math_answers_given: stores the answers given by the user in the math reveiwer
        - art_answers_given: stores the answers given by the user in the art reveiwer
        - science_answers_given: stores the answers given by the user in the science reveiwer
      
      - Methods
        - save_answer()
          Saves the answers inputted by the user to a list.
        - get_performance_report()
          Generates a report depending on the performance of the user during the review session.

3. **ExamReviewer Class**
    - Description
      The Exam Reviewer Class provides the methods necessary to generate randomized questions for the user, help them customize their review sessions, and compile detailed performance reports so that they can look back at their results.
      
    - Features
      - Allows for randomization of questions using the generateRandomQuestions method.
      - Allows for customization of review session using the customizeSession method.
      - Allows for a full performance report on one subject using the generateReport method.
      - Allows for full performance report based off the data from all sessions using the get_all_performance_reports() method.

    - Class Structure
      - Attributes
        - subject: corresponds to the subject based off the categories given which the user wants to choose
        - questions: stores the questions found on each reviewer
        - student_answers: stores the answers given by the student per reviewer
          
      - Methods
        - generateRandomQuestions:
          Generates a list of random questions for the user.
        - customizeSession:
          Enables customization of the review session based on topic, type of questions, and number of questions.
        - generateReport:
          Generates a full report on one subject alone.
        - get_all_performance_reports():
          Generates a full performance report derived from all sessions.
     
4. **Menu Methods**
    - Description
      The Menu Methods are a collection of options that the user can choose from, each with a specific function to guide the user through the review process like customizing the reviewer, viewing performance reports, asking users if they wish to renew a session by continuing the review, and many more.

    - Key Features
      - Main Menu (Main_Menu)
        - Initially displays the main menu options for the user to choose from:
          [1] Review
          [2] View Report
          [3] If none is chosen, the options shown are:
          [4] Continue
          [0] Exit

      - Review Menu (Review_Menu)
        - Asks the user which subject they would like to review.
        - Alternatively, they can choose to go back to the previous menu options if they wish to go a different route (Main_Menu).

      - View Report Menu (View_Report_Menu)
        - Asks the user which among the subject’s performance report they have accomplished do they wish to view.
        - Defines the user’s choices for each subject’s performance report.

      - Continue Menu (Continue_Menu)
        - Asks the user if they wish to have another review session.
        - If yes, they are sent back to the Main_Menu, otherwise, they are sent to the Exit_Menu.

      - Exit Menu (Exit_Menu)
        - Asks the user if they want to exit the program
        - If yes, the program ends, otherwise, they are sent back to Continue_Menu.
        
      - Run the Program
        - Asks the user to enter their name in order to start the program.
        - After input, the user will be directed to Main_Menu.

### Important Notes

You will find a file named `Group2_Grade_10_Exam_Reviewer.py` in the `main` directory. Here’s what you need to know about it:

- **Purpose of the File:**
  The `Group2_Grade_10_Exam_Reviewer.py` file combines all the individual code files (`student.py`, `question.py`, `examreviewer.py`, and `menu.py`) into a single script. It’s provided to ensure that you can run the complete project seamlessly.

- **Why Combine?**
  The program was originally designed to be in a single file. However, to track individual contributions and modularize development, we decided to separate the code into different files. The consolidated file brings all those modules together into one script.

- **How to Use:**
  To test our exam reviewer, run the `Group2_Grade_10_Exam_Reviewer.py` file. This file should execute without issues and reflects the complete functionality of the project as intended.


### Credits

This project was done by the following members:

- Baltazar, Aurea Xyreece
  https://github.com/xyreecebaltazar
- Catalan, Glyza Gayle
  https://github.com/glyzacatalan
- Catalan, Maria Graciella
  https://github.com/MargaCatalan
- Certeza, Ulienee Lleonor
  https://github.com/certezayenny
- Cudia, Shanley Pearl
  https://github.com/scudia
- Daquil, Trixia
  https://github.com/tadaquil
- Feliciano, Susanna Beatrix
  https://github.com/sbeafeliciano
- Guiang, Gianina Alexandra
  https://github.com/Nina-118
- Magpayo, Michelle
  https://github.com/ChelGRPI1
- Villarin, Leslie Mae
  https://github.com/lvillarin

