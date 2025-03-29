# IMM(International Monetary Market) Currency Futures Positions

このリポジトリは、IMM通貨先物ポジションのデータを提供することを目的としています。  
現時点では開発初期のため、細部に誤りが含まれる可能性があります。予めご了承ください。

## データ更新について

* 更新タイミング: 毎週日曜日の0時に  `yen_cot.html` ファイルが更新されます。
* ファイルの利用方法: `yen_cot.html` を「Download Raw File」からダウンロードすることで、ローカル環境でHTMLファイルとして閲覧できます。

## データの出所と算出方法

* 出所: 元データは、米国商品先物取引委員会（CFTC）が毎週金曜日（日本時間：土曜日未明）に発表する『Commitments of Traders（COT）レポート』に基づいています。詳細は CFTC公式サイト https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm をご参照ください。
* ファンドや機関投資家、投機筋などが円先物を買ったか売ったかを集計し、ポジションのネット（買いポジション－売りポジション）を算出しています。
* 算出方法: 投機筋（Noncommercial）の円先物の売買動向を集計し、買いポジションと売りポジションの差（ネットポジション）を算出しています。
* 解釈: ネットポジションがマイナスの場合、投機筋による円のショート（売り）ポジションが積み上がっている状態を意味します。

# English version
This repository provides data on IMM currency futures positions.   
Please note that the repositoty is still in its early stages, so there may be minor inaccuracies.

## Data Updates

* Update Schedule: The `yen_cot.html` file is updated every Sunday at 0:00.
* Usage: Download the raw file (`yen_cot.html`) to view it locally as an HTML file.

## Data Source and Calculation Method

* Data Source: The underlying data is based on the "Commitments of Traders (COT) Report" published by the U.S. Commodity Futures Trading Commission (CFTC) every Friday (early Saturday Japan time). For more details, please refer to the CFTC website: https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm.
* Calculation Method: The report aggregates the buying and selling positions of speculators (Noncommercial) in yen futures. The net position is calculated by subtracting the sell positions from the buy positions.
* Interpretation: A negative net position indicates that speculative traders have accumulated short (selling) positions in yen futures.