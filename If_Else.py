# Robot checking if it needs to charge
battery_level = 25

if battery_level < 30:
    print("🔋 Battery low! Going to charging station")
else:
    print("✅ Battery good! Ready to work")



# How this works:
# if asks a question: "Is battery_level less than 30?"
# < means "less than"
# If the answer is YES (True), do the first thing (go charge)
# If the answer is NO (False), do the else thing (keep working)
# The robot makes this decision automatically!
