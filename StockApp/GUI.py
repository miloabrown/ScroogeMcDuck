
from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import ttk

#GUI
def GUI():
    root = Tk()
    root.title("StockMcDuck2.0")
    root.geometry("580x360")

    #Quit button
    quitbut = Button(root,text="Quit",command=root.quit).grid(row=15,column=9,padx=5)

    datelist = ["jess","kyä","ok"]
    #Greeting text
    greeting = Label(root,text=" Hello!  Nice to see you Mr. Scrooge!  Welcome to StockMcDuck2.0",bd=40)
    greeting.config(font=Font(size=12,weight=BOLD))
    greeting.grid(row=2,column=0,columnspan=10)

    #Startdate box
    choice_start = StringVar()
    choice_start.set("Select start date")
    start_date = ttk.Combobox(root, width=15,height=20,textvariable=choice_start)
    start_date["values"] = datelist
    start_date.grid(row=5,column=3)

    #Enddate box 
    choice_end = StringVar()
    choice_end.set("Select end date")
    end_date = ttk.Combobox(root, width=15,height=20,textvariable=choice_end)
    end_date["values"] = datelist
    end_date.grid(row=5,column=4)

    # title2
    f_label=Label(root,text="What information would you like to have?")
    f_label.grid(row=8,column=2,columnspan=10,pady=20,sticky=W)
    f_label.config(font=Font(size=12))

    #checkboxes
    #1)Longest Bullish Trend
    var1= IntVar()
    check1= Checkbutton(root,text="Longest Bullish Trend",variable=var1)
    check1.grid(row=9,column=3,sticky=W)
    #2)Highest trading volumes, and price changes

    var2= IntVar()
    check2= Checkbutton(root,text="Highest trading volumes and price changes",variable=var2)
    check2.grid(row=10,column=3,sticky=W)
    #3)Best opening price compared to SMA5

    var3= IntVar()
    check3= Checkbutton(root,text="Best opening price compared to SMA5",variable=var3)
    check3.grid(row=11,column=3,sticky=W)

    #Submit button
    def submit():
        pass

    sub_but = ttk.Button(root,text="Submit",command = submit)
    sub_but.grid(row=12,column=3,pady=20)

    root.mainloop()