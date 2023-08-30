# Power Generators

### Problem

---

The player in Cloud City is creating a town $M$ in the shape of a square with a side length of $N$. Each cell corresponding to the $r$-th row and $c$-th column has a number $M_{r,c}$ written on it. $M_{r,c}$ is either 0 or 1, and each number has the following meanings:

- If it's 0, there's nothing in the cell.
- If it's 1, there's a house in the cell.

To supply power to the houses in the town, the player needs to install power generators in each house or provide power to a house if any of its adjacent houses in the north, south, east, or west direction has power. Find the minimum number of power generators the player needs to install to supply power to all the houses.

### Input

---

The first line contains the size $N$ of the town.

The next $N$ lines each contain $N$ numbers separated by spaces, representing the state of the town. The value given in the $r$-th row and $c$-th column corresponds to $M_{r,c}$.

- $1≤N≤1000$
- $M_{r,c}$ is either 0 or 1.
- All given numbers are integers.

### Output

---

Output the minimum number of power generators the player needs to install to supply power to all the houses.

Example 1

Input

```
3
0 1 0
1 0 1
1 1 1

```

Output

```
2

```

Example 2

Input

```
4
1 1 1 1
0 0 0 1
1 1 1 1
1 0 0 1

```

Output
```
1
```
