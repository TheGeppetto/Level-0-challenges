def convert_to_hours_and_minutes(number_of_minutes):
    hours = number_of_minutes // 60
    remainder_minutes = number_of_minutes % 60
    if hours == 1:
        hour_plural = " hour"
    else:
        hour_plural = " hours"
    if remainder_minutes == 1:
        minute_plural = " minute"
    else:
        minute_plural = " minutes"
    return  str(hours) + hour_plural + " ," + str(remainder_minutes) + minute_plural

print(convert_to_hours_and_minutes(266))
