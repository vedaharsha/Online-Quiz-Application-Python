import json
import random
import os


class QuizApp:

    def __init__(self):
        self.leaderboard_file = "leaderboard.json"

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Paris", "Madrid", "Lisbon"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "answer": "Mars"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
                "answer": "Pacific"
            },
            {
                "question": "Who wrote 'To Kill a Mockingbird'?",
                "options": [
                    "Harper Lee",
                    "George Orwell",
                    "J.K. Rowling",
                    "Mark Twain"
                ],
                "answer": "Harper Lee"
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["China", "Japan", "Thailand", "India"],
                "answer": "Japan"
            },
            {
                "question": "What is the boiling point of water?",
                "options": ["90°C", "100°C", "110°C", "120°C"],
                "answer": "100°C"
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["1", "2", "3", "5"],
                "answer": "2"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["O2", "H2O", "CO2", "NaCl"],
                "answer": "H2O"
            },
            {
                "question": "Which year did World War II end?",
                "options": ["1945", "1939", "1918", "1950"],
                "answer": "1945"
            },
            {
                "question": "What is the speed of light?",
                "options": [
                    "3x10^8 m/s",
                    "3x10^6 m/s",
                    "1x10^8 m/s",
                    "3x10^7 m/s"
                ],
                "answer": "3x10^8 m/s"
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["Gold", "Oxygen", "Osmium", "Oxide"],
                "answer": "Oxygen"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": [
                    "Leonardo da Vinci",
                    "Van Gogh",
                    "Picasso",
                    "Raphael"
                ],
                "answer": "Leonardo da Vinci"
            },
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Kyoto", "Osaka", "Nagoya"],
                "answer": "Tokyo"
            },
            {
                "question": "Which gas do plants primarily use for photosynthesis?",
                "options": [
                    "Oxygen",
                    "Carbon Dioxide",
                    "Nitrogen",
                    "Helium"
                ],
                "answer": "Carbon Dioxide"
            },
            {
                "question": "Who is known as the father of computers?",
                "options": [
                    "Alan Turing",
                    "Charles Babbage",
                    "Tim Berners-Lee",
                    "Bill Gates"
                ],
                "answer": "Charles Babbage"
            },
            {
                "question": "What is the square root of 144?",
                "options": ["10", "12", "14", "16"],
                "answer": "12"
            },
            {
                "question": "Which planet is closest to the Sun?",
                "options": ["Venus", "Earth", "Mercury", "Mars"],
                "answer": "Mercury"
            },
            {
                "question": "What is the capital of Germany?",
                "options": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
                "answer": "Berlin"
            },
            {
                "question": "Who discovered gravity?",
                "options": ["Newton", "Einstein", "Galileo", "Tesla"],
                "answer": "Newton"
            },
            {
                "question": "What is the symbol for gold?",
                "options": ["Au", "Ag", "Gd", "Go"],
                "answer": "Au"
            },
            {
                "question": "Which desert is the largest hot desert in the world?",
                "options": ["Sahara", "Kalahari", "Gobi", "Thar"],
                "answer": "Sahara"
            },
            {
                "question": "Which year did humans first land on the Moon?",
                "options": ["1969", "1970", "1968", "1971"],
                "answer": "1969"
            },
            {
                "question": "Which is the largest continent?",
                "options": ["Africa", "Asia", "Europe", "Antarctica"],
                "answer": "Asia"
            },
            {
                "question": "What is the longest river traditionally recognized in the world?",
                "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
                "answer": "Nile"
            },
            {
                "question": "What is the chemical symbol for sodium?",
                "options": ["S", "Na", "So", "Sn"],
                "answer": "Na"
            },
            {
                "question": "Who is the author of 'Pride and Prejudice'?",
                "options": [
                    "Jane Austen",
                    "Charlotte Brontë",
                    "Emily Brontë",
                    "Virginia Woolf"
                ],
                "answer": "Jane Austen"
            },
            {
                "question": "Which planet is famous for its prominent rings?",
                "options": ["Mars", "Saturn", "Jupiter", "Neptune"],
                "answer": "Saturn"
            },
            {
                "question": "Which gas is most abundant in Earth's atmosphere?",
                "options": [
                    "Oxygen",
                    "Nitrogen",
                    "Carbon Dioxide",
                    "Hydrogen"
                ],
                "answer": "Nitrogen"
            },
            {
                "question": "Which organ is primarily responsible for filtering blood?",
                "options": ["Liver", "Kidney", "Heart", "Lungs"],
                "answer": "Kidney"
            },
            {
                "question": "What is the capital of Italy?",
                "options": ["Rome", "Milan", "Naples", "Florence"],
                "answer": "Rome"
            },
            {
                "question": "Which metal is liquid at room temperature?",
                "options": ["Mercury", "Gold", "Silver", "Lead"],
                "answer": "Mercury"
            },
            {
                "question": "What is the national animal of India?",
                "options": ["Lion", "Tiger", "Elephant", "Peacock"],
                "answer": "Tiger"
            },
            {
                "question": "What does DNA stand for?",
                "options": [
                    "Deoxyribonucleic Acid",
                    "Dinucleic Acid",
                    "Deoxynucleic Acid",
                    "Dinitrogen Acid"
                ],
                "answer": "Deoxyribonucleic Acid"
            },
            {
                "question": "What is the smallest country in the world?",
                "options": [
                    "Vatican City",
                    "Monaco",
                    "San Marino",
                    "Liechtenstein"
                ],
                "answer": "Vatican City"
            },
            {
                "question": "Who invented the telephone?",
                "options": [
                    "Alexander Graham Bell",
                    "Thomas Edison",
                    "Nikola Tesla",
                    "James Watt"
                ],
                "answer": "Alexander Graham Bell"
            },
            {
                "question": "Which country gifted the Statue of Liberty to the USA?",
                "options": ["France", "Italy", "UK", "Spain"],
                "answer": "France"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Jupiter", "Saturn", "Neptune"],
                "answer": "Jupiter"
            },
            {
                "question": "Which programming language is known for the snake logo?",
                "options": ["Java", "Python", "C++", "Ruby"],
                "answer": "Python"
            },
            {
                "question": "What does CPU stand for?",
                "options": [
                    "Central Processing Unit",
                    "Computer Personal Unit",
                    "Central Program Utility",
                    "Control Processing Unit"
                ],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which data structure follows FIFO?",
                "options": ["Stack", "Queue", "Tree", "Graph"],
                "answer": "Queue"
            },
            {
                "question": "Which data structure follows LIFO?",
                "options": ["Queue", "Stack", "Array", "Linked List"],
                "answer": "Stack"
            },
            {
                "question": "What is the extension of a Python file?",
                "options": [".java", ".py", ".cpp", ".html"],
                "answer": ".py"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "def", "func", "define"],
                "answer": "def"
            },
            {
                "question": "Which keyword is used to create a class in Python?",
                "options": ["object", "class", "struct", "define"],
                "answer": "class"
            },
            {
                "question": "Which library is commonly used for numerical computing in Python?",
                "options": ["NumPy", "Flask", "Django", "Tkinter"],
                "answer": "NumPy"
            },
            {
                "question": "Which library is commonly used for data analysis in Python?",
                "options": ["Pandas", "Turtle", "Random", "OS"],
                "answer": "Pandas"
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "#", "/*", "--"],
                "answer": "#"
            },
            {
                "question": "What is the result of 10 // 3 in Python?",
                "options": ["3", "3.33", "1", "0"],
                "answer": "3"
            },
            {
                "question": "Which keyword is used to handle exceptions in Python?",
                "options": ["catch", "try", "exception", "handle"],
                "answer": "try"
            },
            {
                "question": "Which function is used to find the length of a list in Python?",
                "options": ["size()", "length()", "len()", "count()"],
                "answer": "len()"
            },
            {
                "question": "Which collection stores key-value pairs in Python?",
                "options": ["List", "Tuple", "Set", "Dictionary"],
                "answer": "Dictionary"
            }
        ]

        self.load_leaderboard()

    # -----------------------------
    # Leaderboard Functions
    # -----------------------------

    def load_leaderboard(self):
        try:
            if os.path.exists(self.leaderboard_file):
                with open(self.leaderboard_file, "r") as file:
                    self.leaderboard = json.load(file)
            else:
                self.leaderboard = {}

        except (json.JSONDecodeError, OSError):
            self.leaderboard = {}

    def save_leaderboard(self):
        try:
            with open(self.leaderboard_file, "w") as file:
                json.dump(self.leaderboard, file, indent=4)

        except OSError:
            print("Unable to save leaderboard.")

    def update_leaderboard(self, username, score):
        previous_score = self.leaderboard.get(username, 0)

        if score > previous_score:
            self.leaderboard[username] = score
            self.save_leaderboard()

    def display_leaderboard(self):

        print("\n" + "=" * 45)
        print("              LEADERBOARD")
        print("=" * 45)

        if not self.leaderboard:
            print("No scores available yet.")
            return

        sorted_scores = sorted(
            self.leaderboard.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for rank, (username, score) in enumerate(
                sorted_scores[:10], start=1):

            print(f"{rank}. {username:<20} {score:>5} points")

        print("=" * 45)

    # -----------------------------
    # Ask Question
    # -----------------------------

    def ask_question(self, question_data, question_number, total_questions):

        print("\n" + "-" * 55)
        print(f"Question {question_number} of {total_questions}")
        print("-" * 55)

        print(question_data["question"])

        options = question_data["options"][:]
        random.shuffle(options)

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))

                if 1 <= answer <= len(options):
                    selected_option = options[answer - 1]

                    if selected_option == question_data["answer"]:
                        print("Correct! +10 points")
                        return True
                    else:
                        print(
                            f"Wrong! Correct answer: "
                            f"{question_data['answer']}"
                        )
                        return False

                else:
                    print("Please enter a number between 1 and 4.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    # -----------------------------
    # Start Quiz
    # -----------------------------

    def start_quiz(self, username):

        score = 0
        correct_answers = 0
        wrong_answers = 0

        # Select 5 random questions
        quiz_questions = random.sample(self.questions, 5)

        print("\n" + "=" * 55)
        print("                 QUIZ STARTED")
        print("=" * 55)
        print(f"Player: {username}")
        print("Questions: 5")
        print("Correct Answer: +10")
        print("Wrong Answer: -5")

        for question_number, question in enumerate(
                quiz_questions, start=1):

            is_correct = self.ask_question(
                question,
                question_number,
                len(quiz_questions)
            )

            if is_correct:
                score += 10
                correct_answers += 1
            else:
                score -= 5
                wrong_answers += 1

        # Prevent negative final score
        score = max(score, 0)

        percentage = (correct_answers / 5) * 100

        print("\n" + "=" * 55)
        print("                 QUIZ RESULT")
        print("=" * 55)

        print(f"Player          : {username}")
        print(f"Correct Answers : {correct_answers}")
        print(f"Wrong Answers   : {wrong_answers}")
        print(f"Score           : {score} points")
        print(f"Percentage      : {percentage:.2f}%")

        if percentage == 100:
            print("Performance     : Excellent!")
        elif percentage >= 60:
            print("Performance     : Good job!")
        else:
            print("Performance     : Keep practicing!")

        print("=" * 55)

        # Update leaderboard
        self.update_leaderboard(username, score)

        print("\nYour best score has been saved!")

    # -----------------------------
    # Main Menu
    # -----------------------------

    def run(self):

        while True:

            print("\n" + "=" * 45)
            print("         ONLINE QUIZ APPLICATION")
            print("=" * 45)

            print("1. Start Quiz")
            print("2. Show Leaderboard")
            print("3. Quit")

            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":

                username = input(
                    "Enter your username: "
                ).strip()

                if username:
                    self.start_quiz(username)

                else:
                    print("Username cannot be empty.")

            elif choice == "2":

                self.display_leaderboard()

            elif choice == "3":

                print("\nThank you for using the Online Quiz Application!")
                print("Goodbye!")
                break

            else:

                print("Invalid choice. Please select 1, 2, or 3.")


def main():

    app = QuizApp()
    app.run()


if __name__ == "__main__":
    main()