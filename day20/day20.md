# Remove Connected Components

### Problem

---

You have a 2D array of size $N \times N$. Each cell in the 2D array is represented by $(i, j)$, where $i$ is the row and $j$ is the column. Initially, each cell contains either an uppercase alphabet letter or a period (`.`).

If two adjacent cells in the up, down, left, or right direction have the same letter, they are considered connected. A group of connected cells is referred to as a connected component, and the size of a connected component is equal to the number of cells it contains.

Cloud wants to perform the following operations $Q$ times:

1. Choose a cell at position $(y_i, x_i)$ and replace the character in that cell with an uppercase alphabet letter $d_i$. It is guaranteed that Cloud selects a cell with a period (`.`) initially.
2. Calculate the sizes of all connected components in the array. If there is a connected component with a size greater than or equal to $K$, delete all characters in that component.

After performing all the operations, find the characters in the array.

### Input

---

The first line contains three integers: $N$, $K$, and $Q$, separated by spaces.

The next $N$ lines each contain $N$ characters. The characters are either `.` or an uppercase alphabet letter. The `.` character indicates that the cell is initially empty. The character in the $r$-th row and $c$-th column represents the content of the cell at position $(r, c)$.

The next $Q$ lines each contain two integers $y_i$ and $x_i$, followed by an uppercase alphabet letter $d_i$. This indicates that Cloud wrote the letter $d_i$ in the cell at position $(y_i, x_i)$.

- $3 \leq N \leq 50$
- $2 \leq K \leq 50$
- $1 \leq Q \leq 1000$
- $1 \leq x_i, y_i \leq N$
- Initially, there are no connected components with a size greater than or equal to $K$.
- It is guaranteed that Cloud always selects a cell initially containing `.`.
- $d_i$ is an uppercase alphabet letter.

### Output

---

After performing all the operations, print the characters in the array. Output the contents of the $N \times N$ array in $N$ lines, where each line contains $N$ characters. If a cell is empty (no character), use the `.` character to represent it.

### Example 1

Input

```
5 5 6
AB..C
BBAZZ
....A
BBB.B
CCBAB
3 4 A
3 1 A
3 3 A
3 2 B
3 2 A
1 2 D

```

Output

```
AD..C
...ZZ
.....
....B
CC.AB

```

### Example 2

Input

```
3 3 1
ABA
B.B
ABA
2 2 A

```

Output
```
ABA
BAB
ABA
```
