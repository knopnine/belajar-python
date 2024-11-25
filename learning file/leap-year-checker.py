year = int(input("Enter a year: "))
if year >= 1582 :
    if year%4 == 0 :
        print("Leap Year")
    elif year%400 == 0 :
        print("Leap Year")
    elif year%100 == 0:
        print("Common Year")
    else:
        print("Common Year")
else :
    print("Not within the Gregorian calendar period")