# Student registration page by the use of python - GUI

from tkinter import *
wn = Tk()
wn.geometry('600x800')
wn.title('Registration')
l = Label(wn,text = 'Student Registration Page', font = ('Arial', 30 ,'bold underline'),
         bg = 'black', fg = 'White')
l1 = Label(wn, text = 'Enter name',font = ('Arial 15')
          )
l2 = Label(wn, text = 'Email ID',
           font = ('Arial 15'))
l8 = Label(wn, text = 'Contact no',
           font = ('Arial 15'))
l3 = Label(wn, text = 'Gender',font = ('Arial 15')
          )
l4 = Label(wn, text = 'Course', font = ('Arial 15'))
r1 = Radiobutton(wn, text = 'Male',var = 'Gender', font = 'Arial 15',value = 'Male')
r2 = Radiobutton(wn, text = 'Female',var = 'Gender', font = 'Arial 15',value = 'Female'
                )
var1 = StringVar()
r3 = Checkbutton(wn,text = 'JAVA',font = 'Arial 15',var = var1)
var2 = StringVar()
r4 = Checkbutton(wn,text = 'C',font = 'Arial 15',var = var2)
l5 = Button(wn, text = 'Submit', font = 'Arial 15',bg = 'Green', fg = 'white')
r1.deselect()
#r2.select()
r2.deselect()
r1.place(x = 150,y = 210)
r2.place(x = 250,y = 210)

r3.place(x = 150,y = 250)
r4.place(x = 250, y = 250)
l1.place(x = 30,y = 80)
l2.place(x = 30,y = 120)
l8.place(x = 30,y = 160)
l3.place(x = 30,y = 210)
l4.place(x = 30,y = 250)
l5.place(x = 250,y = 330)

r3.deselect()

r4.deselect()
txt = Entry(wn, font = ('Arial 15'))
txt.place(x= 150,y = 80)
txt1 = Entry(wn, font = ('Arial 15'))
txt1.place(x= 150,y = 120)
txt2 = Entry(wn, font = ('Arial 15'))
txt2.place(x= 150,y = 160)
l.pack()
wn.mainloop()
