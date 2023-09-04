# Small nodes

### Problem

---

There is a graph consisting of $N$ nodes and $M$ bidirectional edges. The nodes of this graph are numbered from 1 to $N$. Edges with the same start and end nodes are not given.

The player intends to move within the graph according to the following rules. The player starts at node $K$.

- A visited node cannot be revisited. The starting node is considered visited.
- The player moves to the node directly connected to the current node through an edge if it is visitable and has the smallest number.

Find the number of distinct visited nodes and the number of the last node when the player can no longer move.

### Input

---

The first line contains three integers $N$, $M$, and $K$, separated by spaces.

The next $M$ lines each contain two integers $s_i$ and $e_i$, separated by spaces, indicating that there is an edge between the nodes.

- $1 \leq N \leq 2000$
- $1 \leq M \leq 200,000$
- $1 \leq K \leq N$
- $1 \leq s_i, e_i \leq N; s_i \neq e_i$

### Output

---

Print the number of visited nodes until the player can no longer move and the number of the last node visited.

Example 1

Input

```
6 6 1
1 2
1 3
2 3
3 4
3 5
4 6

```

Output

```
5 6

```

Example 2

Input

```
6 5 1
1 2
2 3
3 4
4 5
5 6

```

Output

```
6 6

```

Example 3

Input

```
6 5 1
2 3
3 2
6 2
4 2
4 3

```

Output
```
1 1
```
