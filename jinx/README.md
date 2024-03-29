# ジンクス

## Challenge Name

ジンクス

## Problem Statement

無限に広がる二次元格子があります。原点 (0,0) から右に x、上に y 進んだ格子点の座標を (x,y) と表します。

Mさんは格子状の街に住んでおり、自宅が(0,0)、会社が(W,H)に存在しています。
出社する際にMさんは格子上を移動します。
昨日までは最短経路で出社するため、Mさんの現在地を(x,y)として、上(x,y+1)または右(x+1,y)への移動を繰り返し、会社に出社していました。
最短経路で出社する場合、右W回と上H回の移動を組み合わせて、異なる経路数は (W+H)C_W 個となります。

今日Mさんは、道を間違えたため、一度だけ左(x-1,y)か下(x,y-1)方向への移動を含む経路で出社をしました。
最短経路を外れることになってしまいましたが、仕事がとてもうまく進んだので、明日からは左(x-1,y)か下(x,y-1)方向への移動を1度だけ取り入れた経路で出社しようと思います。

明日からのMさんの通勤経路として考えられる経路数を求めてください。
ただし、通勤経路に会社(W,H)を2度含むことはありません。



## Input Format

```
W H
```

## Constraints

- `0 <= W <= 1000`
- `0 <= H <= 1000`
- `(W,H) != (0,0)`

## Output Format

整数を一行で出力してください。

## Sample Case

### Sample Case 1

```
1 1
```

```
16
```

下記の16通りの経路が存在します。
- →→↑←
- →→←↑
- →←→↑
- →←↑→
- →↓↑↑
- ↑↑→↓
- ↑↑↓→
- ↑←→→
- ↑↓→↑
- ↑↓↑→
- ←→→↑
- ←→↑→
- ←↑→→
- ↓→↑↑
- ↓↑→↑
- ↓↑↑→

### Sample Case 2

```
0 2
```

```
12
```
