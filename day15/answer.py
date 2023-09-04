# Input the number of fruits and the player's budget
n, k = map(int, input().split())

# Input the price and satiety of each fruit
fruits = []
for _ in range(n):
    price, satiety = map(int, input().split())
    fruits.append([price, satiety])

# Sort fruits by satiety-to-price ratio in descending orde
fruits.sort(key=lambda x: x[1] / x[0], reverse=True)

total_satiety = 0  # Total satiety of purchased fruits

for price, satiety in fruits:
    if k >= price:
        # If the budget can cover the full price, buy the entire fruit
        k -= price
        total_satiety += satiety
    elif k > 0:
        # If there's budget left but not enough for a full fruit, buy it in pieces
        total_satiety += (k / price) * satiety
        break

# Print the total maximum satiety obtained
print(int(total_satiety))
