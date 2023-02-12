# multi-article-eliza-py
複数の論文にまたがった内容を対話的にクエリできるプログラム。
現在はPythonで試験的に書いているが、いずれRustにしたい。

## 構築コード

```sh
wget https://github.com/kermitt2/grobid/archive/0.7.2.zip .
unzip 0.7.2.zip
cd grobid-0.7.2 && ./gradlew clean install && cd -
```