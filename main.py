# Description: This is a simple typing speed test application that calculates the user's typing speed in words per minute.

# Importing the required libraries
from tkinter import *
from tkinter.messagebox import showinfo

# Setting the time
seconds = 60

# Creating the window
window = Tk()
window.title("Typing Speed Test")
window.geometry("800x400")

# Create the title
label = Label(window, text="Welcome to Typing Speed Test", font=("Arial", 24))
label.pack()

# Creating the timer
timer = Label(window, text=f"Time left: {seconds}", font=("Arial", 16))
timer.pack()

# Create a text widget
text = Text(window, font=("Arial", 16))
text.pack()

# Detect if the user has typed anything, and start the timer
def on_key_release(event):
    start_timer()
    # Unbind the event so that the timer doesn't start again or speed up when the user types more
    text.unbind("<KeyRelease>")

# Timer control function
def start_timer():
    global seconds
    # If the time is up, disable the text widget and show the result
    if seconds == 0:
        text.config(state=DISABLED)
        showinfo("Typing Speed Test", f"Your speed is {calculate_speed()} characters per minute")
        return
    # Counting down the time, displaying the time left, and calling the function again after 1 second
    seconds -= 1
    timer.config(text=f"Time left: {seconds}")
    timer.after(1000, start_timer)

# Calculate the typing speed in words per minute
def calculate_speed():
    text_content = text.get("1.0", END)
    words = text_content.split()
    num_words = len(words)
    num_chars = len(text_content) - num_words + 1
    speed = num_chars / 5
    return speed

# Setting the event listener for the key release
text.bind("<KeyRelease>", on_key_release)

window.mainloop()