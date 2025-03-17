# Day 17: Implementing our own classes
# Main Project: Quiz Game
# The goal of this exercise was to develop further skills in OOP, by implementing a
# quiz game, which, from a database of questions, asks the user whether the given
# sentences are true or false and returns the user's score. The class Question has
# the attributes text and answer, that will be used as a model for creating a list
# with the questions from the database. The class QuizBrain is essentially the game
# engine, that contains the attributes question_number (current question), (score and
# questions_list,) and the methods next_question(), still_has_questions() and check_answer(user_ans, correct_ans).


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = []
for item in question_data:
    questions.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()

