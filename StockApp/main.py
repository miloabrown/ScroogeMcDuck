import datetime
import operator
from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import ttk

info = []
datelist = []
temp_info = []
#Function for reading the given data. If we were to get more data later, this makes it easier to modify
def readFile(input_file):
    #   Reading csv file and adding values to a list...
    with open(input_file,"r")as file:
        for rivi in file:
            r = []
            for value in rivi.strip().split(","):
                r.append(value)
            info.append(r)
    #   getting rid of the titles
    info.remove(info[0])
    temp_info = info.copy()
    #   sort our list so it's in ascending order by date
    temp_info = sorted(temp_info, key=lambda x: datetime.datetime.strptime((x[0]), '%m/%d/%Y')) 
    info.clear()
    #   Let's turn all the "list" items into Day-Objects to make it easier to manage
    for date in temp_info:
        info.append(Day(date[0],date[1],date[2],date[3],date[4],date[5]))
    for day in info:
        datelist.append(day.date)

#   function to get the sma5 for given date
def getSma(date):
    previous5 = []
    info_index = 0
    info_dates = []
    div = 1
    for day in info:
        info_dates.append(day.date)
    if date in info_dates:
        info_index = info_dates.index(date)
        if info_index==0:
            return info[0].close
        elif info_index<5:
            div = info_index
            for i in(info[:info_index]):
                previous5.append(i)
        else:
            div = 5
            for i in(info[info_index-5:info_index]):
                previous5.append(i)
    else:
        print("date not found")
    sum = 0
    for day in previous5:
        sum+=day.close
    sma = sum/div
    if sma==0:
        sma=1
    return sma

#function that returns a list of all the days within the given range ("start" and "end" included)
def timeFrame(start,end):       
    sub_Dates = []
    start_date = min(datetime.datetime.strptime(start, "%m/%d/%Y"),datetime.datetime.strptime(end, "%m/%d/%Y"))
    end_date = max(datetime.datetime.strptime(start, "%m/%d/%Y"),datetime.datetime.strptime(end, "%m/%d/%Y"))
    for day in info:
        day_date = datetime.datetime.strptime(day.date, "%m/%d/%Y")
        if(start_date <= day_date <= end_date):
            sub_Dates.append(day)
    return sub_Dates

#function for part A, returns the longest bullish trend within given range
def longest_bull(dates):    
    max_result = 0
    result = 0

    for index in range(0,len(dates)):
        previous = dates[index-1].close
        current = dates[index].close
        if current>previous:
            result+=1
        else:
            if result>max_result:
                max_result=result
            result = 0
            
    if result>max_result:
        max_result=result
    return max_result

#   function for part B, returns a list of tuples, that contain the dates,
#   trading volume and the difference between the "high" and "low" of that day.
#   list is ordered by 1)trading volume (highest to lowest), 2) price change
def highest_volume_price(dates):     
    volume_price={}                 
    ans_list = []
    for day in dates:
        volume_price[day.date] = (int(day.volume),float(day.p_change))
    sorted_vp = dict(sorted(volume_price.items(), key=operator.itemgetter(1),reverse=True))
    for key in sorted_vp:
        ans_list.append((key,str(sorted_vp[key][0]),str(sorted_vp[key][1])))
    return ans_list

#Function for part C, returns a list of tuples that contain dates and opening price compared to sma5 of the day as a percentage
#List is in order: best opening price compared to sma5 first
def bestOpen(dates):
    ans=[]
    dates_cp = dates.copy()
    for day in dates:
        ans.append ((day.date,round((((day.open/getSma(day.date))-1)*100),2)))  #rounded to 5 decimals. This can be tweaked for more precision.
    ans = sorted(ans,key=lambda x : (x[1]),reverse=True)     # abs(x[1]) if we just the biggest value change instead of biggest positive change   
    return ans

#Creating a Day class just to make it easier to manage the different values of days
class Day:
    def __init__(self,date,close,volume,open,high,low):
        self.date_as_list = date.split("/")
        self.date = date
        self.day = self.date_as_list[0]
        self.month = self.date_as_list[1]
        self.year = self.date_as_list[2]
        
        self.close = float(close.strip(" $"))
        self.volume = int(volume)    
        self.open = float(open.strip(" $"))        
        self.high = float(high.strip(" $"))      
        self.low = float(low.strip(" $"))
        self.p_change = str(round(abs(self.high-self.low),2))

    def toString(self):
        return((self.date,self.close,self.volume,self.open,self.high,self.low,self.p_change))

