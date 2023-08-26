n = int(input())  # Input the number of ingredients

taste_list = list(map(int, input().split()))  # Input the taste levels for each ingredient
s = 0  # Sum of taste levels of ingredients

for i in range(n):
    # Up to the point before the maximum value, ingredient taste should increase or stay the same as the next element
    if i < taste_list.index(max(taste_list)):
        if taste_list[i] > taste_list[i+1]:  # If ingredient taste decreases
            s = 0  # The burger taste is imperfect, so the burger's taste becomes 0
            break  # If s becomes 0, there's no need to continue the loop
        else:
            s += taste_list[i]
    # For the maximum value, add the ingredient taste to the sum
    elif i == taste_list.index(max(taste_list)):
        s += taste_list[i]
    # After the maximum value, ingredient taste should decrease or stay the same as the previous element
    else:
        if taste_list[i] > taste_list[i-1]:  # If taste increases
            s = 0
            break
        else:
            s += taste_list[i]

# Print the sum of ingredient taste levels
print(s)
