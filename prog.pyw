from tkinter import *
from playsound import playsound
from random import randint
root = Tk()
root.attributes("-fullscreen", False)
root.title('Iron Man')
root.configure(bg='maroon')
'''#1F3247'''
root.iconbitmap(None)
root.geometry("238x600")
root.resizable(height = 0, width = 0)

def up2Change():
    q=int(open('data/data.data','r').read())
    if q%2==0:frames = [PhotoImage(file='data/Up.gif',format = 'gif -index %i' %(i)) for i in range(7)]
    if q%2!=0:frames = [PhotoImage(file='data/Up2.gif',format = 'gif -index %i' %(i)) for i in range(7)]
    def update(ind):
        try:
            frame = frames[ind]
            frame=frames[ind]
            ind += 1
            label.configure(image=frame)
            label.image = frame
            root.after(100, update, ind)
        except:
            pass
    root.after(0, update, 0)
    open('data/data.data','w+').write(str(q+1))

def midChange():
    q=int(open('data/data2.data','r').read())
    if q%2==0:
        frames = [PhotoImage(file='data/Middle.gif',format = 'gif -index %i' %(i)) for i in range(6)]
    if q%2!=0:
        frames = [PhotoImage(file='data/Middle2.gif',format = 'gif -index %i' %(i)) for i in range(6)]
    def update(ind):
        try:
            frame = frames[ind]
            frame=frames[ind]
            ind += 1
            button3.configure(image=frame)
            button3.image = frame
            root.after(100, update, ind)
        except:
            pass
    root.after(0, update, 0)
    open('data/data2.data','w+').write(str(q+1))

def ritChange():
    q=int(open('data/data4.data','r').read())
    if q%2!=0:
        photo = PhotoImage(file = "data/Right.png")
        button.image = photo
        button.config(image=photo)
        del photo
    playsound('data/right.mp3')
def letChange():playsound('data/left.mp3')
def downChange():
    q=int(open('data/data3.data','r').read())
    if q%2!=0:
        playsound('data/down.mp3')
        photo = PhotoImage(file = "data/Down2.png")
    if q%2==0:
        playsound('data/chest2.mp3')
        photo = PhotoImage(file = "data/Down.png")        
    button4.image = photo
    button4.config(image=photo)
    del photo
    open('data/data3.data','w+').write(str(q+1))
def audChange():
    q=int(open('data/data.data','r').read())
    if q%2==0:
        a=randint(0,3)
        if a==0:
            photo = PhotoImage(file = "data/Right2.png")
            button.image = photo
            button.config(image=photo)
            del photo
            open('data/data4.data','w+').write(str(q+1))
        playsound('data/'+str(a)+'.mp3')
    if q%2!=0:playsound('data/myturn.mp3')
open('data/data.data','w+').write('1')
open('data/data2.data','w+').write('1')
open('data/data3.data','w+').write('1')
open('data/data4.data','w+').write('1')
#Button
photo6 = PhotoImage(file = "data/Up.png")
label2 = Button(root,command=up2Change,image=photo6,bg='maroon',borderwidth=0,activebackground='maroon')
label2.place(x=74,y=31)
label = Button(root,command=up2Change,bg='maroon',borderwidth=0,activebackground='maroon')
label.place(x=74,y=31) 
button = Button(root,text='sta',bg='yellow',activeforeground='cyan',fg='yellow',borderwidth=0,activebackground='cyan',command=exit)
button.place(x=5,y=5)
button69 = Button(root,text='sta',bg='cyan',activeforeground='yellow',fg='cyan',borderwidth=0,activebackground='yellow',command=audChange)
button69.place(x=210,y=5)
photo = PhotoImage(file = "data/Right.png")
button = Button(root, image = photo, bg='maroon',borderwidth=0,activebackground='maroon',command=ritChange)
button.place(x=0,y=106)
photo2 = PhotoImage(file = "data/Left.png")
button1 = Button(root, image = photo2, bg='maroon',borderwidth=0,activebackground='maroon',command=letChange)
button1.place(x=176,y=106)
photo4 = PhotoImage(file = "data/Middle.png")
button3 = Button(root, image = photo4, bg='maroon',borderwidth=0,activebackground='maroon',command=midChange)
button3.place(x=61,y=100)
photo5 = PhotoImage(file = "data/Down.png")
button4 = Button(root, image = photo5, bg='maroon',borderwidth=0,activebackground='maroon',command=downChange)
button4.place(x=53,y=250)

root.mainloop()
