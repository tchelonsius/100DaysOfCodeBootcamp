import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = '#375362'


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.config(padx=20,pady=20)
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        self.button_pressed = False

        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,125,
            width=280,
            text=self.quiz.next_question(),
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)

        # score label
        self.score = tk.Label(
            text=f"score: {self.quiz.score}",
            font=("Arial", 15, "bold"),
            background=THEME_COLOR
        )
        self.score.grid(column=1, row=0)

        # images
        false_img = tk.PhotoImage(file="images/false.png")
        true_img = tk.PhotoImage(file="images/true.png")

        # buttons
        self.false_button = tk.Button(image=false_img, highlightthickness=0, command=self.true_pressed)
        self.false_button.grid(column=0,row=2)
        self.true_button = tk.Button(image=true_img, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(column=1, row=2)

        self.window.mainloop()

    def true_pressed(self):
        if self.button_pressed:
            return
        self.button_pressed = True
        if self.quiz.check_answer("true"):
            self.canvas.config(background="green")
            self.score.config(text=f"score: {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        self.window.after(700,func=self.show_next_question)

    def false_pressed(self):
        if self.button_pressed:
            return
        self.button_pressed = True
        if self.quiz.check_answer("false"):
            self.canvas.config(background="green")
            self.score.config(text=f"score: {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        self.window.after(700, func=self.show_next_question)

    def show_next_question(self):
        if not self.quiz.still_has_questions():
            self.canvas.config(background="white")
            self.canvas.itemconfig(
                self.question_text,
                text=f"End of the quiz. Your final score: {self.quiz.score}/{len(self.quiz.question_list)}"
            )
        else:
            self.canvas.config(background="white")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
            self.button_pressed = False
