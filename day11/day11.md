# Pain (2)

### Problem

---

In the Cloud-Ground game, there is a system called **Pain**. If the pain level is high, it becomes difficult to win in the game. Therefore, it's important to use items wisely to decrease the pain level to 0.

Within the game, there are two types of items that can reduce the pain level. The items are named $A$ and $B$, and when each item is used, it decreases the pain level by $A_p$ and $B_p$ respectively. Each item can be acquired as many times as desired.

The player has currently taken $N$ damage from battles with enemies, resulting in the current pain level. Let's find the **minimum number of items** required for the player to reduce the pain level to 0. However, please note that using an item cannot result in a negative pain level.

### Input

---

The first line contains an integer $N$ representing the player's current pain level.

The second line contains two integers $A_p$ and $B_p$, representing the pain level that can be reduced by items $A$ and $B$ respectively.

- $2≤N≤10^6$
- $2≤A_p≤B_p≤13$
- $A_p$ and $B_p$ are not multiples of each other.

### Output

---

Print the **minimum number of items** the player needs to use in order to reduce the pain level to 0. If it's not possible to reduce the pain level to 0, print -1.

**Example 1**

Input

```
11
2 7

```

Output

```
3

```

**Example 2**

Input

```
10000
4 13

```

Output

```
772

```

**Example 3**

Input

```
10
3 5

```

Output
```
2
```
