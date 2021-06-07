def is_year_leap(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year % 400!=0:
        return False
    else:
        return True

def days_in_month(year, month):
    monthdays=[3,0,3,2,3,2,3,3,2,3,2,3]
    if is_year_leap(year) and month==1:
        return 1
    else:
        return monthdays[month]

def day_of_year(year, month, day):
    days=["Sunday", "Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    odays=day
    for i in range(((year//400)*400)+1, (year-1)):
        if is_year_leap(i):
           odays+=2

        else:
            odays+=1

    for i in range(month):
        odays+=days_in_month(year,i)
    odays=(odays)%7
    return days[odays]
day=int(input("Enter the day"))
month=int(input("Enter the month"))
year=int(input("Enter the year"))


print(day_of_year(year, month, day))
