from question_model import Question
from data import question_data
import random

question_bank = []
print("This is the bank of questions: ", question_bank)

for data in question_data:
    text = data["text"]
    answer = data["answer"]
    question = Question(text, data)
    question_bank.append(question)

