from datetime import datetime, timedelta, timezone
from pytz import timezone

format = "%A %d %B %Y %H:%M:%S"
tzs_list = ["US/Eastern", "Europe/London", "Australia/Sydney", "Pacific/Honolulu"]

print("Pick which timezone you would like the current time for:")
for i in range(len(tzs_list)):
    print("    {} = {}".format(i+1, tzs_list[i]))

option = int(input("Type your option (1-{}): ".format(len(tzs_list))))
if (option < 1 or option > len(tzs_list)):
    print("That option is not valid. Exiting...")
    exit()

option -= 1

user_datetime_formatted = datetime.now().strftime(format)
remote_datetime_formatted = datetime.now(timezone(tzs_list[option])).strftime(format)

print("\nYour current date and time is:\n{}\n".format(user_datetime_formatted))
print("The date and time in {} is:\n{}".format(tzs_list[option], remote_datetime_formatted))