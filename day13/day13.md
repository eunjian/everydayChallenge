# Power Plant

### Problem

---

The player in Cloud City is building a town $M$ in the shape of a square with a side length of $N$. Each cell has a building, and the cell at the $r$-th row and $c$-th column contains the integer $M_{r,c}$ which represents the **type** of building in that cell.

Buildings of the same type that are adjacent to each other in the north, south, east, or west direction can share power. A group of buildings that can share power if they have $K$ or more buildings is called a **complex**.

The player wants to install a generator to supply power to each complex. However, due to cost constraints, they can install only **one** generator. A generator can supply power to all complexes that belong to a specific building type. Therefore, the player will supply power to the building type with the **largest number of complexes**. If there are multiple such building types, the player will choose the one with the larger $M_{r,c}$.

Find the type number of the building to which the player should supply power.

### Input

---

The first line contains the town's size $N$ and the complex standard $K$, separated by a space.

The next $N$ lines each contain $N$ numbers separated by a space, representing the town's status. The value given in the $r$-th line and $c$-th position corresponds to $M_{r,c}$.

- $1≤N≤1000$
- $1≤K≤50$
- $1≤M_{r,c}≤30$
- Input will be provided that has at least one complex.
- All given numbers are integers.

### Output

---

Print the type number of the building to which the player should supply power.

**Example 1**

Input

```
3 2
1 1 3
2 2 3
3 3 2

```

Output

```
3

```

**Example 2**

Input

```
5 3
1 1 1 2 2
3 3 3 1 2
1 1 2 1 1
1 2 2 2 2
3 1 1 1 1

```

Output
```
1
```
