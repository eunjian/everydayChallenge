# Receive the player's pain level as input.
n = int(input())

# Receive the pain reduction values for items A and B as input.
a, b = map(int, input().split())

# Store the pain reduction values of items A and B in a list.
items = [a, b]

# Initialize a list to store the minimum number of items needed.
d = [1000001] * (n + 1)
d[0] = 0

# Iterate over items A and B.
for i in range(2):
    for j in range(items[i], n + 1):
        # Calculate the minimum number of items required to achieve the current pain level j.
        d[j] = min(d[j], d[j - items[i]] + 1)

# Print the minimum number of items needed to reduce the player's pain level to 0.
# If it's not possible to reduce the pain level to 0, print -1.
if d[n] == 1000001:
    print(-1)
else:
    print(d[n])
