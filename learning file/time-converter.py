# converter penambahan waktu sederhana

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
end = mins + dura
if end >= 60:
        totalHour= (hour+(end//60))%24
        totalMins= end%60
print("\nit has been " + str(dura) + " minutes since " + str(hour) + ":" + str(mins))
print("the time is now " + str(totalHour) + ":"+ str(totalMins) + "\ncan you feel the time ?")