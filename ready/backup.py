import random

class QuizQuestion:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.high_scores = []
        self.username = ""
       

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        random.shuffle(self.questions)
        correct_answers = []  # To store correct answers
        incorrect_answers = []  # To store incorrect answers
        for question_num, question in enumerate(self.questions, start=1):

            if question_num == 1:
                print(f"/*--- WELCOME {self.username} ----*/")
            
            print(f"Question {question_num}: {question.question}")
            print(question.question)
           
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")

            while True:
                user_answer = input("Enter the number of your answer (1 to 4): ")
                if user_answer.isdigit():
                    user_answer = int(user_answer)
                    if 1 <= user_answer <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                else:
                    print("Invalid input. Please enter a valid number.")

            if question.is_correct(user_answer - 1):
                print("Hurray, Correct !\n")
                self.score += 1
                correct_answers.append(question)
                print("/-------------------/\n")
            else:
                print("Oh, Wrong Answer!\n")
                incorrect_answers.append((question, user_answer))
                print("/-------------------/\n")

        percentage_score = (self.score / len(self.questions)) * 100
        print(f"You got {self.score} out of {len(self.questions)} questions correct.")
        print(f"Your percentage score: {percentage_score:.2f}%")

        # Provide feedback on correct and incorrect answers
        print("\nCorrectly answered questions:")
        for i, question in enumerate(correct_answers, start=1):
            print(f"{i}. {question.question}")

        print("\nIncorrectly answered questions:")
        for i, (question, user_answer) in enumerate(incorrect_answers, start=1):
            print(f"{i}. {question.question}")
            print(f"Your answer: {question.options[user_answer - 1]}")
            print(f"Correct answer: {question.options[question.correct_option]}\n")
      

    def reset(self):
        self.score = 0

    def add_high_score(self, username, score):
        self.high_scores.append((username, score))

    def get_average_score(self):
        if not self.high_scores:
            return 0
        total_score = sum(score for _, score in self.high_scores)
        return total_score / len(self.high_scores)

if __name__ == "__main__":
    quiz = Quiz()

    # The Quiz Questions
    question1 = QuizQuestion("What is the capital of England?", ["London", "Berlin", "Paris", "Madrid"], 0)
    question2 = QuizQuestion("Who among the following president of the United States was driven by the Queen?", ["Obama", "Trump", "Biden", "Nixon"], 0)
    question3 = QuizQuestion("What is the speed limit on highways in the United Kingdom", ["30mph", "40mph", "80mph", "70mph"], 3)
    question4 = QuizQuestion("What is most widely used web programming lanaguage", ["Python ", "Javascript", "PHP", "Java"], 2)
    question5 = QuizQuestion("Which ocean seperates Africa from the Americas", ["Atlantic", "Pacific", "Indian", "Artic"], 0)
    question6 = QuizQuestion("Which English city are the Beatles from?", ["Manchester", "London", "Birmingham", "Liverpool"], 3)
    question7 = QuizQuestion("What is the official London residence of the Queen?", ["Buckingham Palace", "London", "Chester", "Tower Bridge"], 0)
    question8 = QuizQuestion("In which city was the soft drink Vimto invented?", ["Newcastle", "London", "Manchester", "Liverpool"], 1)
    question9 = QuizQuestion("Which English team city won the most UEFA champions league?", ["Manchester", "Liverpool", "Birmingham", "Nottingham"], 1)
    question10 = QuizQuestion("Which British author wrote Oliver Twist?", ["Charles Dickens", "Charles Ken", "Charles Jones", "Charles Bolt"], 0)
    question11 = QuizQuestion("Is an English bulldog bigger or smaller than a French bulldog?", ["Same size", "Smaller", "Bigger", "Twice as Big"], 2)
    question12 = QuizQuestion("In which city can you find the Clifton Suspension bridge?", ["Manchester", "London", "Bristol", "Liverpool"], 2)
    question13 = QuizQuestion("In which city was Cadbury founded?", ["Manchester", "London", "Birmingham", "Liverpool"], 2)
    question14 = QuizQuestion("Which secret agent organisation does James Bond work for?", ["1953", "M16", "CIA", "KGB"], 0)
    question15 = QuizQuestion("In which UK city was the rock band ‘Oasis’ formed?", ["Brigthon", "London", "Birmingham", "Manchester"], 3)

#appending the questions to the class quiz to create each question instance
    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)
    quiz.add_question(question4)
    quiz.add_question(question5)
    quiz.add_question(question6)
    quiz.add_question(question7)
    quiz.add_question(question8)
    quiz.add_question(question9)
    quiz.add_question(question10)
    quiz.add_question(question11)
    quiz.add_question(question12)
    quiz.add_question(question13)
    quiz.add_question(question14)
    quiz.add_question(question15)

    

#Loop running the app , basically the main running logic flow
    while True:
        quiz.username = input("Please provide us with your name: ")
        if not quiz.username:
            print("Oh sorry, name cant be empty. Please input your name.")
            continue

        while True:
            num_questions = input("Enter the number of questions you want to answer: ")
            if num_questions.isdigit():
                num_questions = int(num_questions)
                if 1 <= num_questions <= len(quiz.questions):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(quiz.questions)}.")
            else:
                print(f"Oh, Invalid input. Please enter a valid number NOTE:(only numbers between 1 and {len(quiz.questions)}) is accepted.")

        selected_questions = random.sample(quiz.questions, num_questions)
        quiz.questions = selected_questions
        quiz.take_quiz()
        quiz.add_high_score(quiz.username, quiz.score) 
        average_score = quiz.get_average_score()
        
        
        choice = input("Do you want to take the quiz again? (yes/no): ")
        if choice.lower() == 'no':
            break

    # Displaying high scores
    print("High Scores:")
    for i, (username, score) in enumerate(sorted(quiz.high_scores, key=lambda x: x[1], reverse=True)[:5], start=1):
        print(f"{i}. {username}: Score: {score}")
    print(f"Average score: {average_score:.2f}")
