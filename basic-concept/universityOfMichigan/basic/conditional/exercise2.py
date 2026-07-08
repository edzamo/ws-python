##3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.


hrs = input("Enter Hours:")
rph=input("rate per hour:")
hours = float(hrs)
rateHours=float(rph)

if hours<=40:
    pay=hours*rateHours
else:
    pay=40*rateHours+(hours-40)*rateHours*1.5
print(pay)

##other solution
hrs = input("Enter Hours:")
rph=input("rate per hour:")
hours = float(hrs)
rateHours=float(rph)    

if hours >40:
    reg= rateHours*hours
    otp=(hours-40.0)*(rateHours*0.5)
    pay=reg+otp
else:
    pay=hours*rateHours
print(pay)