#! /usr/bin/python
from Tkinter import *
root=Tk()
root.title('Calculator')
#Screen
Display=Entry(root,font=('arial',30,'bold'),fg='white',bg='black',justify='right',bd=20)
Display.grid(columnspan=4)
#Row1
b7=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='7').grid(row=1,column=0)
b8=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='8').grid(row=1,column=1)
b8=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='9').grid(row=1,column=2)
bC=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='clear',bg='purple').grid(row=1,column=3)
#Row2
b4=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='4').grid(row=2,column=0)
b4=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='5').grid(row=2,column=1)
b5=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='6').grid(row=2,column=2)
bplus=Button(root,padx=64,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='+',bg='purple').grid(row=2,column=3)
#Row3
b1=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='1').grid(row=3,column=0)
b2=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='2').grid(row=3,column=1)
b3=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='3').grid(row=3,column=2)
bminus=Button(root,padx=69,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='-',bg='purple').grid(row=3,column=3)
#Row4
b0=Button(root,padx=30,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='0').grid(row=4,column=0)
bdot=Button(root,padx=35,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='.',bg='purple').grid(row=4,column=1)
bdivison=Button(root,padx=35,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='/',bg='purple').grid(row=4,column=2)
bmultiply=Button(root,padx=64,pady=15,bd=5,fg='black',font=('arial',30,'bold'),text='*',bg='purple').grid(row=4,column=3)
root.mainloop()