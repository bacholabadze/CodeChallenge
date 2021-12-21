import math
from tkinter import *
import os  # For Playing Audios

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
ORANGE = '#FC9918'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
# ------------------------------------------------------------------------- #
reps = 1  # count repetitions
timer = None

is_paused = False
seconds_left = 0  # remaining paused seconds


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, seconds_left, is_paused
    is_paused = False
    reps = 1
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    if seconds_left:
        print(f'seconds_left: {seconds_left}')
        window.after_cancel(timer)
    seconds_left = 0


# ---------------------------- TIMER PAUSE ------------------------------- #
def pause_timer():
    if seconds_left:
        title_label.config(text='Paused', fg=ORANGE)
        global is_paused
        is_paused = True
        window.after_cancel(timer)
        os.system("mpg123 " + "audios/paused.mp3")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, is_paused
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # Unpause
    if is_paused:
        title_label.config(text='Work', fg=GREEN)
        count_down(seconds_left)
        is_paused = False
        os.system("mpg123 " + "audios/work.mp3")
    else:
        # If it's the 8th rep:
        if reps % 8 == 0:
            title_label.config(text='Break', fg=RED)
            count_down(long_break_seconds)
            os.system("mpg123 " + "audios/long_break.mp3")
        # If it's the 2nd/4th/6th rep:
        elif reps % 2 == 0:
            title_label.config(text='Break', fg=PINK)
            count_down(short_break_seconds)
            os.system("mpg123 " + "audios/short_break.mp3")
        # If it's the 1st/3rd/5th/7th rep:
        else:
            title_label.config(text='Work', fg=GREEN)
            count_down(work_seconds)
            os.system("mpg123 " + "audios/work.mp3")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(time_count):
    global seconds_left, timer, reps
    minutes = int(time_count / 60)
    seconds = int(time_count % 60)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if seconds < 10:
        seconds = '0' + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if time_count > 0:
        timer = window.after(1000, count_down, time_count - 1)
        seconds_left = time_count
    else:
        reps += 1
        start_timer()
        marks = math.floor(reps / 2) * '✓'
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='images/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 125, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

pause_button = Button(text='Pause', highlightthickness=0, command=pause_timer)
pause_button.grid(column=1, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text='', fg=GREEN, bg=YELLOW, font=('Arial', 20, 'bold'))
check_marks.grid(column=1, row=3)

window.mainloop()
