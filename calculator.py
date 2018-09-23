#! /usr/bin/python
from Tkinter import *
root=Tk()
root.title('Calculator')
#Screen
Display=Entry(root,font=('arial',30,'bold'),fg='white',bg='green',justify='right',bd=50)
Display.grid(columnspan=4)
#Rows
b7=Button(root,padx=15,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='7').grid(row=1,column=0)
b8=Button(root,padx=15,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='8').grid(row=1,column=1)
b8=Button(root,padx=15,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='9').grid(row=1,column=2)
bC=Button(root,padx=15,pady=15,bd=8,fg='black',font=('arial',30,'bold'),text='clear',bg='purple').grid(row=1,column=3)

root.mainloop()