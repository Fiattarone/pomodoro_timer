import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f481"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
breaks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global breaks, reps
    breaks = ""
    reps = 0
    check_marks.config(text=f"Number of Breaks:\n{breaks}")
    timer_label.config(text="TIMER", fg=RED)
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps, breaks
    reps += 1
    if not reps % 8:
        tick(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=YELLOW)
        breaks += "✅"
        check_marks.config(text=f"Number of Breaks:\n{breaks}")
    elif reps % 2:
        if len(breaks) > 3:
            breaks = ""
            check_marks.config(text=f"Number of Breaks:\n{breaks}")
        tick(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=RED)
    else:
        tick(SHORT_BREAK_MIN*60)
        timer_label.config(text="BREAK", fg=PINK)
        breaks += "✅"
        check_marks.config(text=f"Number of Breaks:\n{breaks}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def tick(tick_down):
    global timer
    minutes = math.floor(tick_down/60)
    seconds = tick_down % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(text_item, text=f"{minutes}:{seconds}")
    # print("tick")
    if tick_down > 0:
        timer = window.after(1, tick, tick_down-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(pady=50, padx=50, bg=GREEN)

timer_label = Label(text="Timer", font=(FONT_NAME, 44, "bold"), bg=GREEN, fg=RED)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, highlightthickness=0)
canvas.config(bg=GREEN)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_item = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(justify="right", text="Start", command=start_timer, bg=YELLOW, fg=RED, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(justify="left", text="Reset", command=reset_timer, bg=YELLOW, fg=RED, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(text=f"Number of breaks:\n{breaks}", bg=GREEN, highlightthickness=0, fg=RED)
check_marks.grid(row=3, column=1)
window.mainloop()
