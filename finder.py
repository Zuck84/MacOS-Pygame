from tkinter import *

root = Tk()

label_text = Label(root, text="Finder", font=(None, 20))
label_text.pack()

photo = PhotoImage(file="finder_picture.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()
