import tkinter as tk
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5B913B"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_controller = 1
timer_dict = {
    1: [WORK_MIN*60, "Working Time"],
    2: [SHORT_BREAK_MIN*60, "Short Break"],
    3: [WORK_MIN*60, "Working Time"],
    4: [SHORT_BREAK_MIN*60, "Short Break"],
    5: [WORK_MIN*60, "Working Time"],
    6: [LONG_BREAK_MIN*60, "Long Break"]
}
# variables to disable the buttons when already been pressed.
start_pressed = False
reset_pressed = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer_controller, timer_dict, start_pressed, reset_pressed
    if not start_pressed:
        return
    start_pressed = False
    reset_pressed = True

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global timer_controller, timer_dict, start_pressed
    if start_pressed:
        return
    start_pressed = True
    value = timer_dict[timer_controller][0]
    timer_label["text"]=timer_dict[timer_controller][1]
    count_down(value)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(value):
    global timer_controller, start_pressed, reset_pressed
    if reset_pressed:
        reset_pressed=False
        start()
        return
    canvas.itemconfig(timer_text, text=convert(value))
    if value>0:
        window.after(1000, count_down, value-1)
    elif value==0:
        timer_controller += 1
        start_pressed = False
        if timer_controller%2 != 0:
            check_marks["text"]+="✅"
        timer_label["text"]="Press start"
        return

# seconds to minutes and seconds
def convert(seconds):
    minutes = seconds//60
    seconds = seconds%60
    if minutes<10:
        minutes = "0"+str(minutes)
    if seconds<10:
        seconds = "0"+str(seconds)
    return f"{minutes}:{seconds}"

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=30, bg=YELLOW)

# Labels
timer_label=tk.Label(text="Timer",font=(FONT_NAME,40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.config(pady=20)
timer_label.grid(column=1, row=0)

# Background image
canvas = tk.Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
bg_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=bg_image)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

# Buttons
start_button = tk.Button(text="Start", command=start)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

# check marks displayed after each working+rest section
check_marks = tk.Label(text="", bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