#Creating our GUI
def GUI():
    root = Tk()
    root.title("StockMcDuck2.0")
    root.geometry("580x360")

    #Quit button
    quitbut = Button(root,text="Quit",command=root.quit).grid(row=15,column=9,padx=5)

    #Greeting text
    greeting = Label(root,text=" Hello!  Nice to see you Mr. Scrooge!  Welcome to StockMcDuck2.0",bd=20)
    greeting.config(font=Font(size=12,weight=BOLD))
    greeting.grid(row=2,column=0,columnspan=10)

    #Start_date "box"
    label_start = Label(root,text="Select start date").grid(row=4,column=3,pady=5)
    choice_start = StringVar()
    choice_start.set(datelist[0])
    start_date = ttk.Combobox(root, width=15,height=20,textvariable=choice_start)
    start_date["values"] = datelist
    start_date.grid(row=5,column=3)

    #End_date "box" 
    label_end = Label(root,text="Select end date").grid(row=4,column=4,pady=5)
    choice_end = StringVar()
    choice_end.set(datelist[1])
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
        top = Toplevel()
        top.geometry("1200x600")

        #Scrollable frame
        main_frame = Frame(top)
        main_frame.pack(fill=BOTH, expand=1)
        canvas = Canvas(main_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scroll = ttk.Scrollbar(main_frame,orient=VERTICAL,command = canvas.yview)
        scroll.pack(side=RIGHT,fill=Y)
        canvas.config(yscrollcommand=scroll.set)
        canvas.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        second_frame = Frame(canvas)
        canvas.create_window((0,0),window=second_frame,anchor="nw")
        
        back_but = Button(second_frame,text="Back",command=top.destroy).grid(row=4,column=6,pady=40)
        #LongestBull
        if(var1.get()==1):
            label1 = Label(second_frame,text =("Longest bullish trend was: "))
            label1.config(font=Font(size=12,weight=BOLD))
            label1.grid(row=0,column=0,padx=10)
            days = Label(second_frame,text=str(longest_bull(timeFrame(choice_start.get(),choice_end.get())))+" days").grid(row=1,column=0,sticky=N)
        #volume & price change
        datesString = ""
        volumeString = ""
        priceString = ""
        ans2 = highest_volume_price(timeFrame(choice_start.get(),choice_end.get()))
        for row in ans2:
            datesString+=(row[0]+"\n")
            volumeString+=(row[1]+"\n")
            priceString+=(row[2]+"\n")
        if(var2.get()==1):
            label2 = Label(second_frame,text =("Dates ordered by highest trading volumes and price changes:"))
            label2.config(font=Font(size=12,weight=BOLD))
            label2.grid(row=0,column=1,columnspan=3,padx=10)
            date_label = Label(second_frame,text=("Date"+"\n"+datesString)).grid(row=1,column=1,padx=10)
            vol_label = Label(second_frame,text=("Volume"+"\n"+volumeString)).grid(row=1,column=2)
            price_label = Label(second_frame,text=("Price change"+"\n"+priceString)).grid(row=1,column=3)
        #bestopen
        datesString3 = ""
        percentageString = ""
        ans3 = bestOpen(timeFrame(choice_start.get(),choice_end.get()))
        for row in ans3:
            datesString3 += (row[0]+"\n")
            percentageString += (str(row[1])+"%\n")
        if(var3.get()==1):
            label3 = Label(second_frame,text =("Dates ordered by best opening price compared to SMA 5:"))
            label3.config(font=Font(size=12,weight=BOLD))
            label3.grid(row=0,column=5,columnspan=2,padx=10)
            date_label3 = Label(second_frame,text=("Date"+"\n"+datesString3)).grid(row=1,column=5,padx=10)
            percentage_label = Label(second_frame,text=("Open price/SMA 5"+"\n"+percentageString)).grid(row=1,column=6)

    sub_but = ttk.Button(root,text="Submit",command=submit)
    sub_but.grid(row=12,column=3,pady=20)

    root.mainloop()
    
#Read file:
readFile("StockApp\HistoricalQuotes.csv")
#Run Gui:
GUI()