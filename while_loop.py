# Robot charging battery
battery_level = 20
print(f"🔋 Battery at {battery_level}% - Starting charge...")

while battery_level < 100:
    battery_level = battery_level + 10  # Charge by 10% each cycle
    print(f"⚡ Charging... {battery_level}%")

print("✅ Battery fully charged!")



# How this works:
# while means "keep doing this as long as something is true"
# The condition battery_level < 100 means "less than 100%"
# Each time through the loop, we add 10% to the battery
# then battery reaches 100%, the condition becomes false and the loop stops
