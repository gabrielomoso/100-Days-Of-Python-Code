from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Row 0
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        # Row 1
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text questions",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Row 2
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(command=self.true_pressed)
        self.true_button.config(image=true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(command=self.false_pressed)
        false_img = PhotoImage(file="images/false.png")
        self.false_button.config(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
