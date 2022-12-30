#Dependencies
from tkinter import Label , Tk , Text , Canvas , Button
from tkinter.messagebox import showinfo , showwarning
from random import randint
#GUI
root=Tk()
root.title('Magic Squares')
root.geometry('300x300')
#Canvas
canvas=Canvas(root , width=300 , height=300)
canvas.pack()
#Label
l1=Label(text='Magic Squares' , font=('Fira Sans' , 12))
canvas.create_window(150 , 50, window=l1)
#Button
b1=Button(root , text='Start' , font=('Fira Sans' , 12) , bg='blue' , fg='white')
canvas.create_window(150 , 100 , window=b1)
b2=Button(root , text='Exit' , font=('Fira Sans' , 12) , bg='red' , fg='white' , width=4)
canvas.create_window(150 , 150, window=b2)
b3=Button(root , text='Easy' , font=('Fira Sans' , 12) , bg='blue' , fg='white')
b4=Button(root , text='Medium' , font=('Fira Sans' , 12) , bg='blue' , fg='white')
b5=Button(root , text='Hard' , font=('Fira Sans' , 12) , bg='blue' , fg='white')
#Text
t1=Text(root , width=2 , height=1)
t2=Text(root , width=2 , height=1)
t3=Text(root , width=2 , height=1)
t4=Text(root , width=2 , height=1)
t5=Text(root , width=2 , height=1)
t6=Text(root , width=2 , height=1)
t7=Text(root , width=2 , height=1)
t8=Text(root , width=2 , height=1)
t9=Text(root , width=2 , height=1)
#Functions
#UI Elements
def ui_elements():
    canvas.delete('all')
    canvas.create_window(150 , 40, window=Label(text=num , font=('Fira Sans' , 12)))
    canvas.create_window(100 , 70, window=t1)
    canvas.create_window(150 , 70, window=t2)
    canvas.create_window(200 , 70, window=t3)
    canvas.create_window(100 , 100, window=t4)
    canvas.create_window(150 , 100 , window=t5)
    canvas.create_window(200 , 100, window=t6)
    canvas.create_window(100 , 130, window=t7)
    canvas.create_window(150 , 130, window=t8)
    canvas.create_window(200 , 130, window=t9)
    canvas.create_window(150 , 170, window=bvrfi)

def play_f():
    canvas.delete('all')
    canvas.create_window(150 , 50, window=Label(root , text='Select Game Mode' , font=('Fira Sans' , 12)))
    canvas.create_window(150 , 100, window=b3)
    canvas.create_window(150 , 150, window=b4)
    canvas.create_window(150 , 200, window=b5)

def easy_f():
    global num
    num=randint(-10 , 10)
    ui_elements()

def medium_f():
    global num
    num=randint(-100 , 100)
    ui_elements()

def hard_f():
    global num
    num=randint(-1000 , 1000)
    ui_elements()

def verify_f():
    n1=t1.get(0.0 , 3.0)
    n2=t2.get(0.0 , 3.0)
    n3=t3.get(0.0 , 3.0)
    n4=t4.get(0.0 , 3.0)
    n5=t5.get(0.0 , 3.0)
    n6=t6.get(0.0 , 3.0)
    n7=t7.get(0.0 , 3.0)
    n8=t8.get(0.0 , 3.0)
    n9=t9.get(0.0 , 3.0)
    if n1=='\n' or n2=='\n' or n3=='\n' or n4=='\n' or n5=='\n' or n6=='\n' or n7=='\n' or n8=='\n' or n9=='\n':
        showwarning('Error' , 'Please enter a number on the text boxes')
    else:
        s1=int(n1)+int(n2)+int(n3)
        s2=int(n4)+int(n5)+int(n6)
        s3=int(n7)+int(n8)+int(n9)
        s4=int(n1)+int(n5)+int(n9)
        s5=int(n3)+int(n5)+int(n7)
        if int(s1) and int(s2) and int(s3) and int(s4) and int(s5) == int(num):
            showinfo('Sucess' , 'You succesfully solved the magic square')
        else:
            showwarning('Error' , 'Please ensure that the sum of the row, columns and the diagonals is same as the number above')
bvrfi=Button(root , text='Verify' , font=('Fira Sans' , 12) , bg='blue' , fg='white' , width=4 , command=verify_f)
#Commands
b1.configure(command=play_f)
b2.configure(command=root.destroy)
b3.configure(command=easy_f)
b4.configure(command=medium_f)
b5.configure(command=hard_f)
#Exec
root.mainloop()
