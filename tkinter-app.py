from tkinter import *

def on_button_click():
    label.config(fg="orange")
    label.config(bg="white")
    root.configure(bg="white")

root = Tk()
root.title("app")
root.geometry("400x300")
root.configure(bg="black")
root.resizable(False, False)

label = Label(root, text="welcome to app", fg="white", bg="black", font=("Comic Sans MS", 16, "bold"))
label.pack(pady=20)

btn1 = Button(root, text="Click", fg="black", bg="white", font=("Comic Sans MS", 12), command=on_button_click)
btn1.pack(pady=10)

root.mainloop()