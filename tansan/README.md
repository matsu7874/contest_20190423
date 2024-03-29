# tansan

## Challenge Name

炭酸かレモンか

## Problem Statement

ある会社F社には、二種類の炭酸飲料T, Lが冷蔵庫に用意されており、社員はいつでもそれらを飲むことができます。
F社の社員が炭酸飲料を飲む際には、３つのルールがあります。
 - みんなが一番冷えた飲料が飲めるように、決まった順番に沿って取ること。
 - 一本冷蔵庫から飲料を取ったら、倉庫から新たに一本を奥（順番の最後尾）に置くこと。
 - 新たに一本飲料を置く際には、取った飲料「ではない種類」の飲料を一本置くこと。（「同じ種類」ではないことに注意！）
いま、冷蔵庫にはM本の炭酸飲料が入っており、それらは最初に取られるものから順に
a_1, a_1, a_2, ... , a_M
ただし、a_i = T or L　（1≦i≦M）
の順番に入っているとします。
冷蔵庫が上記の順番になってから、AさんがN人目として炭酸飲料を取りに来ました。
Aさんが手に入れる炭酸飲料はTとLのどちらでしょうか？

## Input Format

```
N M
a_1
a_2
...
a_M
```

## Constraints

- `1 <= N <= 10^9`
- `1 <= M <= 10^5`

## Output Format

L または T

## Sample Case

### Sample Case 1

```
5 3
L
T
T
```

```
L
```

便利のため、最初の冷蔵庫の状態を手前から順に書いて、
 (L T T) のように表すことにします。
一人目の社員はLを取りますが、「Lではない種類」のTを入れるので、
一人目の社員が取った後：(T T T)
同様にして、
二人目の社員が取った後：(T T L)
三人目の社員が取った後：(T L L)
四人目の社員が取った後：(L L L)
となります。
よって、五人目の社員は一番手前にあるLを取ることになります。

### Sample Case 2

```
100 5
T
L
T
L
T
```

```
L
```
