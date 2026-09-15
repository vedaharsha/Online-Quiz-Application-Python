# Online Quiz Application with Leaderboard

A Python-based console quiz application that allows users to answer randomly selected questions, receive scores, and compete through a persistent leaderboard.

## Project Overview

The application randomly selects 5 questions from a collection of 50 questions. Users answer multiple-choice questions and receive points based on their performance.

Correct answers receive **+10 points**, while incorrect answers receive **-5 points**.

The application also maintains a leaderboard using a JSON file.

## Features

- 50-question question bank
- Random selection of 5 questions
- Randomized answer options
- Username-based quiz sessions
- Input validation
- Correct answer feedback
- +10 points for correct answers
- -5 points for incorrect answers
- Final score calculation
- Percentage calculation
- Correct and wrong answer statistics
- Performance feedback
- Top 10 leaderboard
- Best score tracking
- Persistent leaderboard using JSON
- Error handling
- Replay without restarting the application

## Technologies Used

- Python
- JSON
- Random module
- OS module
- Object-Oriented Programming
- File Handling
- Exception Handling

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vedaharsha/Online-Quiz-Application-Python.git
```

### 2. Open the project folder

```bash
cd Online-Quiz-Application-Python
```

### 3. Run the application

```bash
python online_quiz.py
```

If `python` does not work, try:

```bash
py online_quiz.py
```

## How the Application Works

1. The user selects **Start Quiz**.
2. The user enters a username.
3. The application randomly selects 5 questions.
4. The answer options are shuffled.
5. The user selects an answer.
6. The application validates the input.
7. Correct answers receive +10 points.
8. Incorrect answers receive -5 points.
9. The final score and percentage are displayed.
10. The user's best score is stored in the leaderboard.

## Leaderboard

The application stores leaderboard information in:

```text
leaderboard.json
```

The leaderboard displays the top 10 players based on their best scores.

## Learning Outcomes

This project helped me strengthen my understanding of:

- Python programming
- Object-Oriented Programming
- Lists and dictionaries
- Functions and classes
- Randomization
- File handling
- JSON data storage
- Exception handling
- Input validation
- Program logic

## Future Enhancements

- Tkinter graphical user interface
- Difficulty levels
- Timer for each question
- Category-based quizzes
- Database-based leaderboard
- User authentication
- Online multiplayer quiz mode

## Author

Veda Harsha
