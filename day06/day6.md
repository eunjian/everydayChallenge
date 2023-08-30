# **String Division**

### **Problem**

---

A string $S$ of length $N$ is given. The player aims to divide the string $S$ into three non-overlapping substrings. All substrings must have a length of at least 1 and must be consecutive in the original string.

The player can earn points based on how the string is divided. The points are calculated according to the following steps:

- When the string $S$ is divided as specified, all distinct substrings that appear are removed and sorted lexicographically to form a sequence $P$.
- If the three divided substrings are the $i$-th, $j$-th, and $k$-th strings in the sequence $P$, the player earns $i+j+k$ points.

For example, consider the string **`abcd`**. There are three possible ways to divide it into three non-overlapping substrings: **`{a, b, cd}`**, **`{a, bc, d}`**, and **`{ab, c, d}`**. If we remove duplicates and sort the substrings lexicographically, the sequence $P$ becomes **`a, ab, b, bc, c, cd, d`**. In this case, if we choose the division **`{ab, c, d}`**, the earned points would be $2+5+7=14$, which is the maximum possible score.

Given a string $S$, find the maximum score that can be obtained when dividing it into three substrings.

### **Input**

---

The first line contains an integer $N$, the length of the string.

The second line contains the string $S$.

- $3 \leq N \leq 100$
- $S$ consists of lowercase alphabets.

### **Output**

---

Print the maximum score that can be obtained by dividing the string.

**Example 1**

Input

```
4
abcd
```

Output

```
14
```

**Example 2**

Input

```
3
abz
```

Output
```
6
```
