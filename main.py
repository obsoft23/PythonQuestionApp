import random
from question_class import QuizQuestion
from question_class import Quiz


if __name__ == "__main__": #making sure am running the main program script
    quiz = Quiz()

    # creating each question object and with its properties, options and answer
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

    

#Loop running the app , basically the main app running logic flow
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

        selected_questions = random.sample(quiz.questions, num_questions) #chosing random elements from the quiz questions list
        quiz.questions = selected_questions
        quiz.take_quiz()
        quiz.add_high_score(quiz.username, quiz.score)  #storing each username and score
        average_score = quiz.get_average_score()
        selected_questions = 0
        quiz.reset()
        
        
        choice = input("Do you want to take the quiz again? (yes/no): ")
        if choice.lower() == 'no':
            break

    #  high scores caluclated display
    print("High Scores:")
    for i, (username, score) in enumerate(sorted(quiz.high_scores, key=lambda x: x[1], reverse=True)[:5], start=1):
        print(f"{i}. {username}: Score: {score}")
    print(f"Average attempted user score: {average_score:.2f}")
