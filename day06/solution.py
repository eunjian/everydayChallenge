from itertools import combinations

N = int(input())  # Input the length of the string
S = input()  # Input the string

# Declare set P to store substring
P = set()

# Declare an array to store the indices of spaces
blank = [i for i in range(1, N)]
# Save combinations of two spaces
comb = list(combinations(blank, 2))

# Each element in the comb array follows the (f, s) format mentioned earlier.
for f, s in comb:
    # Add substrings to P
    P.add(S[:f])
    P.add(S[f:s])
    P.add(S[s:])

# Convert the set of found substrings into a list
P = list(P)

# Python's sort function can also sort strings lexicographically!
P.sort()

# Declare a variable to store the maximum score
result = 0

# For each f, s in comb, let's find the maximum score through exhaustive search.
for f, s in comb:
    temp = 0

    # Find the positions of substrings in P.
    # Here, adding +1 to the index gives the score as mentioned in the problem.
    temp += P.index(S[:f]) + 1
    temp += P.index(S[f:s]) + 1
    temp += P.index(S[s:]) + 1

    result = max(result, temp)

# Print the answer!
print(result)
