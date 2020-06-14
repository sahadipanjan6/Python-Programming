''' Question: Write a Python program to convert seconds to day, hour, minutes and seconds.

Solution: '''

get_total_seconds = int(input('Enter total seconds: '))
get_days = get_total_seconds // (24*60*60)
get_hours = (get_total_seconds - get_days*24*60*60) // 3600
get_mins = (get_total_seconds-get_days*24*3600-get_hours*3600) // 60
get_sec = (get_total_seconds - get_days*24*3600 - get_hours*3600 - get_mins*60)

print("{} = {} days, {} hours, {} minutes, {} seconds".format(get_total_seconds, get_days, get_hours, get_mins, get_sec))
