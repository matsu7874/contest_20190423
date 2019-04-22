# 『たかし君とおやつ』の解説

全探索で十分間に合います。(後述の動的計画法でも解けますが、こちらの方が速いです)
たかし君が使えるお金の残りと、何番目のお菓子までを買ったかを記録しておくと良い感じに探索できます

pythonでの実装の一例です。
再帰関数を使っています
```python
def canPayExactly(n, i):
    # 残金0 ==> 丁度払えるのでTrue
    if n == 0:
        return True
    # M番目までのお菓子を買ったがお金が余っている ==> False
    if i >= M:
        return False

    price = a[i]
    // i番目のお菓子は0個から (n/a[i]) 個まで買うことができる
    for x in range(n // price + 1):
        if canPayExactly(n - price*x, i+1):
            return True
    return False
```

事前に価格を昇順ソートしておき、枝刈りを行うとより効率的です

動的計画法で解く。
`dp[i][j] = i番目までのおやつの組み合わせで、合計金額がちょうどj円となるような買い方があるか`
とすると、
`dp[i][j] = dp[i-1][j] || dp[i][j-a_i]` と表せる。
最終的に`dp[M][N]`が`true`なら`Yes`を、`false`なら`No`を出力すれば良い。
計算量はO(MN)