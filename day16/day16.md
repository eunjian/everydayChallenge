# **Alliance**
### **Problem**

---

There are $N$ islands on the sea. The islands are numbered from 1 to $N$ consecutively. There are also $M$ bridges connecting different pairs of islands. All bridges are one-way, and there can be at most two bridges between any two islands: one in each direction.

One day, a conflict arises between the islands. All the islands want to form alliances with each other to increase their power. Two islands, $a$ and $b$, will form an alliance if there are direct bridges from $a$ to $b$ and from $b$ to $a$. If $a$ forms an alliance with $b$ and $b$ forms an alliance with $c$, then $a$ and $c$ are also considered to be in the same alliance, even if there is no direct bridge between them.

Even if two islands do not form alliances with other islands, they are still considered to be in the same alliance.

You need to find the number of alliances among the $N$ islands.

### Example

---

In the first example, following the given definition, islands **1** and **4** form an alliance. There are no other island pairs that form alliances.

Therefore, there are **3** alliances in total, which are **[1, 4], [2], [3]**.

In the second example, islands **1**, **2**, and **3** form a single alliance.

Therefore, there is **1** alliance in total, which is **[1, 2, 3]**.

### Input

---

The first line of input contains two integers, $N$ and $M$, separated by a space, where $N$ is the number of islands, and $M$ is the number of bridges.

The next $M$ lines each contain two integers, $s_i$ and $e_i$, separated by a space, representing a bridge from island $s_i$ to island $e_i$.

- $2≤N≤2000$
- $1≤M≤200000$
- $1≤s_i,e_i≤N; s≠e$
- All numbers are integers.

### Output

---

Print the number of alliances among the $N$ islands.

**Example 1**

Input

```
4 6
2 3
4 1
1 2
3 4
1 4
2 4

```

Output

```
3

```

**Example 2**

Input

```
3 6
1 2
1 3
2 1
2 3
3 1
3 2

```

Output

```
1

```
