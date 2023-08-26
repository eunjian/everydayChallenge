# Implementing Bomb

### Problem

---

There is a rectangular land of size $N \times N$. When dividing the land into small squares of size $1 \times 1$, the land's coordinates located at the $y$-th row from the top and the $x$-th column from the left are denoted as $(y, x)$. Additionally, each land has a value called **bomb value**, and all initial bomb values are set to 0.

$K$ bombs are to be dropped onto this land. When a bomb is dropped on a $1 \times 1$ square of land, it affects the bomb value of that land as well as the bomb values of the land adjacent to it vertically, horizontally, and diagonally. The extent to which the bomb value changes depends on the **state of the land**.

- If it's outside the area of the $N \times N$ region or the state of the land is `#`, the bomb value remains unchanged.
- If the state of the land is `0`, the bomb value increases by 1.
- If the state of the land is `@`, the bomb value increases by 2.

After dropping all the bombs, let's find the highest bomb value among all lands.

### Example Explanation

---

The first example can be represented with the following diagram.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/82a69052-85f1-4506-a3d6-cff8d7234e16)

When a bomb is dropped at $(2,2)$, the bomb values change as follows. The land at $(3,2)$ with state `#` is not affected by the bomb.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/2487a38c-0353-464e-80ea-ec9ba7d7432e)

When a bomb is dropped at $(2,3)$, the bomb values change as follows. The land at $(1,3)$ with state `@` increases its bomb value by 2 due to the bomb.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/1bf58b95-8de8-4844-b1da-4a4eb1d74584)

Finally, after two bombs are dropped at $(1,4)$, the bomb values are as follows.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/76a6b40b-3def-4b72-b24b-621e679f9f7a)

The highest bomb value among all lands is 6, so the answer should be 6.

### Input

---

The first line contains two integers $N$ and $K$, the side length of the land, and the number of times bombs are to be dropped.

The next $N$ lines contain $N$ characters each, representing the state of the land. The character given on the $r$-th line and $c$-th position represents the state of the land at the coordinates $(r,c)$.

The next $K$ lines contain the coordinates $y$ and $x$ where bombs are to be dropped.

- $1≤N≤200$
- $1≤K≤500 000$
- The state of the land is one of `0`, `@`, `#`.
- $1≤y,x≤N$
- All given numbers in the input are integers.

### Output

---

After all the bombs are dropped, print the highest bomb value among all lands.

**Example 1**

Input

```
4 4
0 0 @ 0
0 0 0 0
0 # 0 0
0 0 0 @
2 2
2 3
1 4
1 4

```

Output

```
6

```

**Example 2**

Input

```
4 4
0 @ 0 0
@ 0 @ 0
0 @ 0 0
0 0 0 0
2 2
2 2
2 2
2 2

```

Output
```
8
```
