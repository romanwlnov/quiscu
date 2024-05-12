# Create a datetime object for the current date and time
now = datetime.now()

# Print the current date and time
print(now)

# Create a datetime object for a specific date and time
date_time = datetime(2023, 3, 8, 14, 30)

# Print the specific date and time
print(date_time)

# Create a timedelta object for a duration of time
duration = timedelta(days=1, hours=2, minutes=30)

# Add the duration to the datetime object
new_date_time = date_time + duration

# Print the new date and time
print(new_date_time)
