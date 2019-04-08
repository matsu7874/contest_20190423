# N-nacci

## Challenge Name

N-nacci

## Problem Statement

2つの自然数N,Mが与えられます。
次のような漸化式を満たす数列`{a_n}` について、
M項目の数`a_M`を10^9 + 7で割った余りを出力してください。

```
a_i = 0 (i <= 0)
a_1 = 1
a_n = a_(n-1) + a_(n-2) + ... + a_(n-N)
```

## Input Format

```
N M
```

## Constraints

- `2 <= N <= 100`
- `0 <= M <= 500 000`

## Output Format

`a_M`を`10^9 + 7`で割った余りを一行で出力してください。

## Sample Case

### Sample Case 1

```
2 5
```

```
5
```

フィボナッチ数列の5番目の項は5です
```
a_1 = 1
a_2 = a_1 + a_0 = 1 + 0 = 1
a_3 = a_2 + a_1 = 1 + 1 = 2
a_4 = a_3 + a_2 = 2 + 1 = 3
a_5 = a_4 + a_3 = 3 + 2 = 5
```

### Sample Case 2

```
4 6
```

```
15
```

### Sample Case 3
```
100 0
```

```
0
```

制約条件に注意して解いてください