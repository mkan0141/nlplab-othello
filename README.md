# 1. まず初めにすること
このリポジトリを自分のPCにダウンロードする必要があります．GitBashとかiTermとかで保存したいディレクトリに移動したら以下のコマンドを叩いてください．($は必要ないのでコピーしなくていいです(以下同じです))  
nlplab-othelloディレクトリがあったら成功です．
```
$ git clone https://github.com/mkan0141/nlplab-othello
```



# 2. 担当箇所をする前に
## 2.1 更新作業
リモートリポジトリ(github)が更新されているかもしれないので，リモートリポジトリの内容をローカルリポジトリ(自分のPC)に反映させる必要があります．
```bash
$ git pull origin [ブランチ名]

ex) masterブランチを更新させるなら
$ git pull origin master
```
## 2.2 ソースコードを書く前に
自分の担当箇所をするときは，新しくbranchを作って，自分が作ったbranch上で作業してください．基本的にはマージするまで自分が作ったブランチで作業します．

branchの作り方は
```
$ git checkout -b [ブランチ名]

ex) nekoブランチを作るなら
$ git checkout -b neko
```

branchを作ったらリモートリポジトリに反映させてください．

```
$ git push origin [ブランチ名]
ex) nekoブランチを反映させるなら
$ git push origin neko
```

反映されているかgithub上で確認してください．

## 2.3 リモートリポジトリに反映させるまでの一連の流れ

1. add(コミットしたいエリアに移動させる)
```bash
$ git add [ファイル名]
```

2. commitする
```bash
$ git commit -m "コミットメッセージ"
```

3. pushする
```bash
$ git push origin [作業してるブランチ名]
```

## 2.4 今いるbranchの確認の仕方
```
$ git branch
```

## 2.5 ブランチの移動の仕方
```
$ git checkout [ブランチ名]
```

## 2.6 その他便利なコマンド

```bash
$ git status
$ git log
```