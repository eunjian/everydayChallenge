# Alternative Routes

### Problem

---

The player lives in a country with $N$ cities numbered from 1 to $N$ and $M$ roads. Each road connects two different cities bidirectionally, and the player can only travel between two cities using the given roads.

The player wants to travel from city $S$ to city $E$ by car. When the player moves between two cities, they always take the path with the fewest cities. For example, in the diagram below, if the player wants to travel from city 1 to city 4, they will always take the path 1→3→4, which passes through a total of three cities. They will not choose the path 1→5→2→4, which passes through a total of four cities.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/02aa543f-8a8b-412c-b0b3-19ae021abfac)


The path with the fewest cities may not be unique. In the example below, when the player wants to travel from city 3 to city 1, they have two options: 3→2→1 and 3→4→1. In such cases, the player can choose either path.

![image](https://github.com/eunjian/goormchallenge/assets/46674129/d3464e1b-4c3d-4837-863c-b4fecbf3f972)

In the player's country, construction work is frequently carried out. On the $i$-th day, construction work will be carried out in city $i$. While construction work is ongoing in a city, all roads connected to that city are temporarily closed and cannot be used.

The player will travel from city $S$ to city $E$ every day for the next $N$ days. For each day, you need to calculate the number of cities included in the path that the player will take. If the player cannot travel from the starting city to the destination city, or if the starting city or destination city is under construction, you should output -1 for that day.

### Example 1

Input

```
5 5 1 4
1 3
4 3
2 5
4 2
1 5

```

Output

```
-1
3
4
-1
3

```

### Example 2

Input

```
4 4 3 1
4 1
4 3
3 2
2 1

```

Output

```
-1
3
-1
3

```

### Example 3

Input

```
9 10 1 9
1 2
1 3
3 4
2 5
4 5
5 6
6 7
5 8
7 9
8 9

```

Output
```
-1
6
5
5
-1
5
5
6
-1
```
