# B) Which dates within a given date range had a) the highest trading volume and b) the most significant stock price change within a day?

# Use High and Low prices to calculate the stock price change within a day. (Stock price change from 2$ to 1$ is equally significant as change from 1$ to 2$.)
# Expected output: List of dates, volumes and price changes. The list is ordered by volume and price change. So if two dates have the same volume, the one with the more significant price change should come first.



# Option 2

# def highest_volume_price(dates):
#     volume = []
#     price = []
#     volume_tmp = dates.copy()
#     price_change = dates.copy()
#     #a) highest volume within a day
#     volume_tmp = sorted(volume_tmp, key=lambda x: x.volume,reverse=True)
#     #b) highest stock price change within a day
#     price_change = sorted(price_change,key=lambda x: x.p_change,reverse=True)
#     for day in volume_tmp:
#         volume.append(day.date+" "+str(day.volume)+" "+str(day.p_change))
#         print((day.date+" "+str(day.volume)+" "+str(day.p_change)))