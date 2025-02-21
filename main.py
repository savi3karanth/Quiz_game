from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = QuizBrain(question_bank)

while quizz.still_having_question():
    quizz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quizz.score}/{quizz.question_number}")
