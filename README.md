# IMM(International Monetary Market) 通貨先物ポジション

##

まだあまりいじってないので、細かい点は間違いがあるかと思われますので、ご注意ください。

## データ更新

* 日曜の0痔に、 `yen_cot.html` ファイルが更新されます。
* `yen_cot.html` を download raw file してもらえれば、手元でhtmlで参照できるかと思います。

## データの出所と算出方法

* 米国の商品先物取引委員会（CFTC）が毎週金曜日（日本時間土曜日未明）に発表する『Commitments of Traders（COT）レポート』が元データです。
* https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm
* ファンドや機関投資家、投機筋などが円先物を買ったか売ったかを集計し、ポジションのネット（買いポジション－売りポジション）を算出しています。
* このネットポジションがマイナスの場合、投機筋の円ショート（売り）ポジションが積み上がっている状態を意味します。