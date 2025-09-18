# Robot doing morning system checks
print("🤖 Starting morning checks...")

for check_number in range(1, 6):  # Check systems 1, 2, 3, 4, 5
    print(f"✅ System {check_number} check complete")

print("🚀 All systems ready!")



# How this works:
# for means "do something multiple times"
# check_number becomes 1, then 2, then 3, then 4, then 5
# range(1, 6) creates numbers from 1 to 5 (stops before 6)
# The indented code runs once for each number
# This is like telling the robot "check system 1, then system 2, then system 3..." automatically
