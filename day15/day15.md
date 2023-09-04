# Fruits purchase

### Problem

---

The player who went to the mart to buy fruit faced a great challenge. This is because there are too many fruits to choose from, and deciding which fruit to buy is very difficult. Currently, there are $N$ types of fruits available at the mart, each with a price of $P_i$, and the player can obtain satiety of $C_i$ when eating that fruit.

Interestingly, in this mart, it is possible to purchase fruits in pieces. If you want to buy a fruit for a price of $p$, the player can cut that fruit into $p$ pieces and then purchase only the desired number of pieces. At this time, the price for each piece is 1, and the satiety obtained when eaten is $\frac{C_i}{P_i}$.

The player has $K$ money. The player wants to select fruits to buy in order to maximize the **sum of the satiety of the purchased fruits** within the given amount. When the player purchases fruits in the optimal way, let's find the **maximum sum of satiety of the purchased fruits**.

### Example Explanation

---

In the first example, the optimal way to maximize the sum of satiety of the purchased fruits is to buy **the second, third, fourth, and sixth** fruits as a whole and buy **one piece of the first** fruit.

### Input

---

The first line contains the number of fruits sold in the mart $N$ and the amount of money the player has $K$, separated by a space.

The next $N$ lines contain the price $P_i$ and the satiety obtained when eating that fruit $C_i$, separated by a space.

- $1≤N≤1000$
- $1≤K≤10^9$
- $1≤P_i≤10^9$
- $1≤C_i≤10^9$
- $C_i$ is always a multiple of $P_i$.
- All numbers given in the input are integers.

### Output

---

Output the **maximum sum of satiety of the purchased fruits** by the player.

**Example 1**

Input

```
6 13
2 8
7 35
1 5
3 12
10 30
1 7

```

Output

```
63

```

**Example 2**

Input

```
5 4
1 999999996
1 999999997
1 999999998
1 999999999
1 1000000000

```

Output

```
3999999994

```

**Example 3**

Input

```
1 1
1000000000 1000000000

```

Output
```
1
```
