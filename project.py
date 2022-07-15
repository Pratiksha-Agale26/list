# # from cProfile import label
# from tkinter import *

# # from click import command
# root = Tk()

# # my_label = Label(root,text = "Hello World i love python")

# # my_label.pack()
# # root.title("MY BOX GUI")
# # root.title("MY GUI APP")
# root.title("MY BUTTON")
# root.geometry("500x500")

# e = Entry(root,width = 30,fg = "red")
# e.grid(row=0,column=1)

# ee = Entry(root,width = 30,fg = "black")
# ee.grid(row=0,column=2)

# # def my_click():
# #     my_label = Label(root,text = "WELCOME TO THE COURSE!",fg="red")
# #     my_label.pack()
# def clickme():
#     mylabel = Label(root,text = "hello" +" "+ e.get())
#     mylabel.grid(row=3,column=1)
#     e.delete(0,END)

# def click2():
#     mylabel = Label(root,text = "hello" +" "+ ee.get())
#     mylabel.grid(row=3,column=2)
#     ee.delete(0,END)

# # my_label = Label(root,text = "Hi").pack()
# # my_label2 = Label(root,text = "how you doing today").pack()
# # my_label = Label(root, text="My new GUI app !")
# # my_label2 = Label(root, text = 'this is line 2')
# # mybutton = Button(root, text = "HEY CLICK THIS!",command= my_click,fg = "black",bg='green',padx=30,pady=30)
# # mybutton.pack()
# myButton = Button(root,text = "enter first NAME",padx=10,pady=10,bg="white",fg="green",command=clickme)
# myButton.grid(row=2,column=1)

# myButton =Button(root,text = "enter last NAME",padx=10,pady=10,bg="white",fg="green",command=click2)
# myButton.grid(row=2,column=1)
# # my_label.grid(row=0,column=0)
# # my_label2.grid(row=2,column=3)

# root.mainloop()

from cgitb import text
from tkinter import *
root = Tk()

root.title("CHATBOT")
# root.geometry("500x500")

# e=Entry(root,width=100)
e= Entry(root,width = 30,fg = "blue")
e.grid(row=0,column=1)

def send():
    send="YOU :"+ e.get()
    text.insert(END,"\n"+send)
    if (e.get()=="hello"):
        text.insert(END,"\n"+"Bestie :hii")
    elif (e.get()=="hii"):
        text.insert(END,"\n"+"Bestie :Hello")
    elif (e.get()=="how are you"):
        text.insert(END,"\n"+"Bestie :fine and you")
    elif (e.get()=="yes,i'm also fine"):
        text.insert(END,"\n"+"Bestie :nice to hear")
    elif (e.get()=="i miss you a lots"):
        text.insert(END,"\n"+"Bsetie :i also")
    else:
        text.insert(END,"\n"+"Bestie :sorry i didn't get it")
    e.delete(0,END)

text=Text(root)
text.grid(row=0,column=0,columnspan=2)
# e=Entry(root,width=100)
send=Button(root,text="send",command=send,bg="light blue").grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()