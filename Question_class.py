import random 


#defining a class about each question and its properties
class QuizQuestion:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

#a class about each quiz 

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
        correct_answers = []  # to keep track of correct answers
        incorrect_answers = []  # will keep track of incorrect answers
        for question_num, question in enumerate(self.questions, start=1): # to loop through index and element

            if question_num == 1:
                print(f"/*--- WELCOME {self.username} ----*/")
            
            print(f"(Question {question_num} ) : {question.question}")
           
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")
                

            while True:
                user_answer = input("Please provide your answer, between (1 to 4): ")
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