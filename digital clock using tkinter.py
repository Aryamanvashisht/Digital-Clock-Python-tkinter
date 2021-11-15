
#Importing the Tkinter module
from tkinter import *

#Importing strftime from time module
from time import strftime

#setting up window by creating instance of TK class
root=Tk()

#Giving the title of the display window
root.title("DIGITAL CLOCK")
DIGITAL CLOCK")

#Setting the widthxheight+x-axis+y-axis of window
root.geometry("1350x700+0+0")

#config is used to access an object's attributes after its initialisation.
root.config(bg="#081923")

# function for getting the system time in hour
def hr():
    string = strftime('%H')
    #type = int(string)
    #s = str(type-12)
    s= str(int(string)-12)
    lbl_hr.config(text=s)
    lbl_hr.after(1000,hr)
    
# function for getting the system time in Minute
def min():
    string = strftime('%M')
    lbl_min.config(text=string)
    lbl_min.after(1000, min)
    
# function for getting the system time in second
def sec():
    string = strftime('%S')
    lbl_sec.config(text=string)
    lbl_sec.after(1000, sec)
    
# function for getting the system AM/PM
def Meridian():
    string = strftime('%p')
    lbl_noon.config(text=string)
    lbl_noon.after(1000, Meridian)

#Label is widget used to implement display boxes
#Label contains many key-value pairs like fg,bg,font text etc.

#Label for hour hand
lbl_hr =Label(root,text="12",font=("times new roman",50,"bold"),bg="#0875B7",fg="white")
lbl_hr.place(x=350,y=200,width=150,height=150)

#Label for hour hand text
lbl_hr2 =Label(root,text="HOUR",font=("times new roman",20,"bold"),bg="#0875B7",fg="white")
lbl_hr2.place(x=350,y=360,width=150,height=50)

#Label for Minute hand
lbl_min =Label(root,text="12",font=("times new roman",50,"bold"),bg="#008EA4",fg="white")
lbl_min.place(x=520,y=200,width=150,height=150)

#Label for Minute hand text
lbl_min2 =Label(root,text="MINUTE",font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
lbl_min2.place(x=520,y=360,width=150,height=50)

#Label for second hand
lbl_sec =Label(root,text="12",font=("times new roman",50,"bold"),bg="#7352a2",fg="white")
lbl_sec.place(x=690,y=200,width=150,height=150)

#Label for second hand text
lbl_sec2 =Label(root,text="SECOND",font=("times new roman",20,"bold"),bg="#7352a2",fg="white")
lbl_sec2.place(x=690,y=360,width=150,height=50)

#Label for Anti and prime meridian
lbl_noon =Label(root,text="AM",font=("times new roman",50,"bold"),bg="#DF002A",fg="white")
lbl_noon.place(x=860,y=200,width=150,height=150)

#Label for  Anti and prime meridian text
lbl_noon2 =Label(root,text="AM/PM",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
lbl_noon2.place(x=860,y=360,width=150,height=50)

#calling of above functions:-
hr()
min()
sec()
Meridian()

#Mainloop is used for holding the window and wait for event to close
mainloop()

