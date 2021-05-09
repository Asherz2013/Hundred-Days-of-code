# Class to manage the quiz state

# TODO: Asking the questions
# TODO: Checking if the answer was correct
# TODO: Checking if we're at the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_choice, correct_answer):
        if user_choice.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        # Retrieve the item at the current question_number from the questions_list.
        # Use the input() frunction to show the user the Question Text and ask for the user's answer.
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_choice, question.answer)
