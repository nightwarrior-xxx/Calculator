#! /usr/bin/python
from Tkinter import *

def button(number):
    global operator
    operator=operator + str(number)
    text_input.set(operator)

def clear():
    global operator
    operator=''
    text_input.set(operator)
    Display.insert(0,"Come Again!!")

def equal():
    global operator
    result=float(eval(operator))
    text_input.set(result)
    operator=''


root=Tk()
root.title('Calculator')


operator=''
text_input=StringVar()
#Display
Display=Entry(root,font=('arial',30,'bold'),fg='white',bg='black',justify='right',bd=20,textvariable=text_input)
Display.grid(columnspan=4)
#Row1
b7=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='7',command=lamdha:button(7)).grid(row=1,column=0)
b8=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='8',command=lamdha:button(8)).grid(row=1,column=1)
b9=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='9',command=lamdha:button(9)).grid(row=1,column=2)
bC=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='clear',bg='green',command=lamdha:clear()).grid(row=1,column=3)
#Row2
b4=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='4',command=lamdha:button(4)).grid(row=2,column=0)
b4=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='5',command=lamdha:button(5)).grid(row=2,column=1)
b5=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='6',command=lamdha:button(6)).grid(row=2,column=2)
bplus=Button(root,padx=64,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='+',bg='purple',command=lamdha:button('+')).grid(row=2,column=3)
#Row3
b1=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='1',command=lamdha:button(1)).grid(row=3,column=0)
b2=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='2',command=lamdha:button(2)).grid(row=3,column=1)
b3=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='3',command=lamdha:button(3)).grid(row=3,column=2)
bminus=Button(root,padx=69,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='-',bg='purple',command=lamdha:button('-')).grid(row=3,column=3)
#Row4
b_dot=Button(root,padx=35,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='.',bg='purple',command=lamdha:button('.')).grid(row=4,column=0)
b0=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='0',command=lamdha:button(0)).grid(row=4,column=1)
b_divison=Button(root,padx=35,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='/',bg='purple',command=lamdha:button('/')).grid(row=4,column=2)
b_multiply=Button(root,padx=65,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='*',bg='purple',command=lamdha:button('*')).grid(row=4,column=3)
#Row5

b_open_bracket=Button(root,padx=34,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='(',bg='purple',command=lamdha:button('(')).grid(row=5,column=0)
b_close_bracket=Button(root,padx=34,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text=')',bg='purple',command=lamdha:button(')')).grid(row=5,column=1)
b_equal=Button(root,padx=114,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='=',bg='green',command=lamdha:equal()).grid(row=5,column=2,columnspan=2)
root.mainloop()