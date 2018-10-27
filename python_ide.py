from tkinter import *
import tkinter.messagebox
from io import StringIO

root = Tk()
root.geometry('1000x800')
v= IntVar()
v.set(1)
root.title("Run Python Code")
color ='gray77'
colorText = 'black'
root.configure(bg=color)
root.resizable(width=False, height=False)
def choose_color():

    global colorText
    global color
    colorText = 'black'
    if v.get()==0:
        color='black'
    elif v.get()==1:
        color='gray77'
    else:
        color='white'
    if color =='black':
        colorText='white'
    invoke_changes()


def clear_python():
    python_code.delete('1.0', END)


def run():
    #run python code
    #show python code to user
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(python_code.get('1.0', END))
    sys.stdout = old_stdout
    tkinter.messagebox.showinfo('Result', redirected_output.getvalue())


"""tkinter gui"""
top = Frame(root, width=1000, height=100, bg=color)
top.pack(side=TOP)
label = Label(root, text='choose IDE Color', bg=color)
label.place(x=0, y=0)


r_btn = Radiobutton(root, text= 'black', bg=color, variable=v, value=0,command= lambda :choose_color())
r_btn.place(x=5, y=15)


r_btn1 = Radiobutton(root, text= 'gray', bg=color, variable=v, value=1,command= lambda :choose_color())
r_btn1.place(x=5, y=55)

r_btn2 = Radiobutton(root, text= 'white', bg=color, variable=v, value=2,command= lambda :choose_color())
r_btn2.place(x=5, y=95)

bottom = Frame(root, width=1000, height=900, bg=color)
bottom.pack(side=BOTTOM)

btn_claer= Button(top,text='Clear', bg=color,font=('ariel', 25,'bold'), command= lambda :clear_python())
btn_claer.pack(side=TOP)

btn_run = Button(top,text='Run',  bg=color, font=('ariel', 25, 'bold'), command= lambda :run())
btn_run.pack(side=TOP)
python_code = Text(bottom, font=('ariel', 25,'bold'), bg=color)
python_code.pack(side=TOP)


def invoke_changes():
    root.configure(bg=color)
    btn_claer.configure(bg=color)
    btn_run.configure(bg=color)
    r_btn.configure(bg=color)
    r_btn1.configure(bg=color)
    r_btn2.configure(bg=color)
    python_code.configure(bg=color)
    bottom.configure(bg=color)
    label.configure(bg=color)
    top.configure(bg=color)
    python_code.configure(foreground=colorText)
    label.configure(foreground=colorText)
    btn_run.configure(foreground=colorText)
    btn_claer.configure(foreground=colorText)
    r_btn.configure(foreground=colorText)
    r_btn1.configure(foreground=colorText)
    r_btn2.configure(foreground=colorText)

root.mainloop()


""""
for i in range(0, 10):
	print(i)
"""
