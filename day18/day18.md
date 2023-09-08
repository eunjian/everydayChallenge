# Overlapping Points

### Problem

---

There is a square with a side length of $N$. A player wants to count the number of points where two half-lines intersect after drawing $M$ half-lines on this square. The process of drawing a half-line by the player is as follows:

1. Choose a starting square $(y, x)$. $(y, x)$ is the square located in the y-th row and x-th column of the given square when divided into $1\times1$ squares.
2. Determine the direction $d$ to draw the half-line. The direction is one of up, down, left, or right, and is always parallel to the edges of the square.
3. Draw the half-line. The half-line always starts from the edge of the starting square and is drawn in a way that parallel lines passing through the same square do not intersect.

The following figure shows an example of drawing three half-lines on a square with a length of 4:

- (3,2), right/ (3,3), left/ (3,2), up

![image](https://github.com/eunjian/goormchallenge/assets/46674129/a5a16c19-4bd4-4627-997d-8ffba1f6ab13)

There are two horizontal half-lines passing through squares (3,2) and (3,3), but since these two half-lines are parallel to each other, there is no overlap point. However, the vertical half-line passing through the square (3,2) intersects with the other two half-lines, so there are ultimately two overlapping points.

Let's find the number of overlapping points that occur after the player draws all the half-lines.

### Example

---

The first example can be represented graphically as follows, with six overlapping points:

![image](https://github.com/eunjian/goormchallenge/assets/46674129/024cd51d-5c3b-4f07-920d-03d70d4c67d3)

### Input

---

The first line contains two integers $N$ and $M$, separated by a space, representing the size of the square and the number of half-lines to be drawn, respectively.

The next $M$ lines each contain three integers $y_i$, $x_i$, and $d_i$, separated by spaces. This represents the information of the half-line drawn starting from the square $(y_i, x_i)$ in the direction of $d_i$.

- $1≤N≤100$
- $1≤M≤100,000$
- $1≤x_i,y_i≤N$
- $d_i$ is one of the four characters `U`, `D`, `L`, `R`, representing up, down, left, and right directions, respectively.

### Output

---

After drawing all the half-lines, print the number of overlapping points.

**Example 1**

Input

```
3 5
2 1 R
1 1 D
2 3 L
3 3 U
2 2 D

```

Output

```
6

```

**Example 2**

Input

```
3 3
2 2 R
2 2 L
1 2 D

```

Output
```
2
```
