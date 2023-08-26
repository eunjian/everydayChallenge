# Input the player's pain level
n = int(input())
# Initialize the count of used items
count = 0

# List of pain-reducing items in descending order
items = [14, 7, 1]

# Find the minimum number of items needed to reduce the pain level
for item in items:
    count += n // item  # Count how many of the current item are used
    n %= item  # Update the remaining pain level after using the item

# Print the minimum number of items required
print(count)
