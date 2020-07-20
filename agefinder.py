from datetime import datetime, date
age = int(input("How old are you? "))
birthday = int(input("What day of the month, were you born on? (1-31)? "))
birthmonth = int(input("What month were you born in (1-12)? "))

date_today = datetime.now()

birthyear = date_today.year - age
if (birthmonth > date_today.month or (birthmonth == date_today.month and birthday > date_today.day)):
    birthyear -= 1
        

birthdate_formatted = date(birthyear, birthmonth, birthday).strftime("%A %d %B %Y")
print("Your birthdate was {}.".format(birthdate_formatted))