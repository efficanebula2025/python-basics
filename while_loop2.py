
# Robot moving toward a target
robot_position = 0
target_position = 50

print("🎯 Moving toward target...")

while robot_position < target_position:
    robot_position = robot_position + 5  # Move 5 meters forward
    distance_remaining = target_position - robot_position
    print(f"📍 Position: {robot_position}m, Distance remaining: {distance_remaining}m")

print("🏁 Target reached!")

# How this works:
# The robot keeps moving forward (5 meters at a time)
# After each move, it calculates how far is left to go
# It stops when it reaches the target position
# This is how real robots navigate to specific locations
