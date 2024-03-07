from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    question = Question(text, data)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()
