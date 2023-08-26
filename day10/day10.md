# GameJam

### Problem

---

The **player** participated in the **GameJam**. GameJam is a competition where teams are formed on the spot to create game rules and then translate those rules into code to create a game.

The team the **player** is in has created a simple board game that can be played on a board of size $N \times N$. The progress of the game and the rules are as follows:

1. The game takes place on a grid board with a side length of $N$. The board is divided into $N^2$ squares, each with a side length of 1.
2. Each square contains an instruction that says to move **one step** in the direction `<command>` by `<count>` squares.
3. The player places a piece on one of the squares of the board at the beginning of the game.
4. The piece moves according to the instructions on each square. If it moves out of the board during the movement, it wraps around to the opposite side of the board. For example, if it needs to move right from the rightmost square, it will appear on the leftmost square of that row. Similarly, if it needs to move downward from the bottom square, it will appear on the top square of that column. The piece continues moving as long as there are more steps to take.
5. The game ends if the piece needs to revisit a square it has already visited before. Otherwise, the game continues until it reaches an end.
6. The score of the game is the number of **distinct squares** visited by the piece until the game ends, including the starting square.

The **player** wants to practice the game with **Goorm** to showcase it at the final presentation of GameJam. Given the initial square where each of them places their piece, find out who got the higher score between them. Note that the games played by the **player** and **Goorm** are independent.

### Input

---

The first line contains an integer $N$, the size of the grid board.

The second line contains two integers $R_g$ and $C_g$, the coordinates where **Goorm** places the piece, separated by a space. It means the piece is placed in the row $R_g$ and the column $C_g$ of the board.

The third line contains two integers $R_p$ and $C_p$, the coordinates where the **player** places the piece, separated by a space. It means the piece is placed in the row $R_p$ and the column $C_p$ of the board.

The following $N$ lines contain instructions for each square on the board. Each line consists of $N$ instructions in the format `<count> <command>`, separated by a space. The instruction on line $i$ and the position $j$ represents the instruction on the square at the row $r$ and the column $c$ of the board. Here, `<count>` is the number of steps, and `<command>` represents the direction of movement.

- $3≤N≤200$
- $1≤R_g,C_g,R_p,C_p≤N$
- `<count>` is an integer between 1 and $N$, inclusive.
- `<command>` is one of `U`, `D`, `R`, `L`, representing up, down, right, and left, respectively. In this problem, the upward direction corresponds to decreasing row numbers.
- All given numbers in the input are integers.

### Output

---

If **Goorm** wins the game, print `goorm` and the score obtained by **Goorm**, separated by a space. If the **player** wins, print `player` and the score obtained by the **player**, separated by a space. There won't be any test cases where both **Goorm** and the **player** tie.

**Example1**

Input

```
3
1 1
3 3
1L 2L 1D
2U 3R 1D
2R 2R 1U

```

Output

```
goorm 4

```

**Example 2**

Input

```
4
4 2
2 4
1L 3D 3L 1U
2D 2L 4U 1U
2D 2L 4U 3L
4D 4D 1R 4R

```

Output
```
player 6
```
