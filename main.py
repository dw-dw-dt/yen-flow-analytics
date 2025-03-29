import cot_reports as cot
import datetime as dt
import pandas as pd
import plotly.express as px


# 直近までのデータを取得
years = range(2017, dt.datetime.now().year + 1)
reports = [cot.cot_year(year=year) for year in years] # このやり方だと2003年以前と2007年がなぜが取得できないので、2017年以降をひとまず取得
reports.append(cot.cot_hist(cot_report_type = "legacy_fut")) # 1986年から2016年までのデータはこちらのメソッドで取得

# 各年のデータを縦に連結
report = pd.concat(reports, ignore_index=True)

# 日付カラム名を指定し、日付型に変換
date_col = "As of Date in Form YYYY-MM-DD"
report[date_col] = pd.to_datetime(report[date_col])

# Japanese Yenのみ抽出
yen_report = report[report['Market and Exchange Names']=='JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE']
# report[report['Market and Exchange Names'].str.contains('JAPANESE YEN')]['Market and Exchange Names'].unique()
# によると、以下の通り他にもいくつかある
# array(['JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE',
#        'EURO FX/JAPANESE YEN XRATE - CHICAGO MERCANTILE EXCHANGE',
#        'JAPANESE YEN - INTERNATIONAL MONETARY MARKET',
#        'U.S. DOLLARS-JAPANESE YEN - NEW YORK FUTURES EXCHANGE',
#        'JAPANESE YEN - PHILADELPHIA BOARD OF TRADE',
#        'EURO FX/JAPANESE YEN XRATE - NEW YORK BOARD OF TRADE',
#        'EURO FX/JAPANESE YEN XRATE - NEW YORK COTTON EXCHANGE'],
#       dtype=object)

# 整形
yen_df = yen_report.sort_values(date_col, ascending=True).reset_index(drop=True)[[date_col, 'Noncommercial Positions-Long (All)', 'Noncommercial Positions-Short (All)']]

# Netの非商業ポジションを計算
yen_df['Net Noncommercial Positions'] = yen_df['Noncommercial Positions-Long (All)'] - yen_df['Noncommercial Positions-Short (All)']

# Plotly Express でラインチャートを作成
fig = px.line(
    yen_df, 
    x="As of Date in Form YYYY-MM-DD", 
    y="Net Noncommercial Positions",
    title="Net Noncommercial Yen Positions Over Time; IMM(International Monetary Market) Data",
    labels={
        "As of Date in Form YYYY-MM-DD": "Date",
        "Net Noncommercial Positions": "Net Noncommercial Positions"
    }
)
# fig.show()
fig.write_html("docs/yen_cot.html")