# Quiz-Application
Quiz Application

This repository contains a simple Python-based quiz application. The project consists of two scripts:

questions.py: A script to create a questions.txt file containing multiple-choice quiz questions.

quiz_application.py: A quiz application script that reads the questions from questions.txt, allows users to attempt the quiz, and stores the results in scores.txt.

Features

Interactive command-line interface.

Validates user input for selecting answers.

Keeps track of the user's score.

Stores scores in a file (scores.txt) for future reference.

Files in the Repository

1. questions.py

This script creates a questions.txt file with predefined questions, options, and correct answers.

File Output:

questions.txt

Questions Format:
Each question is stored in the following format:

Question,Option1,Option2,Option3,Option4,CorrectOption

Example:

What is the capital of France?,Berlin,Madrid,Paris,Rome,C

2. quiz_application.py

This script provides the main quiz functionality:

Reads questions from questions.txt.

Prompts the user for their name.

Validates user input for selecting an answer.

Displays whether the selected answer is correct or not.

Saves the user's score in scores.txt.

File Input:

questions.txt: Contains the quiz questions.

File Output:

scores.txt: Stores the user's name and score in the format:

USER NAME, SCORES
John Doe,3/5

How to Use

Prerequisites

Ensure you have Python installed on your system (Python 3.6 or higher).

Steps to Run

Clone this repository:

git clone https://github.com/SunnyS-aurabh/Quiz-Application.git

Run questions.py to generate the questions.txt file:

python questions.py

Run the quiz application:

python quiz_application.py

Follow the on-screen instructions to attempt the quiz.

Rules for the Quiz

Each question has four options (A, B, C, D).

Enter your answer by typing the option (A, B, C, or D).

Scores are calculated based on correct answers.

Example Execution

Sample Input and Output:

Welcome to the Quiz Application!
Rules:
- Each question has 4 options.
- Enter the option (A, B, C, D) as your answer.

Press Enter to Start!

Please Enter Your Name: John Doe

Question 1: What is the capital of France?
A. Berlin
B. Madrid
C. Paris
D. Rome
Enter the option! C
Your Answer: C
Correct!

Question 2: What is the largest planet in our solar system?
A. Mercury
B. Venus
C. Earth
D. Jupiter
Enter the option! D
Your Answer: D
Correct!
...

Quiz Complete!
Your Score: 4/5

Error Handling

If questions.txt is missing, the application displays an error message: Error: The questions.txt file is missing.

If any file operation fails, an error message is displayed with details.


Contribution

Feel free to fork this repository and submit pull requests for improvements or additional features. Suggestions are always welcome!
