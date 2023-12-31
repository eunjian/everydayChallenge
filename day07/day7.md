# Cloud Finder Flags

### Problem

---

The Cloud Finder game is played on a grid-shaped game board $M$ with a side length of $N$. Some cells on the game board contain **clouds**, and the player wins the game by finding all the positions of clouds on the board.

The player, who is the creator of the Cloud Finder game, wants to make it easier to find clouds by placing **flags** on the game board. Flags can be placed only on cells that do not contain clouds and are adjacent to at least one cloud in the eight directions: up, down, left, right, and diagonally. Each flag placed in this manner is assigned a value corresponding to the number of clouds among the eight adjacent cells.

The player has placed flags on all possible cells where they can be placed. Now, the player wonders how many flags have a value of $K$. Your task is to count the number of flags with a value of $K$ on behalf of the player.

### Example Explanation

---

In the first example, the given game board is as follows. For convenience, let's denote the cell in the $r$-th row and the $c$-th column of the game board as $M_{r,c}$.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/5d74a887-d26f-4ed0-a505-f690775b9a81)

$M_{3,2}$ is an empty cell that is also adjacent to clouds in the eight directions. Since there are four clouds in total, the value of the flag at this position will be **4**.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/ab9a32db-73e8-42ad-b602-a142bcd1bda2)

The result of placing flags on all possible positions of the game board would be as shown below. Empty cells are where no flag is placed.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/fbe8898f-56f3-433b-8340-b217a68aca94)

### Input

---

The first line contains two integers $N$ and $K$, separated by a space, representing the size of the game board and the desired value of flags, respectively. The next $N$ lines contain information about each cell of the game board. Each line contains $N$ characters separated by spaces. The character provided in the $r$-th row and the $c$-th column represents the information of cell $M_{r,c}$. `0` represents an empty cell, while `1` represents a cell with a cloud.

- $1 \leq N \leq 1000$
- $1 \leq K \leq 8$
- Both $N$ and $K$ are integers.
- Each character representing cell information is either `0` or `1`.

### Output

---

Print the number of flags with a value of $K$.

**Example 1**

Input

```
4 2
0 0 0 1
0 0 1 0
0 0 1 0
0 1 1 1

```

Output

```
2

```

**Example 2**

Input

```
5 8
0 1 1 1 1
0 1 0 1 0
0 1 1 1 1
0 1 1 0 1
0 1 0 1 0

```

Output
```
1
```
