from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("To-do-list")
root.geometry("500x500")
root.resizable(False,False)

#Functions
def delete_item():
    my_listbox.delete(ANCHOR)

def add_item(event):
      my_listbox.insert(END, my_entry.get())
      my_entry.delete(0,END)

def cross_item():
    #Cross of item
    my_listbox.itemconfig(my_listbox.curselection(), fg="gray")
    #Cross xong thì nó tự động bỏ ra để thấy laf đã cross
    my_listbox.selection_clear(0, END)

def uncross_item():
    #UNcross of item
    my_listbox.itemconfig(my_listbox.curselection(), fg="black")
    #Uncross xong thì nó tự động bỏ ra để thấy laf đã uncross
    my_listbox.selection_clear(0, END)

def delete_all():
    my_listbox.delete(0, END)

#Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#LIstbox
my_listbox = Listbox(my_frame,width=40,height=5,bg="#9AC6C5",fg="black",bd=0,font=("poppins",16),highlightthickness=0,selectbackground="#7785AC",activestyle="none")
my_listbox.pack(side=LEFT,fill=BOTH)

#Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

#ADD SCROLLBAR
#Bước 1
my_listbox.config(yscrollcommand=my_scrollbar.set)
#Bước 2
my_scrollbar.config(command=my_listbox.yview)

#Entry to add todolist
my_entry = Entry(root, width=35, font=("Helvetica",17))
my_entry.bind("<Return>", add_item)
my_entry.pack(pady=20)
my_entry.focus()

#Add buttons
#Button deleted
icon_delete = PhotoImage(file="icons/delete.png")
delete_button = Button(image=icon_delete,command=delete_item,bd=0,cursor="hand2")
delete_button.place(x=30,y=250)

#Button ADD
icon_add = PhotoImage(file="icons/plus.png")
add_button = Button(image=icon_add,command=lambda:add_item('<Button-1>'),bd=0,cursor="hand2")
add_button.place(x=150,y=250)

#BUtton cross
icon_cross = PhotoImage(file="icons/hidden.png")
cross_button = Button(image=icon_cross,command=cross_item,bd=0,cursor="hand2")
cross_button.place(x=270,y=250)

#Button uncross
icon_uncross = PhotoImage(file="icons/eye.png")
uncross_button = Button(image=icon_uncross,command=uncross_item,bd=0,cursor="hand2")
uncross_button.place(x=400,y=250)

#Button delete all
icon_delete_all = PhotoImage(file="icons/delete-all.png")
uncross_button = Button(image=icon_delete_all,command=delete_all,bd=0,cursor="hand2")
uncross_button.place(x=200,y=350)

root.mainloop()
