from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import random


import tkinter

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer =question["correct_answer"]
    question_false=question["incorrect_answers"]
    random_index=random.choice([0,1,2,3])
    question_false.insert(random_index, question_answer)
    new_question = Question(question_text, question_answer,question_false)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quize_ui=QuizInterface(quiz)
#while quiz.still_has_questions():
    #quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
