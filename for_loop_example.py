# Robot patrolling different rooms
rooms = ["Kitchen", "Living Room", "Bedroom", "Bathroom"]

print("🚁 Starting patrol...")
for room in rooms:
    print(f"🔍 Checking {room}...")
    print(f"✅ {room} is secure")

print("🏠 Patrol complete!")




# How this works:
# rooms is a list (like a shopping list) of room names
# for room in rooms: means "do this for each room in the list"
# room becomes "Kitchen", then "Living Room", then "Bedroom", etc.
# The robot visits each room automatically
