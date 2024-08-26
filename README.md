# mms146-group2-2024
# PROJECT SPECIFICATIONS: EXAM REVIEWER

### Application Overview

The text-based exam reviewer system will serve as a tool for students to review exam questions and answers in a structured manner. For simplicity, the question types are either true or false or multiple choice. It will allow students to access a list of questions, store their answers, and generate performance reports based on their responses.


#### Key Features

1. **Question Bank**

    - Store a list of exam questions categorized by subject or topic.
    - Implement retrieval of random questions for review.

2. **Answer Storage**

    - Allow students to input their answers to each question.
    - Provide a mechanism to save and retrieve answers for future review.

3. **Performance Analysis**

    - Generate reports showing the number of correct and incorrect answers.
    - Calculate overall performance metrics such as scores or percentages.

4. **Customization Options**

    - Allow customization of the review session, such as selecting specific topics or setting time limits.

#### Class Structure

These are the classes and their specifications that we are expected to implement:

1. **Question Class**
    - Attributes:
      - question_text - the question to be displayed to the user
      - options - the choices (true/false, multiple choice)
      - correct_answer - the correct answer for the question
        
    - Methods:
      - display_question - show the selected question to the user
      - check_answer - check the correctness of the answer of the user

2. **Student Class**
    - Attributes:
      - name - name of the student
      - answers - answers given
        
    - Methods:
      - save_answer - save the answer of the student to a list
      - get_performance_report - generate the performance of the student for the review session

3. **ExamReviewer Class**
    - Methods
      - generateRandomQuestions - build a list of random questions for the user
      - customizeSession - let the user customize the review session (type of question, number of question, topic, etc.)
      - generateReport - generate the report of the review session (performance of the students, questions and right answers)

### Important Notes
You will find a file named `Group2_Grade 10 Exam Reviewer.py` in the `main` directory. Here’s what you need to know about it:
    - **Purpose of the File:** The `Group2_Grade 10 Exam Reviewer.py` file combines all the individual code files (`student.py`, `question.py`, `examreviewer.py`, and `menu.py`) into a single script. It’s provided to ensure that you can run the complete project.
    - **Why Combine?:** The program was originally designed to be in a single file. However, we decided to separate the code into different files to track individual contributions and modularize development
    - **How to Use:** To test our exam reviewer, run the `Group2_Grade 10 Exam Reviewer.py` file. This file should execute without issues and reflects the complete functionality of the project as intended.
