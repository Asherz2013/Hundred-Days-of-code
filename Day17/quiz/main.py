from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# For loop to iterate over the question_data
for entry in question_data:
    # Create a Question object from each entry in question_data
    question = Question(entry["question"], entry["correct_answer"])
    # Append each Question object to the question_bank
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")
