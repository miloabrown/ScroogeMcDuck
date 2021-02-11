import datetime
import operator
#   Reading csv file and adding values to a list...
info = []
with open("StockApp\HistoricalQuotes.csv","r")as file:
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

#--------------------------------------------------#

def getSma(date):           #   function to get the sma5 for given date
    previous5 = []
    info_index = 0
    info_dates = []
    for day in info:
        info_dates.append(day.date)
    if date in info_dates:
        info_index = info_dates.index(date)
        if info_index<5:
            for i in(info[0:info_index]):
                previous5.append(i)
        else:
            for i in(info[info_index-5:info_index]):
                previous5.append(i)
    else:
        print("date not found")
    sum = 0
    for day in previous5:
        sum+=float(day.close.replace("$",""))
    sma = sum/5
    if sma==0:
        sma=1
    return sma
    


def timeFrame(start,end):
    sub_Dates = []
    start_date = datetime.datetime.strptime(start, "%m/%d/%Y")
    end_date = datetime.datetime.strptime(end, "%m/%d/%Y")
    for day in info:
        day_date = datetime.datetime.strptime(day.date, "%m/%d/%Y")
        if(start_date <= day_date <= end_date):
            sub_Dates.append(day)
    return sub_Dates

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

def highest_volume_price(dates):
    volume_price={}
    ans_list = []
    for day in dates:
        volume_price[day.date] = (int(day.volume),float(day.p_change))
    sorted_vp = dict(sorted(volume_price.items(), key=operator.itemgetter(1),reverse=True))
    for key in sorted_vp:
        ans_list.append((key,str(sorted_vp[key][0]),str(sorted_vp[key][1])))
    return ans_list

def bestOpen(dates):
    ans=[]
    dates_cp = dates.copy()
    for day in dates:
        ans.append ((day.date,round(((day.open/getSma(day.date))-1),5)))  #rounded to 5 decimals. This can be tweaked for more precision.
    ans = sorted(ans,key=lambda x : abs(x[1]),reverse=True)
    return ans

class Day:
    def __init__(self,date,close,volume,open,high,low):
        self.date_as_list = date.split("/")
        self.date = date
        self.day = self.date_as_list[0]
        self.month = self.date_as_list[1]
        self.year = self.date_as_list[2]
        
        self.close = close
        self.volume = int(volume)    
        self.open = float(open.replace("$",""))        
        self.high = high      
        self.low = low
        self.p_change = str(round(abs(float(self.high.replace("$",""))-float(self.low.replace("$",""))),2))

    def toString(self):
        return((self.date,self.close,self.volume,self.open,self.high,self.low,self.p_change))

#   Let's turn all the "list" items into Day-Objects to make it easier to manage
info.clear()
for date in temp_info:
    info.append(Day(date[0],date[1],date[2],date[3],date[4],date[5]))


# Testing section #

print(longest_bull(timeFrame("01/21/2020","01/20/2021")))

lista_b =(highest_volume_price(timeFrame("01/21/2020","01/20/2021")))
for i in lista_b:
    print(i)
bestopen_list = bestOpen(timeFrame("01/21/2020","01/20/2021"))
for day in bestopen_list:
    print(day)

