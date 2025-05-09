from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))


quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed this Quiz")
print(f"Your total score is {quiz.score}/{quiz.question_number}")