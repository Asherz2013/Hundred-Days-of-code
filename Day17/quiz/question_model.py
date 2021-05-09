# New question class
# Holds the text to show and the answer of said question

class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer
