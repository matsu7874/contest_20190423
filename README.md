# contest_20190423

## Rimeの使い方

```sh:インストールと動作確認
pip install git+https://github.com/icpc-jag/rime
rime test
```

詳しい使い方は下記を参照

* [icpc-jag/rime: Rime: Automation Tool for Programming Contest Organizers](https://github.com/icpc-jag/rime)
* [Rimeの使い方 - beet's soil](http://beet-aizu.hatenablog.com/entry/2018/08/20/203706)

## 問題の作り方

下記の5つを作りましょう。

### 問題文

問題文です。HackerRankのフォーマットに従って書きましょう。

### solution

想定解法・想定誤答です。`SOLUTION`ファイルで`challenge_cases`を設定することで想定誤答がWAになることを確認可能です。
Pythonなどのスクリプト言語を使用する場合はshebangが必須です。

### generator

テストケースを生成するプログラムです。コンテスト時にサンプルケースにしたいものは必ず`00_sample`のprefixをつけるようにしましょう。

### validator

テストケースに誤りがないか検証するプログラムです。Pythonの場合は`assert`文が使えます。

### editorial

解説を書きましょう。
