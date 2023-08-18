# Could Burger Taste

### Question

Cloud burgers are famous for being delicious, made with various ingredients. A cloud burger is created by stacking $N$ ingredients in order, and the taste of a cloud burger is the sum of the taste levels of all the ingredients used.

To create a perfect cloud burger, the taste levels of the ingredients should follow a pattern where the taste level of the ingredient at the top is higher than or equal to the taste levels of the ingredients below it.

The player has created a cloud burger by stacking $N$ ingredients in order. If the taste level of the $i$-th ingredient stacked is $k_i$, determine the taste of the cloud burger the player has made. If the player has not created a perfect cloud burger, print `0`.


### Input

The first line contains the number of ingredients, $N$.
The following line contains $N$ integers, separated by spaces, each representing the taste level of the $i$-th ingredient ($k_i$).

Constraints:

- $1 \leq N \leq 1000$
- $1 \leq k_i \leq 10^6$
- All numbers provided in the input are integers.


### Output:

Print the taste level of the cloud burger that the player has created. If the cloud burger is not perfect, print `0`.

**Example 1**

Input

```
5
1 2 3 3 1
```

Output

```
10
```

**Example 2**

Input

```
7
1 2 3 5 2 3 1
```

Output

```
0
```
