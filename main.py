from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

que_data = []
for rec in question_data:
    que_data.append(Question(rec['text'], rec['answer']))

brain = QuizBrain(que_data)

while brain.still_has_questions():
    brain.next_question()
print("You have completed the quiz.")
print(f"Your final score was : {brain.score}/{len(que_data)}")
