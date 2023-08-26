n, k = map(int, input().split())  # Input the number of integers (n) and the desired position (k)
int_list = [*map(int, input().split())]  # Input the list of integers

b_list = []  # List to store converted binary values

# Convert decimal integers to binary
for i in int_list:
    b = format(i, 'b')  # Convert to binary
    b_list.append(b)  # Add binary value to the list

# Sort binary values based on the count of ones in descending order, and if the counts are the same, sort by decimal value in descending order
r = sorted(b_list, key=lambda x: (x.count('1'), int(x, 2)), reverse=True)

# Convert and print the position k's number from binary to decimal (index is k-1)
print(int(r[k-1], 2))
