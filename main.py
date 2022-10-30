from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in range(len(question_data)):
    new_question = Question(question_data[data]["question"], question_data[data]["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz_brain.score}/{quiz_brain.question_number}.")