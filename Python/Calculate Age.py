age = int(input("Enter your age: "))  
months = age * 12  
weeks = age * 52  
days = age * 365  
hours = days * 24  
minutes = hours * 60  
seconds = minutes * 60 
answer = input("Enter Time unit (months, weeks, days, hours, minutes, seconds): ").lower()
if answer == "months":
    print(f"Your age in Months: {months}")
elif answer == "weeks":
    print(f"Your age in Weeks: {weeks}")
elif answer == "days":
    print(f"Your age in Days: {days}")
elif answer == "hours":
    print(f"Your age in Hours: {hours}")
elif answer == "minutes":
    print(f"Your age in Minutes: {minutes}")
elif answer == "seconds":
    print(f"Your age in Seconds: {seconds}")
else:
    print("Invalid time unit entered.")