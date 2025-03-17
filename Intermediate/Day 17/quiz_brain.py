class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def next_question(self):
        users_answer = input(f"Q.{self.question_number+1}) {self.questions_list[self.question_number].text} (True/False): ")
        self.check_answer(users_answer, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, users_ans, correct_ans):
        if users_ans.lower()==correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"Your current score is: {self.score}/{self.question_number+1}")

