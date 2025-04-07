# Python program to calculate the time when an alarm will go off

# Ask the user for the current time now in hours (24-hour format)
current_time = int(input("Please Enter the current time (in 24-hour format, e.g., 13 for 1 PM): "))

# Ask the user for the number of hours to wait for the alarm
hours_to_wait = int(input("Please Enter the number of hours to wait for the alarm: "))

# Calculate the time when the alarm will go off
alarm_time = (current_time + hours_to_wait) % 24

# Output the result
print(f"The alarm will go off at {alarm_time}:00.")
