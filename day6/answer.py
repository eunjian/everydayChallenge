from itertools import combinations

n = int(input())  # Input the length of the string
s = input()  # Input the string

p = list()  # Substrings
d = list()  # Split strings into 3 parts

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        # Save the string split into 3 parts
        d.append([s[:i + 1], s[i + 1:j + 1], s[j + 1:]])
        # Save the substrings
        p.append(s[:i + 1])
        p.append(s[i + 1:j + 1])
        p.append(s[j + 1:])

# Remove duplicates from substrings and sort them in lexicographical order
p = sorted(set(p))

# Calculate the maximum score
score = list()
for i in range(len(d)):
    s = 0  # Score
    for item in d[i]:
        s += p.index(item) + 1
    score.append(s)

# Print the maximum score
print(max(score))
