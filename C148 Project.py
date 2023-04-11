from tkinter import *
import random
root = Tk()
root.geometry("800x800")
root.config(bg = "red")

items_label = Label(root, bg="black", fg="white")
random_no_label = Label(root, bg="gold", fg="black")
items_label.place(relx = 0.5, rely = 0.4, anchor=CENTER)
random_no_label.place(relx = 0.5,rely = 0.6, anchor=CENTER)

List1 = ['Bottle', 'Tiffin Box', 'Chips', 'Chocolates', 'Id Card', 'Sunglasses']

items_label["text"] = "Listed Items : " + str(List1)

def random_list():
    random_list = random.sample(range(1,6), 1)
    random_no_label["text"] = "Put item no. = " + str(random_list) + " in bag"
    
btn = Button(root, text = "Which item to put in the bag?", command=random_list, bg="cyan", fg="black")
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)


root.mainloop()