#=======================
#|  HERD IMMUNITY CALC      |
#=======================

#made by : @albarghiffarr_
import locale
locale.setlocale(locale.LC_ALL, '')

print("This is a simple herd immunity calculator based on population. ")

r0 = float(input("Please enter reproduction rate between 0.4 to 4.6 : ")) #this rate may vary between country
d = float(input("Please enter fatality rate here : ")) #enter the death rate from latest report

if r0 < 0.4:
	print("that number is too low")
elif r0 > 4.6:
	print("that number is too high")
else:
	p = round(((1-(1/r0))*100),2)

pop=int(input("Please enter population number : "))

infect=((p*pop)/100)
death=(infect*d)/100

'{:,}'.format(infect)
'{:,}'.format(death)

print("To achieve herd immunity, the number of infected from your population should be " + str(infect) + " people. \nEqual to " + str(p) + "  % of your population ( " + str(pop) + " people). \nwith estimated death of " + str(death) + " people")

print("stay safe, everyone.")