# Robot deciding what to do based on weather
weather = "sunny"
battery_level = 80

if weather == "sunny" and battery_level > 50:
    print("☀️ Perfect day for outdoor patrol!")
elif weather == "rainy":
    print("🌧️ Staying inside today")
elif battery_level < 50:
    print("🔋 Need to charge first")
else:
    print("🤖 Ready for indoor tasks")



# How this works:
# == means "exactly equal to" (is weather exactly "sunny"?)
# and means both things must be true
# elif means "else if" - another choice to check
# The robot checks each condition in order until it finds one that's true
