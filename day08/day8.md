# Pain Management

### Problem

---

In the Cloud-Ground game, there is a **pain** system. If the pain level is high, it becomes difficult to win the game, so it is important to use items wisely to keep the pain level at 0.

Within the game, there are three types of items that can reduce the pain level. The items are named `bandage`, `medicine`, and `painkiller`, and when used, they decrease the pain level by 1, 7, and 14, respectively. Each item can be obtained as many times as desired.

The player has a current pain level of $N$ after taking damage in a battle with enemies. Let's determine the **minimum number of items** the player needs to reduce the pain level to 0.

Please note that items cannot be used if they would result in a negative pain level.

### Input

---

The first line contains an integer $N$ representing the player's pain level.

- $1≤ N≤ 10^9$

### Output

---

Print the minimum number of items the player needs to reduce the pain level to 0.

**Example 1**

Input

```
8
```

Output

```
2
```

**Example 2**

Input

```
100
```

Output
```
9
```
