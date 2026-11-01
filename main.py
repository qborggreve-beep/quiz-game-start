from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quizbrain = Quizbrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()
else:
    quizbrain.end_quiz()




