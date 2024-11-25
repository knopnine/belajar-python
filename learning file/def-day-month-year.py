def isYearLeap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def daysInMonth(year, month):
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    elif month == 1 or month == 3 or month == 5 or month ==7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        return 30

def dayOfYear(year, month, day):
    if (month == 2) & (day is [30, 31]):
        return None
    elif (day == 31) & (month is [1, 3, 5, 7, 8, 10, 12]):
        return None
    elif (month > 12) | (day > 31):
        return None
    else:
        leapp = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dday = 0
        if year%400 == 0:
            for i in range(month):
                dday += leapp[i]
        elif year%100 == 0:
            for i in range(month):
                dday += normal[i]
        elif year%4 == 0:
            for i in range(month):
                dday += leapp[i]
        else:
            for i in range(month):
                dday += normal[i]
    return dday            

print(dayOfYear(2000, 12, 31))