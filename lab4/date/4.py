from datetime import datetime,timedelta 
def date_dif(date2 , date1):
    dif = date2 - date1
    difference = ((dif.days*24*3600) + dif.seconds)
    return difference
print("Print first date(Year-month-date, hour:min:sec) :")
firststr = input()
date1 = datetime.strptime(firststr, '%Y-%m-%d, %H:%M:%S')
print("Print second date(Year-month-date, hour:min:sec) :")
secstr = input()
date2 = datetime.strptime(secstr, '%Y-%m-%d, %H:%M:%S')
print("\n%d seconds" %(date_dif(date2, date1)))
print()