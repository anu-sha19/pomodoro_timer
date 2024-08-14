from tkinter import *
from playsound import playsound
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    title.config(text="Timer", fg="green", font=(FONT_NAME, 25, "normal"))
    canvas.itemconfig(time_keeping, text="0:00")
    check_mark.config(text=" ")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps >= 8 and reps % 8 == 0:
        total_time = LONG_BREAK_MIN * 60
        title.config(text=f"Long Break Well Done!", fg=RED, font=(FONT_NAME, 20, "bold"))

    elif reps % 2 == 0:
        total_time = SHORT_BREAK_MIN * 60
        title.config(text="Short Break", fg=PINK)

    elif reps % 2 != 0:
        total_time = WORK_MIN * 60
        title.config(text=f"Please Study!", fg="green", font=(FONT_NAME, 25, "normal"))

    countdown(total_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Creating labels and buttons
#Label
title = Label(text="Timer", fg="green", bg=YELLOW, font=(FONT_NAME, 30, "normal"))
check_mark = Label(fg="green", bg=YELLOW, font=("Arial", 20, "normal"))
title.grid(column=1, row=0)
check_mark.grid(column=1, row=3)

#Canvas to layer images on top of background color or other items
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_keeping = canvas.create_text(103, 130, text="00:00", fill="white", font=("Arial", 30, "normal"))
canvas.grid(column=1, row=1)

#Button
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)


def countdown(count):
    check = ""
    global reps, timer

    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs == 0:
        count_secs = "00"
    display = f"{count_min}:{count_secs}"
    if int(count) < 10:
        display = count_secs
    canvas.itemconfig(time_keeping, text=display)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check += "✔"
        check_mark.config(text=check)
        playsound("mixkit-warning-alarm-buzzer-991.wav")


window.mainloop()
