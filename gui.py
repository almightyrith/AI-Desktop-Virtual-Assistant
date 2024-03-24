from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text

# Function to handle the user's text input and display bot repsonses in the GUI
def user_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    
    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    
    if bot == "ok sir":
        root.destroy()

# Function to handle/process speech input and display bot responses in GUI
def ask():
    ask_val = speech_to_text.speech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> " + ask_val + "\n")

    if bot_val is not None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")

    if bot_val == "ok sir":
        root.destroy()

# Function to delete text from the text widget in the GUI
def delete_text():
    text.delete("1.0", "end")

# Initialize the Tkinter window
root = Tk()
root.geometry("550x675")
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#6F8FAF")

# Main Frame
main_frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised", bg="#6F8FAF")
main_frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label
text_label = Label(main_frame, text="AI Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
display_image = ImageTk.PhotoImage(Image.open("image/assistant.png"))
image_label = Label(main_frame, image=display_image)
image_label.grid(row=1, column=0, pady=20)

# Add a text widget
text = Text(root, font='Courier 10 bold', bg="#356696")
text.place(x=100, y=375, width=375, height=100)

# Add an entry widget
entry1 = Entry(root, justify=CENTER)
entry1.place(x=100, y=500, width=350, height=30)

# Add buttons
button1 = Button(root, text="Ask", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
button1.place(x=70, y=575)

button2 = Button(root, text="Send", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=user_send)
button2.place(x=400, y=575)

button3 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete_text)
button3.place(x=225, y=575)

root.mainloop()
