from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     
# Driver program
date1 = date(2001, 5, 16)
date2 = date(2022, 11, 28)
print(numOfDays(date1, date2), "days survived in this world until now")
