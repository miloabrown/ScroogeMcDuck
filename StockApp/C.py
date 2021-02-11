# C) Within a given date range, which dates had the best opening price compared to 5 days simple moving average (SMA 5)?

# Calculate simple moving average for day N using the average value of closing prices between days N-1 to N-5.
# Calculate how many percentages (%) is the difference between the opening price of the day and the calculated SMA 5 price of the day.
# Expected output: List of dates and price change percentages. The list is ordered by price change percentages.



#sma(n) = (n-1.close+n-2.close+n-3.close+n-4.close+n-5.close)/5
#(n.open/sma)-1

def bestOpen(dates):
    dates_cp = dates.copy()

    dates_cp = sorted(dates_cp,key=lambda x: ((x.open/getSma(x.date))-1)

def getSma(date):           #   function to get the sma5 for given date
    previous5 = []
    info_index = 0
    for index,day in enumerate(info):
        if day.date == date:
            info_index = index       
    if info_index<5:
        for i in (info[0:info_index]):
            previous5.append(i)
    else:
        for i in (info[info_index-5:info_index]):
            previous5.append(i)
    sum =0
    for day in previous5:
        sum+=float(day.close.replace("$",""))
    sma = sum/5
    return sma