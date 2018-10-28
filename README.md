# marukofu

## 最初に
これは練習用で作った趣味プログラムです。  
制度はなんともいえないので悪しからず

## marukofuについて
マルコフ連鎖による文章自動生成プログラム  
用意された適当な文章を組み合わせてそれっぽい新しい短文を作ります


## 利用環境
この文章生成はpython3.6で検証しています。

janomeという形態素解析ツールを利用させていただいています
https://mocobeta.github.io/janome/

pip install janomeで入ります

## 使い方
modelディレクトリにテキストファイルをセット  
例として夏目漱石の小説、坊ちゃんが入ってます

``` python
import serifu

# SerifuGeneratorにbocchanをセット
s = serifu.SerifuGenerator("bocchan")

# get_serifuで適当なセリフが生成される
s.get_serifu() # 現に君の待遇上の都合もつくんだのであった
```

### 補足
初回のみモデルの初期化を行うため、やや重いです。
２回目以降快適に動作。

## 各ディレクトリについて
```
|-- README.md
|-- model # 使いたいモデル(テキスト)を入れておく
|   `-- bocchan
|-- pickle_model # 初期化されたモデルが入る
`-- serifu.py # プログラム本体
```
