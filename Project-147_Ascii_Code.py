from tkinter import*

root = Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = 'snow')

word = Entry(root)
word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text = "name in ascii value ",bg = "light yellow", fg = "black")

def ascii():
    input = word.get()
    for letter in input :
        label["text"] += str(ord(letter)) + " "
        
btn = Button(root, text = "Show name in Ascii", command = ascii, bg = "gold", fg = "black" )
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()