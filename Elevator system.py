#creating the canvas
import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,bg="white")
canvas.pack(fill=tk.BOTH,expand=True)
#creating the floors 
class Floor():    
    def __init__(self,name,x1,y1,x2,y2,color):
        self.name=name
        self.guı=canvas.create_rectangle((x1,y1),(x2,y2),fill=color)  

f3=Floor("Floor 3",0,0,1440,285,"yellow")
f2=Floor("Floor 2",0,286,1440,571,"red")
f1=Floor("Floor 1",0,572,1440,858,"blue")
#The elevator
elevator=canvas.create_rectangle((640,858),(800,698),fill="black")
is_rec_moving_up=False
is_rec_moving_down=False
ID_for_after=None   #I will use this for .after commands

#Floor info (says where the elevator is)
floor_info=tk.Label(root, text=f1.name, font=("Arial",10))
floor_info.pack()
#this function is for know the elevator's instant floor, also make stop the elevator in floor1 and floor3
def check_floor():
    global floor_info
    x1,y1,x2,y2=canvas.coords(elevator)  #elevator coords
    a1,b1,a2,b2=canvas.coords(f1.guı)  #Floor 1 coords
    c1,d1,c2,d2=canvas.coords(f2.guı)  #Floor 2 coords
    e1,g1,e2,g2=canvas.coords(f3.guı)  #Floor 3 coords
    if y1>b1 and y2<b2:
        floor_info.config(text=f1.name)
    elif y1>d1 and y2<d2:
        floor_info.config(text=f2.name)
    elif  y1>g1 and y2<g2:
        floor_info.config(text=f3.name)
    if  is_rec_moving_up and y1<=73:
        canvas.after_cancel(ID_for_after)
    if is_rec_moving_down and y2>=795:
        canvas.after_cancel(ID_for_after)
#animate and move funcs.
def animate_up():
    global ID_for_after
    canvas.move(elevator,0,-3)
    ID_for_after=root.after(25,animate_up)  #after command
    check_floor()

def animate_down():
    global ID_for_after
    canvas.move(elevator,0,3)
    ID_for_after=root.after(25,animate_down)  #after command
    check_floor()

def move_up():
    global is_rec_moving_up
    global is_rec_moving_down
    global ID_for_after
    if is_rec_moving_up==False:
        if is_rec_moving_down==False: #if the elevator isn't moving just animate it
            is_rec_moving_up=True
            is_rec_moving_down=False
            animate_up()
        else:
            canvas.after_cancel(ID_for_after) #else stop it (after_cancel) and animate it
            is_rec_moving_down=False
            is_rec_moving_up=True
            animate_up()
    
def move_down():
    global is_rec_moving_down
    global is_rec_moving_up
    if is_rec_moving_down==False:
        if is_rec_moving_up==False:    #if the elevator isn't moving just animate it
            is_rec_moving_down=True
            is_rec_moving_up=False
            animate_down()
        else:
            canvas.after_cancel(ID_for_after)   #else stop it (after_cancel) and animate it
            is_rec_moving_up=False
            is_rec_moving_down=True
            animate_down()
#buttons
button_up=tk.Button(root,height=1,width=4, text="UP", command= move_up)
button_down=tk.Button(root,height=1,width=4,text="DOWN", command=move_down)
button_down.pack()
button_up.pack(anchor=tk.CENTER)
#mainloop
root.mainloop()