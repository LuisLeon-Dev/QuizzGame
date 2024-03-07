# TODO: create __init__ method with the question number and question list
class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0

# TODO: asking the questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text}? (True/False): ")

        return user_answer

# TODO: checking if the answer was correct

# TODO: checking if we're the end of the game

