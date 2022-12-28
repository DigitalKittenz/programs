

# input in hours

# output in hours and minutes
hour = 60 # minutes

event_starts = float(input("Event start:\n(Enter in 24 hour format):  "))
event_lasts = float(input("\nEvent lasts:\n(Enter in minutes):  "))

# hours in minute
hours = event_lasts / hour

# total hours
total_hours = event_starts + hours


# 12 hour format with outputs

if total_hours >= 12:
    twelve_hours = total_hours - 12
    print("The event ends at %0.2f" % total_hours, "or %0.2f" % twelve_hours,"pm")
else:
    twelve_hours = total_hours
    print("The event ends at %0.2f" % twelve_hours,"am")

    
