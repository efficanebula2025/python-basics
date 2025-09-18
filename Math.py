# Robot calculating how long its battery will last
battery_percent = 75
battery_drain_per_hour = 10

hours_remaining = battery_percent / battery_drain_per_hour
print("Battery will last", hours_remaining, "hours")

# Robot calculating distance traveled
distance_today = 25
distance_yesterday = 30
total_distance = distance_today + distance_yesterday
print("Total distance traveled:", total_distance, "meters")


# How this works:
# / means divide (75 ÷ 10 = 7.5)
# + means add (25 + 30 = 55)
# The robot does the math and stores the answer in a new box
# We can use the calculated results just like any other information
