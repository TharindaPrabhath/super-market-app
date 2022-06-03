import tkinter as tk
from tkinter import *
import tkinter.messagebox


from PIL import ImageTk, Image


root=Tk()
root.geometry("466x480")
img = PhotoImage(file='c:/New folder/umbrella.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.title("GUI")

status_bar=Label(root, text="Contact- tharindahp@gmail.com", bd=1, relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM)

frame_top=LabelFrame(root, text="Basic Input Section", padx=42, pady=20)
frame_top.place(x=3, y=120)

def button_info_command():
    root5=Tk()
    root5.title("Info")
    img = PhotoImage(file='c:/New folder/umbrella.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    root5.geometry("500x400")

    label_about=Label(root5, text="ABOUT", bg="#A9A9A9", fg="white", font="arial 18")
    label_about.place(x=200, y=20)
    label_info1=Label(root5, text=''' Released Date: 2020/11/28
                                   Last Version : 1.0.0v
                                    Lisence      : Openware
                                    Company      : Symetry
                                   Country      : Sri Lanka   ''' )
    label_info1.place(x=30, y=80)

    label_credit1=Label(root5, text="CEDIT", bg="#A9A9A9", fg="white", font="arial 18")
    label_credit1.place(x=200, y=220)

    label_infoo1=Label(root5, text='''                  Inspired by Gihan Ayya
                                   Special Thanks for #thenewboston
                                                       #Mosh
                                                       #Codemy.com(Youtube Channel)
                                                       
                                   Platinum Thanks for HP notebook 430 ''')

    label_infoo1.place(x=20, y=270)
   
    root5.mainloop()

photo=Image.open("c:/New folder/idimage.ico")
resized=photo.resize((80,80), Image.ANTIALIAS)
newphoto=ImageTk.PhotoImage(resized)
#Image original size 748x752

photo=ImageTk.PhotoImage(file="c:/New folder/idimage.ico")
label_image=Label(root, image=newphoto)
label_image.place(x=3, y=30)

label_common=Label(root, text="BRAND", font="arial 30 bold", bg="#A9A9A9", padx=118, pady=14)
label_common.place(x=84 , y=31)

photo_4=Image.open("c:/New folder/ex.png")
resized_4=photo_4.resize((20,20), Image.ANTIALIAS)
newphoto_4=ImageTk.PhotoImage(resized_4)
#Changing original image size

button_image=PhotoImage(file="c:/New folder/ex.png")
#Original image size 800x800

button_info=Button(root, image=newphoto_4, command=button_info_command)
button_info.place(x=440 , y=4)
#image button

frame_bottom=LabelFrame(root, text="Payment Section", padx=20, pady=20)
frame_bottom.place(x=3, y=280)

button_2_command=IntVar()
button_2_command.set(1)
entry_7_var=StringVar()
var1=IntVar()
var1.set(1)
entry_name_var=StringVar()
entry_bank_name_var=StringVar()
entry_1_var=StringVar()
entry_2_var=StringVar()
entry_3_var=StringVar()
entry_4_var=StringVar()
entry_5_var=StringVar()
entry_status_var=StringVar()
clicked_2=StringVar()
#-------------------Variables---------------------------

def Calculate_values():
    a=entry_1_var.get()
    b=entry_2_var.get()
    c=entry_3_var.get()
    d=entry_4_var.get()
    if a.isdigit() or b.isdigit() or c.isdigit() or d.isdigit():
        total=(int(a) * int(b) )+ (int(c)*int(d))
        entry_5_var.set(total)
        return True
#Basic Calculation
#using isdigit() method , string----->int

def pay_by_cash():
    m=button_2_command.get()    
    if m==1:
        tkinter.messagebox.showinfo("System","You can pay by cash")
#option called 'via Cash' by pressing 'Cash" button in the main window
#open another window

def ok_command():
    
    #q=entry_bank_name_var.get()
    root4=Toplevel()
    root4.title("GUI")
    img = PhotoImage(file='c:/New folder/umbrella.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    root4.geometry("300x100")

    e=clicked.get()
    f=entry_name_var.get()
    g=clicked_2.get()

    photo_3=Image.open("c:/New folder/like.png")
    resized_3=photo_3.resize((40,40), Image.ANTIALIAS)
    newphoto_3=ImageTk.PhotoImage(resized_3)

    photo_3=ImageTk.PhotoImage(file="c:/New folder/like.png")
    label_image=Label(root4, image=newphoto_3)
    label_image.place(x=3, y=30)
    
    label_final=Label(root4, text="Hello" +g+'.'+f+ "! \nYou have paid via your " +e+" Card\nThank You!")
    label_final.pack()

    button_quit_final=Button(root4, text="Quit", width="10", height="1", command=root4.destroy)
    button_quit_final.pack(side=BOTTOM)

    root4.mainloop()
#after entering your name, open another window
#display the summary
# Third function 

def button_has8_1_command_bill():
    root3=Tk()
    root3.title("GUI")
    img = PhotoImage(file='c:/New folder/umbrella.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    
    Statusbar=["Mr","Mrs","Ms","Thero"]

    clicked_2=StringVar()
    clicked_2.set(Statusbar[0])

    label_name=Label(root3, text="Name")
    label_status=Label(root3, text="Status")
    dropdown_2=OptionMenu(root3, clicked_2, *Statusbar)
    entry_name=Entry(root3, textvar=entry_name_var)
    button_ok=Button(root3, text="OK", width="10", height="1", command=ok_command)

    label_name.place(x=20, y=20)
    label_status.place(x=20, y=75)
    entry_name.place(x=80, y=20)
    dropdown_2.place(x=80, y=75)
    button_ok.place(x=50, y=145)
    
    root3.mainloop()
#if you wanted a bill you would be transfered into another window
# asks the customer name
# then press 'OK'   
# Second function 

def counting_8_digits():
    n=entry_7_var.get()
    if len(n)!=8:
        tkinter.messagebox.showinfo("Error","Invalid Card Number")
    else:
        tkinter.messagebox.showinfo("GUI","Thank you for your payment")

        root2=Toplevel()
        root2.geometry("300x120")
        root2.title("GUI")
        img = PhotoImage(file='c:/New folder/umbrella.png')
        root.tk.call('wm', 'iconphoto', root._w, img)

        photo_2=Image.open("c:/New folder/umbrella.png.")
        resized_2=photo_2.resize((40,40), Image.ANTIALIAS)
        newphoto_2=ImageTk.PhotoImage(resized_2)

        photo_2=PhotoImage(file="c:/New folder/umbrella.png.") 
        #Original image size 2000x2000
        label_photo_2=Label(root2, image=newphoto_2)
        label_photo_2.place(x=3, y=3)

        
        label_has8=Label(root2, text="Do you want a bill?")
        button_has8_1=Button(root2, text="Yes", width="10", height=1, command=button_has8_1_command_bill)
        button_has8_2=Button(root2, text="No", width="10", height=1, command=root2.destroy)

        label_has8.pack()
        button_has8_1.place(x=45, y=50)
        button_has8_2.place(x=175, y=50)

        root2.mainloop()
#open another window
#if you want a bill press 'Yes'
#First function

label_1=Label(frame_top, text="Unit Price Rs.")
label_2=Label(frame_top, text="Units")
label_3=Label(frame_top, text="Total Rs.")
entry_1=Entry(frame_top, textvar=entry_1_var)
entry_2=Entry(frame_top, textvar=entry_2_var)
entry_3=Entry(frame_top, textvar=entry_3_var)
entry_4=Entry(frame_top, textvar=entry_4_var)
entry_5=Entry(frame_top, textvar=entry_5_var, state=DISABLED)

#inputs about units and unit prices

button_1=Button(frame_top, text="Calculate", width="12", height="2", command=Calculate_values)
button_1.grid(row=3, column=0)
#'Calculate' button

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=3)
entry_1.grid(row=1, column=0)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=0)
entry_4.grid(row=2, column=1)
entry_5.grid(row=1, column=3)

#Allignment of inputs about units and unit prices
 
label_4=Label(frame_bottom, text="How do you wish to pay?")
label_4.grid(row=4, column=0)

button_2=Button(frame_bottom, text="Cash", command=pay_by_cash, width="10", height="1")
button_2.grid(row=5, column=4)
#'Cash' button for checkbox 2

cbox_1=Checkbutton(frame_bottom, text="via Card")
cbox_2=Checkbutton(frame_bottom, text="via Cash")
cbox_1.grid(row=5, column=0)
cbox_2.grid(row=5, column=3)
#Pay options (Check boxes)

Banks=["BOC","SEYLAN","PEOPLES' BANK","SAMPATH"]
#Drop down menu items

clicked=StringVar()
clicked.set(Banks[1])

dropdown=OptionMenu(frame_bottom, clicked, *Banks)
label_5=Label(frame_bottom, text="Bank Name")
label_6=Label(frame_bottom, text="Card Number")
entry_6=Entry(frame_bottom, textvar=entry_bank_name_var)#Bank Name
entry_7=Entry(frame_bottom, textvar=entry_7_var)#Card Number
#description about Bank

dropdown.grid(row=6, column=1)
label_5.grid(row=6, column=0)
label_6.grid(row=7, column=0)
#entry_6.grid(row=6, column=1)
entry_7.grid(row=7, column=1)
#Allignment of description about Bank

button_3=Button(frame_bottom, text="OK", command=counting_8_digits, width="10", height="1")
button_3.grid(row=8, column=0)
#creating 'OK' button

root.mainloop()

#have to connect name label(ok button) with final window(by creating variable)
#have to give a command to 'No' button in 'Do you want a bill' window
#have to give command to quit
#adjust font size, buttons etc